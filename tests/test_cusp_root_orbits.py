"""The orbits of the root classes at a cusp: what the corpus decides of a row (#43).

A row of `integral.cusp_root_orbits` states, at one 0-cusp $\\mathbb{Z}v$ of a subgroup and for one of the
eight standard subgroups or a named one, the $\\Gamma_v$-orbits of the root classes of $K_J = v^\\perp/\\mathbb{Z}v$:
their count, one representative per orbit, and the order of each orbit's transporter group. The schema decides
what a row states; the preamble's admission check decides the arithmetic, which is the card's own Gram tensor and
nothing else:
the cusp is isotropic, every class lies in its $v^\\perp$, and every class has square $-2$, so a wall of square
$-4$ --- no root --- is reported rather than counted. Two rows for one subgroup at one cusp are one row stated
twice, and a key that is neither one of the eight nor an arithmetic-group card of this lattice names no group.

The rows here are this file's fixture: card 029J's own cusp and its own two roots of $K_J$ at Sterk's (4.3.8),
p. 23, with the orbit count as the shape of a row and not as a claim about the card, which states none
(the cusp stabilizer's generators are not certified complete, sage-extensions#312).
"""

from pathlib import Path

from latticedb import checks, corpus, records
from latticedb.model import Lattice

ROOT = Path(__file__).resolve().parent.parent

CUSP = (0, 0, 2, 1, -4, -5, -7, -10, -8, -6, -4, -2)
"""Sterk's (4.3.8), p. 23: the cusp vector card 029J stores for $\\Gamma_{\\mathrm{En},2}$'s fourth cusp."""

ALPHA_9 = (-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
ALPHA_11 = (1, 1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0)
"""The two roots of $K_J$ among the eleven walls of Fig. 10, in the card's own coordinates."""

ALPHA_2 = (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
"""A wall of that chamber of square $-4$: orthogonal to the cusp, and no root of $K_J$."""

EP = (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
"""A vector of the lattice that is no class of $K_J$: it pairs $2$ with the cusp."""


def row(**changes) -> dict:
    """One row at Sterk's fourth cusp: two orbits of one root class each, with the identity transporter."""
    stated = {
        "cusp": list(CUSP),
        "statement": "4.3.8",
        "printed_page": 23,
        "orbits": [
            {"representative": list(ALPHA_9), "classes": [list(ALPHA_9)], "transporter_order": 1},
            {"representative": list(ALPHA_11), "classes": [list(ALPHA_11)], "transporter_order": 1},
        ],
        "orbit_count": 2,
    }
    return {**stated, **changes}


def problems(*rows: dict, key: str = "O") -> list[str]:
    """The catalogue problems of card 029J with these rows added under `key`, in a corpus of that one card."""
    metadata = corpus.front_matter(corpus.read_card(ROOT / "lattices" / "029J.md"))
    metadata["integral"] = {**metadata["integral"], "cusp_root_orbits": {key: list(rows)}}
    lattice = Lattice.model_validate(metadata)
    loaded = corpus.Corpus(
        entries=(corpus.Entry(lattice, "", ROOT / "lattices" / "029J.md"),),
        families={},
        retired={},
        geometric=(),
        geometric_families=(),
        graphs=(),
        genera=(),
        polytopes=(),
        toric_varieties=(),
        geometric_maps=(),
        local_systems=(),
        operators=(),
        moduli_problems=(),
        lattice_families=(),
        lie_groups=(),
        arithmetic_groups=(),
    )
    # The fixture corpus is card 029J alone, so the checks of the arithmetic-group cards it names report
    # their absence; what this file is about is the field, and this keeps the rest out of the assertion.
    return [problem for problem in checks.catalogues.reference_problems(loaded) if "cusp_root_orbits" in problem]


def test_the_root_classes_of_a_cusp_are_admitted_when_they_lie_in_its_v_perp_and_have_square_minus_two() -> None:
    """The two roots of $K_J$ at Sterk's fourth cusp are what the field asks for, and nothing is reported."""
    assert problems(row()) == []


def admissions(*rows: dict) -> list[str]:
    """What the preamble decides of card 029J with these rows added to the field."""
    metadata = corpus.front_matter(corpus.read_card(ROOT / "lattices" / "029J.md"))
    metadata["integral"] = {**metadata["integral"], "cusp_root_orbits": {"O": list(rows)}}
    return records.local_admission_problems(Lattice.model_validate(metadata))


def test_a_wall_that_is_no_root_of_the_boundary_lattice_is_reported() -> None:
    """A $-4$-wall of the chamber lies in $v^\\perp$ and is no root: a row that counted its orbit would report."""
    assert admissions(row()) == []
    stated = row(orbit_count=1, orbits=[{"representative": list(ALPHA_2), "classes": [list(ALPHA_2)], "transporter_order": 1}])
    found = admissions(stated)
    assert len(found) == 1 and "has square -4, not -2, so it is no root" in found[0], found


def test_a_class_outside_the_cusp_orthogonal_is_reported() -> None:
    """A vector that pairs with the cusp is no class of $K_J = v^\\perp/\\mathbb{Z}v$."""
    stated = row(orbit_count=1, orbits=[{"representative": list(EP), "classes": [list(EP)], "transporter_order": 1}])
    found = admissions(stated)
    assert len(found) == 1 and "does not lie in the v^perp of the cusp" in found[0], found


def test_two_rows_at_one_cusp_are_one_row_stated_twice() -> None:
    """A subgroup states the orbits at a cusp once, as it states one chamber there."""
    found = problems(row(), row())
    assert any("two rows state the orbits at the cusp" in problem for problem in found), found


def test_a_key_that_names_no_arithmetic_group_card_of_this_lattice_is_reported() -> None:
    """The eight standard keys are the card's own; a named subgroup must be an arithmetic-group card of it."""
    assert problems(row()) == []
    found = problems(row(), key="gamma-en-2")
    assert any("cusp_root_orbits names gamma-en-2, which is not an arithmetic-group card" in problem for problem in found), found
