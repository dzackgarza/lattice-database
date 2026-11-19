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
p. 23, with the orbit count as the shape of a row. The card itself states the four rows it can decide: one cusp whose
root family is a single class, and the three whose chamber carries a symmetry that Sterk states is realized in
$\\Gamma_v$ --- an isometry of $\\Gamma_v$ carrying one root wall to the other is a proof of one orbit, which a
singleton under the certified generators is not.
"""

from fractions import Fraction
from pathlib import Path

import pytest

from latticedb import certificates, checks, corpus, records
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


def test_the_decided_rows_of_card_029j_read_back_and_certify() -> None:
    r"""#43: the four cusps the card can decide carry their counts, and its certificate is on the shard.

    Sterk's (4.3.6), p. 21, has exactly one wall of square $-2$ among its ten, so the cusp's root family is one class
    and its orbits are one orbit whatever the group acting is. The other three cusps have two, two and four root
    classes, and each chamber's diagram carries a symmetry that Sterk states is realized in $\Gamma_v$: at (4.3.7)
    it exchanges $\alpha_9$ and $\alpha_{13}$, at (4.3.8) $\alpha_9$ and $\alpha_{11}$, and at (4.3.9) it is
    transitive on $\alpha_{11}$, $\alpha_{12}$, $\alpha_{13}$, $\alpha_{14}$. One orbit each, so each row's count is
    1 and its single orbit states every one of those classes with its transporter.
    """
    lattice = Lattice.model_validate(corpus.front_matter(corpus.read_card(ROOT / "lattices" / "029J.md")))
    assert lattice.integral is not None and lattice.integral.cusp_root_orbits is not None
    rows = lattice.integral.cusp_root_orbits["gamma-en-2"]
    assert [(row.statement, row.printed_page, row.orbit_count) for row in rows] == [
        ("4.3.6", 21, 1),
        ("4.3.7", 22, 1),
        ("4.3.8", 23, 1),
        ("4.3.9", 24, 1),
    ]
    assert [len(row.orbits) for row in rows] == [1, 1, 1, 1]
    assert [len(row.orbits[0].classes) for row in rows] == [1, 2, 2, 4]
    assert [row.orbits[0].transporter_order for row in rows] == [1, 2, 2, 4]
    single = rows[0]
    assert single.cusp == (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0), "the cusp is e'"
    assert single.orbits[0].representative == (1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), "alpha_10 = e - f"


def test_the_three_cusped_rows_are_one_orbit_because_the_chamber_is_symmetric() -> None:
    r"""#43: what decides the counts is a symmetry of the chamber, recomputed from the shipped card.

    Sterk prints the chamber at each cusp and its Coxeter diagram, and states that the diagram's symmetry is
    realized in the cusp stabilizer: (4.3.7), p. 22, "the symmetry of the diagram comes from an element in
    $\Gamma_v$" with $G_v = \{\pm1\}W_v \rtimes \mathbb{Z}/2$; (4.3.8), p. 23, "the symmetry is induced by an
    element of $\Gamma_v$"; (4.3.9), p. 24, "Symmetries of the graph can be lifted to $\Gamma_v$". So a permutation of
    the chamber's walls that preserves their squares and pairings carries each root class to its image under an
    element of $\Gamma_v$, and one orbit is what this test recomputes from the card's own Gram tensor. A row whose
    classes were split would have no such symmetry, and this test would say which root walls the diagram does not join.
    """
    lattice = Lattice.model_validate(corpus.front_matter(corpus.read_card(ROOT / "lattices" / "029J.md")))
    assert lattice.integral is not None and lattice.integral.cusp_chambers is not None
    assert lattice.integral.cusp_root_orbits is not None
    gram = [[Fraction(entry) for entry in row] for row in lattice.gram_tensor]
    size = len(gram)

    def pairing(left, right):
        return sum(
            (Fraction(left[i]) * gram[i][j] * Fraction(right[j]) for i in range(size) for j in range(size)),
            Fraction(0),
        )

    def wall_permutations(walls):
        """The permutations of the walls that preserve their squares and their pairings, by extension from a seed."""
        squares = [pairing(wall, wall) for wall in walls]
        count = len(walls)
        found = []

        def extend(partial):
            if len(partial) == count:
                found.append(dict(partial))
                return
            index = len(partial)
            for image in range(count):
                if image in partial.values() or squares[image] != squares[index]:
                    continue
                if all(
                    pairing(walls[index], walls[other]) == pairing(walls[image], walls[seen])
                    for other, seen in partial.items()
                ):
                    partial[index] = image
                    extend(partial)
                    del partial[index]

        extend({})
        return found

    rows = {row.statement: row for row in lattice.integral.cusp_root_orbits["gamma-en-2"]}
    checked = []
    for chamber in lattice.integral.cusp_chambers["gamma-en-2"]:
        walls = [tuple(wall.vector) for wall in chamber.walls]
        roots = [index for index in range(len(walls)) if pairing(walls[index], walls[index]) == -2]
        if len(roots) < 2:
            continue
        row = rows[chamber.statement]
        assert len(row.orbits) == 1, f"{chamber.statement}: the card states {len(row.orbits)} orbits"
        assert sorted(tuple(entry) for entry in row.orbits[0].classes) == sorted(walls[index] for index in roots), (
            f"{chamber.statement}: the row's classes are not the chamber's root walls"
        )
        permutations = wall_permutations(walls)
        reached = {min(roots)}
        frontier = [min(roots)]
        while frontier:
            current = frontier.pop()
            for permutation in permutations:
                image = permutation[current]
                if image in roots and image not in reached:
                    reached.add(image)
                    frontier.append(image)
        assert reached == set(roots), (
            f"{chamber.statement}: the diagram's symmetries reach {sorted(reached)} of the root walls {roots}"
        )
        checked.append((chamber.statement, len(roots)))
    assert checked == [("4.3.7", 2), ("4.3.8", 2), ("4.3.9", 4)], checked


def test_a_second_row_at_one_cusp_is_refused_when_it_changes_the_first() -> None:
    """The writer adds a cusp's row and never rewrites one: a different row at a stored cusp stops it."""
    from latticedb import genus

    held = certificates.load(ROOT, tags=("029J",))
    document = corpus.read_card(ROOT / "lattices" / "029J.md")
    metadata = corpus.front_matter(document)
    stored = metadata["integral"]["cusp_root_orbits"]["gamma-en-2"][0]
    changed = {
        **stored,
        "orbits": [{**stored["orbits"][0], "transporter_order": 2}],
    }
    path = ROOT / "lattices" / "029J.md"
    with pytest.raises(AssertionError, match="is stated twice, differently"):
        genus.store_cusp_root_orbits(path, "gamma-en-2", [changed], "a test that changes the row", held)
    assert corpus.front_matter(corpus.read_card(path))["integral"]["cusp_root_orbits"] == metadata["integral"]["cusp_root_orbits"]


