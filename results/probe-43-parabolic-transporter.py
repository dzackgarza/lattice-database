r"""#43: a transporter built from the parabolic, with the exact membership test as the decider.

A supergroup witness `w` with `w(r) = r'` exists and is cheap (under 15 s), but it moves the cusp.  If `h` is an
element of the stabilizer's own parabolic generators with `h(w(v)) = v` and `h(r') = r' + t v`, then `g = h w` fixes
the cusp and carries `r` to the class of `r'`, and `image.contains(image.reduction_image(g), lift=g)` -- exact, a
discriminant computation -- decides whether `g` is in `G_v`.  A "yes" is a proof that the two root classes are one
orbit.

    run.sh -w /repos/lattice-database -b <repo>:/repos/lattice-database \
        -b <clone>:/repos/sage-extensions -- env PYTHONPATH=... python results/probe-43-parabolic-transporter.py
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

row = metadata["integral"]["cusp_chambers"]["gamma-en-2"][3]
cusp = ambient(tuple(int(entry) for entry in row["cusp"]))
walls = {wall["name"]: ambient(tuple(int(entry) for entry in wall["vector"])) for wall in row["walls"]}
first = next(name for name in walls if name.endswith("alpha_9"))
second = next(name for name in walls if name.endswith("alpha_11"))
image = gamma.isotropic_vector_reduction_image(cusp)
stamp("Gamma, supergroup and image built")

witness = supergroup.vector_equivalence_witness(walls[first], walls[second])
stamp(f"supergroup witness: {witness is not None}")
if witness is None:
    raise SystemExit("no supergroup witness")
w_image_cusp = witness(cusp)
r_image = witness(walls[first])

parabolic = []
for generator in image.subgroup().supergroup().isotropic_stabilizer_generators(image.line()):
    if generator(cusp) in (cusp, -cusp):
        parabolic.append(generator)
stamp(f"{len(parabolic)} parabolic generators that fix the cusp")

# Breadth-first over words in the parabolic, on the pair (image of w(v), image of r).
frontier = [((w_image_cusp, r_image), ())]
seen = {(tuple(w_image_cusp), tuple(r_image))}
answer = None
for depth in range(1, 5):
    following = []
    for (cusp_now, root_now), steps in frontier:
        for index, generator in enumerate(parabolic):
            next_cusp = generator(cusp_now)
            next_root = generator(root_now)
            key = (tuple(next_cusp), tuple(next_root))
            if next_cusp in (cusp, -cusp):
                composite = generator if not steps else generator
                # rebuild the word by applying the generators in the recorded order
                word = steps + (index,)
                candidate = None
                for position in reversed(word):
                    candidate = parabolic[position] if candidate is None else parabolic[position] * candidate
                candidate = candidate * witness
                if candidate(cusp) in (cusp, -cusp):
                    inside = image.contains(image.reduction_image(candidate), lift=candidate)
                    if inside:
                        answer = (word, candidate(candidate(cusp)) is candidate(cusp))
                        break
            if key in seen:
                continue
            seen.add(key)
            following.append(((next_cusp, next_root), steps + (index,)))
        if answer is not None:
            break
    frontier = following
    stamp(f"depth {depth}: states {len(seen)}, answer {answer is not None}")
    if answer is not None or not frontier:
        break

print("TRANSPORTER", None if answer is None else answer[0], flush=True)
if answer is not None:
    word, _ = answer
    candidate = None
    for position in reversed(word):
        candidate = parabolic[position] if candidate is None else parabolic[position] * candidate
    candidate = candidate * witness
    print("carries the first root to", candidate(walls[first]), "| in G_v:", image.contains(image.reduction_image(candidate), lift=candidate), flush=True)
stamp("done")
