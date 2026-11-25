"""#49, #43: card 6JRR's `cusp_root_orbits['gamma-co-2']`, one row at each of the four Gamma_Co,2-cusps.

The values are those printed by `results/probe-49-gamma-co-2-cusps.py` (run output
`results/probe-49-gamma-co-2-cusps.log`). Each row is at one Gamma_{Co,2}-cusp of T_Co, named by the size of the
P_0-orbit of [v/2] among the 527 singular classes and stated by a representative v in card 6JRR's basis. The chamber
whose roots are counted is the face C cap delta^perp of Sterk's chamber at the T_En cusp that v is through the Heegner
embedding T_Co = delta^perp; Sterk prints C, not the face, so a row states no `statement` and Sterk is provenance in the
certificate. The block replaces the earlier rows whole: the 135-orbit row keeps its four orbits; the 120- and
270-orbit rows move from 1 and 1 orbit to 3 and 2, since the earlier rows omitted the roots beta_u = alpha_u + delta;
the 2-orbit row is new.

    sage-docker-python results/store-49-gamma-co-2-cusps.py            # check, write nothing
    sage-docker-python results/store-49-gamma-co-2-cusps.py --write    # write the block and certify it
"""

import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / "src")]

from latticedb import certificates, corpus, genus, records, storage  # noqa: E402
from latticedb.model import Lattice  # noqa: E402

TAG = "6JRR"
CARD = ROOT / "lattices" / f"{TAG}.md"

# (orbit size of [v/2], Sterk's chamber at the T_En cusp, its page, v, the orbits of root classes), 6JRR basis.
ROWS = (
    (2, "4.3.6", 21, [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [[[1, 0, 0, -2, -3, -4, -6, -5, -4, -3, -2]]]),
    (
        120,
        "4.3.7",
        22,
        [0, 1, 1, -2, -3, -4, -6, -5, -4, -3, -2],
        [
            [[1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1]],
            [[1, 0, -2, 2, 3, 4, 6, 5, 4, 3, 2]],
            [[1, 0, 0, -2, -2, -3, -4, -3, -2, -1, 0]],
        ],
    ),
    (
        135,
        "4.3.9",
        24,
        [2, 0, 0, -4, -5, -7, -10, -8, -6, -4, -2],
        [
            [[1, 1, 3, -2, 0, 0, 0, 0, 0, 0, 0]],
            [[1, 4, 4, -2, 2, 4, 5, 4, 3, 2, 1]],
            [[1, 3, 3, -2, 1, 2, 2, 1, 0, 0, 0]],
            [[1, 3, 4, -2, 2, 3, 4, 3, 2, 1, 0], [1, 2, 3, -2, 0, 1, 0, 0, 0, 0, 0]],
        ],
    ),
    (
        270,
        "4.3.8",
        23,
        [0, 2, 1, -4, -5, -7, -10, -8, -6, -4, -2],
        [[[1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0]], [[1, -2, 0, 2, 2, 3, 4, 3, 2, 1, 0]]],
    ),
)

document = corpus.read_card(CARD)
metadata = corpus.front_matter(document)
gram = [[Fraction(x) for x in r] for r in metadata["gram_tensor"]]


def pairing(a, b):
    return sum(Fraction(a[i]) * gram[i][j] * Fraction(b[j]) for i in range(len(gram)) for j in range(len(gram)))


rows = []
for size, statement, page, cusp, orbits in ROWS:
    assert pairing(cusp, cusp) == 0
    for classes in orbits:
        for x in classes:
            assert pairing(x, x) == -2 and pairing(x, cusp) == 0, (size, x)
    rows.append(
        {
            "cusp": cusp,
            "orbits": [{"representative": classes[0], "classes": classes} for classes in orbits],
            "orbit_count": len(orbits),
        }
    )
    print(f"Gamma_Co,2-cusp of orbit size {size} (chamber of Sterk ({statement}), p. {page}): {len(orbits)} orbits")

block = dict(metadata["integral"])
block["cusp_root_orbits"] = {"gamma-co-2": rows}
metadata["integral"] = block
lattice = Lattice.model_validate(metadata)
assert records.local_admission_problems(lattice) == []
computation = genus.name(TAG, "cusp_root_orbits", lattice.definiteness)
digest = certificates.certification_hash(computation, lattice, genus.certified_value("cusp_root_orbits", block["cusp_root_orbits"], lattice))
print(f"{computation} = {digest}")
BY = (
    "Rows at the four Gamma_Co,2-cusps of T_Co, each named by the orbit size (2, 120, 135, 270) of [v/2] under "
    "P_0 = Stab(A_U(2)), the image of Gamma_Co,2 = rho^-1(P_0) (sage-extensions results/issue607-gamma-co-2-rows-by-the-polar-space.md); "
    "results/probe-49-gamma-co-2-cusps.py computes the orbit of each cusp. Each cusp is, through the Heegner embedding "
    "T_Co = delta^perp, delta = e - f, the cusp vector of H. Sterk, Compactifications of the period space of Enriques "
    "surfaces I, Math. Z. 207 (1991): (4.3.6) p. 21, (4.3.7) p. 22, (4.3.9) p. 24, (4.3.8) p. 23, in that order. delta "
    "is a wall of that chamber with only order-4 edges, so by Allcock, Reflection centralizers in Coxeter groups, "
    "arXiv:1106.3822v2, Thm. 5 and Cor. 6, C_W(s_delta) = <s_delta> x W_perp with simple roots the walls orthogonal to "
    "delta and beta_u = alpha_u + delta; the root classes are its simple roots of square -2, no two joined by an odd "
    "path, and the diagram symmetries fixing delta join them: only alpha_13 <-> alpha_14 at (4.3.9), realized in "
    "Gamma_v by (4.3.9), p. 24. The same program computes the rows from card 029J's chambers; "
    "results/issue-49-transporters-and-coble-cusp5.md is the proof"
)
if "--write" not in sys.argv[1:]:
    print("dry run: nothing written")
    raise SystemExit(0)
metadata["certifications"] = {**lattice.certifications, "integral.cusp_root_orbits": digest}
storage.write_text(CARD, records.record_text({k: v for k, v in metadata.items() if k != "integral"} | {"integral": block}, document.content))
held = certificates.load(ROOT, tags=(TAG,))
held[computation] = certificates.Certificate(hash=digest, by=BY)
certificates.save(ROOT, held, tags=(TAG,))
print("written")