COBLE_CUSPS = (
    # (statement, page, cusp in 6JRR's basis, the root classes in 6JRR's basis)
    ("4.3.7", 22, [0, 1, 1, -2, -3, -4, -6, -5, -4, -3, -2], [[1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1]]),
    ("4.3.8", 23, [0, 2, 1, -4, -5, -7, -10, -8, -6, -4, -2], [[1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0]]),
    (
        "4.3.9",
        24,
        [2, 0, 0, -4, -5, -7, -10, -8, -6, -4, -2],
        [
            [1, 3, 3, -2, 1, 2, 2, 1, 0, 0, 0],
            [1, 3, 4, -2, 2, 3, 4, 3, 2, 1, 0],
            [1, 2, 3, -2, 0, 1, 0, 0, 0, 0, 0],
        ],
    ),
)
"""The T_Co side of #43: Sterk's cusps 3--5 and their root classes, in card 6JRR's own basis.

`results/probe-43-coble-row-coordinates.py` carries them there from the chambers stored on 029J: the library's
`delta^perp`, written in $T_{\\mathrm{En}}$'s coordinates, has card 6JRR's Gram tensor entry for entry, so the two
bases are identified by coordinates and no isometry search is needed. What decides membership of
$T_{\\mathrm{Co}} = \\delta^\\perp$ is the pairing with $\\delta$ and not the projection: a projection is integral
whenever $b(v, \\delta)$ is even, and taking that as the test admits walls that are not in the sublattice at all.
"""


