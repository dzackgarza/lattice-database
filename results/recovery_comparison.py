"""Exact structural comparison for the run 42363689427 recovery (#20).

`same` is the only equality this recovery accepts. It is strict where a card holds mathematical
data: a list is compared position by position and must have the same length, so a reordered Gram
matrix, a reordered coordinate vector, a permuted morphism matrix or a lost duplicate is a
difference; a mapping must have the same keys and the same value at each; a scalar must have the
same type and value, so `True` is not `1` and `2` is not `2.0`.

`changed_leaves` reports the field paths a snapshot actually changed against its base, recursing
into mappings, and treats a list as one value. A field the snapshot did not change is not reported:
the check asks for what the run computed, not for the corpus to equal the run.
"""
from __future__ import annotations

MISSING = object()


def same(left: object, right: object) -> bool:
    """Whether two stored values are identical: same structure, same order, same multiplicities."""
    if isinstance(left, dict) or isinstance(right, dict):
        return (
            isinstance(left, dict)
            and isinstance(right, dict)
            and left.keys() == right.keys()
            and all(same(left[key], right[key]) for key in left)
        )
    if isinstance(left, list) or isinstance(right, list):
        return (
            isinstance(left, list)
            and isinstance(right, list)
            and len(left) == len(right)
            and all(same(a, b) for a, b in zip(left, right))
        )
    return type(left) is type(right) and left == right


def changed_leaves(before: dict, after: dict, prefix: str = "") -> dict[str, object]:
    """The dotted paths whose stored value differs, recursing into mappings; a list is one value."""
    changed: dict[str, object] = {}
    for key in sorted(set(before) | set(after)):
        original = before.get(key, MISSING)
        updated = after.get(key, MISSING)
        path = f"{prefix}{key}"
        if isinstance(original, dict) and isinstance(updated, dict):
            changed.update(changed_leaves(original, updated, f"{path}."))
        elif isinstance(updated, dict) and original is MISSING:
            changed.update(changed_leaves({}, updated, f"{path}."))
        elif not same(original, updated):
            changed[path] = updated
    return changed


def at(record: dict, path: str) -> object:
    """The value at a dotted path, or `MISSING` when any step of it is absent."""
    value: object = record
    for step in path.split("."):
        if not isinstance(value, dict) or step not in value:
            return MISSING
        value = value[step]
    return value
