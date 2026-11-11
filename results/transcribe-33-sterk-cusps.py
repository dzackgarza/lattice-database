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

Rows the source does not print are not written:

  (4.3.7) p. 21-22, cusp e' + f' + bar_alpha_8, Fig. 8: the statement prints the figure and the span
  of its roots, not its walls as formulae, and the scan of Fig. 8 does not give them. The row stops.

  (4.3.9) p. 23-24, cusp 2e + 2f + bar_alpha_1, Fig. 12: the basis prints, but the text layer and
  the OCR disagree on four of the six vectors alpha_9, ..., alpha_14, and no reading of either has
  walls orthogonal to the cusp whose Coxeter matrix is |g_ij| = cos(pi/m). The row stops as well.
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

    def wall_row(statement: str, page: int, figure: int, cusp: tuple[int, ...], walls: list[tuple[str, tuple[int, ...]]]) -> dict[str, object]:
        assert form.norm(cusp) == 0, f"{statement}: the cusp is not isotropic"
        assert math.gcd(*[abs(entry) for entry in cusp]) == 1, f"{statement}: the cusp is not primitive"
        for name, v in walls:
            assert form.of(cusp, v) == 0, f"{statement}: the wall {name} is not orthogonal to the cusp"
            assert form.norm(v) < 0, f"{statement}: the wall {name} has square {form.norm(v)}, so it is no wall"
        assert form.rank([v for _, v in walls]) == RANK - 2, f"{statement}: the walls do not span v^perp/Zv over Q"
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

    reference = {
        "citation": (
            f"{STERK}, Section 4.3: the 0-cusps of Gamma_En,2 are the five primitive isotropic vectors of "
            "Proposition 4.2.3, p. 16. (4.3.5), p. 19 with Fig. 4, prints the walls of the chamber at the cusp e; "
            "(4.3.6), p. 21 with Fig. 6, those at e'; (4.3.8), p. 23 with Fig. 10, those at 2e' + f' + bar_alpha_1. "
            "(4.3.7), p. 21-22 with Fig. 8, at e' + f' + bar_alpha_8, and (4.3.9), p. 23-24 with Fig. 12, at "
            "2e + 2f + bar_alpha_1, print theirs only as figures, and those two rows are not stored."
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
