"""#43: the index of Gamma_Co,2, asked as the setwise stabilizer of the vector delta rather than of its perpendicular.

The rows at T_Co cusps 3--5 are keyed to a group that has no card on 6JRR, and the last turn measured that
`O(T_En).setwise_stabilizer(delta^perp.inclusion())` returns a predicate with no exact index: the finite-character
quotient a standard subgroup has does not apply to a setwise stabilizer of a *sublattice*.

But `T_Co = delta^perp` with `delta = e - f` primitive of square -2, so the sublattice's stabilizer is the setwise
stabilizer of the *line* `Z delta`, and the library states the route for that one: "an arrow marking at a primitive
non-isotropic vector asks for the setwise stabilizer of its line, which is the same gluing construction with the sign
on the line allowed" (`lattices.py`, the dispatch of `_marked_automorphism_generators`). This asks for that subgroup
and for its index, bounded per call, so the question "is there a computable group to key the rows to" is answered on
the construction the library attests rather than on a generic predicate.

    .scratch/wt43h-run.sh -u results/probe-43-co2-index.py
"""

import signal
import time

from sage_extensions.all import ZZ, NamedLattices  # noqa: F401,F403

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


def report(label, call, budget=240.0):
    try:
        value = bounded(budget)(call)()
    except Overran as overran:
        print(f"  {label}: did not return inside {overran}", flush=True)
        return None
    except Exception as failure:  # noqa: BLE001 - the refusal is the measurement
        print(f"  {label}: {type(failure).__name__}: {str(failure)[:220]}", flush=True)
        return None
    print(f"  {label}: {str(value)[:220]}", flush=True)
    return value


lattice = NamedLattices.TEn
labels = tuple(lattice.module_generating_set())
delta = lattice.linear_combination({labels[0]: lattice.base_ring()(1), labels[1]: lattice.base_ring()(-1)})
print(f"delta = {delta!r}, q = {lattice.q(delta)}, primitive = {delta.is_primitive()}", flush=True)
group = lattice.O()

print("the vector stabilizer of delta, asked pointwise and setwise:", flush=True)
fixed = report("stabilizer(delta, pointwise)", lambda: group.stabilizer(delta))
if fixed is not None:
    report("  has_finite_coset_space", fixed.has_finite_coset_space)
    report("  index", fixed.index)
line = report("stabilizer(delta, setwise)", lambda: group.stabilizer(delta, action="setwise"))
if line is not None:
    report("  has_finite_coset_space", line.has_finite_coset_space)
    report("  contains_character_kernel", line.contains_character_kernel)
    index = report("  index", line.index)
    print(f"RESULT: index = {index}", flush=True)
print(f"[{time.time() - start:6.1f}s] done", flush=True)
