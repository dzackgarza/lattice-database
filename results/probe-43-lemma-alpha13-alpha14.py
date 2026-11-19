"""#43: the computation behind `results/issue-43-lemma-alpha13-alpha14.md`.

Card 029J's Gram tensor gives the fourteen walls of the (4.3.9) chamber. This states, from that tensor alone: that the
walls span a rank-10 lattice, that delta = e - f lies in the span, the eight symmetries of the wall system, which of them
exchange alpha_13 with alpha_14, and where each of those sends delta. The second one — the symmetry fixing alpha_11 and
alpha_12 — fixes delta, so its realisation preserves T_Co and identifies the two root classes.

    .scratch/wt43u-run.sh -u results/probe-43-lemma-alpha13-alpha14.py
"""

from pathlib import Path

from latticedb import corpus
from sage.all import QQ, ZZ, matrix, vector

metadata = corpus.front_matter(corpus.read_card(Path("/repo/lattices/029J.md")))
gram = matrix(ZZ, [[int(entry) for entry in row] for row in metadata["gram_tensor"]])
rank = gram.nrows()
chamber = metadata["integral"]["cusp_chambers"]["gamma-en-2"][4]  # (4.3.9)
walls = [vector(QQ, [int(entry) for entry in wall["vector"]]) for wall in chamber["walls"]]
names = [wall["name"] for wall in chamber["walls"]]
delta = vector(QQ, [1, -1] + [0] * (rank - 2))

chosen, basis = [], []
for index, wall in enumerate(walls):
    if matrix(QQ, basis + [wall]).rank() > len(basis):
        basis.append(wall)
        chosen.append(index)
print(f"{chamber['statement']}: {len(walls)} walls span rank {len(basis)}")
coefficients = (matrix(QQ, basis) * matrix(QQ, basis).transpose()).inverse() * matrix(QQ, basis) * matrix(QQ, rank, 1, list(delta))
weights = [coefficients[index, 0] for index in range(len(basis))]
rebuilt = sum((weights[index] * basis[index] for index in range(len(basis))), vector(QQ, [0] * rank))
print(f"delta lies in the span of the walls: {rebuilt == delta}")


def pairing(left, right):
    return (matrix(QQ, 1, rank, list(left)) * gram * matrix(QQ, rank, 1, list(right)))[0, 0]


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
print(f"symmetries of the diagram: {len(symmetries)}")
thirteen, fourteen = names.index("\\alpha_13"), names.index("\\alpha_14")
for symmetry in (candidate for candidate in symmetries if candidate[thirteen] == fourteen):
    image = sum((weights[index] * walls[symmetry[chosen[index]]] for index in range(len(basis))), vector(QQ, [0] * rank))
    verdict = "delta" if image == delta else "-delta" if image == -delta else "neither"
    fixed = [names[index] for index in range(len(names)) if symmetry[index] == index]
    print(f"  sends delta to {verdict}; fixes {fixed}")
