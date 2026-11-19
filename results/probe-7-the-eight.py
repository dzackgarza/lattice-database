"""#7: the 8 in 189720 = 23715 * 8 is an index, and the star count agrees with it.

Two routes give the factor 8 of `189720 = 23715 * 8`, and they are the same number:

  * this branch's quotient of two computations on this card — 189720 plane cusps over 23715
    order-four isotropic subgroups (`results/probe-7-star-count.py`);
  * the index `[Stab_{O(q)}(J) : rho(Stab_{O(T_Co)}(P))]` for a plane `P` and its
    `J = [P/2]`, which is `|Stab(J)| / |rho(Stab P)| = 1981808640 / 247726080`
    (sage-extensions `47865446a7c37c85d873f91ac9d74cea472e208c`,
    `results/issue607-gamma-co-2-rows-by-the-polar-space.md:98`, and `:113` for the
    `247726080 = |rho(Stab P)|`; the `1981808640 = |O(q)| / 23715` is
    `results/issue286-acceptance.md:78` and `results/issue286-the-base-point-is-not-a-plane-class.md:16`).

Sources for the index itself, by printed page: D. Dutour Sikiric, K. Hulek, *Moduli of polarised
Enriques surfaces -- computational aspects*, J. London Math. Soc. 110 (2024), arXiv:2302.01679,
Lemma 3.6, printed p. 22; D. Dolgachev, S. Kondo, Izv. Math. 77:3 (2013), SS2 printed p. 510 and SS3
(3.6) with Proposition 3.2, printed p. 513.

The probe asserts the identities; a failure in any of them is a disagreement between the two routes
and is to be reported rather than papered over.
"""
import json
from pathlib import Path

order_of_O_q = 46998591897600        # |O(A_T_Co, q)|, on the card as discriminant_form.orthogonal_group_order
isotropic_subgroups = 23715          # counted: results/probe-7-line-degree.py
stabilizer_of_J = 1981808640         # |O(q)| / 23715; sage-extensions, results/issue286-acceptance.md:78
image_of_plane_stabilizer = 247726080  # |rho(Stab P)|; sage-extensions#360, and issue607-...md:113
plane_cusps = 189720                 # computed on this card: integral.primitive_orbits[Otilde+].planes

checks = {
    "stabilizer_is_order_over_subgroups": order_of_O_q // isotropic_subgroups == stabilizer_of_J,
    "index_is_quotient": stabilizer_of_J // image_of_plane_stabilizer == 8,
    "stars_equal_index": plane_cusps // isotropic_subgroups == stabilizer_of_J // image_of_plane_stabilizer,
    "planes_close": isotropic_subgroups * (stabilizer_of_J // image_of_plane_stabilizer) == plane_cusps,
    "edges_close": 527 * 135 * (stabilizer_of_J // image_of_plane_stabilizer) == 569160,
}
print(json.dumps(checks), flush=True)

card = Path("lattices") / "6JRR.md"
assert "planes: 189720" in card.read_text(), "the card does not state the plane count these identities close on"
print(json.dumps({"all": all(checks.values())}), flush=True)
