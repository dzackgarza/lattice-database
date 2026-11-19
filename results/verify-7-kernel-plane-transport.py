"""#7: the four kernel subgroups share K's plane orbits, so SOtilde and SOtilde+ have 189720.

The lemma. Let `K = ker rho_{T_Co}` and `P_0 = span(e_2, e_3)` the standard primitive isotropic plane
of `T_Co` in this card's basis. If `Stab_K(P_0)` contains isometries whose `(det, sn_R)` pairs
generate `{+-1}^2`, then `K`, `K & SO`, `K & O^+` and `K & SO & O^+` are each transitive on every
`K`-orbit of primitive isotropic planes, so all four have `K`'s number of them.

Proof, as for the ambient case: for `g in K` with `g P_0 = P` and a prescribed pair there is `s` in
`Stab_K(P_0)` with the same pair, and `s^{-1} g` carries `P_0` to `P` with `(+1,+1)`, so it lies in all
four subgroups.

Sources, by printed page: D. Dolgachev, S. Kondo, Izv. Math. 77:3 (2013), SS2 printed p. 510 (the
lattice, its signature and the discriminant kernel) and SS3 (3.6) with Proposition 3.2, printed
p. 513; D. Dutour Sikiric, K. Hulek, J. London Math. Soc. 110 (2024), arXiv:2302.01679, Lemma 3.6,
printed p. 22 (the reduction through the finite image); Gritsenko-Hulek-Sankaran, arXiv:0810.1614,
SS1 and SS3.1 eq. (4), printed p. 8 for the reflection and spinor-norm conventions.

The base row is sage-extensions' own computation of `K`'s plane row,
`results/issue286-the-stage-1-call.md:275` at `47865446a7c37c85d873f91ac9d74cea472e208c`
(`[Otilde cusps] counted 189720 cusps`) and `:372` (527 line cusps, 189720 plane cusps, 569160 edges).
What is computed here is the transport: witnesses in `K`, fixing `P_0`, whose pairs generate all four.
"""
import json

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import ZZ

GRAM = [[2,0,0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0,0,0],[0,0,0,-4,0,2,0,0,0,0,0],[0,0,0,0,-4,0,2,0,0,0,0],[0,0,0,2,0,-4,2,0,0,0,0],[0,0,0,0,2,2,-4,2,0,0,0],[0,0,0,0,0,0,2,-4,2,0,0],[0,0,0,0,0,0,0,2,-4,2,0],[0,0,0,0,0,0,0,0,2,-4,2],[0,0,0,0,0,0,0,0,0,2,-4]]

lattice = Lattices(ZZ)(GRAM)
labels = tuple(lattice.module_generating_set())
e2 = lattice.module_generator(labels[1])
e3 = lattice.module_generator(labels[2])
rank = len(GRAM)

stable = lattice.stable_orthogonal_group()
groups = {
    "K": stable,
    "K&SO": stable.intersection(lattice.SO()),
    "K&O+": stable.intersection(lattice.O_plus()),
    "K&SO+": stable.intersection(lattice.SO()).intersection(lattice.O_plus()),
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
    image_two = [int(entry) for entry in lattice.framing_morphism().lift(morphism(e2))]
    image_three = [int(entry) for entry in lattice.framing_morphism().lift(morphism(e3))]
    outside = [position for position in range(len(labels)) if position not in (1, 2)]
    # The plane span(e_2, e_3) is fixed as a set exactly when both images lie in it and their 2x2
    # block is invertible: a computation on the image vectors, not an assumption about diagonals.
    fixes = all(image_two[position] == 0 and image_three[position] == 0 for position in outside)
    block = [[image_two[1], image_two[2]], [image_three[1], image_three[2]]]
    fixes = fixes and (block[0][0] * block[1][1] - block[0][1] * block[1][0] != 0)
    rows.append({
        "witness": name,
        "image_of_e2": image_two,
        "image_of_e3": image_three,
        "fixes_the_standard_plane": bool(fixes),
        **{key: bool(morphism in group) for key, group in groups.items()},
    })
    print(json.dumps(rows[-1]), flush=True)

pairs = [(-1 if not row["K&SO"] else 1, -1 if not row["K&SO+"] else 1) for row in rows]
generated = {(1, 1)}
for _ in range(4):
    generated |= {(a * c, b * d) for (a, b) in generated for (c, d) in pairs}
print(json.dumps({
    "witness_pairs": pairs,
    "generated": sorted(generated),
    "generates_all_four": generated == {(1, 1), (1, -1), (-1, 1), (-1, -1)},
    "witnesses_in_K": all(row["K"] for row in rows),
}), flush=True)
