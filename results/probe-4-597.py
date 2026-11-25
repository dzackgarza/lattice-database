"""#7/#597: does the owner return a generating family for Otilde(T_Co) today?"""
import time

import frontmatter

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import ZZ

card = frontmatter.load("lattices/6JRR.md").metadata
lattice = Lattices(ZZ)(card["gram_tensor"])
print("T_Co: rank", len(card["gram_tensor"]), "det", card["determinant"], "signature", card["signature"])
started = time.time()
try:
    family = lattice.stable_orthogonal_group_generators()
    print(f"RETURNED {type(family).__name__} of {len(family)} in {time.time() - started:.1f}s")
except Exception as error:  # noqa: BLE001 - the refusal is the answer
    print(f"RAISED {type(error).__name__} after {time.time() - started:.1f}s:")
    print(str(error))
