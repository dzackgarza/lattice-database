#!/usr/bin/env python3
"""Transcribe the ideal-vertex count of card 0124's reflection polyhedron from Sterk (lattice-database#36).

The source is H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I",
Math. Z. 207 (1991), 1-36, Section 4.3, read from the PDF text layer of
`tmp/sources/sterk-1991-compactifications-of-the-period-space-of-enriques-surfaces-i.pdf` and its
OCR `tmp/sterk-1991-part-i.md` (where they differ, the text layer wins).

What the source says for this card. (4.3.4), p. 19, computes the quotients v^perp/Zv of the five
primitive isotropic vectors of (4.2.3) and gets H + E8(-2) for every v other than e; (4.3.6), p. 21,
takes v = e' and identifies

    (e')^perp / Z e'  with  H + E8(-2)  =  U + E8(-2),   card 0124.

It prints the chamber of the reflection group beside Fig. 6: the nodes alpha_1, ..., alpha_8 and
alpha_9 = bar_alpha_8 + 2f, alpha_10 = e - f, with the legend "circle: (-4)-vector, bullet:
(-2)-vector" — the source's sign convention, a vertex being the wall orthogonal to it and marked by
the square of that wall. It adds "As there are no symmetries we have O(H + E8(-2)) = {+1} W_e'", so
the reflection group is the whole orthogonal group up to +-1, and Fig. 7, p. 21, prints its
"two maximal parabolic subdiagrams", which is the number this card stores as `ideal_vertices`.

The reading of Fig. 7 as the ideal vertices is (4.3.3), p. 18, Vinberg's criterion: "the vertices at
infinity of P correspond to the parabolic subdiagrams of rank n - 1 of Sigma(G)", a parabolic
subdiagram being one each of whose connected components is an extended Dynkin diagram and its rank
the number of its vertices minus the number of its components (E. B. Vinberg, The groups of units of
certain quadratic forms, Mat. Sb. 87 (1972), Sterk's [26]). With 10 walls and n = 9, rank n - 1 = 8
selects the subdiagrams of 9 vertices in one affine component and, as the diagram is connected, no
others; the paper counts them rather than this script, which runs no Vinberg search and recognises
no diagram.

The other card of the issue, 0125 = U(2) + E8(-2), is NOT transcribed: see the report in the commit
message. (4.3.5), p. 19, gives its chamber as the diagram of W_e inside G_e, a subgroup of
O(M(2)) that the paper defines by an action on M(2)^*/M(2) and does not identify with the whole
orthogonal group, and Fig. 5, p. 20, prints its "maximal parabolic subdiagrams (modulo symmetries)"
— four, in the paper's words "four equivalence classes" — which is a count of orbits under the
symmetries S_e = Z/2 x Z/2, not the number of ideal vertices of the chamber.

The walls are transcribed as well, so that the row's diagram is the one the count is read from; the
script evaluates the card's own stored form on the source's vectors and nothing else.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

from latticedb import certificates, corpus, genus
from latticedb.model import Lattice

ROOT = Path(__file__).resolve().parent.parent
TAG = "0124"

STERK = 'H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991), 1-36'

E8_EDGES = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))
"""The E8 Dynkin diagram in Sterk's numbering (Fig. 1, p. 3): the chain 1-3-4-5-6-7-8 with alpha_2 at alpha_4."""

STERK_TO_CARD = {i: i + 2 for i in range(1, 9)}
"""Sterk's alpha_i is the card's e_k, 1-indexed: the U summand is e_1, e_2 and E8(-2) is e_3, ..., e_10."""

RANK = 10


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
        for column in range(RANK):
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
            square = product * product / (form.norm(walls[i][1]) * form.norm(walls[j][1]))
            if square == 1:
                order: int | str = "inf"
            elif square in orders:
                order = orders[square]
            else:
                raise SystemExit(f"{walls[i][0]}-{walls[j][0]}: |g|^2 = {square} is not cos^2(pi/m)")
            edges.append({"a": walls[i][0], "b": walls[j][0], "order": order})
    return edges


