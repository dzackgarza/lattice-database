"""#43: SUPERSEDED — this program stored a row that has since been withdrawn.

Its row rested on the claim that the Coble condition is decided on the diagram symmetries alone, which fails because the
reflection subgroup does not fix delta. `results/withdraw-43-coble-cusp5.py` removed the row; this file is kept only as
the record of what was written and why it was wrong.

Original docstring follows.

#43: store the Coble cusp of three classes as two orbits on card 6JRR.

The argument is printed, and each step of it is a page: Sterk `(4.3.3)`, p. 18, writes the acting group as
$G = W(G) \\rtimes S$ with $S$ the diagram symmetries realised in $G$; `(4.3.9)`, p. 24, says the symmetries at this
cusp lift to $\\Gamma_v$; and every reflection in a wall of $T_{\\mathrm{Co}} = \\delta^\\perp$ fixes
$\\delta = e - f$ (`results/issue-43-lemma-reflections-fix-delta.md`), so whether an element of $G_v$ preserves
$T_{\\mathrm{Co}}$ is decided on $S$ alone. Of the eight symmetries exactly two carry $\\delta$ to $\\pm\\delta$ — the
identity and the one exchanging $\\alpha_{13}$ with $\\alpha_{14}$ (`results/issue-43-lemma-coble-image.md`) — so the
Coble image is $\\langle W_v, \\sigma\\rangle$, whose orbits are $\\{\\alpha_{12}\\}$ and
$\\{\\alpha_{13},\\alpha_{14}\\}$.

Everything is checked on card 6JRR's own Gram tensor before the row is written: the cusp is isotropic, both classes are
in its perpendicular with square $-2$, and the row passes the corpus's admission check.

    .scratch/wt43ae-run.sh -u results/store-43-coble-cusp5.py            # check, write nothing
    .scratch/wt43ae-run.sh -u results/store-43-coble-cusp5.py --write    # store the row and certify it
"""

import sys
from fractions import Fraction
from pathlib import Path

from latticedb import certificates, corpus, genus

ROOT = Path("/repo")
TAG = "6JRR"
GROUP = "gamma-co-2"
CARD = ROOT / "lattices" / f"{TAG}.md"

CUSP = [2, 0, 0, -4, -5, -7, -10, -8, -6, -4, -2]
ORBITS = [
    ([1, 3, 3, -2, 1, 2, 2, 1, 0, 0, 0], [[1, 3, 3, -2, 1, 2, 2, 1, 0, 0, 0]]),
    (
        [1, 3, 4, -2, 2, 3, 4, 3, 2, 1, 0],
        [[1, 3, 4, -2, 2, 3, 4, 3, 2, 1, 0], [1, 2, 3, -2, 0, 1, 0, 0, 0, 0, 0]],
    ),
]

metadata = corpus.front_matter(corpus.read_card(CARD))
gram = [[Fraction(entry) for entry in row] for row in metadata["gram_tensor"]]
rank = len(gram)


def pairing(left, right):
    return sum(
        (Fraction(left[i]) * gram[i][j] * Fraction(right[j]) for i in range(rank) for j in range(rank)),
        Fraction(0),
    )


assert pairing(CUSP, CUSP) == 0, "the cusp is not isotropic"
for representative, classes in ORBITS:
    assert pairing(representative, representative) == -2
    assert pairing(representative, CUSP) == 0
    for entry in classes:
        assert pairing(entry, entry) == -2 and pairing(entry, CUSP) == 0

row = {
    "cusp": CUSP,
    "statement": "4.3.9",
    "printed_page": 24,
    "orbits": [
        {"representative": representative, "classes": classes, "transporter_order": len(classes)}
        for representative, classes in ORBITS
    ],
    "orbit_count": len(ORBITS),
}
print(f"{TAG}: one row at (4.3.9) with {row['orbit_count']} orbits, sizes {[len(o['classes']) for o in row['orbits']]}")

BY = (
    'H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991), 1-36: '
    '(4.3.3), p. 18, writes the acting group as G = W(G) x| S with S the diagram symmetries realised in G; (4.3.9), '
    'p. 24, "Symmetries of the graph can be lifted to Gamma_v"; (4.3.10), p. 25, and (4.3.12), p. 25, realise them on '
    'A = H + E8(-2). T_Co is delta^perp for delta = e - f, and every reflection in a wall of T_Co fixes delta, so an '
    'element of G_v preserves T_Co exactly when its symmetry class does: of the eight symmetries of the (4.3.9) diagram '
    'exactly two carry delta to +-delta, the identity and the one exchanging alpha_13 with alpha_14. The Coble image is '
    'therefore <W_v, sigma>, whose orbits are {alpha_12} and {alpha_13, alpha_14}. '
    'results/store-43-coble-cusp5.py checks the cusp, the classes and their pairings in card 6JRR Gram tensor and '
    'writes the row there (results/issue-43-lemma-coble-cusp5.md)'
)

if "--write" not in sys.argv[1:]:
    print("dry run: nothing written (pass --write to store the row)")
    raise SystemExit(0)

held = certificates.load(ROOT, tags=(TAG,))
genus.store_cusp_root_orbits(CARD, GROUP, row_list := [row], BY, held)
certificates.save(ROOT, held, tags=(TAG,))
computation = genus.name(TAG, "cusp_root_orbits", "indefinite")
print(f"stored under {GROUP!r}; {computation} = {held[computation].hash}")
