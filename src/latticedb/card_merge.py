"""Three-way merge of one lattice card, key by key: what a card's two certifying runs conflict on.

A card holds every field of one lattice, and the two runs that certify it reach the same card: the
fields run takes the terminating fields and the searches run the semi-decisions (`SEMI_DECISIONS`),
under concurrency groups of their own. Each run rewrites the card from the copy it checked out, so a
card it holds no field of still carries that card's lines as of its checkout, and each pushes its
snapshot by cherry-picking it onto `main` (`.github/scripts/persist.sh`).

Git merges a card line by line, and the lines of a block are adjacent, so one run's certification
lines and another's conflict. Resolving that conflict to the pushing run drops the other's
references: the certificate stays in `certificates/`, which merges key by key, and the card no longer
cites it, which is a contradiction between the ledger and the card (#21). A block is a map, so this
merge takes it one key at a time and never has to choose between two runs' keys.

Each key's change comes from the side that made one. A key both sides changed differently takes the
incoming run (Git calls the cherry-picked snapshot `theirs`), which is the run that just computed it.
"""

from __future__ import annotations

import sys
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import cast

import yaml
from pydantic import TypeAdapter, ValidationError

from latticedb import storage
from latticedb.card_serialization import KEYS, record_text
from latticedb.model import Yaml

FrontMatter = dict[str, Yaml]

_ABSENT = object()
"""A key that a side does not state; distinct from a key stated as null."""


class Unreadable(ValueError):
    """A side of the merge is not a card, so the merge writes nothing."""


def read(text: str, *, name: str) -> tuple[FrontMatter, str]:
    """The metadata and prose of one card's text."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise Unreadable(f"{name}: no front matter")
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() != "---":
            continue
        try:
            stated = yaml.load("\n".join(lines[1:index]), Loader=yaml.CSafeLoader) or {}
            metadata = TypeAdapter(FrontMatter).validate_python(stated)
        except (yaml.YAMLError, ValidationError) as error:
            raise Unreadable(f"{name}: {error}") from error
        unknown = set(metadata) - set(KEYS)
        if unknown:
            raise Unreadable(f"{name}: {', '.join(sorted(unknown))} is not a key of a card")
        return metadata, "\n".join(lines[index + 1 :]).strip()
    raise Unreadable(f"{name}: no front matter ends")


def _same(left: object, right: object) -> bool:
    """Whether two sides state the same thing, a key neither states included."""
    return left is right or (left is not _ABSENT and right is not _ABSENT and left == right)


def _order(ours: Mapping[str, object], theirs: Mapping[str, object], base: Mapping[str, object]) -> Iterable[str]:
    """The keys in the order `ours` states them, then the ones only `theirs` and then `base` state.

    The merge writes into `ours`, so its key order is kept and a merged card's lines stay where the
    card had them.
    """
    yield from ours
    yield from (key for key in theirs if key not in ours)
    yield from (key for key in base if key not in ours and key not in theirs)


def _merged_value(original: object, mine: object, other: object) -> object:
    """One key's merged value, or `_ABSENT` when neither side keeps it."""
    if _same(mine, other):
        return mine
    if _same(mine, original):
        return other
    if _same(other, original):
        return mine
    if isinstance(mine, dict) and isinstance(other, dict):
        # A block is a map of the card's fields, and the runs hold different fields of it.
        return merge(original if isinstance(original, dict) else {}, mine, other)
    return other


def merge(base: Mapping[str, Yaml], ours: Mapping[str, Yaml], theirs: Mapping[str, Yaml]) -> FrontMatter:
    """The three-way merge of one card's metadata, one key at a time at every depth."""
    merged: FrontMatter = {}
    for key in _order(ours, theirs, base):
        value = _merged_value(base.get(key, _ABSENT), ours.get(key, _ABSENT), theirs.get(key, _ABSENT))
        if value is not _ABSENT:
            merged[key] = cast(Yaml, value)
    return merged


def merge_text(base: str, ours: str, theirs: str) -> str:
    """The text of the card that merges the changes of `ours` and `theirs` over `base`."""
    base_metadata, base_prose = read(base, name="base")
    ours_metadata, ours_prose = read(ours, name="ours")
    theirs_metadata, theirs_prose = read(theirs, name="theirs")
    metadata = merge(base_metadata, ours_metadata, theirs_metadata)
    if ours_prose == theirs_prose or theirs_prose == base_prose:
        prose = ours_prose
    else:
        prose = theirs_prose
    return record_text(metadata, prose)


def merge_files(base: Path, ours: Path, theirs: Path) -> None:
    """Write the merge of `base`, `ours` and `theirs` to `ours`, as Git's merge driver protocol requires.

    The result is written only when the three sides read as cards: a driver that half-writes a card
    would leave a file that no run wrote, and `storage.write_text` keeps the old card if writing the
    new one is interrupted.
    """
    merged = merge_text(base.read_text(), ours.read_text(), theirs.read_text())
    storage.write_text(ours, merged)


def main(argv: list[str] | None = None) -> int:
    """Git's merge driver: `base ours theirs`, the merged card written into `ours`."""
    arguments = sys.argv[1:] if argv is None else argv
    if len(arguments) != 3:
        print("usage: python -m latticedb.card_merge BASE OURS THEIRS", file=sys.stderr)
        return 2
    base, ours, theirs = (Path(argument) for argument in arguments)
    try:
        merge_files(base, ours, theirs)
    except Unreadable as unreadable:
        print(unreadable, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
