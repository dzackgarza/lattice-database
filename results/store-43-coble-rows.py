"""#43: store the two decided T_Co cusps on card 6JRR, under the standard key `O`.

The rows at Sterk's cusps 3 and 4 — (4.3.7), p. 22, and (4.3.8), p. 23 — have **one** root class each: of the chamber's
walls, exactly one lies in $T_{\\mathrm{Co}} = \\delta^\\perp$ ($\\delta = e - f$), is orthogonal to the cusp, and has
square $-2$. A family of one class has one orbit under every subgroup, so the count is the same for `O` and for the
Coble group the cusps belong to, and the row is keyed to the standard subgroup the field always has
(the decision recorded on the issue, 2026-11-19). The cusp-5 row is not stored: with three classes its count depends on
the group, which has no card.

The coordinates are card 6JRR's own: the library's $\\delta^\\perp$, written in $T_{\\mathrm{En}}$'s coordinates, has this
card's Gram tensor entry for entry (`results/probe-43-coble-row-coordinates.py`), and membership of $T_{\\mathrm{Co}}$ is
decided by the pairing with $\\delta$ — not by the projection, which is integral whenever $b(v, \\delta)$ is even and so
admits walls outside the sublattice.

    .scratch/wt43n-run.sh -u results/store-43-coble-rows.py            # check, write nothing
    .scratch/wt43n-run.sh -u results/store-43-coble-rows.py --write    # store the two rows and certify them
"""

import sys
from fractions import Fraction
from pathlib import Path

from latticedb import certificates, corpus, genus

ROOT = Path("/repo")
TAG = "6JRR"
GROUP = "O"
CARD = ROOT / "lattices" / f"{TAG}.md"

CUSPS = (
    # Sterk's statement, its page, the cusp and the one root class, all in card 6JRR's basis.
    ("4.3.7", 22, [0, 1, 1, -2, -3, -4, -6, -5, -4, -3, -2], [1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1]),
    ("4.3.8", 23, [0, 2, 1, -4, -5, -7, -10, -8, -6, -4, -2], [1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0]),
)

metadata = corpus.front_matter(corpus.read_card(CARD))
gram = [[Fraction(entry) for entry in row] for row in metadata["gram_tensor"]]
rank = len(gram)


def pairing(left, right):
    return sum(
        (Fraction(left[i]) * gram[i][j] * Fraction(right[j]) for i in range(rank) for j in range(rank)),
        Fraction(0),
    )


rows = []
for statement, page, cusp, root in CUSPS:
    assert pairing(cusp, cusp) == 0, f"{statement}: the cusp is not isotropic"
    assert pairing(root, root) == -2, f"{statement}: the class is not a root"
    assert pairing(root, cusp) == 0, f"{statement}: the class is not in the cusp's perpendicular"
    rows.append(
        {
            "cusp": cusp,
            "statement": statement,
            "printed_page": page,
            "orbits": [{"representative": root, "classes": [root], "transporter_order": 1}],
            "orbit_count": 1,
        }
    )

BY = (
    'H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991), 1-36: '
    "(4.3.7), p. 22, prints the chamber at the cusp e' + f' + bar_alpha_8 and (4.3.8), p. 23, the chamber at "
    "2e' + f' + bar_alpha_1. T_Co is delta^perp for delta = e - f, so a wall of such a chamber is a wall of T_Co "
    "exactly when it is orthogonal to delta; of the walls that are, exactly one at each cusp is orthogonal to the cusp "
    "and of square -2, so the cusp's root family in K_I = v^perp/Zv is a single class. A one-class family has one "
    "orbit under every subgroup, which is why the row is keyed to the standard subgroup O: the count is the same for O "
    "and for the Coble group the cusps belong to. results/store-43-coble-rows.py checks the cusp, the class and their "
    "pairing in card 6JRR's Gram tensor and writes the row there"
)

print(f"{TAG}: {len(rows)} rows to store under {GROUP!r}: {[row['statement'] for row in rows]}")
if "--write" not in sys.argv[1:]:
    print("dry run: nothing written (pass --write to store the rows)")
    raise SystemExit(0)

held = certificates.load(ROOT, tags=(TAG,))
genus.store_cusp_root_orbits(CARD, GROUP, rows, BY, held)
certificates.save(ROOT, held, tags=(TAG,))
computation = genus.name(TAG, "cusp_root_orbits", "indefinite")
print(f"stored; {computation} = {held[computation].hash}")
