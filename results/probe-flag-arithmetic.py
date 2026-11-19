"""The flag count's arithmetic, against the numbers this card states and the sources' printed pages.

The claim: the incidence relation of K's line and plane cusps is (1080, 3)-biregular, so its edge
count is 527 * 1080 = 189720 * 3 = 569160.

Sources by printed page: D. Dutour Sikiric, K. Hulek, *Moduli of polarised Enriques surfaces --
computational aspects*, J. London Math. Soc. 110 (2024), arXiv:2302.01679, Lemma 3.6, printed p. 22
(the double-coset reduction) and SS3.6 printed p. 22 (the same construction at another lattice);
D. Dolgachev, S. Kondo, Izv. Math. 77:3 (2013), SS2 p. 510 and SS3 (3.6)/Prop. 3.2 p. 513 (T_Co and
its discriminant kernel).

What this checks is that the arithmetic of that relation closes against the card's own numbers: 527
line orbits (the card's constant term, certified) and 189720 plane orbits (row Otilde+, computed on
this card). The two degrees are the sources' numbers and are not recomputed here.
"""
import json

line_orbits = 527
plane_orbits = 189720
stars_per_plane = 8
isotropic_subgroups = 527 * 270 // 6
line_degree = 135 * stars_per_plane
plane_degree = 3

print(json.dumps({
    "isotropic_subgroups": isotropic_subgroups,
    "line_degree": line_degree,
    "plane_degree": plane_degree,
    "lines_times_line_degree": line_orbits * line_degree,
    "planes_times_plane_degree": plane_orbits * plane_degree,
    "edges_close": line_orbits * line_degree == plane_orbits * plane_degree,
    "expected_flag_orbits": plane_orbits * plane_degree,
}))
