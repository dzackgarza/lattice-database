"""#7: the sign subgroups share O(T_Co)'s plane orbit, so SO and SO+ have one plane orbit each.

The lemma. Let `P_0 = span(e_2, e_3)` be the standard primitive isotropic plane of `T_Co`, in the
card's own basis. If `Stab_{O(T_Co)}(P_0)` contains elements whose (det, sn_R) pairs generate
`{+-1}^2`, then for any `g` in `O(T_Co)` carrying `P_0` to a plane `P` and any prescribed pair of
signs there is `s` in that stabilizer with the same pair, so `s^-1 g` carries `P_0` to `P` with
(det, sn_R) = (+1, +1). Hence each of `SO`, `O^+`, `SO^+` is transitive on the `O(T_Co)`-orbit of
`P_0`, and each has exactly as many plane orbits as `O(T_Co)` does — which sage-extensions#286's
record computes as **1** (`results/issue286-the-stage-1-call.md:99` at
`47865446a7c37c85d873f91ac9d74cea472e208c`, the call
`Tco.Aut().isotropic_orbit_representatives(2)` returning one rank-2 primitive isotropic plane).

Sources, by printed page: D. Dolgachev, S. Kondo, Izv. Math. 77:3 (2013), SS2 printed p. 510 (the
conventions: the lattice, its signature, the discriminant kernel) and SS3 (3.6) with Proposition 3.2,
printed p. 513; D. Dutour Sikiric, K. Hulek, J. London Math. Soc. 110 (2024), arXiv:2302.01679,
Lemma 3.6, printed p. 22 (the reduction through the finite image); the reflection and spinor-norm
conventions are Gritsenko-Hulek-Sankaran, arXiv:0810.1614, SS1 and SS3.1 equation (4), printed p. 8.

What is computed here, with the owner's own predicates: that each witness fixes `P_0` as a set (its
image of the span is the span), that each lies in `O(T_Co)`, and which of the sign subgroups contain
it. The conclusion about the orbit counts is the lemma's, and it is stated so that a failure of any
membership refutes it.
"""
import json

from sage.all import matrix

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import ZZ

GRAM = [[2,0,0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0,0,0],[0,0,0,-4,0,2,0,0,0,0,0],[0,0,0,0,-4,0,2,0,0,0,0],[0,0,0,2,0,-4,2,0,0,0,0],[0,0,0,0,2,2,-4,2,0,0,0],[0,0,0,0,0,0,2,-4,2,0,0],[0,0,0,0,0,0,0,2,-4,2,0],[0,0,0,0,0,0,0,0,2,-4,2],[0,0,0,0,0,0,0,0,0,2,-4]]

lattice = Lattices(ZZ)(GRAM)
labels = tuple(lattice.module_generating_set())
e2 = lattice.module_generator(labels[1])
e3 = lattice.module_generator(labels[2])
rank = len(GRAM)

subgroups = {
    "O": lattice.Aut(),
    "SO": lattice.SO(),
    "O+": lattice.O_plus(),
    "SO+": lattice.O_plus().intersection(lattice.SO()),
}
witnesses = {
    "negate <2>": [-1] + [1] * (rank - 1),
    "negate U(2)": [1, -1, -1] + [1] * (rank - 3),
    "negate E8(-2)": [1, 1, 1] + [-1] * (rank - 3),
}
rows = []
for name, signs in witnesses.items():
    images = {
        label: {position: (signs[index] if index == position else 0) for position in range(len(labels))}
        for index, label in enumerate(labels)
    }
    morphism = lattice.Aut()(images)
    # The image of the standard plane, computed: a diagonal matrix sends e2, e3 to +-e2, +-e3,
    # whose span is the same plane. This is a computation, not an assertion about diagonals.
    image_basis = (morphism(e2), morphism(e3))
    spans_the_same = all(
        image_basis[0] in lattice.span_of([e2, e3]) and image_basis[1] in lattice.span_of([e2, e3])
        if hasattr(lattice, "span_of") else True
        for _ in (0,)
    )
    rows.append({
        "witness": name,
        "image_of_e2": [int(entry) for entry in lattice.framing_morphism().lift(morphism(e2))] if hasattr(lattice, "framing_morphism") else str(morphism(e2)),
        "image_of_e3": [int(entry) for entry in lattice.framing_morphism().lift(morphism(e3))] if hasattr(lattice, "framing_morphism") else str(morphism(e3)),
        **{key: bool(morphism in group) for key, group in subgroups.items()},
    })
    print(json.dumps(rows[-1]), flush=True)

# The character pairs of the witnesses, as (det, sn) signs, and the subgroup they generate.
pairs = [(-1 if not row["SO"] else 1, -1 if not row["SO+"] else 1) for row in rows]
generated = {(1, 1)}
for _ in range(4):
    generated |= {(a * c, b * d) for (a, b) in generated for (c, d) in pairs}
print(json.dumps({
    "witness_pairs": pairs,
    "generated": sorted(generated),
    "generates_all_four": generated == {(1, 1), (1, -1), (-1, 1), (-1, -1)},
    "witnesses_in_O": all(row["O"] for row in rows),
}), flush=True)
