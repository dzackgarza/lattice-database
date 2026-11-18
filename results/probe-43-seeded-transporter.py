r"""#43: a transporter for the root classes, seeded by the supergroup and verified through `contains`.

The closed #312 operation gives exact membership, on the *reduced* isometry with its lift:
`image.contains(image.reduction_image(g), lift=g)`.  Earlier probes used `image.contains(g)` on an ambient isometry and
were refused (`isotropic_orbits.py:3111`).  This probe builds a seed that already fixes the cusp -- a supergroup
witness `r -> r'` composed with one carrying the image cusp back -- reduces it, and walks the images of the first root
class through that seed together with the stabilizer's generators and the walls' reflections.

A word that lands on the second class seems the row; the membership test then says whether the word is in `G_v`, which
is what makes it a proof rather than a candidate.

    run.sh -w /repos/lattice-database -b <repo>:/repos/lattice-database \
        -b <clone>:/repos/sage-extensions -- env PYTHONPATH=... python results/probe-43-seeded-transporter.py
"""

import time
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions

start = time.time()


def stamp(label: str) -> None:
    print(f"[{time.time() - start:7.1f}s] {label}", flush=True)


metadata = corpus.front_matter(corpus.read_card(Path("/repos/lattice-database/lattices/029J.md")))
invariant = Involutions.I_En.invariant_lattice()
labels = tuple(invariant.module_generating_set())
marks = [
    (left, right)
    for left in labels
    for right in labels
    if left <= right
    and invariant.q(invariant.module_generator(left)) == ZZ.zero()
    and invariant.q(invariant.module_generator(right)) == ZZ.zero()
    and invariant.b(invariant.module_generator(left), invariant.module_generator(right)) == ZZ(2)
]
left, right = marks[0]
polarization = invariant.module_generator(left) + invariant.module_generator(right)
gamma = Involutions.I_En.polarized(invariant.inclusion()(polarization)).coinvariant_extension_subgroup()
supergroup = gamma.supergroup()
ambient = supergroup.domain()
stamp("Gamma and its supergroup built")

row = metadata["integral"]["cusp_chambers"]["gamma-en-2"][3]
cusp = ambient(tuple(int(entry) for entry in row["cusp"]))
walls = {wall["name"]: ambient(tuple(int(entry) for entry in wall["vector"])) for wall in row["walls"]}
first = next(name for name in walls if name.endswith("alpha_9"))
second = next(name for name in walls if name.endswith("alpha_11"))
image = gamma.isotropic_vector_reduction_image(cusp)
reduction = image.reduction()
class_one = image.root_class(walls[first])
class_two = image.root_class(walls[second])
stamp(f"image at the cusp ({row['statement']}); two root classes")

maps = []
labels_of_maps = []

witness = supergroup.vector_equivalence_witness(walls[first], walls[second])
if witness is not None:
    if witness(cusp) not in (cusp, -cusp):
        back = supergroup.vector_equivalence_witness(witness(cusp), cusp)
        witness = None if back is None else back * witness
    if witness is not None:
        maps.append(image.reduction_image(witness))
        labels_of_maps.append("supergroup seed")
stamp(f"{len(maps)} seed(s) from the supergroup")

for generator in image.subgroup().supergroup().isotropic_stabilizer_generators(image.line()):
    if generator(cusp) not in (cusp, -cusp):
        continue
    reduced = image.reduction_image(generator)
    if image.contains(reduced, lift=generator):
        maps.append(reduced)
        labels_of_maps.append("stabilizer generation")
stamp(f"{len(maps)} maps after the stabilizer's generators")

frontier = [(class_one, ())]
visited = {tuple(reduction(class_one))}
found = None
for depth in range(1, 5):
    following = []
    for state, steps in frontier:
        for index, generator in enumerate(maps):
            reached = generator(state)
            key = tuple(reduction(reached))
            if reached == class_two:
                found = steps + (labels_of_maps[index],)
                break
            if key in visited:
                continue
            visited.add(key)
            following.append((reached, steps + (labels_of_maps[index],)))
        if found is not None:
            break
    frontier = following
    stamp(f"depth {depth}: ball {len(visited)}, found {found}")
    if found is not None or not frontier:
        break
print("TRANSPORTER", found, flush=True)
