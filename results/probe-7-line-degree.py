"""#7: the line degree 1080 = 135 * 8, counted on the discriminant form itself.

The lemma: with `A = A_{T_Co} = (Z/2)^11` and its quadratic form `q`, the number of order-four
totally isotropic subgroups `J <= A` is `23715`, and exactly `135` of them contain a given nonzero
isotropic class. With the `8` stars per `J` that gives the line degree `1080` of the incidence
relation, hence `527 * 1080 = 569160` edges.

Sources, by printed page: D. Dutour Sikiric, K. Hulek, *Moduli of polarised Enriques surfaces --
computational aspects*, J. London Math. Soc. 110 (2024), arXiv:2302.01679, Lemma 3.6, printed p. 22
(the double-coset reduction through the finite image) and SS3.6 printed p. 22 (the finite orbit
counts of the same construction); D. Dolgachev, S. Kondo, Izv. Math. 77:3 (2013), SS2 printed p. 510
and SS3 (3.6) with Proposition 3.2, printed p. 513 (the lattice and its discriminant kernel).

Nothing here reimplements a lattice algorithm: the group, its elements and `q` are the owner's
(`discriminant_quadratic_form()`), and on isotropic elements the polar form is `b(x, y) = q(x + y)`,
so a two-dimensional subspace `{0, x, y, x + y}` is totally isotropic exactly when `q(x + y) = 0`.
"""
import json

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import ZZ

GRAM = [[2,0,0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0,0,0],[0,0,0,-4,0,2,0,0,0,0,0],[0,0,0,0,-4,0,2,0,0,0,0],[0,0,0,2,0,-4,2,0,0,0,0],[0,0,0,0,2,2,-4,2,0,0,0],[0,0,0,0,0,0,2,-4,2,0,0],[0,0,0,0,0,0,0,2,-4,2,0],[0,0,0,0,0,0,0,0,2,-4,2],[0,0,0,0,0,0,0,0,0,2,-4]]

lattice = Lattices(ZZ)(GRAM)
form = lattice.discriminant_quadratic_form()
elements = list(form.elements())
isotropic_set = set(form.isotropic_elements())
zero = next(element for element in elements if element + element == element)
nonzero = [element for element in elements if element != zero and element in isotropic_set]
print(json.dumps({"elements": len(elements), "isotropic": len(isotropic_set), "nonzero_isotropic": len(nonzero)}), flush=True)

# A plane {0, x, y, x + y} is totally isotropic iff all four elements are isotropic; on isotropic
# elements the polar form is q(x + y), so the test is membership in the owner's isotropic set.
pairs = 0
for x in nonzero:
    for y in nonzero:
        if x == y:
            continue
        if x + y in isotropic_set:
            pairs += 1
print(json.dumps({"ordered_pairs": pairs, "planes": pairs // 6, "expected_planes": 23715}), flush=True)

# Planes through one fixed nonzero isotropic class c: both y and y + c count, so divide by two.
c = nonzero[0]
through = sum(1 for y in nonzero if y != c and c + y in isotropic_set)
print(json.dumps({"fixed_class": str(c), "through": through // 2, "expected": 135}), flush=True)
print(json.dumps({"line_degree": (through // 2) * 8, "edges": 527 * (through // 2) * 8}), flush=True)
