"""How many primitive isotropic lines a plane of T_Co holds, against its divided classes.

The statement under test is one this branch made in the previous turn: that the three nonzero
divided classes of a plane are "the classes of the plane's primitive vectors", which read as three
isotropic lines inside the plane. If the plane is a scaled hyperbolic plane, the primitive vectors
(a, b) have norm 4ab, so only the two coordinate lines are isotropic.
"""
import json

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import ZZ

GRAM = [[2,0,0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0],[0,2,0,0,0,0,0,0,0,0,0],[0,0,0,-4,0,2,0,0,0,0,0],[0,0,0,0,-4,0,2,0,0,0,0],[0,0,0,2,0,-4,2,0,0,0,0],[0,0,0,0,2,2,-4,2,0,0,0],[0,0,0,0,0,0,2,-4,2,0,0],[0,0,0,0,0,0,0,2,-4,2,0],[0,0,0,0,0,0,0,0,2,-4,2],[0,0,0,0,0,0,0,0,0,2,-4]]

lattice = Lattices(ZZ)(GRAM)
labels = tuple(lattice.module_generating_set())
# The card's second and third generators span the U(2) summand: (e2, e2) = (e3, e3) = 0, (e2, e3) = 2.
e2 = lattice.module_generator(labels[1])
e3 = lattice.module_generator(labels[2])
report = []
for a, b in ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (3, 2)):
    vector = a * e2 + b * e3
    report.append({"a": a, "b": b, "norm": int(lattice.q(vector)), "primitive": bool(lattice.is_primitive(vector)) if hasattr(lattice, "is_primitive") else None})
print(json.dumps(report, indent=0).replace("\n", ""), flush=True)
