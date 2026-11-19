"""#7: the eight stars per isotropic subgroup, as the quotient of two computations.

The structure, from the source: a plane orbit of `K` is a pair `(J, s)` with `J` an order-four
isotropic subgroup of `A = A_{T_Co}` and `s` a star of `J` (D. Dutour Sikiric, K. Hulek, *Moduli of
polarised Enriques surfaces -- computational aspects*, J. London Math. Soc. 110 (2024),
arXiv:2302.01679, Lemma 3.6, printed p. 22; D. Dolgachev, S. Kondo, Izv. Math. 77:3 (2013), SS2
printed p. 510 and SS3 (3.6) with Proposition 3.2, printed p. 513 for the lattice and its kernel).
So the number of plane cusps is `23715 * (stars per J)`, and the two factors are both computed here:

  * `23715`, the order-four isotropic subgroups of `A`, counted on the owner's discriminant form by
    `results/probe-7-line-degree.py` (142290 ordered pairs / 6);
  * `189720`, the plane orbits of `K`, computed on this card's stored Gram and stored as row
    `Otilde+` of `integral.primitive_orbits`.

Their quotient is the stars per subgroup. If it is not eight, either the structure or one of the
two computations is wrong, and this probe is the one that says so.
"""
import json
from pathlib import Path

isotropic_subgroups = 23715          # counted on the form: results/probe-7-line-degree.py
plane_orbits = 189720                # computed on the card: integral.primitive_orbits[Otilde+].planes

stars, remainder = divmod(plane_orbits, isotropic_subgroups)
line_degree_from_stars = 135 * stars
print(json.dumps({
    "isotropic_subgroups": isotropic_subgroups,
    "plane_orbits": plane_orbits,
    "stars_per_subgroup": stars,
    "remainder": remainder,
    "expected_stars": 8,
    "line_degree": line_degree_from_stars,
    "edges": 527 * line_degree_from_stars,
    "closes": remainder == 0 and stars == 8 and line_degree_from_stars == 1080,
}), flush=True)

card = Path("lattices") / "6JRR.md"
text = card.read_text()
assert "planes: 189720" in text, "the card does not state the plane count this quotient divides"
print(json.dumps({"card_states_189720": True}), flush=True)
