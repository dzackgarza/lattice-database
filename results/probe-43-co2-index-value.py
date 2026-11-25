"""#43: the two orders a `gamma-co-2` card's index is the product of.

The library identifies the restricted stabilizers on $T_{\\mathrm{Co}}$ (sage-extensions
`results/issue359-tco-restricted-stabilizers.md`, rows 1 and 2): $R_{\\Gamma_{\\mathrm{En}}} = \\widetilde
O^{+}(T_{\\mathrm{Co}})$, of index $93997183795200 = 2|O(A_{T_{\\mathrm{Co}}}, q)|$ in $O(T_{\\mathrm{Co}})$, and
$R_{\\Gamma^{K}_{\\mathrm{En}}} = O(T_{\\mathrm{Co}})$, index $1$. The group of the Coble cusps is
$\\Gamma_{\\mathrm{Co},2} = R_{\\Gamma_{\\mathrm{En},2}}$, the kernel of the $T_{\\mathrm{En}}$-side discriminant
character on $\\widetilde O^{+}(T_{\\mathrm{Co}})$, whose image has order $|O(A_{T_{\\mathrm{Co}}}, q)|$. So a card
would state $[O(T_{\\mathrm{Co}}) : \\Gamma_{\\mathrm{Co},2}] = 93997183795200 \\cdot |O(A_{T_{\\mathrm{Co}}}, q)|$.

This computes the second factor on card 6JRR's own Gram tensor, from the library's discriminant group, and multiplies.

    .scratch/wt43q-run.sh -u results/probe-43-co2-index-value.py
"""

import time
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Lattices  # noqa: F401,F403

start = time.time()
metadata = corpus.front_matter(corpus.read_card(Path("/repo/lattices/6JRR.md")))
gram = [[int(entry) for entry in row] for row in metadata["gram_tensor"]]
lattice = Lattices(ZZ)(gram)
print(f"[{time.time() - start:5.1f}s] T_Co from card 6JRR: {lattice!r}", flush=True)
discriminant = lattice.discriminant_group()
order = discriminant.orthogonal_group().order()
print(f"[{time.time() - start:5.1f}s] |O(A_T_Co, q)| = {order}", flush=True)
print(f"RESULT: [O(T_Co) : Gamma_Co,2] = 93997183795200 * {order} = {93997183795200 * int(order)}", flush=True)
