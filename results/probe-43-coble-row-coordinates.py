"""#43: the T_Co cusps 3--5 in *card 6JRR's* own basis, which is what a row of `cusp_root_orbits` states.

The last turn decided two of the three T_Co rows (one root class each) in $T_{\\mathrm{En}}$'s coordinates, where the
029J chambers are stored. A row of `integral.cusp_root_orbits` on 6JRR states its cusp and its classes as lifts in
*that card's* record basis, so this carries them across: `delta^\\perp` in `T_En` coordinates, the integral basis Sage
gives it, the isometry onto card 6JRR's stored Gram tensor, and then the cusp and the root walls written in the card's
basis, each checked to lie in $T_{\\mathrm{Co}}$ and to keep its square.

    .scratch/wt43k-run.sh -u results/probe-43-coble-row-coordinates.py
"""

import time
from fractions import Fraction
from pathlib import Path

from latticedb import corpus
from sage.all import ZZ as SageZZ, matrix, IntegralLattice
from sage_extensions.all import ZZ, NamedLattices  # noqa: F401,F403

start = time.time()
ROOT = Path("/repo")


def stamp(label):
    print(f"[{time.time() - start:6.1f}s] {label}", flush=True)


enriques = NamedLattices.TEn
labels = tuple(enriques.module_generating_set())
rank = int(enriques.module_rank())
gram_en = matrix(SageZZ, [[int(enriques.b(enriques.module_generator(a), enriques.module_generator(b))) for b in labels] for a in labels])

eight = corpus.front_matter(corpus.read_card(ROOT / "lattices" / "6JRR.md"))
gram_co = matrix(SageZZ, [[int(entry) for entry in row] for row in eight["gram_tensor"]])
stamp(f"T_En rank {rank}, 6JRR rank {gram_co.nrows()} and determinant {gram_co.det()}")

# delta = e - f in the first hyperbolic plane; T_Co = delta^perp, from the library's own complement.
delta_element = enriques.linear_combination(
    {labels[0]: enriques.base_ring()(1), labels[1]: enriques.base_ring()(-1)}
)
perpendicular = delta_element.orthogonal_complement()
perpendicular_labels = tuple(perpendicular.module_generating_set())
inclusion = perpendicular.inclusion()


def coordinates(element):
    return [int(entry) for entry in element.to_vector()]


basis_co = matrix(
    SageZZ,
    [coordinates(inclusion(perpendicular.module_generator(label))) for label in perpendicular_labels],
).transpose()
stamp(f"delta^perp: rank {perpendicular.module_rank()}, basis in T_En coordinates {basis_co.nrows()} x {basis_co.ncols()}")
gram_of_basis = basis_co.transpose() * gram_en * basis_co
print("the computed Gram equals card 6JRR's:", gram_of_basis == gram_co, flush=True)
if gram_of_basis != gram_co:
    source = IntegralLattice(gram_of_basis)
    target = IntegralLattice(gram_co)
    print("globally isometric:", source.is_globally_isometric(target), flush=True)
    raise SystemExit("the card's basis is not the computed one; an isometry is needed before the rows can be stated")

# v = x . basis_co^T for a 1x11 row x, so x = (v . basis_co) . (basis_co^T . basis_co)^(-1).
gram_of_basis_inverse = (basis_co.transpose() * basis_co).inverse()


def square_of_T_En(values_of_T_En):
    vector = matrix(SageZZ, 1, rank, [int(entry) for entry in values_of_T_En])
    return int((vector * gram_en * vector.transpose())[0, 0])


def card_coordinates(entries_of_T_En):
    """The same vector in card 6JRR's own basis, asserted to be integral and to keep its square."""
    vector = matrix(SageZZ, 1, rank, [int(entry) for entry in entries_of_T_En])
    solution = (vector * basis_co) * gram_of_basis_inverse
    if any(entry.denominator() != 1 for entry in solution.list()):
        return None  # not a vector of T_Co at all
    return [int(entry) for entry in solution.list()]


coordinates_of_delta = coordinates(delta_element)
delta_row = matrix(SageZZ, 1, rank, coordinates_of_delta)


def in_T_Co(values_of_T_En):
    """Whether a vector of T_En lies in delta^perp, decided by the pairing itself and not by its projection."""
    vector = matrix(SageZZ, 1, rank, [int(entry) for entry in values_of_T_En])
    return int((vector * gram_en * delta_row.transpose())[0, 0]) == 0


def square(values, gram):
    vector = matrix(SageZZ, 1, len(values), values)
    return int((vector * gram * vector.transpose())[0, 0])


old_eight = corpus.front_matter(corpus.read_card(ROOT / "lattices" / "029J.md"))["integral"]["cusp_chambers"]["gamma-en-2"]
rows = []
for chamber in old_eight:
    cusp_en = enriques.linear_combination(
        {labels[index]: enriques.base_ring()(int(entry)) for index, entry in enumerate(chamber["cusp"]) if int(entry)}
    )
    if not in_T_Co(coordinates(cusp_en)):
        continue
    cusp_co = card_coordinates(coordinates(cusp_en))
    assert cusp_co is not None
    assert square(cusp_co, gram_co) == 0, (chamber["statement"], square(cusp_co, gram_co))
    walls = []
    for wall in chamber["walls"]:
        wall_en = enriques.linear_combination(
            {labels[index]: enriques.base_ring()(int(entry)) for index, entry in enumerate(wall["vector"]) if int(entry)}
        )
        if not in_T_Co(coordinates(wall_en)):
            continue
        wall_co = card_coordinates(coordinates(wall_en))
        assert wall_co is not None
        assert square(wall_co, gram_co) == square_of_T_En(wall["vector"]), (wall["name"], square(wall_co, gram_co))
        walls.append((wall["name"], wall_co, square(wall_co, gram_co)))
    roots = [
        (name, values)
        for name, values, q in walls
        if q == -2
        and int((matrix(SageZZ, 1, len(values), values) * gram_co * matrix(SageZZ, len(cusp_co), 1, cusp_co))[0, 0]) == 0
    ]
    print(f"{chamber['statement']}: cusp {cusp_co} (q = {square(cusp_co, gram_co)}), {len(walls)} walls off the cusp, roots {[name for name, _ in roots]}", flush=True)
    for name, values in roots:
        print(f"    {name}: {values}", flush=True)
    if roots:
        rows.append({"statement": chamber["statement"], "cusp": cusp_co, "roots": roots})
print(f"RESULT: {len(rows)} cusps of 6JRR carry a root class: {[row['statement'] for row in rows]}", flush=True)