def main() -> None:
    path = ROOT / "lattices" / f"{TAG}.md"
    lattice = Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
    assert lattice.gram_tensor is not None
    assert (lattice.rank, tuple(lattice.signature or ())) == (RANK, (1, 9)), "0124 is not a rank-10 (1, 9) lattice"
    form = Form(tuple(tuple(Fraction(entry) for entry in row) for row in lattice.gram_tensor))

    # The card is H + E8(-2) in Sterk's decomposition: e_1, e_2 span H and e_3, ..., e_10 are the E8(-2)
    # simple roots in Sterk's own numbering, which the card's Gram confirms.
    e, f = combine({"e": 1}), combine({"f": 1})
    assert form.norm(e) == form.norm(f) == 0 and form.of(e, f) == 1, "the first summand of 0124 is not H"
    alpha = {i: combine({f"a{i}": 1}) for i in range(1, 9)}
    for i, j in E8_EDGES:
        a, b = STERK_TO_CARD[i] - 1, STERK_TO_CARD[j] - 1
        assert form.gram[a][b] == 2, f"alpha_{i} and alpha_{j} are not adjacent on the card"
    assert all(form.gram[STERK_TO_CARD[i] - 1][STERK_TO_CARD[i] - 1] == -4 for i in range(1, 9))
    assert all(form.of(e, alpha[i]) == 0 and form.of(f, alpha[i]) == 0 for i in range(1, 9)), "the summands are not orthogonal"

    # bar_alpha_i in the basis of the simple roots: the dual basis with (bar_alpha_i, alpha_j) = 2 delta_ij,
    # that is bar_alpha_i = -sum_j (C^-1)_{ij} alpha_j, whose square is -2 (C^-1)_{ii}.
    inverted = inverse(cartan())
    bar = {i: combine({f"a{j + 1}": -int(inverted[i - 1][j]) for j in range(8)}) for i in range(1, 9)}
    for i in range(1, 9):
        for j in range(1, 9):
            assert form.of(bar[i], alpha[j]) == (2 if i == j else 0), f"(bar_alpha_{i}, alpha_{j})"
    assert [form.norm(bar[i]) for i in range(1, 9)] == [-8, -16, -28, -60, -40, -24, -12, -4]

    # (4.3.6), p. 21, Fig. 6: alpha_1, ..., alpha_8, alpha_9 = bar_alpha_8 + 2f, alpha_10 = e - f.
    walls: list[tuple[str, tuple[int, ...]]] = [(f"\\alpha_{i}", alpha[i]) for i in range(1, 9)]
    walls += [("\\alpha_9", form.add((1, bar[8]), (2, f))), ("\\alpha_10", form.minus(e, f))]
    for name, v in walls:
        assert form.norm(v) < 0, f"(4.3.6): the wall {name} has square {form.norm(v)}, so it is no wall"
    # Fig. 6's legend: the (-4)-vectors are circled and the (-2)-vector bulleted; alpha_10 = e - f is the
    # only bullet, which is the source's sign convention for the squares.
    squares = {name: form.norm(v) for name, v in walls}
    assert [name for name, square in squares.items() if square == -2] == ["\\alpha_10"], squares
    assert all(square == -4 for name, square in squares.items() if name != "\\alpha_10"), squares
    # The chamber is full-dimensional: its walls span L over Q.
    assert form.rank([v for _, v in walls]) == RANK, "(4.3.6): the walls do not span L over Q"

    gram = [[form.of(u, v) for _, v in walls] for _, u in walls]
    row: dict[str, object] = {
        "statement": "4.3.6",
        "printed_page": 21,
        "figure": 6,
        "walls": [{"name": name, "vector": list(v)} for name, v in walls],
        "wall_count": len(walls),
        "gram": [[str(entry) for entry in row] for row in gram],
        "diagram": diagram(form, walls),
        # Fig. 7, p. 21: "In the picture we see the two maximal parabolic subdiagrams", read as the ideal
        # vertices by (4.3.3), p. 18. The count is the source's; the script computes none of it.
        "ideal_vertices": 2,
    }

    reference = {
        "citation": (
            f"{STERK}, (4.3.4), p. 19, which identifies (e')^perp/Z e' with H + E8(-2) = U + E8(-2), and "
            "(4.3.6), p. 21, which prints the Coxeter diagram of its reflection group as Fig. 6 — the nodes "
            "alpha_1, ..., alpha_8, alpha_9 = bar_alpha_8 + 2f and alpha_10 = e - f, marked by Sterk's legend "
            '"circle: (-4)-vector, bullet: (-2)-vector" — and prints its two maximal parabolic subdiagrams as '
            'Fig. 7: "In the picture we see the two maximal parabolic subdiagrams". A maximal parabolic '
            "subdiagram is a vertex at infinity of the chamber and the count of them is the number of ideal "
            "vertices by Vinberg's criterion, (4.3.3), p. 18 (E. B. Vinberg, The groups of units of certain "
            "quadratic forms, Mat. Sb. 87 (1972))."
        )
    }
    by = (
        f"{reference['citation']} The wall count, the Gram matrix and the Coxeter diagram are what the card's stored "
        "form says about the printed walls: results/transcribe-36-sterk-ideal-vertices.py computed them from the "
        "card's Gram tensor, and ran no Vinberg search. The number of ideal vertices is the source's own count, "
        "read from Fig. 7."
    )

    held = certificates.load(ROOT, tags=[TAG])
    genus.cite_cusp_chambers(path, "O", [row], reference, by, held)
    certificates.save(ROOT, held, tags=[TAG])
    stored = corpus.front_matter(corpus.read_card(path))["integral"]["cusp_chambers"]["O"][0]
    print(
        stored["statement"],
        f"p. {stored['printed_page']}",
        f"Fig. {stored['figure']}",
        "no cusp" if stored.get("cusp") is None else f"cusp {stored['cusp']}",
        f"{stored['wall_count']} walls",
        f"{len(stored['diagram'])} edges",
        f"{stored['ideal_vertices']} ideal vertices",
        flush=True,
    )
    print(math.gcd(*[abs(entry) for name, v in walls for entry in v]), "the gcd of the walls' coordinates", flush=True)
    print(corpus.front_matter(corpus.read_card(path))["certifications"]["integral.cusp_chambers"])


if __name__ == "__main__":
    main()
