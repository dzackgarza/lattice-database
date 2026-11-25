"""#43: store the three cusped rows of `integral.cusp_root_orbits`, each one orbit, from the diagrams' symmetries.

Sterk prints the walls of the chamber at each of the five 0-cusps of $\\Gamma_{\\mathrm{En},2}$ and the symmetry of
that chamber's Coxeter diagram, and states that the symmetry is realised inside the cusp stabilizer:

* (4.3.7), p. 22: "It can be checked that the symmetry of the diagram comes from an element in $\\Gamma_v$ (see
  (4.3.10)). We find $G_v = \\{\\pm1\\}W_v \\rtimes \\mathbb{Z}/2$."
* (4.3.8), p. 23: "the symmetry is induced by an element of $\\Gamma_v$ (see (4.3.10))."
* (4.3.9), p. 24: "Symmetries of the graph can be lifted to $\\Gamma_v$ (see (4.3.10))."

So an isometry of the cusp stabilizer carries one wall of the chamber to another whenever a symmetry of the diagram
does, and with it one root class of $K_J$ to the other.  This program computes that symmetry from the card's own Gram
tensor --- the walls' squares and their pairings --- finds its orbits on the walls of square $-2$, and stores one
orbit per cusp where the family is a single orbit.

    .scratch/wt43c-run.sh -u results/store-43-cusp-orbits.py            # print, write nothing
    .scratch/wt43c-run.sh -u results/store-43-cusp-orbits.py --write    # store the rows and certify them
"""

import sys
from fractions import Fraction
from pathlib import Path

from latticedb import certificates, corpus, genus

ROOT = Path("/repo")
TAG = "029J"
GROUP = "gamma-en-2"
CARD = ROOT / "lattices" / f"{TAG}.md"
BY = (
    'H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991), 1-36: '
    "(4.3.7), p. 22, \"the symmetry of the diagram comes from an element in Gamma_v\" with G_v = {+-1}W_v x Z/2; "
    "(4.3.8), p. 23, \"the symmetry is induced by an element of Gamma_v\"; (4.3.9), p. 24, \"Symmetries of the graph "
    "can be lifted to Gamma_v\"; each with (4.3.10). results/store-43-cusp-orbits.py computes the diagram's "
    "symmetry from the card's Gram tensor and finds one orbit at each of the three cusps, carrying alpha_9 to "
    "alpha_13 at (4.3.7), alpha_9 to alpha_11 at (4.3.8), and alpha_11, alpha_12, alpha_13, alpha_14 transitively "
    "at (4.3.9)"
)

metadata = corpus.front_matter(corpus.read_card(CARD))
gram = [[Fraction(entry) for entry in row] for row in metadata["gram_tensor"]]
rank = len(gram)


def pairing(left, right) -> Fraction:
    return sum(
        (Fraction(left[i]) * gram[i][j] * Fraction(right[j]) for i in range(rank) for j in range(rank)),
        Fraction(0),
    )


def automorphisms(walls) -> list[dict[int, int]]:
    """Every permutation of the walls that preserves their squares and their pairings with each other."""
    count = len(walls)
    squares = [pairing(wall, wall) for wall in walls]
    found: list[dict[int, int]] = []

    def extend(partial: dict[int, int]) -> None:
        if len(partial) == count:
            found.append(dict(partial))
            return
        index = len(partial)
        for image in range(count):
            if image in partial.values() or squares[image] != squares[index]:
                continue
            if all(pairing(walls[index], walls[other]) == pairing(walls[image], walls[seen]) for other, seen in partial.items()):
                partial[index] = image
                extend(partial)
                del partial[index]

    extend({})
    return found


chambers = metadata["integral"]["cusp_chambers"][GROUP]
rows = []
for chamber in chambers:
    walls = [tuple(wall["vector"]) for wall in chamber["walls"]]
    names = [wall["name"] for wall in chamber["walls"]]
    roots = [index for index in range(len(walls)) if pairing(walls[index], walls[index]) == -2]
    if len(roots) < 2:
        print(f"{chamber['statement']}: {len(roots)} root class(es), nothing to store")
        continue
    symmetries = automorphisms(walls)
    moves = {index: sorted({symmetry[index] for symmetry in symmetries}) for index in roots}
    print(f"{chamber['statement']}: {len(walls)} walls, roots {[names[i] for i in roots]}, {len(symmetries)} symmetries")
    for index, images in moves.items():
        print(f"    {names[index]} is carried to {[names[image] for image in images]}")
    # The orbits of the symmetries on the root walls: one orbit is the row.
    remaining = set(roots)
    orbits = []
    while remaining:
        seed = min(remaining)
        orbit = {seed} | {image for image in moves[seed] if image in remaining}
        frontier = [index for index in list(orbit) if index != seed]
        while frontier:
            current = frontier.pop()
            for image in moves[current]:
                if image in remaining and image not in orbit:
                    orbit.add(image)
                    frontier.append(image)
        remaining -= orbit
        orbits.append(sorted(orbit))
    print(f"    orbits on the root walls: {[[names[i] for i in orbit] for orbit in orbits]}")
    if len(orbits) != 1:
        continue
    ordered = orbits[0]
    rows.append(
        {
            "cusp": list(chamber["cusp"]),
            "statement": chamber["statement"],
            "printed_page": chamber["printed_page"],
            "orbits": [
                {
                    "representative": list(walls[ordered[0]]),
                    "classes": [list(walls[index]) for index in ordered],
                    "transporter_order": len(ordered),
                }
            ],
            "orbit_count": 1,
        }
    )

print(f"rows to store: {[row['statement'] for row in rows]}")
if "--write" not in sys.argv[1:]:
    print("dry run: nothing written (pass --write to store the rows)")
    raise SystemExit(0)

held = certificates.load(ROOT, tags=(TAG,))
genus.store_cusp_root_orbits(CARD, GROUP, rows, BY, held)
certificates.save(ROOT, held, tags=(TAG,))
computation = genus.name(TAG, "cusp_root_orbits", "indefinite")
print(f"stored; {computation} hash {held[computation].hash}")
