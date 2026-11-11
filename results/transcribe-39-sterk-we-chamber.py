#!/usr/bin/env python3
"""Transcribe Sterk's chamber of W_e ⊂ G_e onto card 0125, under the key of G_e (lattice-database#39).

The source is H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z.
207 (1991), 1-36, (4.3.5), p. 19, read from the PDF text layer of
`tmp/sources/sterk-1991-compactifications-of-the-period-space-of-enriques-surfaces-i.pdf` (printed page
numbers agree with the PDF's) and its OCR `tmp/sterk-1991-part-i.md`.

What the statement prints. `e^⊥/Ze ≅ H(2) ⊕ E8(-2) = U(2) ⊕ E8(-2)` (4.3.4), p. 19, which is card 0125.
The diagram of `W_e ⊂ G_e` is Fig. 4, p. 19, with twelve nodes — `alpha_1, ..., alpha_8`, the E8 simple
roots, and the four streams printed beside the figure:

    alpha_9  = f' - e'
    alpha_10 = bar_alpha_8 + 2e'
    alpha_11 = 2e' + 2f' + bar_alpha_1 + bar_alpha_8
    alpha_12 = 5e' + 3f' + 2 bar_alpha_2

with `(e', e') = (f', f') = 0`, `(e', f') = 2` in the H(2) summand, and `bar_alpha_i` the dual of
`alpha_i` in E8(-2), `(bar_alpha_i, alpha_j) = 2 delta_ij`. Sterk's Fig. 4 marks every node with a
circle, so every wall has square -4, and the print of (4.3.5) checks its own reading:
`(alpha_k, e' + f')^2 / |(alpha_k, alpha_k)| = 4, 16, 64` for `k = 10, 11, 12`.

Fig. 5, p. 20, prints the maximal parabolic subdiagrams *modulo symmetries*, and p. 20 reads "we do not
only find four equivalence classes in I_1(e^⊥/Ze), but that we find four labelled classes". A maximal
parabolic subdiagram is a vertex at infinity of the chamber, by Vinberg's criterion that the vertices at
infinity are the parabolic subdiagrams of rank n - 1 (Vinberg 1972; Sterk (4.3.3), p. 18). The four
classes are the orbits of those subdiagrams under the symmetries of the diagram, which Sterk identifies
with `S_e ≅ Z/2 × Z/2` — so the row states them as orbits and no vertex count, the vertices of one
class being different vertices of the chamber.

The walls are the source's; the Gram matrix, the Coxeter diagram and the ideal vertices are what the
card's Gram tensor says about them, and the owner's Coxeter-diagram owner is asked for the diagram and
its automorphism group rather than the recognition being repeated here.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from latticedb import certificates, corpus, genus
from latticedb.model import Lattice
from sage_extensions.all import ZZ  # noqa: F401
from sage_extensions.categories.coxeter_diagrams import CoxeterDiagrams
from sage_extensions.categories.lattices import Lattices
from sage_extensions.categories.sets.indexed_families import finite_indexed_family_from_values

ROOT = Path(__file__).resolve().parent.parent
TAG = "0125"
GROUP = "g-e"
RANK = 10
SAGE_EXTENSIONS_REVISION = "5a9874e22ea18fb223ff53cf2a3e48dd63c022b4"
"""The sage-extensions commit whose Coxeter-diagram owner produced the diagram and its orbits."""

E8_EDGES = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))
"""The E8 Dynkin diagram in Sterk's numbering (Fig. 1, p. 3): the chain 1-3-4-5-6-7-8 with alpha_2 at alpha_4."""

STERK_TO_CARD = {i: i + 2 for i in range(1, 9)}
"""Sterk's alpha_i is the card's e_k, 1-indexed: the U(2) summand is e_1, e_2 and E8(-2) is e_3, ..., e_10."""


def cartan() -> list[list[Fraction]]:
    """The E8 Cartan matrix in Sterk's numbering."""
    matrix = [[Fraction(2 if i == j else 0) for j in range(8)] for i in range(8)]
    for i, j in E8_EDGES:
        matrix[i - 1][j - 1] = Fraction(-1)
        matrix[j - 1][i - 1] = Fraction(-1)
    return matrix


