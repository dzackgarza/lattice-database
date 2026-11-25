"""#43: what the owner's main decides of a cusp's root-class orbits today.  Run in the pinned image.

The three rows still missing from card 029J --- Sterk's (4.3.7), (4.3.8) and (4.3.9), pp. 22--24 --- need a decision
of whether two *classes* of $K_J = v^\\perp/\\mathbb{Z}v$ lie in one $\\Gamma_v$-orbit.  The previous turns recorded that
the owner's ambient equivalence works and that the class-level one is what is missing, and this probe asks the owner's
current `main` for each part, one bounded stage at a time, so that a stage which does not return is a measurement with
its own line:

  A  the card's own row at (4.3.8), the reduction image at its cusp, and the class-level entry point;
  B  the family the image acts with: is it certified to generate $G_v$, and where does the obstruction say it stops;
  C  `Stab_{O(L)}(v)`'s generators, which is sage-extensions#603's subject, bounded at 240 s;
  D  the ambient witness that exists (fast), and the subgroup's own equivalence bounded at 180 s.

Every stage prints `RESULT` before the next one starts; the image is killed only if a stage overruns its own alarm.

    .scratch/wt-run.sh results/probe-43-dependency-603.py
"""

import signal
import time
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions, NamedLattices  # noqa: F401,F403

CARD = Path("/repo/lattices/029J.md")
NUMBER = 4  # Sterk's (4.3.8), p. 23
start = time.time()


def stamp(label: str) -> None:
    print(f"[{time.time() - start:7.1f}s] {label}", flush=True)


class Overran(Exception):
    """A stage did not return inside its own budget."""


def bounded(seconds: float):
    def entry(function):
        def run(*arguments, **keywords):
            def raise_overran(signum, frame):
                raise Overran(f"{seconds:.0f} s")

            previous = signal.signal(signal.SIGALRM, raise_overran)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                return function(*arguments, **keywords)
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
                signal.signal(signal.SIGALRM, previous)

        return run

    return entry


row = corpus.front_matter(corpus.read_card(CARD))["integral"]["cusp_chambers"]["gamma-en-2"][NUMBER - 1]
lattice = NamedLattices.TEn
labels = tuple(lattice.module_generating_set())


def vector(entries):
    return lattice.linear_combination(
        {
            label: lattice.base_ring()(int(entry))
            for label, entry in zip(labels, entries, strict=True)
            if int(entry)
        }
    )


cusp = vector(row["cusp"])
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
polarization = invariant.module_generator(marks[0][0]) + invariant.module_generator(marks[0][1])
group = Involutions.I_En.polarized(invariant.inclusion()(polarization)).coinvariant_extension_subgroup()
image = group.isotropic_vector_reduction_image(cusp)
reduction = image.reduction()
stamp("Gamma_En,2 and the reduction image at the card's cusp built")

# A. The class-level entry point the previous turns named.
print("image type:", type(image).__mro__[0].__name__, flush=True)
print("class-level vectors_are_equivalent on the image:", hasattr(type(image), "vectors_are_equivalent"), flush=True)
print("instance-level vectors_are_equivalent:", hasattr(image, "vectors_are_equivalent"), flush=True)
print(
    "class-level entries of the image:",
    sorted(name for name in dir(type(image)) if not name.startswith("_")),
    flush=True,
)
classes = []
for wall in walls:
    class_ = image.root_class(wall)
    if all(class_ != seen for seen in classes):
        classes.append(class_)
roots = [class_ for class_ in classes if reduction.q(class_) == -ZZ(2)]
print(
    "RESULT A",
    {"statement": row["statement"], "wall_classes": len(classes), "roots": len(roots)},
    flush=True,
)
stamp(f"{len(classes)} classes of the walls, {len(roots)} of them roots of K_J")

# B. The family the image acts with, and what the owner says it misses.
print("generators_are_certified_complete:", image.generators_are_certified_complete(), flush=True)
print("generation_obstruction:", image.generation_obstruction(), flush=True)
try:
    family = tuple(image.generators())
    print("RESULT B", {"certified": False, "generators": len(family)}, flush=True)
except ValueError as refusal:
    print("RESULT B", {"certified": False, "generators": f"ValueError: {refusal}"}, flush=True)
stamp("image's own generators and obstruction read")

# C. sage-extensions#603's subject: library-built generators of Stab_{O(L)}(v) at a vector.
try:
    family = bounded(240.0)(lambda: tuple(group.supergroup().vector_stabilizer_generators(image.vector())))()
    print("RESULT C", {"returned": True, "generators": len(family)}, flush=True)
except Overran as overran:
    print("RESULT C", {"returned": False, "budget": str(overran)}, flush=True)
except Exception as failure:  # noqa: BLE001 - the refusal is the measurement
    print("RESULT C", {"returned": False, "raised": f"{type(failure).__name__}: {failure}"}, flush=True)
stamp("vector_stabilizer_generators at the cusp asked")

# D. The ambient witness that exists, and the subgroup's own equivalence for the pair, on the classes' own lifts.
lifts = tuple(image.class_lift(root) for root in roots)
print("lifts of the two classes:", [f"[{index}] {list(lift.to_vector())[:4]}..." for index, lift in enumerate(lifts)], flush=True)
ambient = bounded(120.0)(lambda: group.supergroup().vector_equivalence_witness(lifts[0], lifts[1]))()
print("RESULT D ambient witness:", ambient is not None, flush=True)
try:
    found = bounded(180.0)(lambda: group.vector_equivalence_witness(lifts[0], lifts[1]))()
    print("RESULT D subgroup witness:", found is not None, flush=True)
except Overran as overran:
    print("RESULT D subgroup witness: did not return inside", str(overran), flush=True)
except Exception as failure:  # noqa: BLE001 - the refusal is the measurement
    print("RESULT D subgroup witness:", f"{type(failure).__name__}: {failure}", flush=True)
stamp("subgroup equivalence asked")
