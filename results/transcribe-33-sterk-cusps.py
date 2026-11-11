#!/usr/bin/env python3
"""Transcribe Sterk's chambers at the 0-cusps of Gamma_En,2 onto the card of 029J (lattice-database#33).

The source is H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I",
Math. Z. 207 (1991), 1-36, Section 4.3: statements (4.3.5) p. 19 with Fig. 4, (4.3.6) p. 21 with
Fig. 6 and (4.3.8) p. 23 with Fig. 10, read from the PDF text layer of `tmp/sterk-1991-part-i.pdf`
and its OCR `tmp/sterk-1991-part-i.md` (where they differ, the text layer wins).

The script evaluates the card's own stored bilinear form on the source's vectors and nothing else:
it computes no lattice invariant, recognises no diagram and starts no Vinberg search. The walls and
the cusp are the source's; the Gram matrix, the Coxeter diagram and the wall count are what the
stored form says about them, and the script refuses to write a row that its own checks falsify.

Sterk's basis of L_- = H + H(2) + E8(-2) in the basis e_1, ..., e_12 of the card of 029J
(`U + U(2) + E8(-2)`):

    e = e_1, f = e_2            the hyperbolic plane H, (e, f) = 1
    e' = e_3, f' = e_4          the H(2) summand,       (e', f') = 2
    alpha_1 .. alpha_8          the E8(-2) simple roots, in Sterk's numbering (Fig. 1, p. 3)

The card's eight E8(-2) basis vectors e_5, ..., e_12 are the E8 tree with the branch at e_8 and the
arms {e_6}, {e_7, e_5} and {e_9, e_10, e_11, e_12}; Sterk's numbering has the branch at alpha_4 and
the arms {alpha_2}, {alpha_3, alpha_1}, {alpha_5, alpha_6, alpha_7, alpha_8}. The two are the same
labelled tree under

    alpha_1 = e_5, alpha_2 = e_6, alpha_3 = e_7, alpha_4 = e_8,
    alpha_5 = e_9, alpha_6 = e_10, alpha_7 = e_11, alpha_8 = e_12,

which the script checks against the card's Gram tensor rather than assumes.

`bar_alpha_i` is the dual basis of the simple roots, `(bar_alpha_i, alpha_j) = 2 delta_ij` — Sterk's
own note in (4.3.5): "(bar_alpha_i, alpha_i) = 2, because we are working in E8(-2)". Its norms are
-2 (C^-1)_ii, so bar_alpha_1 has norm -8, bar_alpha_2 -16 and bar_alpha_8 -4, which is what makes
(4.3.5)'s printed check (alpha_i, e' + f')^2 / |(alpha_i, alpha_i)| = 4, 16, 64 hold for
i = 10, 11, 12.

The other two statements print their walls beside their figures as well, and both are transcribed.

(4.3.7), p. 22 with Fig. 8, at the cusp v = e' + f' + bar_alpha_8: the nodes alpha_1, ..., alpha_7 of
the figure and the five vectors printed beside it, alpha_9 = f - e, alpha_10 = 2f' + bar_alpha_8,
alpha_11 = 2e - 2f' - bar_alpha_8 = (e + f) - alpha_9 - alpha_10, alpha_12 = 2e + (bar_alpha_1 -
bar_alpha_8) and alpha_13 = (e + f) + (alpha_8 - f'). The paper checks its own reading twice: the span
of the roots it prints, Z{alpha_1, ..., alpha_7, alpha_8 - f', e + f, e - f}, contains all twelve walls,
and in (4.3.16), p. 27, it reads the primitive isotropic plane Z v + Z w off this diagram with
w = alpha_9 + alpha_12 + alpha_1 + alpha_3 + alpha_4 + alpha_5 + alpha_6 + alpha_7 + alpha_13, which with
these vectors is isotropic, primitive, orthogonal to exactly those nine walls, and in their span. The
script asserts both.

(4.3.9), p. 24 with Fig. 12, at the cusp v = 2e + 2f + bar_alpha_1: the basis of v^perp/Zv prints on
p. 23 and the walls beside the figure on p. 24, where a tilde with a bar is the dual in the E8(-2)
summand spanned by alpha-tilde_1, ..., alpha-tilde_8, as bar_alpha_i is for alpha_i. The nodes inside
that summand are alpha-tilde_1, alpha_2, alpha_4, ..., alpha_7 and the dual of alpha-tilde_8, and the row
shows why alpha-tilde_3 = f' + alpha_3 cannot be one of them: with it the pair alpha-tilde_3-alpha_14 has
b = -4 against squares -4 and -2, so |g| = sqrt 2, which is no cos(pi/m) of Sterk's table. The span the
page prints, Z{e-tilde + f-tilde, e-tilde - f-tilde, alpha-tilde_1, ..., alpha-tilde_8}, contains all
thirteen walls.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

from latticedb import certificates, corpus, genus
from latticedb.model import Lattice

ROOT = Path(__file__).resolve().parent.parent
TAG = "029J"

STERK = 'H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991), 1-36'

E8_EDGES = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))
"""The E8 Dynkin diagram in Sterk's numbering (Fig. 1, p. 3): the chain 1-3-4-5-6-7-8 with alpha_2 at alpha_4."""

