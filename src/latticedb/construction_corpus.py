"""Author cards for Gram presentations constructed from known lattice specimens.

The preamble supplies every lattice construction and the resulting Gram tensor.
This module assigns cards, joins repeated tensors, and records construction links.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from shutil import disk_usage
from typing import Iterable

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import corpus, records
from latticedb.model import Yaml


_MIN_FREE_BYTES = 2 * 1024**3
ZZ = session_ring_objects()["ZZ"]


@dataclass(frozen=True)
class PopulationResult:
    """Numbers of newly authored and already held Gram presentations."""

    new_cards: int
    existing_cards: int


def _gram_rows(lattice: Lattices.ParentMethods) -> list[list[int]]:
    rank = int(lattice.module_rank())
    gram = lattice.gram_tensor()
    return [[int(gram[row, column]) for column in range(rank)] for row in range(rank)]


def _tag_at(value: int) -> str:
    digits = []
    while value:
        value, digit = divmod(value, len(corpus.TAG_ALPHABET))
        digits.append(corpus.TAG_ALPHABET[digit])
    return "".join(reversed(digits)).zfill(4)


class _CardWriter:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.grams = corpus.gram_index(root)
        self.index = corpus._read_index(root)
        assert self.index is not None
        self.next_number = int(corpus.next_tag(root), len(corpus.TAG_ALPHABET))
        self.new_cards = 0
        self.existing_cards = 0
        self.pending_relations: dict[str, set[tuple[str, str]]] = defaultdict(set)

    def add(self, lattice: Lattices.ParentMethods, operation: str, parents: tuple[str, ...] = ()) -> str:
        rows = _gram_rows(lattice)
        gram = records.gram_tensor(rows)
        key = corpus.gram_key(gram)
        construction = f"{operation} of {', '.join(parents)}" if parents else operation
        held = self.grams.get(key)
        if held:
            tag = held[0]
            self.existing_cards += 1
            for parent in set(parents):
                if parent != tag:
                    self.pending_relations[tag].add((parent, f"This presentation is obtained by {construction}."))
                    self.pending_relations[parent].add((tag, f"This presentation contributes to {tag} by {construction}."))
            return tag

        if self.new_cards % 128 == 0 and disk_usage(self.root).free < _MIN_FREE_BYTES:
            raise OSError("construction corpus stopped before the filesystem fell below 2 GiB free")
        tag = _tag_at(self.next_number)
        self.next_number += 1
        distinct_parents = tuple(dict.fromkeys(parent for parent in parents if parent != tag))
        related: list[dict[str, str]] = [
            {"tag": parent, "relation": f"This presentation is obtained by {construction}."}
            for parent in distinct_parents
        ]
        metadata: dict[str, Yaml] = {
            "tag": tag,
            "name": f"Constructed lattice {tag}",
            "latex": rf"L_{{\mathrm{{{tag}}}}}",
            "rank": int(lattice.module_rank()),
            "gram_tensor": rows,
            "related": related,
        }
        prose = f"The selected Gram tensor is obtained by {construction}."
        path = self.root / "lattices" / f"{tag}.md"
        with path.open("x") as output:
            output.write(records.record_text(metadata, prose))
        self.grams[key] = [tag]
        self.index.grams[key] = [tag]
        self.new_cards += 1
        for parent in distinct_parents:
            self.pending_relations[parent].add((tag, f"This presentation contributes to {tag} by {construction}."))
        if self.new_cards % 1000 == 0:
            corpus.save_index(self.root, self.index)
            print(f"{self.new_cards} construction cards authored", flush=True)
        return tag

    def flush(self) -> None:
        for tag, additions in self.pending_relations.items():
            path = self.root / "lattices" / f"{tag}.md"
            document = corpus.read_card(path)
            metadata = corpus.front_matter(document)
            related = list(metadata.get("related", []))
            held = {(entry["tag"], entry["relation"]) for entry in related}
            for target, relation in sorted(additions):
                if (target, relation) not in held:
                    related.append({"tag": target, "relation": relation})
            metadata["related"] = related
            path.write_text(records.record_text(metadata, document.content))
        self.pending_relations.clear()
        corpus.save_index(self.root, self.index)


def populate_standard_sums(
    root: Path,
    seeds: Iterable[Lattices.ParentMethods],
    *,
    max_rank: int,
    max_content: int,
) -> PopulationResult:
    """Store the twists and unordered orthogonal sums of known untwisted indecomposables.

    The supplied seed family is the preamble's known objects of the property
    category. The caller chooses a finite rank and content; this does not claim
    to enumerate every object of that category. A completed run is idempotent.
    """
    if max_rank < 1 or max_content < 1:
        raise ValueError("max_rank and max_content must be positive")
    category = Lattices(ZZ)
    writer = _CardWriter(root)
    unique: dict[str, Lattices.ParentMethods] = {}
    for lattice in seeds:
        assert lattice in category.Untwisted().Indecomposable()
        if int(lattice.module_rank()) > max_rank:
            continue
        key = corpus.gram_key(records.gram_tensor(_gram_rows(lattice)))
        unique.setdefault(key, lattice)

    variants: list[tuple[Lattices.ParentMethods, str]] = []
    seen: set[str] = set()
    try:
        for base in unique.values():
            base_tag = writer.add(base, "the named standard construction")
            for scale in (1, -1, 2, -2):
                if abs(scale) > max_content:
                    continue
                lattice = base if scale == 1 else base.twist(scale)
                if int(lattice.form_content()) > max_content:
                    continue
                key = corpus.gram_key(records.gram_tensor(_gram_rows(lattice)))
                if key in seen:
                    continue
                seen.add(key)
                tag = base_tag if scale == 1 else writer.add(lattice, f"scaling the form by {scale}", (base_tag,))
                variants.append((lattice, tag))

        def extend(start: int, factors: tuple[Lattices.ParentMethods, ...], tags: tuple[str, ...], rank: int) -> None:
            for index in range(start, len(variants)):
                lattice, tag = variants[index]
                new_rank = rank + int(lattice.module_rank())
                if new_rank > max_rank:
                    continue
                new_factors = (*factors, lattice)
                new_tags = (*tags, tag)
                if factors:
                    result = category.orthogonal_sum(new_factors)
                    writer.add(result, "orthogonal sum", new_tags)
                extend(index, new_factors, new_tags, new_rank)

        extend(0, (), (), 0)
    finally:
        writer.flush()
    return PopulationResult(writer.new_cards, writer.existing_cards)
