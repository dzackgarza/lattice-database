"""#43: is there a computed group to key the T_Co rows to?

The rows at T_Co cusps 3--5 are orbits under the cusp stabilizer of Gamma_Co,2, and `integral.cusp_root_orbits` takes
a named subgroup only as the slug of an arithmetic-group card of the same lattice. 6JRR has no such card. The one
definition of Gamma_Co,2 the project holds is by construction -- the stabilizer in O(T_En) of T_Co, a non-degenerate
sublattice -- not by citation, so such a card could exist only with values *computed*. This asks the owner for exactly
that, bounded at 240 s per call: the orthogonal group of T_En, the setwise stabilizer of T_Co in it, and its index.

    .scratch/wt43g-run.sh -u results/probe-43-co2-key.py
"""

import signal
import time

from sage_extensions.all import NamedLattices  # noqa: F401,F403

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


lattice = NamedLattices.TEn
labels = tuple(lattice.module_generating_set())
group = lattice.O()
print(f"[{time.time() - start:6.1f}s] O(T_En): {group!r}", flush=True)
print("candidates:", [name for name in dir(group) if "stabil" in name or "subobject" in name], flush=True)

# T_Co = delta^perp for delta = e - f, the card's first two basis vectors; b(e, e) = b(f, f) = 0 and b(e, f) = 1.
delta = lattice.linear_combination({labels[0]: lattice.base_ring()(1), labels[1]: lattice.base_ring()(-1)})
print(f"delta = {delta!r}, q = {lattice.q(delta)}", flush=True)
try:
    perpendicular = bounded(240.0)(lambda: delta.orthogonal_complement())()
    print(f"[{time.time() - start:6.1f}s] delta^perp rank {perpendicular.module_rank()}: {perpendicular!r}", flush=True)
except Overran as overran:
    print(f"RESULT: delta^perp did not return inside {overran}", flush=True)
    raise SystemExit(0)

stabilizer = bounded(240.0)(lambda: group.setwise_stabilizer(perpendicular.inclusion()))()
print(f"[{time.time() - start:6.1f}s] setwise stabilizer built: {type(stabilizer).__name__}", flush=True)
for label, call in (
    ("has_finite_coset_space", lambda: stabilizer.has_finite_coset_space()),
    ("contains_character_kernel", lambda: stabilizer.contains_character_kernel()),
    ("finite_character_quotient", lambda: stabilizer.finite_character_quotient()),
):
    try:
        print(f"  {label}: {bounded(120.0)(call)()}", flush=True)
    except Overran as overran:
        print(f"  {label}: did not return inside {overran}", flush=True)
    except Exception as failure:  # noqa: BLE001
        print(f"  {label}: {type(failure).__name__}: {str(failure)[:200]}", flush=True)
try:
    image = bounded(240.0)(lambda: stabilizer.discriminant_image())()
    order = bounded(240.0)(lambda: image.cardinality())()
    print(f"RESULT: the finite character image of the stabilizer has order {order}", flush=True)
except Overran as overran:
    print(f"RESULT: the discriminant image did not return inside {overran}", flush=True)
except Exception as failure:  # noqa: BLE001
    print(f"RESULT: {type(failure).__name__}: {str(failure)[:300]}", flush=True)
