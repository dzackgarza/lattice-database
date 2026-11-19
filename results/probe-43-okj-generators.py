"""#43: where the line stabilizer's family gets its `O(K_J)` generators, and whether that link is owned.

`_isotropic_line_stabilizer_generators` builds `P_v`'s family from one integral lift per generator of `O(K_J)` and
the Levi kernel's generators.  The family is complete exactly when those two links are, so this asks the middle link
what it is: whether `O(K_J)` reports a selected generating resolution, and what its family is.

    .scratch/wt43c-run.sh -u results/probe-43-okj-generators.py
"""

import time
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions, NamedLattices  # noqa: F401,F403

CARD = Path("/repo/lattices/029J.md")
start = time.time()
row = corpus.front_matter(corpus.read_card(CARD))["integral"]["cusp_chambers"]["gamma-en-2"][3]
lattice = NamedLattices.TEn
labels = tuple(lattice.module_generating_set())
cusp = lattice.linear_combination(
    {label: lattice.base_ring()(int(entry)) for label, entry in zip(labels, row["cusp"], strict=True) if int(entry)}
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
quotient = image.reduction().quotient_lattice()
orthogonal = quotient.O()
print(f"K_J = {quotient}", flush=True)
print("has_selected_group_resolution:", orthogonal.has_selected_group_resolution(), flush=True)
print("group_generators_are_computable:", orthogonal.group_generators_are_computable(), flush=True)
try:
    family = tuple(orthogonal.group_generators())
    print(f"RESULT: O(K_J) reports {len(family)} generators, in {time.time() - start:.1f}s", flush=True)
except Exception as failure:  # noqa: BLE001 - the refusal is the measurement
    print("RESULT:", f"{type(failure).__name__}: {failure}", flush=True)
