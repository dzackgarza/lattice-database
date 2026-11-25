"""Three-way reconciliation of a stored record with a recovered copy of the same record.

Recovery of a run's artifact means three versions of one file: the *base* revision the run read, the
*current* tree, and the *recovered* file, which is the base with the artifact's patch applied. This
module merges them at the level of stored fields, so a field current main has gained since the base is
kept, a field the artifact computed is taken, and a field both changed differently is a conflict that
the caller must see and report: it is never resolved by silently choosing one side.
"""

from __future__ import annotations

from collections.abc import Callable

from latticedb.record_types import Yaml

MISSING: object = object()
"""A key or an item that a version does not have at all, which is not the same as a null value."""

type Conflict = str
"""The dotted path of a field both the current tree and the recovered file changed."""

type Identity = Callable[[Yaml], Yaml]


def _dotted(path: tuple[str, ...], name: str = "") -> str:
    return ".".join((*path, name) if name else path)


def merge(
    base: Yaml,
    current: Yaml,
    recovered: Yaml,
    *,
    path: tuple[str, ...] = (),
    key: Identity | None = None,
) -> tuple[Yaml, list[Conflict]]:
    """The union of `current` and `recovered` over `base`, and the paths where they disagree.

    A field only one side changed from `base` takes that side's value; a field both changed to the same
    value takes it; a field only one side has at all takes that side's value; a field both changed
    differently keeps `current` and is reported. A mapping is
    merged key by key, so a block both sides extended keeps both extensions. A list is merged by the
    identity `key` gives its items, when one is given, and otherwise is reported as a conflict unless
    one side left it as `base` had it.
    """
    if current is MISSING:
        # Nothing on the current side to lose: the recovered value is the only one there is.
        return recovered, []
    if recovered is MISSING:
        return current, []
    if current == recovered:
        return current, []
    if base == current:
        return recovered, []
    if base == recovered:
        return current, []

    if isinstance(current, dict) and isinstance(recovered, dict):
        base_mapping = base if isinstance(base, dict) else {}
        merged: dict[str, Yaml] = {}
        conflicts: list[Conflict] = []
        for name in [*current, *(one for one in recovered if one not in current)]:
            value, found = merge(
                base_mapping.get(name, MISSING),
                current.get(name, MISSING),
                recovered.get(name, MISSING),
                path=(*path, name),
                key=key,
            )
            if value is not MISSING:
                merged[name] = value
            conflicts.extend(found)
        return merged, conflicts

    if isinstance(current, list) and isinstance(recovered, list) and key is not None:
        base_items = base if isinstance(base, list) else []
        merged_items = list(current)
        known = [key(item) for item in merged_items]
        conflicts = []
        for item in recovered:
            identity = key(item)
            if identity in known:
                twin = merged_items[known.index(identity)]
                if twin != item and item not in base_items:
                    conflicts.append(_dotted(path, str(identity)))
                continue
            merged_items.append(item)
            known.append(identity)
        return merged_items, conflicts

    return current, [_dotted(path, "")]