def test_the_coble_cusps_rows_are_admissible_values_of_the_field() -> None:
    """#43: the T_Co rows are arithmetic before they are a question of keys.

    Card 6JRR states no `cusp_root_orbits` row, because the field's key must name a subgroup this corpus has a card
    for and there is none for the Coble group. That is a question about *naming* the group; the rows themselves are
    arithmetic on 6JRR's Gram tensor, and this test decides that arithmetic: each cusp is isotropic, each class lies
    in its cusp's perpendicular and has square $-2$, and the row passes the admission check the corpus applies to any
    row of the field. The rows are held under a standard subgroup here, which is a fixture and not a claim about which
    group the card must name.
    """
    metadata = corpus.front_matter(corpus.read_card(ROOT / "lattices" / "6JRR.md"))
    rows = [
        {
            "cusp": cusp,
            "statement": statement,
            "printed_page": page,
            "orbits": [{"representative": classes[0], "classes": classes, "transporter_order": len(classes)}],
            "orbit_count": 1,
        }
        for statement, page, cusp, classes in COBLE_CUSPS
    ]
    metadata["integral"] = {**metadata["integral"], "cusp_root_orbits": {"O": rows}}
    lattice = Lattice.model_validate(metadata)
    assert [len(row.orbits[0].classes) for row in lattice.integral.cusp_root_orbits["O"]] == [1, 1, 3]
    assert records.local_admission_problems(lattice) == []


