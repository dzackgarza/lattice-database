"""#43: does the whole line stabilizer, not only its Gamma_v part, move a cusp's root classes?

The row's count is the number of orbits under $\\Gamma_v$, and $\\Gamma_v \\subseteq P_v = \\mathrm{Stab}_{O(L)}(\\mathbb{Z}v)$,
so a class that no element of $P_v$ carries to another is in an orbit of its own under $\\Gamma_v$ as well.  The
library's public `isotropic_stabilizer_generators(line)` returns $P_v$'s family --- one integral lift per generator of
$O(K_J)$ together with the selected kernel generators (`_isotropic_line_stabilizer_generators`, sage-extensions main
41b75d7) --- so walking the given classes with that family answers the wider question.  It is the *smaller* answer
that the card needs: an orbit under $P_v$ that is larger than an orbit under $\\Gamma_v$ cannot be told apart here,
and a singleton under $P_v$ is a singleton under $\\Gamma_v$ only if the family really generates $P_v$
(`generation_obstruction` still says it does not).

    .scratch/wt43c-run.sh -u results/probe-43-stabilizer-orbits.py [row]   # row 4 is Sterk's (4.3.8)
"""

import sys
import time
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions, NamedLattices  # noqa: F401,F403

CARD = Path("/repo/lattices/029J.md")
NUMBER = int(sys.argv[1]) if len(sys.argv) > 1 else 4
start = time.time()
row = corpus.front_matter(corpus.read_card(CARD))["integral"]["cusp_chambers"]["gamma-en-2"][NUMBER - 1]
lattice = NamedLattices.TEn
labels = tuple(lattice.module_generating_set())


def vector(entries):
    return lattice.linear_combination(
        {label: lattice.base_ring()(int(entry)) for label, entry in zip(labels, entries, strict=True) if int(entry)}
    )


cusp = vector(row["cusp"])
walls = tuple(vector(wall["vector"]) for wall in row["walls"])
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
reduction = image.reduction()
classes = []
for wall in walls:
    class_ = image.root_class(wall)
    if all(class_ != seen for seen in classes):
        classes.append(class_)
roots = [class_ for class_ in classes if reduction.q(class_) == -ZZ(2)]
print(f"row {row['statement']}: {len(classes)} wall classes, {len(roots)} roots of K_J", flush=True)

family = tuple(group.supergroup().isotropic_stabilizer_generators(image.line()))
maps = [image.reduction_image(generator) for generator in family]
print(f"P_v family: {len(family)} generators, reduced", flush=True)

position = {index: index for index in range(len(roots))}
components = []
remaining = set(position)
while remaining:
    seed = min(remaining)
    orbit = {seed}
    frontier = [seed]
    while frontier:
        current = frontier.pop()
        for image_map in maps:
            landed = image_map(roots[current])
            for index, other in enumerate(roots):
                if index in orbit or landed != other:
                    continue
                orbit.add(index)
                frontier.append(index)
    remaining -= orbit
    components.append(sorted(orbit))
print(f"RESULT: {len(components)} components of sizes {[len(c) for c in components]}", flush=True)
print(f"[{time.time() - start:6.1f}s]", flush=True)