STERK_TO_CARD = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 10, 7: 11, 8: 12}
"""Sterk's alpha_i is the card's e_k, 1-indexed."""

RANK = 12


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
    """A vector written in Sterk's basis: `e`, `f`, `ep`, `fp`, and `a1` .. `a8` for the simple roots."""
    basis = [0] * RANK
    for name, value in terms.items():
        match name:
            case "e":
                basis[0] += value
            case "f":
                basis[1] += value
            case "ep":
                basis[2] += value
            case "fp":
                basis[3] += value
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
    form = Form(tuple(tuple(Fraction(entry) for entry in row) for row in lattice.gram_tensor))

    # The E8 block of the card is Sterk's labelled tree under the identification the docstring states.
    for i, j in E8_EDGES:
        a, b = STERK_TO_CARD[i] - 1, STERK_TO_CARD[j] - 1
        assert form.gram[a][b] == 2, f"alpha_{i} and alpha_{j} are not adjacent on the card"
    assert all(form.gram[STERK_TO_CARD[i] - 1][STERK_TO_CARD[i] - 1] == -4 for i in range(1, 9))

    e, f = combine({"e": 1}), combine({"f": 1})
    ep, fp = combine({"ep": 1}), combine({"fp": 1})
    alpha = {i: combine({f"a{i}": 1}) for i in range(1, 9)}

    # bar_alpha_i in the basis of the simple roots: the dual basis with (bar_alpha_i, alpha_j) = 2 delta_ij,
    # that is bar_alpha_i = -sum_j (C^-1)_{ij} alpha_j, whose square is -2 (C^-1)_{ii}.
    inverted = inverse(cartan())
    bar = {i: combine({f"a{j + 1}": -int(inverted[i - 1][j]) for j in range(8)}) for i in range(1, 9)}
    for i in range(1, 9):
        for j in range(1, 9):
            assert form.of(bar[i], alpha[j]) == (2 if i == j else 0), f"(bar_alpha_{i}, alpha_{j})"
    assert [form.norm(bar[i]) for i in range(1, 9)] == [-8, -16, -28, -60, -40, -24, -12, -4]

    def wall_row(
        statement: str,
        page: int,
        figure: int,
        cusp: tuple[int, ...],
        walls: list[tuple[str, tuple[int, ...]]],
        span: list[tuple[int, ...]] | None = None,
    ) -> dict[str, object]:
        assert form.norm(cusp) == 0, f"{statement}: the cusp is not isotropic"
        assert math.gcd(*[abs(entry) for entry in cusp]) == 1, f"{statement}: the cusp is not primitive"
        for name, v in walls:
            assert form.of(cusp, v) == 0, f"{statement}: the wall {name} is not orthogonal to the cusp"
            assert form.norm(v) < 0, f"{statement}: the wall {name} has square {form.norm(v)}, so it is no wall"
        if span is not None:
            for name, v in walls:
                assert form.rank([*span, v]) == form.rank(span), f"{statement}: the wall {name} is not in the span the page prints"
            for u in span:
                assert form.of(cusp, u) == 0, f"{statement}: the span the page prints is not in v^perp"
        assert form.rank([v for _, v in walls]) == RANK - 2, f"{statement}: the walls do not span v^perp/Zv over Q"
        assert form.rank([*(v for _, v in walls), cusp]) == RANK - 1, f"{statement}: the cusp is in the span of the walls"
        gram = [[form.of(u, v) for _, v in walls] for _, u in walls]
        return {
            "cusp": list(cusp),
            "statement": statement,
            "printed_page": page,
            "figure": figure,
            "walls": [{"name": name, "vector": list(v)} for name, v in walls],
            "wall_count": len(walls),
            "gram": [[str(entry) for entry in row] for row in gram],
            "diagram": diagram(form, walls),
        }

    rows: list[dict[str, object]] = []

    # (4.3.5), p. 19, Fig. 4: the cusp e. The walls alpha_1 .. alpha_8, alpha_9 = f' - e',
    # alpha_10 = bar_alpha_8 + 2e', alpha_11 = 2e' + 2f' + bar_alpha_1 + bar_alpha_8,
    # alpha_12 = 5e' + 3f' + 2 bar_alpha_2.
    walls = [(f"\\alpha_{i}", alpha[i]) for i in range(1, 9)]
    walls += [
        ("\\alpha_9", form.minus(fp, ep)),
        ("\\alpha_10", form.add((2, ep), (1, bar[8]))),
        ("\\alpha_11", form.add((2, ep), (2, fp), (1, bar[1]), (1, bar[8]))),
        ("\\alpha_12", form.add((5, ep), (3, fp), (2, bar[2]))),
    ]
    x = form.add((1, ep), (1, fp))
    printed = [form.of(x, walls[k][1]) ** 2 / abs(form.norm(walls[k][1])) for k in (9, 10, 11)]
    assert printed == [4, 16, 64], f"(4.3.5) prints 4, 16, 64 for alpha_10, alpha_11, alpha_12 and the card gives {printed}"
    rows.append(wall_row("4.3.5", 19, 4, e, walls))

    # (4.3.6), p. 21, Fig. 6: the cusp e'. The walls alpha_1 .. alpha_8, alpha_9 = bar_alpha_8 + 2f,
    # alpha_10 = e - f; the statement marks the (-4)- and the (-2)-vectors.
    walls = [(f"\\alpha_{i}", alpha[i]) for i in range(1, 9)]
    walls += [("\\alpha_9", form.add((1, bar[8]), (2, f))), ("\\alpha_10", form.minus(e, f))]
    rows.append(wall_row("4.3.6", 21, 6, ep, walls))

    # (4.3.8), p. 23, Fig. 10: the cusp 2e' + f' + bar_alpha_1, whose quotient v^perp/Zv has the basis
    # e, f, -e' + alpha_1, alpha_2, ..., alpha_8. The walls alpha_2 .. alpha_8, alpha_9 = f - e,
    # alpha_10 = bar_alpha_8 + 2e', alpha_11 = e + f + alpha_1 - e',
    # alpha_12 = 2e - 2e' + bar_alpha_8 - bar_alpha_1.
    cusp = form.add((2, ep), (1, fp), (1, bar[1]))
    walls = [(f"\\alpha_{i}", alpha[i]) for i in range(2, 9)]
    walls += [
        ("\\alpha_9", form.minus(f, e)),
        ("\\alpha_10", form.add((1, bar[8]), (2, ep))),
        ("\\alpha_11", form.add((1, e), (1, f), (1, alpha[1]), (-1, ep))),
        ("\\alpha_12", form.add((2, e), (-2, ep), (1, bar[8]), (-1, bar[1]))),
    ]
    rows.append(wall_row("4.3.8", 23, 10, cusp, walls))

    # (4.3.7), p. 22, Fig. 8: the cusp v = e' + f' + bar_alpha_8. The statement's basis of v^perp/Zv is
    # e, f, alpha_1, ..., alpha_7, -f' + bar_alpha_8, and the span of its roots Z{alpha_1, ..., alpha_7,
    # alpha_8 - f', e + f, e - f}. The walls are the seven nodes alpha_1, ..., alpha_7 and the five vectors
    # printed beside the figure: alpha_9 = f - e, alpha_10 = 2f' + bar_alpha_8,
    # alpha_11 = 2e - 2f' - bar_alpha_8 = (e + f) - alpha_9 - alpha_10,
    # alpha_12 = 2e + (bar_alpha_1 - bar_alpha_8), alpha_13 = (e + f) + (alpha_8 - f').
    cusp = form.add((1, ep), (1, fp), (1, bar[8]))
    span_437 = [
        *[alpha[i] for i in range(1, 8)],
        form.minus(alpha[8], fp),
        form.add((1, e), (1, f)),
        form.minus(e, f),
    ]
    walls = [(f"\\alpha_{i}", alpha[i]) for i in range(1, 8)]
    walls += [
        ("\\alpha_9", form.minus(f, e)),
        ("\\alpha_10", form.add((2, fp), (1, bar[8]))),
        ("\\alpha_11", form.add((2, e), (-2, fp), (-1, bar[8]))),
        ("\\alpha_12", form.add((2, e), (1, bar[1]), (-1, bar[8]))),
        ("\\alpha_13", form.add((1, e), (1, f), (1, alpha[8]), (-1, fp))),
    ]
    # alpha_11 is printed both as a formula and as (e + f) - alpha_9 - alpha_10.
    assert walls[9][1] == form.add((1, e), (1, f), (-1, walls[7][1]), (-1, walls[8][1])), "(4.3.7): alpha_11 is not (e + f) - alpha_9 - alpha_10"
    # (4.3.16), p. 27: the paper reads the isotropic plane Z v + Z w off this diagram with
    # w = alpha_9 + alpha_12 + alpha_1 + alpha_3 + alpha_4 + alpha_5 + alpha_6 + alpha_7 + alpha_13.
    assert [walls[k][0] for k in (7, 10, 0, 2, 3, 4, 5, 6, 11)] == [
        "\\alpha_9", "\\alpha_12", "\\alpha_1", "\\alpha_3", "\\alpha_4", "\\alpha_5", "\\alpha_6", "\\alpha_7", "\\alpha_13",
    ], "(4.3.7): the walls are not in the order this script numbers them"
    w = form.add(*[(1, walls[k][1]) for k in (7, 10, 0, 2, 3, 4, 5, 6, 11)])
    assert form.norm(w) == 0, "(4.3.7): the paper's w is not isotropic"
    assert math.gcd(*[abs(entry) for entry in w]) == 1, "(4.3.7): the paper's w is not primitive"
    assert form.of(w, cusp) == 0, "(4.3.7): the paper's w is not orthogonal to the cusp"
    assert [name for name, v in walls if form.of(w, v) == 0] == ["\\alpha_1", "\\alpha_3", "\\alpha_4", "\\alpha_5", "\\alpha_6", "\\alpha_7", "\\alpha_9", "\\alpha_12", "\\alpha_13"], "(4.3.7): the paper's w is not orthogonal to the walls of its parabolic subdiagram"
    rows.append(wall_row("4.3.7", 22, 8, cusp, walls, span_437))

    # (4.3.9), p. 24, Fig. 12: the cusp v = 2e + 2f + bar_alpha_1. Its quotient v^perp/Zv has the basis the
    # statement prints on p. 23, e~ = e + e' + f' - alpha_1, f~ = f + e' + f' - alpha_1, alpha~_1 = e' - f',
    # alpha~_2 = alpha_2, alpha~_3 = f' + alpha_3, alpha~_4 ... alpha~_8, and the span of its roots
    # Z{e~ + f~, e~ - f~, alpha~_1, ..., alpha~_8}. The nodes inside the E8(-2) summand are alpha~_1, alpha_2,
    # alpha_4, ..., alpha_7 and the dual of alpha~_8, and the six vectors beside the figure are
    # alpha_9 = 2e~ - alpha~_1, alpha_10 = 2e~ + (dual alpha~_2 - dual alpha~_3), alpha_11 = f~ - e~,
    # alpha_12 = e~ + f~ + (dual alpha~_6 - dual alpha~_3),
    # alpha_13 = e~ + f~ + (dual alpha~_1 + dual alpha~_8 - dual alpha~_3), alpha_14 = e~ + f~ + alpha~_3.
    cusp = form.add((2, e), (2, f), (1, bar[1]))
    e_tilde = form.add((1, e), (1, ep), (1, fp), (-1, alpha[1]))
    f_tilde = form.add((1, f), (1, ep), (1, fp), (-1, alpha[1]))
    alpha_tilde = {1: form.minus(ep, fp), 2: alpha[2], 3: form.add((1, fp), (1, alpha[3]))}
    alpha_tilde |= {i: alpha[i] for i in range(4, 9)}
    # e~ and f~ span an H-summand, alpha~_1 ... alpha~_8 an E8(-2)-summand, as the statement says.
    assert form.norm(e_tilde) == form.norm(f_tilde) == 0 and form.of(e_tilde, f_tilde) == 1, "(4.3.9): e~, f~ are no H"
    assert all(form.of(e_tilde, alpha_tilde[i]) == 0 and form.of(f_tilde, alpha_tilde[i]) == 0 for i in range(1, 9)), "(4.3.9): the summands are not orthogonal"
    tilde_gram = [[form.of(alpha_tilde[i], alpha_tilde[j]) for j in range(1, 9)] for i in range(1, 9)]
    assert tilde_gram == [[-2 * cartan()[i - 1][j - 1] for j in range(1, 9)] for i in range(1, 9)], (
        "(4.3.9): alpha~_1 ... alpha~_8 are not E8(-2) in Sterk's numbering"
    )
    # the dual of alpha~_i in the E8(-2) summand: (dual alpha~_i, alpha~_j) = 2 delta_ij, an integral
    # combination of the alpha~_j because the E8 Cartan matrix has determinant 1
    inverted_tilde = inverse(tilde_gram)
    for i in range(1, 9):
        for j in range(8):
            assert (2 * inverted_tilde[i - 1][j]).denominator == 1, f"(4.3.9): dual alpha~_{i} is not integral"
    dual_tilde = {
        i: form.add(*[(int(2 * inverted_tilde[i - 1][j]), alpha_tilde[j + 1]) for j in range(8) if inverted_tilde[i - 1][j] != 0])
        for i in range(1, 9)
    }
    for i in range(1, 9):
        assert [form.of(dual_tilde[i], alpha_tilde[j]) for j in range(1, 9)] == [2 if i == j else 0 for j in range(1, 9)], f"(4.3.9): dual alpha~_{i}"
    assert [form.norm(dual_tilde[i]) for i in range(1, 9)] == [-8, -16, -28, -60, -40, -24, -12, -4], "(4.3.9): the duals of alpha~ are not the E8(-2) dual basis"
    span_439 = [form.add((1, e_tilde), (1, f_tilde)), form.minus(e_tilde, f_tilde), *[alpha_tilde[i] for i in range(1, 9)]]
    walls = [
        ("\\widetilde\\alpha_1", alpha_tilde[1]),
        ("\\alpha_2", alpha_tilde[2]),
        *[(f"\\alpha_{i}", alpha_tilde[i]) for i in range(4, 8)],
        ("\\overline{\\widetilde\\alpha}_8", dual_tilde[8]),
        ("\\alpha_9", form.add((2, e_tilde), (-1, alpha_tilde[1]))),
        ("\\alpha_10", form.add((2, e_tilde), (1, dual_tilde[2]), (-1, dual_tilde[3]))),
        ("\\alpha_11", form.minus(f_tilde, e_tilde)),
        ("\\alpha_12", form.add((1, e_tilde), (1, f_tilde), (1, dual_tilde[6]), (-1, dual_tilde[3]))),
        ("\\alpha_13", form.add((1, e_tilde), (1, f_tilde), (1, dual_tilde[1]), (1, dual_tilde[8]), (-1, dual_tilde[3]))),
        ("\\alpha_14", form.add((1, e_tilde), (1, f_tilde), (1, alpha_tilde[3]))),
    ]
    rows.append(wall_row("4.3.9", 24, 12, cusp, walls, span_439))

    # The card lists the cusps in the order the statements number them: (4.3.5), (4.3.6), (4.3.7), (4.3.8), (4.3.9).
    rows.sort(key=lambda row: str(row["statement"]))

    reference = {
        "citation": (
            f"{STERK}, Section 4.3: the 0-cusps of Gamma_En,2 are the five primitive isotropic vectors of "
            "Proposition 4.2.3, p. 16. (4.3.5), p. 19 with Fig. 4, prints the walls of the chamber at the cusp e; "
            "(4.3.6), p. 21 with Fig. 6, those at e'; (4.3.7), p. 22 with Fig. 8, those at e' + f' + bar_alpha_8; "
            "(4.3.8), p. 23 with Fig. 10, those at 2e' + f' + bar_alpha_1; (4.3.9), pp. 23-24 with Fig. 12, those "
            "at 2e + 2f + bar_alpha_1."
        )
    }
    by = (
        f"{reference['citation']} The Gram matrix, the Coxeter diagram and the wall count are what the card's stored "
        "form says about those walls: results/transcribe-33-sterk-cusps.py computed them from the card's Gram tensor, "
        "and no Vinberg search was run for them."
    )

    held = certificates.load(ROOT, tags=[TAG])
    genus.cite_cusp_chambers(path, "gamma-en-2", rows, reference, by, held)
    certificates.save(ROOT, held, tags=[TAG])
    for row in corpus.front_matter(corpus.read_card(path))["integral"]["cusp_chambers"]["gamma-en-2"]:
        print(row["statement"], f"p. {row['printed_page']}", f"Fig. {row['figure']}", f"cusp {row['cusp']}", f"{row['wall_count']} walls", f"{len(row['diagram'])} edges", flush=True)
    print(corpus.front_matter(corpus.read_card(path))["certifications"]["integral.cusp_chambers"])


if __name__ == "__main__":
    main()
