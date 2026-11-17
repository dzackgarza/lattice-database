"""Which branch the SOtilde+ line walk takes, and what one representative costs."""
import itertools
import json
import sys
import time

sys.stdout.reconfigure(line_buffering=True)


def hwm_mib():
    for line in open("/proc/self/status"):
        if line.startswith("VmHWM"):
            return int(line.split()[1]) // 1024
    return -1


import sage_extensions
from sage.rings.integer_ring import ZZ
from sage_extensions.all import Lattices

print("sage_extensions", sage_extensions.__file__, flush=True)
gram = json.load(open("/repo/.scratch/tco/gram.json"))
L = Lattices(ZZ)(gram)
stable = L.stable_orthogonal_group()
plus = L.O_plus()
special = L.SO()
group = stable.intersection(plus).intersection(special)

start = time.time()
quotient = group.finite_character_quotient()
print(f"finite_character_quotient: {time.time() - start:.2f}s  {quotient}  peak {hwm_mib()} MiB", flush=True)

start = time.time()
ambient = list(L.Aut().isotropic_orbit_representatives(1))
print(f"ambient row: {len(ambient)} lines in {time.time() - start:.1f}s peak {hwm_mib()} MiB", flush=True)

for position, representative in enumerate(ambient[:6]):
    start = time.time()
    image = quotient.isotropic_line_stabilizer_image(representative)
    seconds = time.time() - start
    branch = image if image in (None, "NOSPLIT") else f"image {type(image).__name__}"
    print(f"  line {position}: {branch} in {seconds:.2f}s peak {hwm_mib()} MiB", flush=True)
    if image not in (None, "NOSPLIT"):
        start = time.time()
        splittings = list(itertools.islice(quotient.splitting_isometries_from_line_class(*image), 4))
        print(f"    splittings (first 4): {len(splittings)} in {time.time() - start:.2f}s peak {hwm_mib()} MiB", flush=True)
