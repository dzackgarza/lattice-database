"""#7: on a specimen, the flag orbits and the incidence edges are the same count.

The claim this tests is the one link in the `569160` chain that is a theorem and not a count: the
forgetful map from isotropic-flag orbits to pairs of (line cusp, plane cusp) is injective, so the
edge count of the incidence relation equals the number of flag orbits. `T_Co`'s kernel rows are
189720 planes wide and cannot be walked here, so the test is the smallest specimen with more than
one orbit on each side: `T_En`'s stored Gram under `O(T_En)`, which has two line cusps and two plane
cusps.

Sources, by printed page: D. Dutour Sikiric, K. Hulek, *Moduli of polarised Enriques surfaces --
computational aspects*, J. London Math. Soc. 110 (2024), arXiv:2302.01679, Lemma 3.6, printed p. 22
(the double-coset reduction) and SS3.6 printed p. 22 (the Tits building of the period space);
D. Dolgachev, S. Kondo, Izv. Math. 77:3 (2013), SS2 printed p. 510 and SS3 (3.6) with Proposition 3.2,
printed p. 513 (the lattice and its discriminant kernel).

Both sides are the owner's calls: `cusps(1)`, `cusps(2)`, `tits_building_incidence()` and
`isotropic_orbit_representatives(2, flag=True)`. A refutation is a pair of unequal counts.
"""
import json
import time
from pathlib import Path

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import ZZ

from latticedb import corpus
from latticedb.model import Lattice

record = corpus.front_matter(corpus.read_card(Path("lattices") / "029J.md"))
gram = Lattice.model_validate(record).gram_tensor
lattice = Lattices(ZZ)(gram)
group = lattice.Aut()
started = time.monotonic()

lines = group.cusps(1).cardinality()
print(json.dumps({"lines": int(lines), "wall_s": round(time.monotonic() - started, 1)}), flush=True)
planes = group.cusps(2).cardinality()
print(json.dumps({"planes": int(planes), "wall_s": round(time.monotonic() - started, 1)}), flush=True)
edges = group.tits_building_incidence().cardinality()
print(json.dumps({"edges": int(edges), "wall_s": round(time.monotonic() - started, 1)}), flush=True)
flags = group.isotropic_orbit_representatives(2, flag=True).cardinality()
print(json.dumps({"flag_orbits": int(flags), "wall_s": round(time.monotonic() - started, 1)}), flush=True)
print(json.dumps({"equal": int(edges) == int(flags), "edges": int(edges), "flags": int(flags)}), flush=True)
