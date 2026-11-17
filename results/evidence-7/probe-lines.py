"""Probe the T_Co primitive isotropic LINE series through the public owner call.

Stages are recorded as they finish to results.json, so an external timeout that
kills a stage keeps the stages already measured.
"""
import json
import os
import sys
import time
import traceback

sys.stdout.reconfigure(line_buffering=True)

OUT = "/repo/.scratch/tco/results.json"
record = {"stages": {}}


def hwm_mib():
    try:
        for line in open("/proc/self/status"):
            if line.startswith("VmHWM"):
                return int(line.split()[1]) // 1024
    except OSError:
        return -1
    return -1


def flush():
    json.dump(record, open(OUT, "w"), indent=1, default=str)


class Stage:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.t = time.time()
        print(f">> {self.label}", flush=True)
        return self

    def __exit__(self, kind, value, tb):
        seconds = time.time() - self.t
        entry = record["stages"].setdefault(self.label, {})
        entry["seconds"] = round(seconds, 2)
        entry["peak_mib"] = hwm_mib()
        if kind is not None:
            entry["error"] = f"{kind.__name__}: {value}"
            print(f"!! {self.label} raised after {seconds:.1f}s: {kind.__name__}: {value}", flush=True)
            traceback.print_exception(kind, value, tb, file=sys.stdout)
        else:
            print(f"<< {self.label}: {seconds:.2f}s  peak {hwm_mib()} MiB", flush=True)
        flush()
        return False


import sage.version
import sage_extensions
import sage_extensions.timing as timing
from sage.rings.integer_ring import ZZ
from sage_extensions.all import Lattices

print("sage", sage.version.version, "python", sys.version.split()[0], flush=True)
print("sage_extensions at", sage_extensions.__file__, flush=True)
record["sage"] = sage.version.version
record["sage_extensions"] = sage_extensions.__file__
try:
    record["sage_extensions_commit"] = str(timing.current_commit())
except Exception as error:  # the timing provenance is itself the point
    record["sage_extensions_commit"] = f"unavailable: {type(error).__name__}: {error}"
print("sage_extensions commit", record["sage_extensions_commit"], flush=True)
try:
    import dzack_research
    record["dzack_research"] = dzack_research.__file__
    print("dzack_research at", dzack_research.__file__, flush=True)
except Exception as error:
    print("dzack_research unavailable:", error, flush=True)
flush()

gram = json.load(open("/repo/.scratch/tco/gram.json"))
with Stage("construct"):
    L = Lattices(ZZ)(gram)
    print("  rank", L.rank(), "det", L.determinant(), "sig", L.signature_pair(),
          "even", L.is_even(), "witt", L.witt_index(), flush=True)
    record["lattice"] = {"rank": int(L.rank()), "determinant": int(L.determinant()),
                         "signature": list(L.signature_pair()), "even": bool(L.is_even()),
                         "witt_index": int(L.witt_index())}

groups = {}
with Stage("O = L.Aut()"):
    groups["O"] = L.Aut()
with Stage("Otilde = L.stable_orthogonal_group()"):
    groups["Otilde"] = L.stable_orthogonal_group()
with Stage("O+ = L.O_plus()"):
    groups["O+"] = L.O_plus()
with Stage("SO = L.SO()"):
    groups["SO"] = L.SO()
with Stage("SOtilde = Otilde & SO"):
    groups["SOtilde"] = groups["Otilde"].intersection(groups["SO"])
with Stage("SO+ = O+ & SO"):
    groups["SO+"] = groups["O+"].intersection(groups["SO"])
with Stage("Otilde+ = Otilde & O+"):
    groups["Otilde+"] = groups["Otilde"].intersection(groups["O+"])
with Stage("SOtilde+ = SOtilde & O+"):
    groups["SOtilde+"] = groups["SOtilde"].intersection(groups["O+"])

record["constants"] = {}
for name in ("O", "SO", "O+", "SO+", "Otilde", "SOtilde", "Otilde+", "SOtilde+"):
    with Stage(f"constant {name}"):
        orbits = groups[name].isotropic_orbit_representatives(1)
        cardinality = orbits.cardinality()
        value = cardinality.finite_value() if hasattr(cardinality, "finite_value") else int(cardinality)
        print(f"  {name}: {value}  ({len(tuple(orbits))} representatives enumerated)", flush=True)
        record["constants"][name] = int(value)
        flush()

with Stage("primitive_orbit_series()"):
    series = L.primitive_orbit_series()
    print("  ", series, flush=True)
    record["series"] = repr(series)
    flush()

print("RESULT", json.dumps(record["constants"], sort_keys=True), flush=True)
