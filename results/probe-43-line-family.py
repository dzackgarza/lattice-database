"""#43: is the cusp stabilizer's own family available from the library now, and does it move the classes?

The three rows still missing from card 029J need one decision: whether two classes of $K_J = v^\\perp/\\mathbb{Z}v$
lie in one orbit under $\\Gamma_v$.  The library's `_isotropic_line_stabilizer_generators` now constructs the setwise
line stabilizer's generators from the Levi split (sage-extensions main 41b75d7), which would be the family the walk
has been missing.  This probe asks for it at the card's own cusp and filters it through the image's exact membership test, so that what
it walks with is inside $\\Gamma_v$ --- a merge is then a proof of one orbit, whatever the family's completeness.

    .scratch/wt43c-run.sh -u results/probe-43-line-family.py [row]      # row 4 is Sterk's (4.3.8) by default
"""

import time
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions, NamedLattices  # noqa: F401,F403

import sys

CARD = Path("/repo/lattices/029J.md")
NUMBER = int(sys.argv[1]) if len(sys.argv) > 1 else 4  # Sterk's (4.3.8), p. 23, unless a row is named
start = time.time()


def stamp(label: str) -> None:
    print(f"[{time.time() - start:7.1f}s] {label}", flush=True)


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
stamp(f"card row {row['statement']}, image built: {image.generators_are_certified_complete()=}")
print("class-level vectors_are_equivalent:", hasattr(type(image), "vectors_are_equivalent"), flush=True)

classes = []
for wall in walls:
    class_ = image.root_class(wall)
    if all(class_ != seen for seen in classes):
        classes.append(class_)
roots = [class_ for class_ in classes if reduction.q(class_) == -ZZ(2)]
print(f"RESULT A: {len(classes)} classes of the walls, {len(roots)} roots of K_J", flush=True)

# The library's own line-stabilizer family, through the public call the dispatch routes.
line = image.line()
try:
    family = tuple(group.supergroup().isotropic_stabilizer_generators(line))
    print(f"RESULT B: the line stabilizer family has {len(family)} members", flush=True)
except Exception as failure:  # noqa: BLE001 - the refusal is the measurement
    print("RESULT B:", f"{type(failure).__name__}: {failure}", flush=True)
    raise SystemExit(0)
stamp("line stabilizer family collected")

inside = []
for generator in family:
    try:
        if image.contains(image.reduction_image(generator), lift=generator):
            inside.append(generator)
    except Exception as failure:  # noqa: BLE001
        print("  membership raised:", type(failure).__name__, str(failure)[:120], flush=True)
print(f"RESULT C: {len(inside)} of {len(family)} members lie in Gamma_v", flush=True)
stamp("family filtered by the exact membership test")

orbits = image.root_class_orbits(tuple(roots), stabilizer_generators=tuple(inside))
sizes = [len(tuple(orbit.index_set())) for orbit in orbits]
print(f"RESULT D: {len(sizes)} components of sizes {sizes}", flush=True)
stamp("root classes walked")
