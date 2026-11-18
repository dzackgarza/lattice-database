r"""#43: do the cusp stabilizer's root classes merge?  Asked of the owner's exact equivalence.

sage-extensions#312 closed with the group that ``Stab_Gamma(v)`` induces on ``v^perp/ZZ v`` for a
subgroup ``Gamma <= O(L)`` cut out by a condition on ``A_L`` -- a *predicate* subgroup -- whose
`vectors_are_equivalent` decides equivalence of two vectors exactly, by walking the coset in the
finite discriminant quotient.  The rows of card 029J at Sterk's (4.3.7)--(4.3.9) ask exactly this:
are two root classes of ``K_J = v^perp/ZZ v`` in one orbit of the cusp stabilizer?

A class of a root ``r`` is carried to a class of ``r'`` by an element of ``Stab_Gamma(v)`` exactly
when that element carries the rank-two degenerate lattice ``ZZ v + ZZ r`` onto ``ZZ v + ZZ r'`` --
the radical ``ZZ v`` is characteristic, so ``r`` goes to ``r' + t v`` for some integer ``t``.  So the
question is answered by `vectors_are_equivalent` on the pairs ``(r, r' + t v)``, and the probe asks
it for the ``t`` a stabilizer element can produce, then checks the witness it gets.

    run.sh -w /repos/lattice-database -b <repo>:/repos/lattice-database \
        -b <clone>:/repos/sage-extensions -- env PYTHONPATH=... python results/probe-43-equivalence-at-cusps.py
"""

from pathlib import Path

from latticedb import corpus
from sage_extensions.all import ZZ, Involutions, NamedLattices

CARD = Path("/repos/lattice-database/lattices/029J.md")
TOLERANCE = 6

row_of = corpus.front_matter(corpus.read_card(CARD))
lattice = NamedLattices.TEn


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
left, right = marks[0]
polarization = invariant.module_generator(left) + invariant.module_generator(right)
gamma = Involutions.I_En.polarized(invariant.inclusion()(polarization)).coinvariant_extension_subgroup()
ambient = gamma.supergroup().domain()
print("Gamma built; predicate machinery:", hasattr(gamma, "vectors_are_equivalent"), flush=True)


def vector(entries):
    """One vector of the card, as an element of the lattice Gamma itself acts on."""
    return ambient(tuple(int(entry) for entry in entries))

for row in row_of["integral"]["cusp_chambers"]["gamma-en-2"][2:5]:
    cusp = vector(row["cusp"])
    walls = [vector(wall["vector"]) for wall in row["walls"]]
    names = [wall["name"] for wall in row["walls"]]
    roots = [(name, wall) for name, wall in zip(names, walls) if wall.q() == -ZZ(2)]
    print(f"{row['statement']} p.{row['printed_page']}: roots {[name for name, _ in roots]}", flush=True)
    for index in range(1, len(roots)):
        first_name, first = roots[0]
        second_name, second = roots[index]
        verdict = None
        for shift in range(-TOLERANCE, TOLERANCE + 1):
            candidate = second + shift * cusp
            witness = gamma.vector_equivalence_witness(first, candidate)
            if witness is not None:
                moves_cusp = witness(cusp) in (cusp, -cusp)
                verdict = (shift, bool(moves_cusp), bool(witness(first) == candidate))
                break
        print(f"    {first_name} -> {second_name}: witness at shift {verdict}", flush=True)
