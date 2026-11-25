#!/usr/bin/env python3
"""Run the repository's own checks on the cards #40 touches, without reading the whole corpus (lattice-database#40).

`checks.one_shard` calls `corpus.load`, which reads all 302,504 cards (about 7.5 GiB) in one process;
this VM does not have that much free while other work runs, so this reads the four cards `0125`'s
morphisms name plus the `lie-groups` catalogue, and runs the same check modules on them.
"""

from __future__ import annotations

import dataclasses
from pathlib import Path

from latticedb import certificates, corpus
from latticedb.catalogues import LieGroup
from latticedb.checks import catalogues, records, relations

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    invalid: list[str] = []
    scoped = corpus.cards(ROOT, ["0125", "0153", "029J", "029L"])
    loaded = dataclasses.replace(scoped, lie_groups=corpus._catalogue(ROOT, "lie-groups", LieGroup, invalid))
    assert not invalid, invalid
    held = certificates.load(ROOT, tags=["0125"])
    cards = frozenset({"0125"})
    print("records:", records.problems(loaded, held, cards))
    print("morphisms:", relations.morphism_problems(loaded, cards))
    print("catalogues:", catalogues.problems(loaded))
    card = loaded.entries[0].lattice
    print("self-morphisms of 0125:", len([morphism for morphism in card.morphisms if morphism.target == "0125"]))
    print("arithmetic_groups:", card.arithmetic_groups)


if __name__ == "__main__":
    main()
