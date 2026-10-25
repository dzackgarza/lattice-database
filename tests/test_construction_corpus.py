"""Known lattice constructions become individual cards keyed by their Gram tensors."""

from pathlib import Path

import yaml

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import construction_corpus, corpus
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
