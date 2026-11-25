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
    # Ask the actual page form for its stored Gram data, reading coefficients as exact fractions.
    gram = form.gram_tensor()
    actual = tuple(tuple(Fraction(int(gram[row, column].numerator()), int(gram[row, column].denominator())) for column in (0, 1)) for row in (0, 1))
    assert actual == ((Fraction(2), Fraction(-1)), (Fraction(-1), Fraction(2)))


def rational_card() -> Lattice:
    """A genuine rank-one rational-valued card; it states no integer Gram entry."""
    return Lattice.model_validate({
        "tag": "00R1",
        "name": "An ordinary rational-valued lattice",
        "latex": r"\langle 1/2 \rangle",
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


def rational_plane() -> Lattice:
    """The rank-two rational-valued form with Gram (1, -1/2; -1/2, 1) and determinant 3/4.

    This is the shape the triangle's mirror form has in its positive-definite part: two walls of
    norm 1 meeting at the angle pi/3, whose Gram entry is -cos(pi/3) = -1/2. It is a genuine
    rational-valued card -- three of its four entries are not integers -- so every form it presents
    must be constructed in the declared value module rather than by coercing a scalar.
    """
    return Lattice.model_validate({
        "tag": "00R2",
        "name": "Two mirrors at an angle of pi/3",
        "latex": r"\langle 1, -1/2; -1/2, 1 \rangle",
        "rank": 2,
        "gram_tensor": [["1", "-1/2"], ["-1/2", "1"]],
        "signature": [2, 0],
        "determinant": "3/4",
        "definiteness": "positive_definite",
        "integral": {"parity": "odd"},
    })


def test_a_nontrivial_isometry_of_a_rational_form_is_stored_and_admitted() -> None:
    """The exchange of the two mirrors is an isometry of the rational form; a near miss is not.

    $G = \\begin{pmatrix} 1 & -1/2 \\\\ -1/2 & 1 \\end{pmatrix}$ has equal diagonal entries and equal
    off-diagonal entries, so the transposition of the two basis vectors, $P = \\begin{pmatrix}0&1\\\\1&0
    \\end{pmatrix}$, satisfies $P^{\\mathsf T} G P = G$ exactly, and $-P$ and $2P$ satisfy it at scale 1
    and 4 respectively. The matrix $\\begin{pmatrix}1&0\\\\1&1\\end{pmatrix}$ does not, and the checker
    has to say so: an acceptance test that only ever tries the identity cannot tell a working
    form-preserving check from one that answers "yes" to everything.

    Each verdict is `records.morphism_problems`, the repository's own stored-morphism checker, over
    the card's own Gram tensor read as exact rationals through `records.rational_gram`.
    """
    card = rational_plane()
    isometry = Morphism.model_validate({"target": card.tag, "name": "exchange", "matrix": [[0, 1], [1, 0]], "scale": 1})
    assert records.morphism_problems(isometry, card, card) == [], "P^T G P = G for the exchange"
    negated = Morphism.model_validate({"target": card.tag, "name": "minus the exchange", "matrix": [[0, -1], [-1, 0]], "scale": 1})
    assert records.morphism_problems(negated, card, card) == [], "(-P)^T G (-P) = G, so it is an isometry too"
    scaled = Morphism.model_validate({"target": card.tag, "name": "the exchange scaled by 2", "matrix": [[0, 2], [2, 0]], "scale": 4})
    assert records.morphism_problems(scaled, card, card) == [], "(2P)^T G (2P) = 4G, the stated scale"
    shear = Morphism.model_validate({"target": card.tag, "name": "a shear", "matrix": [[1, 0], [1, 1]], "scale": 1})
    assert records.morphism_problems(shear, card, card) == [
        "a shear: the matrix does not define the stated form-preserving morphism"
    ], "a shear of a rational-valued form is not an isometry, and the checker must reject it"
    wrong_scale = Morphism.model_validate({"target": card.tag, "name": "the exchange at the wrong scale", "matrix": [[0, 1], [1, 0]], "scale": 2})
    assert records.morphism_problems(wrong_scale, card, card) == [
        "the exchange at the wrong scale: the matrix does not define the stated form-preserving morphism"
    ], "the scale is part of the claim: G is not 2G"
