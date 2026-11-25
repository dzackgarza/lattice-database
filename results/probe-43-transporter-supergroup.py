r"""#43: a transporter for a cusp's root classes, built from the closed #312 operation's cheap parts.

The closed operation gives, for a subgroup cut out by a condition on `A_L`, the image `G_v = Stab_Gamma(v) |-> O(v^perp/ZZ v)`
with an exact membership test (`image.contains`, a discriminant computation), and it gives exact vector equivalence on
the subgroup (`vectors_are_equivalent`).  The subgroup's own equivalence walks a coset of an infinite stabilizer and does
not return here (18 min 20 s, no result).

So build the transporter the other way round, from the two cheap parts:

1. a witness `w` in the *supergroup* carrying `r` to `r' + t v` -- the supergroup is `O(T_En)` restricted by the
   polarization, and its vector equivalence is the route the subgroup route calls first anyway;
2. an element `h` of the supergroup carrying `w(v)` back to `v`, so `h w` fixes the cusp line;
3. ask `image.contains(h w)` -- the exact discriminant test -- to decide whether `h w` is in the stabilizer's image.

A "yes" is a proof that the two root classes are one `Stab_Gamma(v)`-orbit.  A "no" is not a proof of the converse
without completeness of the image's generators, and is reported as unknown.

    run.sh -w /repos/lattice-database -b <repo>:/repos/lattice-database \
        -b <clone>:/repos/sage-extensions -- env PYTHONPATH=... python results/probe-43-transporter-supergroup.py
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
stamp(f"Gamma and its supergroup built; supergroup {type(supergroup).__name__}")

row = metadata["integral"]["cusp_chambers"]["gamma-en-2"][3]
cusp = ambient(tuple(int(entry) for entry in row["cusp"]))
walls = {wall["name"]: ambient(tuple(int(entry) for entry in wall["vector"])) for wall in row["walls"]}
first = next(name for name in walls if name.endswith("alpha_9"))
second = next(name for name in walls if name.endswith("alpha_11"))
stamp(f"cusp and roots: {first} square {walls[first].q()}, {second} square {walls[second].q()}")

witness = supergroup.vector_equivalence_witness(walls[first], walls[second])
stamp(f"supergroup witness for the pair: {witness is not None}")
if witness is None:
    raise SystemExit("no supergroup witness, so this route cannot start")
print("witness carries the first root to", witness(walls[first]), "and the cusp to", witness(cusp), flush=True)

image = gamma.isotropic_vector_reduction_image(cusp)
stamp("image at the cusp")
if witness(cusp) != cusp:
    back = supergroup.vector_equivalence_witness(witness(cusp), cusp)
    stamp(f"a witness carrying the image cusp back: {back is not None}")
    if back is not None:
        candidate = back * witness
        print("composite fixes the cusp:", candidate(cusp) == cusp, "| carries the first root to", candidate(walls[first]), flush=True)
        print("is it in the stabilizer's image?", image.contains(candidate), flush=True)
else:
    print("witness already fixes the cusp; is it in the image?", image.contains(witness), flush=True)
stamp("done")
