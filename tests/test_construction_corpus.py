"""Known lattice constructions become individual cards keyed by their Gram tensors."""

from pathlib import Path

import yaml

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import construction_corpus, corpus, records
from latticedb.model import Lattice

ZZ = session_ring_objects()["ZZ"]


def test_rank_two_sum_corpus_contains_every_multiset_of_rank_one_twists(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    (tmp_path / corpus.RETIRED_FILE).write_text(yaml.safe_dump({}))
    seeds = Lattices(ZZ).Untwisted().Indecomposable().known_objects(max_rank=1)

    result = construction_corpus.populate_standard_sums(tmp_path, seeds, max_rank=2, max_content=2)

    assert result.new_cards == 14
    grams = corpus.gram_index(tmp_path)
    assert len(grams) == 14
    assert all(len(tags) == 1 for tags in grams.values())
    assert "2,0;0,-2" in grams
    assert "1,0;0,-1" in grams
    cards = {
        path.stem: Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
        for path in (tmp_path / "lattices").glob("*.md")
    }
    assert all(
        any(back.tag == tag for back in cards[link.tag].related)
        for tag, card in cards.items()
        for link in card.related
    )
    assert construction_corpus.populate_standard_sums(tmp_path, seeds, max_rank=2, max_content=2).new_cards == 0


def test_construction_prefix_stores_each_eligible_expression(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    (tmp_path / corpus.RETIRED_FILE).write_text(yaml.safe_dump({}))
    category = Lattices(ZZ)
    plane = category("U")

    construction_corpus.populate_construction_prefix(
        tmp_path, (plane,), max_expressions=5, max_rank=4, max_content=2
    )

    expected = (
        plane,
        category.orthogonal_sum((plane, plane)),
        category.tensor_product((plane, plane)),
        plane.twist(2),
        plane.twist(-2),
    )
    grams = corpus.gram_index(tmp_path)
    for lattice in expected:
        assert corpus.gram_key(construction_corpus.records.gram_tensor(construction_corpus._gram_rows(lattice))) in grams
    cards = [Lattice.model_validate(corpus.front_matter(corpus.read_card(path))) for path in (tmp_path / "lattices").glob("*.md")]
    assert all(card.rank <= 4 for card in cards)
    assert construction_corpus.populate_construction_prefix(
        tmp_path, (plane,), max_expressions=5, max_rank=4, max_content=2
    ).new_cards == 0


def test_construction_prefix_stores_proper_gluing_inclusions(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    (tmp_path / corpus.RETIRED_FILE).write_text(yaml.safe_dump({}))
    plane = Lattices(ZZ)("U").twist(2)

    construction_corpus.populate_construction_prefix(
        tmp_path, (plane,), max_expressions=4, max_rank=2, max_content=2
    )

    cards = {
        path.stem: Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
        for path in (tmp_path / "lattices").glob("*.md")
    }
    assert all(card.rank == 2 for card in cards.values())
    assert sum(len(card.morphisms) for card in cards.values()) == 3
    assert all(morphism.scale == 1 and morphism.target in cards for card in cards.values() for morphism in card.morphisms)
    assert all(
        records.morphism_problems(morphism, card, cards[morphism.target]) == []
        for card in cards.values()
        for morphism in card.morphisms
    )
    assert all(
        any(back.tag == tag for back in cards[link.tag].related)
        for tag, card in cards.items()
        for link in card.related
    )


def test_standard_products_visit_tensor_and_gluing_families(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    (tmp_path / corpus.RETIRED_FILE).write_text(yaml.safe_dump({}))
    category = Lattices(ZZ)
    plane = category("U")

    construction_corpus.populate_standard_products(
        tmp_path, (plane,), max_rank=4, max_content=2,
        max_inclusions_per_source=4,
    )

    cards = {
        path.stem: Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
        for path in (tmp_path / "lattices").glob("*.md")
    }
    product = category.tensor_product((plane, plane))
    product_rows = tuple(
        tuple(int(product.gram_tensor()[i, j]) for j in range(4))
        for i in range(4)
    )
    assert any(card.gram_tensor == product_rows for card in cards.values())
    assert sum(len(card.morphisms) for card in cards.values()) >= 3
    assert all(
        records.morphism_problems(morphism, card, cards[morphism.target]) == []
        for card in cards.values()
        for morphism in card.morphisms
    )


def test_overlattice_sweep_uses_stored_sum_card(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    (tmp_path / corpus.RETIRED_FILE).write_text(yaml.safe_dump({}))
    plane = Lattices(ZZ)("U")
    construction_corpus.populate_standard_sums(
        tmp_path, (plane,), max_rank=2, max_content=2
    )
    cards = {
        path.stem: Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
        for path in (tmp_path / "lattices").glob("*.md")
    }
    scaled_gram = ((0, 2), (2, 0))
    source_tag = next(tag for tag, card in cards.items() if card.gram_tensor == scaled_gram)

    construction_corpus.populate_overlattices_of_cards(
        tmp_path, (source_tag,), max_rank=2, max_content=2
    )

    updated = {
        path.stem: Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
        for path in (tmp_path / "lattices").glob("*.md")
    }
    assert len(updated[source_tag].morphisms) == 3
    assert all(
        records.morphism_problems(morphism, updated[source_tag], updated[morphism.target]) == []
        for morphism in updated[source_tag].morphisms
    )


def test_standard_products_keep_both_tensor_presentations(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    (tmp_path / corpus.RETIRED_FILE).write_text(yaml.safe_dump({}))
    category = Lattices(ZZ)
    plane, a2 = category("U"), category("A2")

    construction_corpus.populate_standard_products(
        tmp_path, (plane, a2), max_rank=4, max_content=1,
        max_inclusions_per_source=0,
    )

    grams = corpus.gram_index(tmp_path)
    left = category.tensor_product((plane, a2))
    right = category.tensor_product((a2, plane))
    left_key = corpus.gram_key(records.gram_tensor(construction_corpus._gram_rows(left)))
    right_key = corpus.gram_key(records.gram_tensor(construction_corpus._gram_rows(right)))
    assert left_key != right_key
    assert left_key in grams and right_key in grams
