"""Three-way merge of a top-level YAML map, one key at a time.

The files of `certificates/` and `exceeded.yaml` map a computation name, which begins with
its card's tag, to one record. Certification shards own disjoint tags, so two shards
never change the same key; Git's line merge still conflicts when their keys are
adjacent. Git calls this merge as the driver of those files (`.gitattributes`).
"""

from pathlib import Path

import yaml

Mapping = dict[str, object]


def _load(path: Path) -> Mapping:
    data = yaml.load(path.read_text(), Loader=yaml.CSafeLoader) or {}
    assert isinstance(data, dict), f"{path} holds no top-level map"
    return data


def merge(base: Mapping, ours: Mapping, theirs: Mapping) -> Mapping:
    """Take each key's change from the side that made one; a key both sides changed differently conflicts."""
    merged: Mapping = {}
    conflicts = []
    for key in sorted(base.keys() | ours.keys() | theirs.keys()):
        original, mine, other = base.get(key), ours.get(key), theirs.get(key)
        if mine == other or other == original:
            value = mine
        elif mine == original:
            value = other
        else:
            conflicts.append(key)
            continue
        if value is not None:
            merged[key] = value
    if conflicts:
        raise ValueError("both sides changed " + ", ".join(conflicts))
    return merged


def merge_files(base: Path, ours: Path, theirs: Path) -> None:
    """Write the merge of `base`, `ours` and `theirs` to `ours`, as Git's merge driver protocol requires."""
    merged = merge(_load(base), _load(ours), _load(theirs))
    ours.write_text(yaml.dump(merged, Dumper=yaml.CSafeDumper, sort_keys=False, allow_unicode=True))
