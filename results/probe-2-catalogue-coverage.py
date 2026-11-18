"""What of issue #2's acceptance the corpus already holds, measured against the sources.

Run in the research image:

    run.sh -b $PWD:/repo -w /repo -- /usr/bin/env \
        PYTHONPATH=/repo/research/src:/repo/src /sage/.venv/bin/python \
        results/probe-2-catalogue-coverage.py

A card is matched to a catalogue entry by its Gram tensor and nothing else: the
`GRAM` section is the catalogue's own definition of the entry, and
`gram-index.json` maps a Gram tensor to the tags that state it. A name is not a
match, for two recorded reasons: a dual lattice is not a second record
(`README.md:210`), and the corpus names a lattice by its form, so the root
lattice A1 is the card named `<1>` with alias `I_{1,0}`.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.request import urlopen

from latticedb import nebe_sloane

CATALOGUE = "https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES"
TABLES = (("densest packings", f"{CATALOGUE}/density.html"), ("modular lattices", f"{CATALOGUE}/modular.html"))
# Pages a table links to that are not an entry of the catalogue.
NOT_ENTRIES = {
    "index", "mod_foot", "abbrev", "density", "modular", "unimodular", "perfect", "stronglyperfect",
    "nipp", "nipp5", "ExtLat", "htmltostd", "stdtoGAP", "stdtoMACSYMA", "stdtoMAGMA", "stdtoMAPLE", "stdtoPARI",
}


def gram_key(components: tuple[tuple[int, ...], ...]) -> str:
    """The key `corpus.gram_index` files a Gram tensor under."""
    return ";".join(",".join(str(value) for value in row) for row in components)


def archive() -> dict[str, dict[str, str]]:
    """Catalogue entry name -> {'gram': key} where the section is readable, or {'unreadable': why}."""
    path = Path(__file__).resolve().parent.parent / "sources" / "nebe_sloane" / "union.gz"
    found: dict[str, dict[str, str]] = {}
    for row in nebe_sloane.archive_rows(path):
        gram = row.sections.get("GRAM")
        if gram is None:
            continue
        try:
            found.setdefault(row.name, {"gram": gram_key(nebe_sloane.components(gram))})
        except (AssertionError, ValueError, ArithmeticError) as complaint:
            found.setdefault(row.name, {"unreadable": f"{type(complaint).__name__}: {complaint}"[:80]})
    return found


def table_entries(url: str) -> list[str]:
    """The catalogue entries a table page links to, in page order."""
    with urlopen(url, timeout=60) as response:
        page = response.read().decode("latin-1")
    entries: list[str] = []
    for target in re.findall(r'href="([A-Za-z0-9_.\-+]+?)(?:\.html)?"', page):
        if target in NOT_ENTRIES or not re.search(r"[A-Z]", target) or target in entries:
            continue
        entries.append(target)
    return entries


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    index = json.loads((root / "gram-index.json").read_text())["grams"]
    entries = archive()
    readable = {name: value["gram"] for name, value in entries.items() if "gram" in value}
    unreadable = {name: value["unreadable"] for name, value in entries.items() if "unreadable" in value}
    held = {name: key for name, key in readable.items() if key in index}
    print("== item 1f: every entry of the standard-format archive")
    print(f"entry names stating a GRAM section: {len(entries)}")
    print(f"whose GRAM this intake cannot read: {len(unreadable)}")
    for name, why in sorted(unreadable.items()):
        print(f"    {name}: {why}")
    print(f"whose GRAM a card states: {len(held)} of {len(readable)}")
    print(f"whose GRAM no card states: {len(readable) - len(held)}")
    print("    " + ", ".join(sorted(name for name in readable if name not in held)))
    for title, url in TABLES:
        linked = table_entries(url)
        on_card = [name for name in linked if entries.get(name, {}).get("gram") in index]
        no_card = [name for name in linked if name in readable and readable[name] not in index]
        unknown = [name for name in linked if name not in entries]
        print(f"\n== item 1d/1e: the table of {title}")
        print(f"entries linked: {len(linked)}; with a card: {len(on_card)}; without: {len(no_card)}; not an archive entry: {len(unknown)}")
        print(f"    without a card: {no_card}")
        print(f"    not an archive entry: {unknown}")


if __name__ == "__main__":
    main()
