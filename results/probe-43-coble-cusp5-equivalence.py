"""#43: the one decision cusp 5 still needs — are its three root classes one orbit under Gamma_Co,2?

The row at Sterk's (4.3.9) has three root classes in $T_{\\mathrm{Co}}$ ($\\alpha_{12}, \\alpha_{13}, \\alpha_{14}$), all
$O(K_I)$-equivalent, and no element of the families this repository can construct carries one to another. What would
decide it is the owner's exact equivalence: ask $\\Gamma_{\\mathrm{En},2}$ for a witness carrying one class to another,
and check that the witness it returns preserves $T_{\\mathrm{Co}}$ — if it does, it lies in $\\Gamma_{\\mathrm{Co},2}$ and
the two classes are one orbit.

    .scratch/wt43s-run.sh -u results/probe-43-coble-cusp5-equivalence.py
"""

import signal
import time
from fractions import Fraction
from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions, NamedLattices  # noqa: F401,F403

CARD = Path("/repo/lattices/029J.md")
start = time.time()


class Overran(Exception):
    pass


def bounded(seconds: float):
    def entry(function):
        def run(*arguments, **keywords):
            def raise_overran(signum, frame):
                raise Overran(f"{seconds:.0f}s")

            previous = signal.signal(signal.SIGALRM, raise_overran)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                return function(*arguments, **keywords)
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
                signal.signal(signal.SIGALRM, previous)

        return run

    return entry


def entries(element):
    return tuple(Fraction(int(entry)) for entry in element.to_vector())


row = corpus.front_matter(corpus.read_card(CARD))["integral"]["cusp_chambers"]["gamma-en-2"][4]  # (4.3.9)
enriques = NamedLattices.TEn
labels = tuple(enriques.module_generating_set())
rank = int(enriques.module_rank())


def vector(values):
    return enriques.linear_combination(
        {labels[index]: enriques.base_ring()(int(entry)) for index, entry in enumerate(values) if int(entry)}
    )


cusp = vector(row["cusp"])
walls_of_record = {wall["name"]: tuple(int(entry) for entry in wall["vector"]) for wall in row["walls"]}
roots = [name for name in ("\\alpha_12", "\\alpha_13", "\\alpha_14") if name in walls_of_record]
print(f"{row['statement']}: classes {roots}", flush=True)

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
print(f"[{time.time() - start:6.1f}s] Gamma_En,2 built", flush=True)
# The lattice the group's isometries act on: a second construction of T_En coerces by name only.
domain = group.supergroup().lattice()
domain_labels = tuple(domain.module_generating_set())


def domain_vector(values):
    return domain.linear_combination(
        {domain_labels[index]: domain.base_ring()(int(entry)) for index, entry in enumerate(values) if int(entry)}
    )


walls = {name: entries(domain_vector(values)) for name, values in walls_of_record.items()}
delta = domain_vector([1, -1] + [0] * (rank - 2))
delta_entries = entries(delta)

for left, right in ((roots[0], roots[1]), (roots[0], roots[2]), (roots[1], roots[2])):
    try:
        witness = bounded(300.0)(lambda: group.vector_equivalence_witness(domain_vector(walls[left]), domain_vector(walls[right])))()
    except Overran as overran:
        print(f"  {left} -> {right}: did not return inside {overran}", flush=True)
        continue
    except Exception as failure:  # noqa: BLE001 - the refusal is the measurement
        print(f"  {left} -> {right}: {type(failure).__name__}: {str(failure)[:200]}", flush=True)
        continue
    if witness is None:
        print(f"  {left} -> {right}: no witness in Gamma_En,2", flush=True)
        continue
    image_of_delta = entries(witness(delta))
    preserves = image_of_delta == delta_entries or image_of_delta == tuple(-entry for entry in delta_entries)
    print(f"  {left} -> {right}: witness found; preserves T_Co: {preserves}", flush=True)
    if preserves:
        print(f"RESULT: {left} and {right} are one Gamma_Co,2-orbit, by an exhibited element", flush=True)
