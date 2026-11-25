"""#43: a bounded word search for an element of Gamma_Co,2 moving alpha_12 — the last route to cusp 5's count.

At Sterk's (4.3.9) the chamber has fourteen walls; eleven lie in $T_{\\mathrm{Co}} = \\delta^\\perp$ and their reflections
fix $\\delta$ (and every class), the other three — $\\alpha_9$, $\\alpha_{10}$, $\\alpha_{11}$ — give reflections that move
$\\delta$. Together with the diagram symmetry $\\sigma$ exchanging $\\alpha_{13}$ with $\\alpha_{14}$, which fixes $\\delta$,
they are the only isometries of the chamber that can both fix $\\delta$ and move a class. So an element of
$\\Gamma_{\\mathrm{Co},2}$ carrying $\\alpha_{12}$ to $\\alpha_{13}$ or $\\alpha_{14}$ exists exactly when some word in those
four generators does.

This walks words up to a given length, in the rank-10 span of the walls, and reports every word whose isometry fixes
$\\delta$ up to sign and carries the class of $\\alpha_{12}$ to another class of the row.

    .scratch/wt43ao-run.sh -u results/probe-43-coble-word.py [depth]
"""

import sys
from itertools import product

from latticedb import corpus
from sage.all import QQ, matrix, vector
from pathlib import Path

DEPTH = int(sys.argv[1]) if len(sys.argv) > 1 else 6
meta = corpus.front_matter(corpus.read_card(Path("/repo/lattices/029J.md")))
gram = matrix(QQ, [[QQ(entry) for entry in row] for row in meta["gram_tensor"]])
n = gram.nrows()
chamber = meta["integral"]["cusp_chambers"]["gamma-en-2"][4]
walls = [vector(QQ, [QQ(entry) for entry in wall["vector"]]) for wall in chamber["walls"]]
names = [wall["name"] for wall in chamber["walls"]]
cusp = vector(QQ, [QQ(entry) for entry in chamber["cusp"]])


def pairing(left, right):
    return (matrix(QQ, 1, n, list(left)) * gram * matrix(QQ, n, 1, list(right)))[0, 0]


delta = vector(QQ, [1, -1] + [0] * (n - 2))
independent, chosen = [], []
for index, wall in enumerate(walls):
    if matrix(QQ, independent + [list(wall)]).rank() > len(independent):
        independent.append(list(wall))
        chosen.append(index)
basis = matrix(QQ, independent)
coefficients = (basis * basis.transpose()).inverse() * basis


def in_span(value):
    return (coefficients * matrix(QQ, n, 1, list(value))).column(0)


def from_span(coords):
    return (matrix(QQ, 1, len(independent), list(coords)) * basis).row(0)


# The generators, as matrices on the span.
generators = {}
for name in ("\\alpha_9", "\\alpha_10", "\\alpha_11"):
    wall = walls[names.index(name)]
    scale = 2 / pairing(wall, wall)
    columns = []
    for position in range(len(independent)):
        image = from_span(matrix(QQ, 1, len(independent), [1 if k == position else 0 for k in range(len(independent))]).row(0))
        reflected = image - scale * pairing(image, wall) * wall
        columns.append(in_span(reflected))
    generators[name] = matrix(QQ, len(independent), len(independent), [list(column) for column in columns]).transpose()

squares = [pairing(wall, wall) for wall in walls]
symmetries = []


def extend(partial):
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
thirteen, fourteen = names.index("\\alpha_13"), names.index("\\alpha_14")
for symmetry in (candidate for candidate in symmetries if candidate[thirteen] == fourteen and candidate[names.index("\\alpha_12")] == names.index("\\alpha_12")):
    columns = [in_span(walls[symmetry[chosen[position]]]) for position in range(len(independent))]
    generators["sigma"] = matrix(QQ, len(independent), len(independent), [list(column) for column in columns]).transpose()
    break
print("generators:", sorted(generators), flush=True)

delta_span = in_span(delta)
classes = {name: in_span(walls[names.index(name)]) for name in ("\\alpha_12", "\\alpha_13", "\\alpha_14")}


def same_class(left, right):
    difference = left - right
    values = [difference[i] / cusp_span[i] for i in range(len(independent)) if cusp_span[i] != 0]
    if not values:
        return False
    scale = values[0]
    return all(value == scale for value in values) and all(
        difference[i] == 0 for i in range(len(independent)) if cusp_span[i] == 0
    )


cusp_span = in_span(cusp)
labels = list(generators)
identity = matrix.identity(QQ, len(independent))
found = []
frontier = [(identity, "")]
seen = {tuple(identity.list())}
for depth in range(1, DEPTH + 1):
    nxt = []
    for word, name in frontier:
        for label in labels:
            image = generators[label] * word
            key = tuple(image.list())
            if key in seen:
                continue
            seen.add(key)
            nxt.append((image, name + label))
            moves_delta = image * delta_span in (delta_span, -delta_span)
            if moves_delta:
                moved = image * classes["\\alpha_12"]
                for other in ("\\alpha_13", "\\alpha_14"):
                    if same_class(moved, classes[other]):
                        found.append(name + label)
    frontier = nxt
    print(f"depth {depth}: {len(seen)} words, {len(found)} carry alpha_12 to another class while fixing delta", flush=True)
    if found:
        break
print("RESULT:", found[:5] if found else "no word up to this depth", flush=True)
