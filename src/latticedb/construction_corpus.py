"""Author cards for Gram presentations constructed from known lattice specimens.

The preamble supplies every lattice construction and the resulting Gram tensor.
This module assigns cards, joins repeated tensors, and records construction links.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from shutil import disk_usage
from typing import Iterable

from sage_extensions.categories.lattices import Lattices
from sage_extensions.categories.lattice_morphisms import LatticeEmbeddingMethods
from sage_extensions.rings import session_ring_objects

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
        self.pending_morphisms: dict[str, list[dict[str, Yaml]]] = defaultdict(list)

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
        for tag in self.pending_relations.keys() | self.pending_morphisms.keys():
            path = self.root / "lattices" / f"{tag}.md"
            document = corpus.read_card(path)
            metadata = corpus.front_matter(document)
            related = list(metadata.get("related", []))
            held = {(entry["tag"], entry["relation"]) for entry in related}
            for target, relation in sorted(self.pending_relations.get(tag, ())):
                if (target, relation) not in held:
                    related.append({"tag": target, "relation": relation})
            metadata["related"] = related
            morphisms = list(metadata.get("morphisms", []))
            existing_maps = {(entry["target"], tuple(tuple(row) for row in entry["matrix"])) for entry in morphisms}
            for morphism in self.pending_morphisms.get(tag, ()):
                key = (morphism["target"], tuple(tuple(row) for row in morphism["matrix"]))
                if key not in existing_maps:
                    morphisms.append(morphism)
                    existing_maps.add(key)
            if morphisms:
                metadata["morphisms"] = morphisms
            path.write_text(records.record_text(metadata, document.content))
        self.pending_relations.clear()
        self.pending_morphisms.clear()
        corpus.save_index(self.root, self.index)


def _store_inclusion(writer: _CardWriter, source: str, target: str, inclusion: LatticeEmbeddingMethods) -> None:
    domain = inclusion.domain()
    codomain = inclusion.codomain()
    assert int(inclusion.index()) > 1
    assert int(domain.module_rank()) == int(codomain.module_rank())
    columns = tuple(
        inclusion(domain.module_generator(label)).to_vector()
        for label in domain.module_generating_set()
    )
    writer.pending_morphisms[source].append({
        "target": target,
        "name": f"Integral overlattice inclusion of index {int(inclusion.index())}",
        "matrix": [
            [int(ZZ(column(label))) for column in columns]
            for label in codomain.module_generating_set()
        ],
        "scale": 1,
    })


def _standard_variants(
    writer: _CardWriter,
    seeds: Iterable[Lattices.ParentMethods],
    max_rank: int,
    max_content: int,
) -> list[tuple[Lattices.ParentMethods, str]]:
    category = Lattices(ZZ)
    unique: dict[str, Lattices.ParentMethods] = {}
    for lattice in seeds:
        assert lattice in category.Untwisted().Indecomposable()
        if int(lattice.module_rank()) > max_rank:
            continue
        key = corpus.gram_key(records.gram_tensor(_gram_rows(lattice)))
        unique.setdefault(key, lattice)

    variants: list[tuple[Lattices.ParentMethods, str]] = []
    seen: set[str] = set()
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
    return variants


def populate_construction_prefix(
    root: Path,
    seeds: Iterable[Lattices.ParentMethods],
    *,
    max_expressions: int,
    max_rank: int,
    max_content: int,
) -> PopulationResult:
    """Store an initial segment of the preamble's unbounded construction enumeration.

    ``max_expressions`` bounds this database run, not the mathematical iterator.
    Each eligible expression retains its construction links. Proper overlattice
    inclusions also become stored morphisms on their source cards.
    """
    if max_expressions < 0 or max_rank < 1 or max_content < 1:
        raise ValueError("max_expressions must be nonnegative and rank/content positive")
    category = Lattices(ZZ)
    writer = _CardWriter(root)
    tags: dict[int, str] = {}
    try:
        for expression in islice(category.construction_enumeration(seeds), max_expressions):
            lattice = expression.lattice
            if int(lattice.module_rank()) > max_rank or int(lattice.form_content()) > max_content:
                continue
            parents = tuple(tags[id(factor)] for factor in expression.factors if id(factor) in tags)
            if len(parents) != len(expression.factors):
                continue
            tag = writer.add(lattice, expression.operation, parents)
            tags[id(expression)] = tag
            if expression.operation == "overlattice":
                inclusion = expression.witness
                assert inclusion is not None
                _store_inclusion(writer, parents[0], tag, inclusion)
    finally:
        writer.flush()
    return PopulationResult(writer.new_cards, writer.existing_cards)


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
    try:
        variants = _standard_variants(writer, seeds, max_rank, max_content)

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


def populate_standard_products(
    root: Path,
    seeds: Iterable[Lattices.ParentMethods],
    *,
    max_rank: int,
    max_content: int,
    max_inclusions_per_source: int | None = None,
) -> PopulationResult:
    """Store tensor products of all known small twists and their proper overlattices.

    The optional inclusion count is a database-run budget. With no count, every
    inclusion supplied by the preamble is visited for each source.
    """
    if max_rank < 1 or max_content < 1:
        raise ValueError("max_rank and max_content must be positive")
    if max_inclusions_per_source is not None and max_inclusions_per_source < 0:
        raise ValueError("max_inclusions_per_source must be nonnegative")
    category = Lattices(ZZ)
    writer = _CardWriter(root)
    try:
        variants = _standard_variants(writer, seeds, max_rank, max_content)
        sources: dict[str, tuple[Lattices.ParentMethods, str]] = {
            corpus.gram_key(records.gram_tensor(_gram_rows(lattice))): (lattice, tag)
            for lattice, tag in variants
        }
        for left, left_tag in variants:
            for right, right_tag in variants:
                if int(left.module_rank()) * int(right.module_rank()) > max_rank:
                    continue
                product = category.tensor_product((left, right))
                if int(product.form_content()) > max_content:
                    continue
                tag = writer.add(product, "tensor product", (left_tag, right_tag))
                key = corpus.gram_key(records.gram_tensor(_gram_rows(product)))
                sources.setdefault(key, (product, tag))
        for lattice, source_tag in sources.values():
            if max_inclusions_per_source == 0:
                continue
            if lattice.is_nondegenerate() is not True:
                continue
            inclusions = lattice.integral_overlattice_inclusions()
            if max_inclusions_per_source is not None:
                inclusions = islice(inclusions, max_inclusions_per_source)
            for inclusion in inclusions:
                if int(inclusion.index()) == 1:
                    continue
                target = inclusion.codomain()
                if int(target.form_content()) > max_content:
                    continue
                target_tag = writer.add(target, "taking a proper integral overlattice", (source_tag,))
                _store_inclusion(writer, source_tag, target_tag, inclusion)
    finally:
        writer.flush()
    return PopulationResult(writer.new_cards, writer.existing_cards)


def populate_overlattices_of_cards(
    root: Path,
    tags: Iterable[str],
    *,
    max_rank: int,
    max_content: int,
    max_sources: int | None = None,
    max_inclusions_per_source: int | None = None,
) -> PopulationResult:
    """Store preamble-supplied proper integral overlattices of selected cards."""
    if max_rank < 1 or max_content < 1:
        raise ValueError("max_rank and max_content must be positive")
    if max_sources is not None and max_sources < 0:
        raise ValueError("max_sources must be nonnegative")
    if max_inclusions_per_source is not None and max_inclusions_per_source < 0:
        raise ValueError("max_inclusions_per_source must be nonnegative")
    category = Lattices(ZZ)
    selected: list[tuple[int, str, list[list[int]]]] = []
    for tag in set(tags):
        metadata = corpus.front_matter(corpus.read_card(root / "lattices" / f"{tag}.md"))
        gram = metadata.get("gram_tensor")
        if gram is None:
            continue
        rank = len(gram)
        if rank <= max_rank:
            selected.append((rank, tag, gram))
    selected.sort(key=lambda entry: (entry[0], int(entry[1], len(corpus.TAG_ALPHABET))))
    if max_sources is not None:
        selected = selected[:max_sources]

    writer = _CardWriter(root)
    try:
        for _, source_tag, gram in selected:
            if max_inclusions_per_source == 0:
                continue
            lattice = category(gram)
            if int(lattice.form_content()) > max_content or lattice.is_nondegenerate() is not True:
                continue
            inclusions = lattice.integral_overlattice_inclusions()
            if max_inclusions_per_source is not None:
                inclusions = islice(inclusions, max_inclusions_per_source)
            for inclusion in inclusions:
                if int(inclusion.index()) == 1:
                    continue
                target = inclusion.codomain()
                if int(target.form_content()) > max_content:
                    continue
                target_tag = writer.add(target, "taking a proper integral overlattice", (source_tag,))
                _store_inclusion(writer, source_tag, target_tag, inclusion)
    finally:
        writer.flush()
    return PopulationResult(writer.new_cards, writer.existing_cards)
