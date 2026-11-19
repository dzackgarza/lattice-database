"""#43: do the T_Co cusps' root classes merge under the part of the Enriques stabilizer that preserves T_Co?

$\\Gamma_{\\mathrm{Co},2} = \\mathrm{Stab}_{O(T_{\\mathrm{En}})}(T_{\\mathrm{Co}}) \\cap \\Gamma_{\\mathrm{En},2}$ with
$T_{\\mathrm{Co}} = \\delta^\\perp$, $\\delta = e - f$, so every generator of the Enriques cusp stabilizer that carries
$\\delta$ to $\\pm\\delta$ lies in $\\Gamma_{\\mathrm{Co},2}$ and fixes the cusp; one that carries a root class of
$K_I$ to another is a proof that they are one orbit. That is the row's question at the T_Co cusps 3--5, asked with the
family the owner does return: a merge is a value, and a failure to merge claims nothing.

Everything here is integer linear algebra in the coordinates of the lattice the generators act on; the generators are
read as matrices by applying them to their own domain's basis, so no element is coerced between two constructions of
$T_{\\mathrm{En}}$.

    .scratch/wt43j-run.sh -u results/probe-43-coble-classes.py [row]      # 5 is Sterk's (4.3.9)
"""

import sys
import time
from fractions import Fraction
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions, NamedLattices  # noqa: F401,F403

CARD = Path("/repo/lattices/029J.md")
NUMBER = int(sys.argv[1]) if len(sys.argv) > 1 else 5
start = time.time()


def entries(element):
    """Coordinates in the lattice's own basis, in the order its module generators come."""
    return tuple(Fraction(int(entry)) for entry in element.to_vector())


row = corpus.front_matter(corpus.read_card(CARD))["integral"]["cusp_chambers"]["gamma-en-2"][NUMBER - 1]
enriques = NamedLattices.TEn
labels = tuple(enriques.module_generating_set())
rank = int(enriques.module_rank())

cusp = enriques.linear_combination(
    {labels[i]: enriques.base_ring()(int(entry)) for i, entry in enumerate(row["cusp"]) if int(entry)}
)
invariant = Involutions.I_En.invariant_lattice()
invariant_labels = tuple(invariant.module_generating_set())
marks = [
    (left, right)
    for left in invariant_labels
    for right in invariant_labels
    if left <= right
    and invariant.q(invariant.module_generator(left)) == ZZ.zero()
    and invariant.q(invariant.module_generator(right)) == ZZ.zero()
    and invariant.b(invariant.module_generator(left), invariant.module_generator(right)) == ZZ(2)
]
polarization = invariant.module_generator(marks[0][0]) + invariant.module_generator(marks[0][1])
group = Involutions.I_En.polarized(invariant.inclusion()(polarization)).coinvariant_extension_subgroup()
image = group.isotropic_vector_reduction_image(cusp)
family = tuple(group.supergroup().isotropic_stabilizer_generators(image.line()))
print(f"[{time.time() - start:6.1f}s] {row['statement']}: {len(family)} generators of the cusp stabilizer", flush=True)

domain = family[0].domain()
basis = tuple(domain.module_generating_set())
gram = [[int(domain.b(domain.module_generator(a), domain.module_generator(b))) for b in basis] for a in basis]
assert gram == [
    [int(enriques.b(enriques.module_generator(a), enriques.module_generator(b))) for b in labels] for a in labels
], "the generators act on a lattice other than T_En's"


def pairing(left, right):
    return sum((left[i] * gram[i][j] * right[j] for i in range(rank) for j in range(rank)), Fraction(0))


def matrix(generator):
    """The generator's matrix, from the images of its own domain's basis."""
    images = [entries(generator(domain.module_generator(label))) for label in basis]
    return [[images[column][index] for column in range(rank)] for index in range(rank)]


def applied(matrix_of, coordinates):
    return tuple(sum((coordinates[j] * matrix_of[i][j] for j in range(rank)), Fraction(0)) for i in range(rank))


cusp_entries = entries(cusp)
delta_entries = tuple(Fraction(1) if index == 0 else Fraction(-1) if index == 1 else Fraction(0) for index in range(rank))
walls = [entries(enriques.linear_combination({labels[i]: enriques.base_ring()(int(entry)) for i, entry in enumerate(wall["vector"]) if int(entry)})) for wall in row["walls"]]
names = [wall["name"] for wall in row["walls"]]
roots = [
    index
    for index in range(len(walls))
    if pairing(walls[index], delta_entries) == 0 and pairing(walls[index], walls[index]) == -2
]
print(f"  {len(walls)} walls, {len(roots)} in T_Co of square -2: {[names[i] for i in roots]}", flush=True)


def same_class(left, right):
    """Whether two vectors of $T_{\\mathrm{Co}}$ differ by a rational multiple of the cusp: one class of $K_I$."""
    difference = [left[i] - right[i] for i in range(rank)]
    scales = {difference[i] / cusp_entries[i] for i in range(rank) if cusp_entries[i] != 0}
    return len(scales) == 1 and all(difference[i] == 0 for i in range(rank) if cusp_entries[i] == 0)


preserving = []
for generator in family:
    matrix_of = matrix(generator)
    image_of_delta = applied(matrix_of, delta_entries)
    if image_of_delta == delta_entries or image_of_delta == tuple(-entry for entry in delta_entries):
        preserving.append(matrix_of)
print(f"[{time.time() - start:6.1f}s] {len(preserving)} of {len(family)} generators preserve T_Co", flush=True)

merges: dict[tuple[int, int], int] = {}
for matrix_of in preserving:
    for source in roots:
        image_of_wall = applied(matrix_of, walls[source])
        for target in roots:
            if source != target and same_class(image_of_wall, walls[target]):
                merges[tuple(sorted((source, target)))] = merges.get(tuple(sorted((source, target))), 0) + 1
for pair, count in sorted(merges.items()):
    print(f"    {names[pair[0]]} ~ {names[pair[1]]} by {count} element(s) of Gamma_Co,2", flush=True)
if not merges:
    print("    no merge found", flush=True)

components = {index: {index} for index in roots}
for pair in merges:
    left, right = pair
    if components.get(left) is components.get(right):
        continue
    joined = components.pop(left, set()) | components.pop(right, set())
    for member in joined:
        components[member] = joined
print(f"RESULT {row['statement']}: {len(components)} components, sizes {sorted(len(c) for c in components.values())}", flush=True)
