"""#43: which construction answers the line stabilizer's generators on the owner's main, the library's or the port's.

`_marked_automorphism_generators` (sage-extensions `lattices.py`) tries the library-owned family first and falls
back to the port when the construction refuses.  The owner's debug switches print which one ran, and this asks the
same call with them on, so the evidence says what the 28 members are.

    .scratch/wt43c-run.sh -u results/probe-43-line-route.py
"""

import os
import time
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions, NamedLattices  # noqa: F401,F403

os.environ["SE_DEBUG_STAGES"] = "1"
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
family = tuple(group.supergroup().isotropic_stabilizer_generators(image.line()))
print(f"[{time.time() - start:6.1f}s] RESULT: {len(family)} members", flush=True)
