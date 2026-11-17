"""Does the same subgroup answer affordably when it is built another way?

SOtilde+ is `stable ∩ SO ∩ O+`. The driver builds it as (stable ∩ SO) ∩ O+ and
that walk did not return; this measures the other constructions of the same
subgroup, one per process-lifetime stage, recording each to results-alt.json.
"""
import json
import sys
import time
import traceback

sys.stdout.reconfigure(line_buffering=True)
OUT = "/repo/.scratch/tco/results-alt.json"
record = {"stages": {}}


def hwm_mib():
    for line in open("/proc/self/status"):
        if line.startswith("VmHWM"):
            return int(line.split()[1]) // 1024
    return -1


def available_mib():
    for line in open("/proc/meminfo"):
        if line.startswith("MemAvailable"):
            return int(line.split()[1]) // 1024
    return -1


def flush():
    json.dump(record, open(OUT, "w"), indent=1, default=str)


import sage_extensions
from sage.rings.integer_ring import ZZ
from sage_extensions.all import Lattices

record["sage_extensions"] = sage_extensions.__file__
gram = json.load(open("/repo/.scratch/tco/gram.json"))
L = Lattices(ZZ)(gram)
stable = L.stable_orthogonal_group()
plus = L.O_plus()
special = L.SO()

variants = {
    "(Otilde & O+) & SO": stable.intersection(plus).intersection(special),
    "SO & (O+ & Otilde)": special.intersection(plus.intersection(stable)),
    "O+ & (SO & Otilde)": plus.intersection(special.intersection(stable)),
}

for label, group in variants.items():
    start = time.time()
    print(f">> {label}", flush=True)
    try:
        orbits = group.isotropic_orbit_representatives(1)
        cardinality = orbits.cardinality()
        value = cardinality.finite_value() if hasattr(cardinality, "finite_value") else int(cardinality)
        record["stages"][label] = {
            "seconds": round(time.time() - start, 2),
            "peak_mib": hwm_mib(),
            "constant": int(value),
        }
        print(f"<< {label}: {value} in {time.time() - start:.1f}s peak {hwm_mib()} MiB", flush=True)
    except Exception as error:
        record["stages"][label] = {
            "seconds": round(time.time() - start, 2),
            "peak_mib": hwm_mib(),
            "error": f"{type(error).__name__}: {error}",
        }
        print(f"!! {label}: {type(error).__name__}: {error}", flush=True)
        traceback.print_exc(file=sys.stdout)
    flush()
    print(f"   available {available_mib()} MiB", flush=True)
