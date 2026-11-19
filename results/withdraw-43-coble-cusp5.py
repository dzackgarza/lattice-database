"""#43: withdraw the (4.3.9) row — its proof has a gap the reviewer found.

The row rested on `results/issue-43-lemma-coble-cusp5.md` step 3: for $g = ws \\in G_v = W_v \\rtimes S$, "since $w$
fixes $\\delta$", the Coble condition would be decided on the symmetries alone. That step is false: $W_v$ is generated
by the reflections in **all fourteen** walls of the $T_{\\mathrm{En}}$ chamber, and only the eleven walls that lie in
$T_{\\mathrm{Co}}$ give reflections fixing $\\delta$ — the other three move it (`results/issue-43-lemma-reflections-fix-delta.md`
says so, and the reviewer is right to combine the two). A product of a symmetry that does not preserve $\\delta$ with one
of those three reflections may preserve it and carry $\\alpha_{12}$ to another class, so two orbits is not established
and the count could be one.

This removes the row, its certificate entry and the cell that held it, leaving card 6JRR with the two rows whose count
needs no group at all.

    .scratch/wt43ag-run.sh -u results/withdraw-43-coble-cusp5.py            # check, write nothing
    .scratch/wt43ag-run.sh -u results/withdraw-43-coble-cusp5.py --write    # remove the row
"""

import sys
from pathlib import Path

from latticedb import certificates, corpus, genus, records, storage
from latticedb.model import Lattice

ROOT = Path("/repo")
TAG = "6JRR"
CARD = ROOT / "lattices" / f"{TAG}.md"

document = corpus.read_card(CARD)
metadata = corpus.front_matter(document)
block = dict(metadata["integral"])
rows = dict(block["cusp_root_orbits"])
print("before:", {key: [row["statement"] for row in value] for key, value in rows.items()})
removed = [row for row in rows.pop("gamma-co-2", [])]
block["cusp_root_orbits"] = rows
metadata["integral"] = block
lattice = Lattice.model_validate(metadata)
computation = genus.name(TAG, "cusp_root_orbits", lattice.definiteness)
digest = certificates.certification_hash(computation, lattice, genus.certified_value("cusp_root_orbits", rows, lattice))
print("after:", {key: [row["statement"] for row in value] for key, value in rows.items()})
print(f"removed {len(removed)} row(s); the field's new hash is {digest}")

if "--write" not in sys.argv[1:]:
    print("dry run: nothing written")
    raise SystemExit(0)

metadata["certifications"] = {**lattice.certifications, "integral.cusp_root_orbits": digest}
storage.write_text(CARD, records.record_text({key: value for key, value in metadata.items() if key != "integral"} | {"integral": block}, document.content))
held = certificates.load(ROOT, tags=(TAG,))
entry = held.get(computation)
by = entry.by if entry is not None and entry.by else "research preamble"
by = (
    "H. Sterk, \"Compactifications of the period space of Enriques surfaces, Part I\", Math. Z. 207 (1991), 1-36: "
    "(4.3.7), p. 22, and (4.3.8), p. 23, print the chambers at those cusps; T_Co is delta^perp for delta = e - f, and of "
    "each chamber's walls exactly one that lies in T_Co is orthogonal to the cusp and of square -2, so the cusp's root "
    "family in K_I is a single class and its orbits are one orbit under every subgroup. The (4.3.9) row was withdrawn: "
    "its count of two relied on W_v fixing delta, which is false for the three chamber walls outside T_Co. "
    "results/store-43-coble-rows.py writes these two rows and results/withdraw-43-coble-cusp5.py removed the third"
)
held[computation] = certificates.Certificate(hash=digest, by=by)
certificates.save(ROOT, held, tags=(TAG,))
print(f"stored; {computation} = {digest}")
