"""#49: store the transporter order at (4.3.9) on card 029J, and the Coble cusp (4.3.9) row on card 6JRR.

The values are those printed by `results/probe-49-cusp-symmetries.py` (run output
`results/probe-49-cusp-symmetries.log`); `results/issue-49-transporters-and-coble-cusp5.md` gives the proof.

1. 029J, `integral.cusp_root_orbits['gamma-en-2']` at (4.3.9): the eight diagram symmetries are isometries of K_J and
   induce a group of order 8 on the four root walls, so the transporter order is 8, not 4.
2. 6JRR, `integral.cusp_root_orbits['gamma-co-2']` at (4.3.9): four orbits, {beta_9}, {beta_10}, {alpha_12} and
   {alpha_13, alpha_14}, with beta_k = alpha_k + alpha_11 (029J coordinates). A 6JRR vector is a 029J vector of delta^perp
   with its first coordinate (that of e, equal to that of f) dropped.

    sage-docker-python results/store-49-transporters-and-coble-cusp5.py            # check, write nothing
    sage-docker-python results/store-49-transporters-and-coble-cusp5.py --write    # write both cards and certify
"""

import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / "src"), "/repos/research/src", "/repos/sage-extensions/src"]

from latticedb import certificates, corpus, genus, records, storage  # noqa: E402
from latticedb.model import Lattice  # noqa: E402

WRITE = "--write" in sys.argv[1:]

# 1. card 029J
card = ROOT / "lattices" / "029J.md"
document = corpus.read_card(card)
metadata = corpus.front_matter(document)
block = dict(metadata["integral"])
rows = dict(block["cusp_root_orbits"])
en = [dict(row) for row in rows["gamma-en-2"]]
(row439,) = [row for row in en if row["statement"] == "4.3.9"]
assert row439["orbits"][0]["transporter_order"] in (4, 8)
row439["orbits"] = [{**row439["orbits"][0], "transporter_order": 8}]
rows["gamma-en-2"] = en
block["cusp_root_orbits"] = rows
metadata["integral"] = block
lattice = Lattice.model_validate(metadata)
computation = genus.name("029J", "cusp_root_orbits", lattice.definiteness)
digest = certificates.certification_hash(computation, lattice, genus.certified_value("cusp_root_orbits", rows, lattice))
print(f"029J: (4.3.9) transporter order 8; {computation} = {digest}")
BY_EN = (
    'H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991), 1-36: (4.3.6), '
    "p. 21, has one root wall; (4.3.7), p. 22, (4.3.8), p. 23, and (4.3.9), p. 24, state that the diagram symmetries are "
    "realized in Gamma_v. The transporter order is the order of the permutation group the realized symmetries induce on "
    "the orbit's root walls: results/probe-49-cusp-symmetries.py computes the Gram-preserving permutations of each "
    "chamber's walls from this card, checks each is an isometry of K_J = v^perp/Zv, and prints the orders 1, 2, 2, 8"
)
if WRITE:
    metadata["certifications"] = {**lattice.certifications, "integral.cusp_root_orbits": digest}
    storage.write_text(card, records.record_text({k: v for k, v in metadata.items() if k != "integral"} | {"integral": block}, document.content))
    held = certificates.load(ROOT, tags=("029J",))
    held[computation] = certificates.Certificate(hash=digest, by=BY_EN)
    certificates.save(ROOT, held, tags=("029J",))

# 2. card 6JRR
TAG = "6JRR"
CARD = ROOT / "lattices" / f"{TAG}.md"
CUSP = [2, 0, 0, -4, -5, -7, -10, -8, -6, -4, -2]
BETA_9 = [1, 1, 3, -2, 0, 0, 0, 0, 0, 0, 0]
BETA_10 = [1, 4, 4, -2, 2, 4, 5, 4, 3, 2, 1]
ALPHA_12 = [1, 3, 3, -2, 1, 2, 2, 1, 0, 0, 0]
ALPHA_13 = [1, 3, 4, -2, 2, 3, 4, 3, 2, 1, 0]
ALPHA_14 = [1, 2, 3, -2, 0, 1, 0, 0, 0, 0, 0]
ORBITS = [([BETA_9], 1), ([BETA_10], 1), ([ALPHA_12], 1), ([ALPHA_13, ALPHA_14], 2)]
gram = [[Fraction(x) for x in r] for r in corpus.front_matter(corpus.read_card(CARD))["gram_tensor"]]


def pairing(a, b):
    return sum(Fraction(a[i]) * gram[i][j] * Fraction(b[j]) for i in range(len(gram)) for j in range(len(gram)))


assert pairing(CUSP, CUSP) == 0
for classes, _ in ORBITS:
    for x in classes:
        assert pairing(x, x) == -2 and pairing(x, CUSP) == 0
row = {
    "cusp": CUSP,
    "statement": "4.3.9",
    "printed_page": 24,
    "orbits": [{"representative": c[0], "classes": c, "transporter_order": t} for c, t in ORBITS],
    "orbit_count": len(ORBITS),
}
BY_CO = (
    "delta = e - f = -alpha_11 is a wall of Sterk's (4.3.9) chamber (p. 24) with no odd edge, so by Allcock, Reflection "
    "centralizers in Coxeter groups, arXiv:1106.3822v2, Theorem 5 and Corollary 6, C_W(s_11) = <s_11> x W_perp with W_perp "
    "the Coxeter group whose simple roots are the walls orthogonal to alpha_11 and beta_k = alpha_k + alpha_11 for the "
    "order-4 edges k = 9, 10; no symmetry other than sigma (alpha_13 <-> alpha_14) fixes alpha_11 and no odd path joins "
    "distinct root walls of W_perp, so with G_v in {+-1} W_v x| Aut(diagram) the root classes fall in four orbits under "
    "Gamma_Co,2, sigma being realized by (4.3.9), p. 24. results/probe-49-cusp-symmetries.py on card 029J computes it; "
    "results/issue-49-transporters-and-coble-cusp5.md is the proof"
)
print(f"{TAG}: (4.3.9) row with {len(ORBITS)} orbits")
if WRITE:
    held = certificates.load(ROOT, tags=(TAG,))
    genus.store_cusp_root_orbits(CARD, "gamma-co-2", [row], BY_CO, held)
    certificates.save(ROOT, held, tags=(TAG,))
    print("written")
else:
    print("dry run: nothing written")
