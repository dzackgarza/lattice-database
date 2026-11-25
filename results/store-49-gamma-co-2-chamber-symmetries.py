"""#49, #43: card 6JRR's computed cusp face chambers, and `chamber_symmetries` on its `gamma-co-2` root-orbit rows.

The values are the JSON line of `results/probe-49-gamma-co-2-chamber-symmetries.log`, which
`results/probe-49-gamma-co-2-chamber-symmetries.py` printed. At each Gamma_Co,2-cusp the program:
- writes the face chamber as an `integral.cusp_chambers['gamma-co-2']` row (computed, so it states no statement);
- stores each generator's isometry as a `morphisms` entry of the card;
- adds to the cusp's `cusp_root_orbits` row the image S of the Gamma_Co,2 cusp stabilizer among the diagram's symmetries.
Each element of S is exhibited as an integral isometry of T_Co that fixes v and has discriminant image in P_0. No
lifting statement of Sterk's is used. The root-class orbits under S are the stored ones; the program asserts this.

    sage-docker-python results/store-49-gamma-co-2-chamber-symmetries.py --write
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / "src")]

from latticedb import certificates, corpus, genus, records, storage  # noqa: E402
from latticedb.model import Lattice  # noqa: E402

TAG, GROUP = "6JRR", "gamma-co-2"
CARD = ROOT / "lattices" / f"{TAG}.md"
log = (ROOT / "results" / "probe-49-gamma-co-2-chamber-symmetries.log").read_text().splitlines()
(line,) = [x for x in log if x.startswith("JSON ")]
computed = {tuple(r["cusp"]): r for r in json.loads(line[5:])}

BY_CHAMBERS = (
    "The chamber at each Gamma_Co,2-cusp v of T_Co: the face C cap delta^perp of the chamber C that card 029J stores "
    "at the T_En cusp of v (H. Sterk, Math. Z. 207 (1991), (4.3.6)-(4.3.9), pp. 21-24), through T_Co = delta^perp, "
    "delta = e - f. It is the chamber of W_perp in C_W(s_delta) = <s_delta> x W_perp (Allcock, arXiv:1106.3822v2, "
    "Thm. 5, Cor. 6): the walls of C orthogonal to delta and alpha_u + delta for the order-4 neighbours u of delta. "
    "results/probe-49-gamma-co-2-chamber-symmetries.py computes the walls, the Gram matrix and the diagram from the two "
    "cards' Gram tensors"
)
held = certificates.load(ROOT, tags=(TAG,))
rows = [
    {k: computed[c][k] for k in ("cusp", "walls", "wall_count", "gram", "diagram")}
    for c in sorted(computed, key=lambda c: [r["cusp"] for r in corpus.front_matter(corpus.read_card(CARD))["integral"]["cusp_root_orbits"][GROUP]].index(list(c)))
]
WRITE = "--write" in sys.argv[1:]

document = corpus.read_card(CARD)
metadata = corpus.front_matter(document)
block = dict(metadata["integral"])
orbit_rows = []
for row in block["cusp_root_orbits"][GROUP]:
    c = computed[tuple(row["cusp"])]
    stored = sorted(sorted(map(tuple, o["classes"])) for o in row["orbits"])
    assert stored == sorted(sorted(map(tuple, o)) for o in c["root_orbits"]), row["cusp"]
    orbit_rows.append({**row, "chamber_symmetries": {"order": c["symmetry_order"], "generators": c["symmetry_generators"]}})
    print(f"cusp {row['cusp']}: |S| = {c['symmetry_order']}, generators {c['symmetry_generators']}")
BY_ORBITS = (
    held[f"{TAG} integral.cusp_root_orbits"].by
    + ". chamber_symmetries: S is the image of the Gamma_Co,2 stabilizer of v among the Gram-preserving permutations of "
    "the face walls (in the order of the cusp's cusp_chambers row). Each permutation is realized as a rational isometry "
    "g0 of T_Co fixing v, and the lifts E(v, a) g0 range over the Eichler transvections of v (Gritsenko-Hulek-Sankaran, "
    "arXiv:0810.1614, Sect. 3.1, eq. (4)). The permutation is in S exactly when some integral lift has discriminant "
    "image, its matrix mod 2, in P_0 = Stab(A_U(2)). results/probe-49-gamma-co-2-chamber-symmetries.py decides this; "
    "|S| = 1, 1, 2, 1 at the 2-, 120-, 135- and 270-orbit cusps. The (4.3.9) swap alpha_13 <-> alpha_14 is exhibited, "
    "not taken from a lifting statement"
)
if not WRITE:
    print("dry run")
    raise SystemExit(0)
genus.store_cusp_chambers(CARD, GROUP, rows, BY_CHAMBERS, held)
document = corpus.read_card(CARD)
metadata = corpus.front_matter(document)
block = dict(metadata["integral"])
block["cusp_root_orbits"] = {GROUP: orbit_rows}
metadata["integral"] = block
# each generator of S is stored with the isometry of T_Co that realizes it
morphisms = [m for m in metadata.get("morphisms", []) if not m["name"].startswith("Gamma_Co,2 cusp-face symmetry")]
for cusp, c in computed.items():
    for index, (sigma, witness) in enumerate(zip(c["symmetry_generators"], c["symmetry_witnesses"])):
        morphisms.append(
            {
                "target": TAG,
                "name": f"Gamma_Co,2 cusp-face symmetry {list(cusp)} #{index + 1}",
                "description": (
                    f"An element of Gamma_Co,2 that fixes the cusp {list(cusp)} and permutes the walls of its cusp_chambers row by "
                    f"{sigma}: an integral isometry whose matrix mod 2 stabilizes span(e_1, f_1). "
                    "results/probe-49-gamma-co-2-chamber-symmetries.py computes it"
                ),
                "matrix": witness,
                "scale": 1,
            }
        )
metadata["morphisms"] = morphisms
lattice = Lattice.model_validate(metadata)
assert records.local_admission_problems(lattice) == []
computation = genus.name(TAG, "cusp_root_orbits", lattice.definiteness)
digest = certificates.certification_hash(computation, lattice, genus.certified_value("cusp_root_orbits", block["cusp_root_orbits"], lattice))
metadata["certifications"] = {**lattice.certifications, "integral.cusp_root_orbits": digest}
storage.write_text(CARD, records.record_text({k: v for k, v in metadata.items() if k != "integral"} | {"integral": block}, document.content))
held[computation] = certificates.Certificate(hash=digest, by=BY_ORBITS)
certificates.save(ROOT, held, tags=(TAG,))
print("written", digest)
