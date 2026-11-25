"""#43: does the owner certify the orbit count of a cusp's root classes?  Run in the pinned image.

Card 029J's row for Sterk's (4.3.8), p. 23, gives the cusp and its eleven walls in the card's own coordinates,
which are `T_{En}`'s.  The probe builds `Gamma_{En,2}` on `T_{En}` as sage-extensions' own test does, the
reduction image at that cusp, the root classes of `K_J` among the walls, and the stabilizer's orbits of them.
What it prints decides the issue's second requirement: `generators_are_certified_complete` says whether the
acting family is the cusp stabilizer or only a subgroup of it, and `generation_obstruction` says what is missing.

    run.sh -w /repos/lattice-database -b <repo>:/repos/lattice-database -b <clone>:/repos/sage-extensions \
        -- env PYTHONPATH=/repos/research/src:/repos/lattice-database/src python results/probe-43-cusp-root-class-orbits.py
"""

import time
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions, NamedLattices  # noqa: F401,F403

CARD = Path("/repos/lattice-database/lattices/029J.md")
NUMBER = 4

start = time.time()


def stamp(label: str) -> None:
    print(f"[{time.time() - start:7.1f}s] {label}", flush=True)


row = corpus.front_matter(corpus.read_card(CARD))["integral"]["cusp_chambers"]["gamma-en-2"][NUMBER - 1]

lattice = NamedLattices.TEn
labels = tuple(lattice.module_generating_set())


def vector(entries):
    """One vector of the card, in `T_{En}`'s basis, from the entries the card stores."""
    return lattice.linear_combination(
        {
            label: lattice.base_ring()(int(entry))
            for label, entry in zip(labels, entries, strict=True)
            if int(entry)
        }
    )


cusp = vector(row["cusp"])
assert lattice.q(cusp) == ZZ.zero() and cusp.is_primitive() is True
walls = tuple(vector(wall["vector"]) for wall in row["walls"])
stamp(f"card row {row['statement']}, cusp {tuple(row['cusp'])}, {len(walls)} walls")

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
left, right = marks[0]
polarization = invariant.module_generator(left) + invariant.module_generator(right)
group = Involutions.I_En.polarized(invariant.inclusion()(polarization)).coinvariant_extension_subgroup()
stamp("Gamma_En,2 built")

image = group.isotropic_vector_reduction_image(cusp)
reduction = image.reduction()
stamp("reduction image at the card's cusp built")
print("generators_are_certified_complete:", image.generators_are_certified_complete())
print("generation_obstruction:", image.generation_obstruction())

classes = []
for wall in walls:
    class_ = image.root_class(wall)
    if all(class_ != seen for seen in classes):
        classes.append(class_)
roots = [class_ for class_ in classes if reduction.q(class_) == -ZZ(2)]
stamp(f"{len(classes)} classes of the walls, {len(roots)} of them roots of K_J")

stabilizer = tuple(image.subgroup().supergroup().isotropic_stabilizer_generators(image.line()))
stamp(f"{len(stabilizer)} stabilizer generators")
orbits = image.root_class_orbits(tuple(roots), stabilizer_generators=stabilizer)
sizes = [len(tuple(orbit.index_set())) for orbit in orbits]
stamp(f"{len(sizes)} components, of sizes {sizes}")
print(
    "RESULT",
    {
        "statement": row["statement"],
        "wall_classes": len(classes),
        "roots": len(roots),
        "components": len(sizes),
        "sizes": sizes,
        "certified_complete": image.generators_are_certified_complete(),
    },
)
