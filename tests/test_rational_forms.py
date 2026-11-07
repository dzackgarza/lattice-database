"""#18: rational-valued card forms are admitted through the existing application paths.

The original `a2-su21-satake` page at 406b357c7f failed with `Fraction(2, 1)`. Its actual card is
used unchanged here. A legal scalar `1/2` Gram tensor (the one in the provider's handover) is the
rank-one case checked through the relational-admission and stored-morphism application code.

These are behavior assertions against the actual owner operations, not a simulation of a Sage provider.
"""

from fractions import Fraction
from pathlib import Path

import frontmatter

from latticedb import records
from latticedb.corpus import front_matter
from latticedb.graphs import WeightedGraph
from latticedb.model import Lattice, Morphism


def test_the_original_a2_su21_satake_page_constructs_its_form() -> None:
    """Reproduce run 42327825818's exact page input: constructing each encoded root pairing."""
    source = Path(__file__).resolve().parent.parent / "graphs" / "a2-su21-satake.md"
    graph = frontmatter.load(str(source)).metadata
    form = WeightedGraph.model_validate(graph)._gram_form()
    assert form is not None
    # Both displayed simple roots have root_length_squared 2, while the Cartan pairing off the
    # diagonal is -1. Reproducing that form, not just invoking a constructor, is the acceptance.
    assert form.gram_tensor() == ((Fraction(2), Fraction(-1)), (Fraction(-1), Fraction(2)))


def rational_card() -> Lattice:
    """A genuine rank-one rational-valued card; it states no integer Gram entry."""
    return Lattice.model_validate({
        "tag": "00R1",
        "name": "An ordinary rational-valued lattice",
        "latex": "\langle 1/2 \rangle",
        "rank": 1,
        "gram_tensor": [["1/2"]],
        "signature": [1, 0],
        "determinant": "1/2",
        "definiteness": "positive_definite",
        "integral": {"parity": "odd"},
        "root_span": {
            "roots": [],
            "norms": [],
            "embedding": [[1]],
            "summands": [{"tag": "00R1", "scale": 1}],
        },
    })


def test_relational_admission_keeps_a_rational_card_gram_tensor() -> None:
    """Its stated orthogonal sum is valid, with no arbitrary scalar coercion."""
    card = rational_card()
    assert records.relational_admission_problems(card, {card.tag: card}) == []


def test_identity_is_a_valid_morphism_for_a_rational_card() -> None:
    """The existing stored-morphism checker accepts the identity through the declared value module."""
    card = rational_card()
    morphism = Morphism.model_validate({
        "target": card.tag,
        "name": "identity",
        "matrix": [[1]],
        "scale": 1,
    })
    assert records.morphism_problems(morphism, card, card) == []