def inverse(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(matrix)
    augmented = [row[:] + [Fraction(int(i == j)) for j in range(size)] for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(row for row in range(column, size) if augmented[row][column] != 0)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for row in range(size):
            if row != column and augmented[row][column] != 0:
                factor = augmented[row][column]
                augmented[row] = [a - factor * b for a, b in zip(augmented[row], augmented[column], strict=True)]
    return [row[size:] for row in augmented]


def combine(terms: dict[str, int]) -> tuple[int, ...]:
    """A vector written in Sterk's basis: `e`, `f`, and `a1` .. `a8` for the simple roots."""
    basis = [0] * RANK
    for name, value in terms.items():
        match name:
            case "e":
                basis[0] += value
            case "f":
                basis[1] += value
            case _:
                basis[STERK_TO_CARD[int(name[1:])] - 1] += value
    return tuple(basis)


class Form:
    """The card's own bilinear form, evaluated on vectors of the card's basis."""

    def __init__(self, gram: tuple[tuple[Fraction, ...], ...]) -> None:
        self.gram = gram

    def of(self, u: tuple[int, ...], v: tuple[int, ...]) -> Fraction:
        return sum(Fraction(u[i]) * self.gram[i][j] * Fraction(v[j]) for i in range(RANK) for j in range(RANK))

    def norm(self, u: tuple[int, ...]) -> Fraction:
        return self.of(u, u)

    def times(self, u: tuple[int, ...], scalar: int) -> tuple[int, ...]:
        return tuple(scalar * entry for entry in u)

    def plus(self, u: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(a + b for a, b in zip(u, v, strict=True))

    def minus(self, u: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(a - b for a, b in zip(u, v, strict=True))

    def add(self, *terms: tuple[int, tuple[int, ...]]) -> tuple[int, ...]:
        total = (0,) * RANK
        for scalar, v in terms:
            total = self.plus(total, self.times(v, scalar))
        return total

    def rank(self, vectors: list[tuple[int, ...]]) -> int:
        """The rank over Q of the vectors' coordinates, by elimination."""
        rows = [[Fraction(entry) for entry in v] for v in vectors]
        count = 0
        for column in range(len(rows[0]) if rows else 0):
            pivot = next((row for row in range(count, len(rows)) if rows[row][column] != 0), None)
            if pivot is None:
                continue
            rows[count], rows[pivot] = rows[pivot], rows[count]
            scale = rows[count][column]
            rows[count] = [entry / scale for entry in rows[count]]
            for row in range(len(rows)):
                if row != count and rows[row][column] != 0:
                    factor = rows[row][column]
                    rows[row] = [a - factor * b for a, b in zip(rows[row], rows[count], strict=True)]
            count += 1
        return count


def diagram(form: Form, walls: list[tuple[str, tuple[int, ...]]]) -> list[dict[str, object]]:
    """The Coxeter diagram: each pair of walls that is not orthogonal, with the order of its reflections."""
    edges: list[dict[str, object]] = []
    orders = {Fraction(1, 4): 3, Fraction(1, 2): 4, Fraction(3, 4): 6}
    for i in range(len(walls)):
        for j in range(i + 1, len(walls)):
            product = form.of(walls[i][1], walls[j][1])
            if product == 0:
                continue
            cosine = product * product / (form.norm(walls[i][1]) * form.norm(walls[j][1]))
            if cosine == 1:
                order: int | str = "inf"
            elif cosine in orders:
                order = orders[cosine]
            else:
                raise SystemExit(f"{walls[i][0]}-{walls[j][0]}: |g|^2 = {cosine} is not cos^2(pi/m)")
            edges.append({"a": walls[i][0], "b": walls[j][0], "order": order})
    return edges


def main() -> None:
    path = ROOT / "lattices" / f"{TAG}.md"
    card = Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
    assert card.gram_tensor is not None
    assert (card.rank, tuple(card.signature or ())) == (RANK, (1, 9)), "0125 is not a rank-10 (1, 9) lattice"
    form = Form(tuple(tuple(Fraction(entry) for entry in row) for row in card.gram_tensor))
    rows = [[int(entry) for entry in row] for row in card.gram_tensor]
    lattice = Lattices(ZZ)(rows)

    # The card is H(2) + E8(-2) in Sterk's decomposition and numbering, which its Gram confirms.
    e, f = combine({"e": 1}), combine({"f": 1})
    assert form.norm(e) == form.norm(f) == 0 and form.of(e, f) == 2, "the first summand of 0125 is not H(2)"
    alpha = {i: combine({f"a{i}": 1}) for i in range(1, 9)}
    for i, j in E8_EDGES:
        a, b = STERK_TO_CARD[i] - 1, STERK_TO_CARD[j] - 1
        assert form.gram[a][b] == 2, f"alpha_{i} and alpha_{j} are not adjacent on the card"
    assert all(form.gram[STERK_TO_CARD[i] - 1][STERK_TO_CARD[i] - 1] == -4 for i in range(1, 9))
    assert all(form.of(e, alpha[i]) == 0 and form.of(f, alpha[i]) == 0 for i in range(1, 9)), "the summands are not orthogonal"

    # bar_alpha_i in the basis of the simple roots: the dual basis with (bar_alpha_i, alpha_j) = 2 delta_ij.
    inverted = inverse(cartan())
    bar = {i: combine({f"a{j + 1}": -int(inverted[i - 1][j]) for j in range(8)}) for i in range(1, 9)}
    for i in range(1, 9):
        for j in range(1, 9):
            assert form.of(bar[i], alpha[j]) == (2 if i == j else 0), f"(bar_alpha_{i}, alpha_{j})"

    # (4.3.5), p. 19, Fig. 4: the twelve walls.
    walls: list[tuple[str, tuple[int, ...]]] = [(f"\\alpha_{i}", alpha[i]) for i in range(1, 9)]
    walls += [
        ("\\alpha_9", form.minus(f, e)),
        ("\\alpha_10", form.add((2, e), (1, bar[8]))),
        ("\\alpha_11", form.add((2, e), (2, f), (1, bar[1]), (1, bar[8]))),
        ("\\alpha_12", form.add((5, e), (3, f), (2, bar[2]))),
    ]
    names = [name for name, _ in walls]
    # Fig. 4 circles every node: every wall has square -4.
    assert [form.norm(v) for _, v in walls] == [-4] * 12, [form.norm(v) for _, v in walls]
    # (4.3.5) checks its own reading of the controlling vector e' + f' on the three printed walls.
    controlling = form.add((1, e), (1, f))
    printed = [form.of(controlling, walls[k][1]) ** 2 / abs(form.norm(walls[k][1])) for k in (9, 10, 11)]
    assert printed == [4, 16, 64], f"(4.3.5) prints 4, 16, 64 for alpha_10, alpha_11, alpha_12 and the card gives {printed}"
    # The chamber is full-dimensional: its walls span L over Q.
    assert form.rank([v for _, v in walls]) == RANK, "the walls do not span L over Q"
    edges = diagram(form, walls)

    # The owner's Coxeter-diagram owner reads the same walls: same twelve vertices, and its automorphism
    # group is S_e, which Sterk gives as Z/2 x Z/2.
    roots = tuple(lattice(v) for _, v in walls)
    owned = CoxeterDiagrams().from_roots(finite_indexed_family_from_values(None, roots))
    assert int(owned.cardinality()) == len(walls), "the owner's diagram does not have one vertex per wall"
    symmetries = owned.Aut()
    assert int(symmetries.cardinality()) == 4, f"S_e has order 4 and the diagram's automorphisms have order {symmetries.cardinality()}"
    # The diagram the card stores is the owner's on the same walls.
    mine = {frozenset((names.index(str(edge["a"])), names.index(str(edge["b"])))) for edge in edges}
    theirs = {frozenset((int(i), int(j))) for i, j in owned.edges()}
    assert mine == theirs, f"the card's diagram {sorted(map(sorted, mine))} is not the owner's {sorted(map(sorted, theirs))}"

    # The ideal vertices: the rays of the chamber that lie on the light cone. Each is a maximal parabolic
    # subdiagram — the walls orthogonal to it — of rank n - 1 = 8 (Vinberg's criterion, (4.3.3), p. 18).
    cone = lattice.rational_polyhedral_cone(tuple(lattice.algebraic_correlation_morphism()(root) for root in roots), wall_roots=roots, complete=True)
    rays = [tuple(int(entry) for entry in ray) for ray in cone.primitive_rays()]
    ideal = [ray for ray in rays if form.norm(ray) == 0]
    assert all(form.norm(ray) >= 0 for ray in rays), "a ray of the chamber is inside the light cone"
    subdiagrams: list[frozenset[int]] = []
    for ray in ideal:
        orthogonal = frozenset(index for index, (_, vector) in enumerate(walls) if form.of(ray, vector) == 0)
        components = _components(orthogonal, edges, names)
        assert len(orthogonal) - components == RANK - 2, f"the walls orthogonal to {ray} have rank {len(orthogonal) - components}, not n - 1"
        subdiagrams.append(orthogonal)

    # The orbits of those subdiagrams under S_e = Aut(diagram): Sterk's four classes, Fig. 5 and p. 20.
    automorphisms = tuple(symmetries)
    seen: set[frozenset[int]] = set()
    orbits: list[list[tuple[int, ...]]] = []
    for subdiagram in subdiagrams:
        if subdiagram in seen:
            continue
        orbit = {frozenset(int(g(index + 1)) - 1 for index in subdiagram) for g in automorphisms}
        assert orbit <= set(subdiagrams), "a symmetry of the diagram sends an ideal vertex outside the ideal vertices"
        seen |= orbit
        orbits.append(sorted(tuple(sorted(member)) for member in orbit))
    orbits.sort(key=lambda orbit: (len(orbit), orbit[0]))
    assert len(orbits) == 4, f"Sterk finds four classes of maximal parabolic subdiagrams (Fig. 5, p. 20) and these are {len(orbits)}"
    assert sum(len(orbit) for orbit in orbits) == len(ideal), "the orbits do not partition the ideal vertices"

    # Sterk's own reading of the same figure: the diagram of 029J's (4.3.5) row, transcribed there earlier.
    earlier = next(
        row
        for row in corpus.front_matter(corpus.read_card(ROOT / "lattices" / "029J.md"))["integral"]["cusp_chambers"]["gamma-en-2"]
        if row["statement"] == "4.3.5"
    )
    assert {(edge["a"], edge["b"], edge["order"]) for edge in earlier["diagram"]} == {(edge["a"], edge["b"], edge["order"]) for edge in edges}, (
        "the twelve walls give a different diagram than 029J's row for the same figure"
    )

    gram = [[form.of(u, v) for _, v in walls] for _, u in walls]
    row: dict[str, object] = {
        "statement": "4.3.5",
        "printed_page": 19,
        "figure": 4,
        "walls": [{"name": name, "vector": list(vector)} for name, vector in walls],
        "wall_count": len(walls),
        "gram": [[str(entry) for entry in gram_row] for gram_row in gram],
        "diagram": edges,
        # Fig. 5, p. 20, prints the four classes and not a count of vertices, so the row states the classes.
        "parabolic_orbits": [
            {"subdiagrams": [[names[index] for index in subdiagram] for subdiagram in orbit]} for orbit in orbits
        ],
    }

    reference = {
        "citation": (
            'H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991), 1-36, '
            "(4.3.4), p. 19, which identifies (e')^perp/Z e' with H(2) + E8(-2) = U(2) + E8(-2); (4.3.5), p. 19, which "
            "defines G_e as the subgroup of O(M(2)) whose induced map on M(2)*/M(2) respects the decomposition, prints "
            "the diagram of the reflection group W_e of G_e as Fig. 4 — the nodes alpha_1, ..., alpha_8, "
            "alpha_9 = f' - e', alpha_10 = bar_alpha_8 + 2e', alpha_11 = 2e' + 2f' + bar_alpha_1 + bar_alpha_8 and "
            "alpha_12 = 5e' + 3f' + 2 bar_alpha_2, all of square -4 — and prints its maximal parabolic subdiagrams "
            "modulo the symmetries S_e = Z/2 x Z/2 as Fig. 5; and p. 20, where the maximal parabolic subdiagrams "
            "modulo symmetries are, in the paper's words, four equivalence classes: \"we do not only find four "
            "equivalence classes in I_1(e^perp/Ze), but that we find four labelled classes\". A maximal parabolic "
            "subdiagram is a vertex at infinity of the chamber by Vinberg's criterion, (4.3.3), p. 18 (E. B. Vinberg, "
            "The groups of units of certain quadratic forms, Mat. Sb. 87 (1972))."
        )
    }
    by = (
        f"{reference['citation']} The wall count, the Gram matrix and the Coxeter diagram are what the card's stored form says "
        "about the printed walls, and the maximal parabolic subdiagrams are the primitive rays of the chamber on the light cone; "
        "the diagram and its automorphism group S_e are the sage-extensions Coxeter-diagram owner's (CoxeterDiagrams().from_roots "
        f"and Aut(), at sage-extensions {SAGE_EXTENSIONS_REVISION}), so no recognition is repeated here and no Vinberg search was "
        "run on the subgroup. results/transcribe-39-sterk-we-chamber.py computed them."
    )

    held = certificates.load(ROOT, tags=[TAG])
    genus.cite_cusp_chambers(path, GROUP, [row], reference, by, held)
    certificates.save(ROOT, held, tags=[TAG])
    stored = corpus.front_matter(corpus.read_card(path))["integral"]["cusp_chambers"][GROUP][0]
    print(f"{stored['statement']} p. {stored['printed_page']} Fig. {stored['figure']}: {stored['wall_count']} walls, {len(stored['diagram'])} edges")
    print("ideal vertices:", len(ideal), "in", len(stored["parabolic_orbits"]), "orbits of sizes", [len(orbit["subdiagrams"]) for orbit in stored["parabolic_orbits"]])
    for orbit in stored["parabolic_orbits"]:
        print("  orbit:", orbit["subdiagrams"])
    print("certificate:", corpus.front_matter(corpus.read_card(path))["certifications"]["integral.cusp_chambers"])


def _components(positions: frozenset[int], edges: list[dict[str, object]], names: list[str]) -> int:
    """The number of connected components of the subdiagram on the walls at `positions`."""
    parent = {index: index for index in positions}

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    for edge in edges:
        i, j = names.index(str(edge["a"])), names.index(str(edge["b"]))
        if i in parent and j in parent:
            parent[find(i)] = find(j)
    return len({find(index) for index in positions})


if __name__ == "__main__":
    main()