def test_card_6jrr_states_the_two_decided_coble_cusps() -> None:
    """#43: the two T_Co cusps whose root family is one class each are on the card, under the standard key `O`.

    The decision recorded on the issue: the rows at Sterk's cusps 3 and 4 are stored under the standard subgroup `O`,
    because their root family has one class and a one-class family has one orbit for every subgroup, so the row states
    the same count for `O` and for the Coble group the cusps belong to. The cusp-5 row is not stored: with three
    classes its count depends on the group, which has no card.
    """
    lattice = Lattice.model_validate(corpus.front_matter(corpus.read_card(ROOT / "lattices" / "6JRR.md")))
    assert lattice.integral is not None and lattice.integral.cusp_root_orbits is not None
    rows = lattice.integral.cusp_root_orbits["O"]
    assert [(row.statement, row.printed_page, row.orbit_count) for row in rows] == [("4.3.7", 22, 1), ("4.3.8", 23, 1)]
    assert [len(row.orbits[0].classes) for row in rows] == [1, 1]
    assert [row.orbits[0].representative for row in rows] == [
        (1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    ]
    assert records.local_admission_problems(lattice) == []
    # The certificate is cited on the card and held by its shard; nothing in the field's own checks contradicts.
    cited = lattice.certifications.get("integral.cusp_root_orbits")
    assert cited is not None
    loaded = corpus.cards(ROOT, ("6JRR",))
    held = certificates.load(ROOT, tags=("6JRR",))
    problems = checks.records.problems(loaded, held, frozenset({"6JRR"}))
    assert not [problem for problem in problems if "cusp_root_orbits" in problem], problems


def test_the_coble_group_card_states_the_index_its_computation_certifies() -> None:
    """#43: `gamma-co-2` exists because the library builds the group, and its index is a computation.

    The decision of 2026-11-19 holds the cusp-5 row until this card exists and is certified by computation from the
    library's own construction of $\Gamma_{\mathrm{Co},2} = R_{\Gamma_{\mathrm{En},2}}$ — never authored from the
    project's draft. The card states the parent it restricts inside, the index, and no value it does not compute; this
    test states that, and that 6JRR cites the certificate its shard holds.
    """
    from latticedb.catalogues import ArithmeticGroup

    root = ROOT
    card = ArithmeticGroup.model_validate(corpus.front_matter(corpus.read_card(root / "arithmetic-groups" / "gamma-co-2.md")))
    assert card.lattice == "6JRR" and card.parent_group == "otilde-plus-t-co"
    assert card.data.index_in_orthogonal_group == 93997183795200 * 46998591897600
    assert card.data.cardinality == "aleph0"
    assert card.standard_name is None, "the group is named by construction, not one of the eight"
    loaded = corpus.cards(root, ("6JRR",))
    held = certificates.load(root, tags=("6JRR",))
    lattice = next(entry.lattice for entry in loaded.entries if entry.lattice.tag == "6JRR")
    field = "arithmetic-group.gamma-co-2.index_in_orthogonal_group"
    cited = lattice.certifications.get(field)
    assert cited is not None and held.get("6JRR " + field) is not None
    assert held["6JRR " + field].hash == cited
    entry = next(entry for entry in loaded.entries if entry.lattice.tag == "6JRR")
    assert [problem for problem in checks.records.arithmetic_problems(loaded, held, entry) if "gamma-co-2" in problem] == []


def test_only_one_delta_preserving_symmetry_moves_a_coble_class() -> None:
    r"""#43: of the (4.3.9) diagram's symmetries, two preserve $\delta$ up to sign, and only one moves a class.

    $T_{\mathrm{Co}} = \delta^\perp$ with $\delta = e - f$, so a symmetry of the chamber can be an element of the Coble
    cusp stabilizer only if it carries $\delta$ to $\pm\delta$. This states, from the shipped card, that exactly two of
    the eight do — the identity and one exchanging $\alpha_{13}$ with $\alpha_{14}$ — and that neither carries
    $\alpha_{12}$ to another of the three, which is the question the cusp-5 row waits on
    (`results/issue-43-lemma-coble-image.md`). A change to the card's walls or Gram tensor that moved either fact would
    fail here rather than silently in a lemma.
    """
    from sage.all import QQ, matrix

    lattice = Lattice.model_validate(corpus.front_matter(corpus.read_card(ROOT / "lattices" / "029J.md")))
    assert lattice.integral is not None and lattice.integral.cusp_chambers is not None
    gram = matrix(QQ, [[Fraction(entry) for entry in row] for row in lattice.gram_tensor])
    size = gram.nrows()

    def pairing(left, right):
        return (matrix(QQ, 1, size, list(left)) * gram * matrix(QQ, size, 1, list(right)))[0, 0]

    chamber = next(row for row in lattice.integral.cusp_chambers["gamma-en-2"] if row.statement == "4.3.9")
    walls = [tuple(wall.vector) for wall in chamber.walls]
    names = [wall.name for wall in chamber.walls]
    from sage.all import QQ, vector

    delta = vector(QQ, [1, -1] + [0] * (size - 2))
    squares = [pairing(wall, wall) for wall in walls]

    symmetries: list[dict[int, int]] = []

    def extend(partial: dict[int, int]) -> None:
        if len(partial) == len(walls):
            symmetries.append(dict(partial))
            return
        index = len(partial)
        for image in range(len(walls)):
            if image in partial.values() or squares[image] != squares[index]:
                continue
            if all(pairing(walls[index], walls[other]) == pairing(walls[image], walls[seen]) for other, seen in partial.items()):
                partial[index] = image
                extend(partial)
                del partial[index]

    extend({})
    assert len(symmetries) == 8, len(symmetries)
    independent, chosen = [], []
    for index, wall in enumerate(walls):
        if matrix(QQ, independent + [list(wall)]).rank() > len(independent):
            independent.append(list(wall))
            chosen.append(index)
    basis = matrix(QQ, independent)
    coefficients = (basis * basis.transpose()).inverse() * basis * matrix(QQ, size, 1, list(delta))

    def image_of_delta(symmetry: dict[int, int]):
        from sage.all import QQ, vector

        return vector(
            QQ,
            [
                sum(
                    (coefficients[position, 0] * walls[symmetry[chosen[position]]][row] for position in range(len(independent))),
                    QQ(0),
                )
                for row in range(size)
            ],
        )

    preserving = [symmetry for symmetry in symmetries if image_of_delta(symmetry) in (delta, -delta)]
    assert len(preserving) == 2, len(preserving)
    moved = {
        names[index]: names[symmetry[index]]
        for symmetry in preserving
        for index in range(len(names))
        if symmetry[index] != index
    }
    assert sorted(moved) == sorted(
        ["\\alpha_2", "\\alpha_4", "\\alpha_5", "\\alpha_7", "\\alpha_8", "\\overline{\\widetilde\\alpha}_8", "\\alpha_13", "\\alpha_14"]
    ), sorted(moved)
    twelve = names.index("\\alpha_12")
    assert all(symmetry[twelve] == twelve for symmetry in preserving), "a delta-preserving symmetry moves alpha_12"


def test_card_6jrr_states_the_coble_cusp_of_three_classes_as_two_orbits() -> None:
    r"""#43: Sterk's (4.3.9) on the Coble card is two orbits, $\{\alpha_{12}\}$ and $\{\alpha_{13},\alpha_{14}\}$.

    The argument is printed: `(4.3.3)`, p. 18, has $G = W(G) \rtimes S$ with $S$ the diagram symmetries realised in $G$;
    `(4.3.9)`, p. 24, says the symmetries lift; and every reflection in a $T_{\mathrm{Co}}$ wall fixes
    $\delta = e - f$, so whether an element preserves $T_{\mathrm{Co}}$ is decided on $S$ alone. Of the eight
    symmetries exactly two fix $\delta$ — the identity and the one exchanging $\alpha_{13}$ with $\alpha_{14}$ — so the
    Coble image is $\langle W_v, \sigma\rangle$, which fixes $\alpha_{12}$.
    """
    lattice = Lattice.model_validate(corpus.front_matter(corpus.read_card(ROOT / "lattices" / "6JRR.md")))
    assert lattice.integral is not None and lattice.integral.cusp_root_orbits is not None
    rows = lattice.integral.cusp_root_orbits["gamma-co-2"]
    assert [(row.statement, row.orbit_count) for row in rows] == [("4.3.9", 2)]
    row = rows[0]
    assert row.printed_page == 24
    assert [len(orbit.classes) for orbit in row.orbits] == [1, 2]
    assert [orbit.transporter_order for orbit in row.orbits] == [1, 2]
    assert [orbit.representative for orbit in row.orbits] == [
        (1, 3, 3, -2, 1, 2, 2, 1, 0, 0, 0),
        (1, 3, 4, -2, 2, 3, 4, 3, 2, 1, 0),
    ]
    assert sorted(tuple(entry) for entry in row.orbits[1].classes) == sorted(
        [(1, 3, 4, -2, 2, 3, 4, 3, 2, 1, 0), (1, 2, 3, -2, 0, 1, 0, 0, 0, 0, 0)]
    )
    assert records.local_admission_problems(lattice) == []


def test_the_chambers_own_reflections_do_not_move_the_root_classes() -> None:
    """#43: at every cusped row the root walls have different orthogonal neighbour sets, so no word in the walls moves one to another.

    The chamber's walls generate the reflection subgroup $W_v$ of the cusp stabilizer, and every wall is orthogonal to
    the cusp, so every reflection in one of them fixes the cusp: $W_v \\subseteq \\Gamma_v$. In a Coxeter system
    conjugate standard parabolics are equal, and the setwise stabilizer of a wall's mirror is the parabolic generated
    by that wall together with the walls orthogonal to it, so two walls in one $W_v$-orbit have equal orthogonal
    neighbour sets. Different sets are therefore a proof that no word in the walls carries one root class to the other
    --- which is why these counts are not a question a search can answer: the part of $\\Gamma_v$ that this card can
    construct provably cannot identify the classes, and the rest is what a primitive isotropic line withholds
    (sage-extensions#603).
    """
    lattice = Lattice.model_validate(corpus.front_matter(corpus.read_card(ROOT / "lattices" / "029J.md")))
    assert lattice.integral is not None and lattice.integral.cusp_chambers is not None
    gram = [[Fraction(entry) for entry in row] for row in lattice.gram_tensor]

    def pairing(left: tuple[int, ...], right: tuple[int, ...]):
        return sum((Fraction(left[i]) * gram[i][j] * Fraction(right[j]) for i in range(len(gram)) for j in range(len(gram))), Fraction(0))

    root_counts = []
    for row in lattice.integral.cusp_chambers["gamma-en-2"]:
        walls = [tuple(wall.vector) for wall in row.walls]
        roots = [index for index in range(len(walls)) if pairing(walls[index], walls[index]) == -2]
        root_counts.append(len(roots))
        neighbours = {
            index: frozenset(j for j in range(len(walls)) if j != index and pairing(walls[index], walls[j]) == 0)
            for index in roots
        }
        assert len(set(neighbours.values())) == len(roots), f"{row.statement}: two root walls share their orthogonal neighbour set"
        for earlier in range(len(roots)):
            for later in range(earlier + 1, len(roots)):
                left, right = neighbours[roots[earlier]], neighbours[roots[later]]
                assert left != right, f"{row.statement}: {row.walls[roots[earlier]].name} and {row.walls[roots[later]].name} agree"
                shown = sorted(left.symmetric_difference(right))
                assert shown, f"{row.statement}: no wall tells {row.walls[roots[earlier]].name} from {row.walls[roots[later]].name}"
    assert root_counts == [0, 1, 2, 2, 4], root_counts
