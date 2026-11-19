"""#7: the sign isometries that fix the standard primitive isotropic plane of T_Co.

The statement used is the published reduction through the finite character image — D. Dutour
Sikirić, K. Hulek, Lemma 3.6, printed p. 22 — with the lattice and discriminant kernel of
D. Dolgachev, S. Kondō, §2 printed p. 510 and §3 (3.6) with Proposition 3.2, printed p. 513.
What this script does is decide that statement's hypothesis on this card's Gram tensor; it
introduces no statement of its own.

for every primitive isotropic plane `P`
of `T_Co`, the stabilizer of `P` inside `K = ker rho_{T_Co}` maps onto `{+-1}^2` under the pair
(determinant, real spinor norm), so none of `K`, `K & SO`, `K & O+`, `K & SO+` splits another's
plane orbits and all four have the same 189720 of them.

  * D. Dolgachev, S. Kondo, "The rationality of the moduli spaces of Coble surfaces and of nodal
    Enriques surfaces", Izv. Math. 77:3 (2013): section 2, printed p. 510, the conventions (the
    lattice, its signature, the discriminant kernel); section 3, eq. (3.6) with Proposition 3.2,
    printed p. 513, where `N = <2> + E(2)` is `T_Co`'s lattice and the moduli space is named.
  * D. Dutour Sikiric, K. Hulek, "Moduli of polarised Enriques surfaces -- computational aspects",
    J. London Math. Soc. 110 (2024), arXiv:2302.01679, Lemma 3.6, printed p. 22: the double-coset
    reduction through the finite image, which is what makes a character kernel's orbits read off
    the ambient ones.

The three witnesses are the proof's, written in the card's own basis: negate the single positive
vector, negate the hyperbolic block (where the standard plane lives), negate the negative-definite
block. Each is diagonal with +-1 entries, so it fixes the hyperbolic block's span as a set and it is
an isometry iff `M^T G M = G`; whether it lies in each subgroup is the owner's membership predicate
and not a local test.

Prints one row per witness: the subgroup memberships, hence the character pair it exhibits.
"""
import json

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import ZZ

GRAM = [[2,0,0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0,0,0],[0,0,0,-4,0,2,0,0,0,0,0],[0,0,0,0,-4,0,2,0,0,0,0],[0,0,0,2,0,-4,2,0,0,0,0],[0,0,0,0,2,2,-4,2,0,0,0],[0,0,0,0,0,0,2,-4,2,0,0],[0,0,0,0,0,0,0,2,-4,2,0],[0,0,0,0,0,0,0,0,2,-4,2],[0,0,0,0,0,0,0,0,0,2,-4]]

lattice = Lattices(ZZ)(GRAM)
labels = tuple(lattice.module_generating_set())
stable = lattice.stable_orthogonal_group()
subgroups = {
    "O": lattice.Aut(),
    "SO": lattice.SO(),
    "O+": lattice.O_plus(),
    "Otilde": stable,
    "SOtilde": stable.intersection(lattice.SO()),
    "Otilde+": stable.intersection(lattice.O_plus()),
}
witnesses = {
    "negate <2>": [-1] + [1] * (len(GRAM) - 1),
    "negate U(2)": [1, -1, -1] + [1] * (len(GRAM) - 3),
    "negate E8(-2)": [1, 1, 1] + [-1] * (len(GRAM) - 3),
}
for name, signs in witnesses.items():
    images = {
        label: {position: (signs[index] if index == position else 0) for position in range(len(labels))}
        for index, label in enumerate(labels)
    }
    morphism = lattice.Aut()(images)
    record = {"witness": name}
    for key, group in subgroups.items():
        try:
            record[key] = bool(morphism in group)
        except Exception as error:  # a membership the owner cannot decide is reported, not assumed
            record[key] = f"{type(error).__name__}"
    print(json.dumps(record), flush=True)
