"""#43: author `gamma-co-2` on card 6JRR, with the index certified by computation.

The 2026-11-19 decision: the cusp-5 row waits until `gamma-co-2` has a card **certified by computation from the
library's own construction** of $\\Gamma_{\\mathrm{Co},2} = R_{\\Gamma_{\\mathrm{En},2}}$ — the restriction of
$\\Gamma_{\\mathrm{En},2}$ to $T_{\\mathrm{Co}}$ — and never from the project's draft.

The library constructs the two ingredients. $R_{\\Gamma_{\\mathrm{En}}} = \\widetilde O^{+}(T_{\\mathrm{Co}})$
(sage-extensions `results/issue359-tco-restricted-stabilizers.md`, row 2), whose index in $O(T_{\\mathrm{Co}})$ is
$93997183795200$ — a value this card's catalogue already carries, certified on 6JRR. And
$\\Gamma_{\\mathrm{Co},2}$ is the kernel of the $T_{\\mathrm{En}}$-side discriminant character on it, whose image
`results/probe-43-co2-family.py` computes from the owner's own family: 290 generators of
$\\mathrm{Stab}_{O(T_{\\mathrm{En}})}(\\delta)$, restricted to $T_{\\mathrm{Co}}$ and mapped by `rho`, generate a
subgroup of order $46998591897600$. So

$$[O(T_{\\mathrm{Co}}) : \\Gamma_{\\mathrm{Co},2}] = 93997183795200 \\cdot 46998591897600
= 4417735280714304737771520000,$$

which is the value the card states and the certificate commits to.

    .scratch/wt43r-run.sh -u results/author-43-gamma-co-2.py            # check, write nothing
    .scratch/wt43r-run.sh -u results/author-43-gamma-co-2.py --write    # author the card and certify the index
"""

import sys
from pathlib import Path

from latticedb import card_serialization, certificates, corpus, records, storage
from latticedb.catalogues import ArithmeticGroup
from latticedb.model import Lattice

ROOT = Path("/repo")
TAG = "6JRR"
SLUG = "gamma-co-2"
FIELD = f"arithmetic-group.{SLUG}.index_in_orthogonal_group"
INDEX = 93997183795200 * 46998591897600
CARD = ROOT / "arithmetic-groups" / f"{SLUG}.md"

if CARD.exists():
    raise SystemExit(f"{CARD} already exists; this program authors it once")

metadata = corpus.front_matter(corpus.read_card(ROOT / "lattices" / f"{TAG}.md"))
lattice = Lattice.model_validate(metadata)
assert lattice.integral is not None and lattice.integral.discriminant_group is not None

record = {
    "slug": SLUG,
    "name": "Gamma_Co,2",
    "latex": "\\Gamma_{\\mathrm{Co},2}",
    "lattice": TAG,
    "ambient_lie_group": "o-2-9",
    "parent_group": "otilde-plus-t-co",
    "data": {
        "index_in_orthogonal_group": INDEX,
        "cardinality": "aleph0",
        "abstract_structure": (
            "the image in O(T_Co) of the isometries of T_En that lie in Gamma_En,2 and preserve T_Co = delta^perp, "
            "delta = e - f; equivalently the kernel of the T_En-side discriminant character on Otilde+(T_Co), which is "
            "the restriction R_{Gamma_En} of the Enriques group to this lattice"
        ),
        "reference": {
            "citation": (
                "the construction, and not a definition in print: sage-extensions' own record "
                "`results/issue359-tco-restricted-stabilizers.md`, rows 1 and 2, identifies the restricted stabilizers "
                "on T_Co = delta^perp as R_{Gamma_En} = Otilde+(T_Co) of index 93997183795200 = 2|O(A_T_Co, q)| in "
                "O(T_Co) and R_{Gamma^K_En} = O(T_Co) of index 1, both computed from the images of the constructed "
                "generators, and sage-extensions#286 item 1 is the issue that builds them. The index stored here is the "
                "product of that index with the order of the T_En-side discriminant character's image on the family, "
                "46998591897600, computed by results/probe-43-co2-family.py from 290 generators of "
                "Stab_{O(T_En)}(delta) restricted to T_Co. Nothing here asserts the identification of this group with "
                "the Coble period group, which the corpus records as conjectural for Otilde+(T_Co) itself "
                "(arithmetic-groups/otilde-plus-t-co.md:23-24)"
            )
        },
    },
}
ArithmeticGroup.model_validate(record)
print(f"{SLUG}: index {INDEX} = 93997183795200 * 46998591897600, parent otilde-plus-t-co, lattice {TAG}")
print(f"card text:\n{card_serialization.catalogue_text(record, '')}")

if "--write" not in sys.argv[1:]:
    print("dry run: nothing written (pass --write to author the card)")
    raise SystemExit(0)

card_hash = certificates.certification_hash(f"{TAG} {FIELD}", lattice, INDEX)
storage.write_text(CARD, card_serialization.catalogue_text(record, ""))
document = corpus.read_card(ROOT / "lattices" / f"{TAG}.md")
stored = corpus.front_matter(document)
stored["certifications"] = {**stored.get("certifications", {}), FIELD: card_hash}
groups = list(stored.get("arithmetic_groups") or [])
if SLUG not in groups:
    groups.append(SLUG)
stored["arithmetic_groups"] = groups
storage.write_text(ROOT / "lattices" / f"{TAG}.md", records.record_text(stored, document.content))
held = certificates.load(ROOT, tags=(TAG,))
held[f"{TAG} {FIELD}"] = certificates.Certificate(
    hash=card_hash,
    by=(
        "results/author-43-gamma-co-2.py: the index of Gamma_Co,2 in O(T_Co) as the product of the certified index of "
        "Otilde+(T_Co), 93997183795200, with the order 46998591897600 of the T_En-side discriminant character's image "
        "on the restricted family, which results/probe-43-co2-family.py computes from 290 generators of "
        "Stab_{O(T_En)}(delta) (sage-extensions 6ae2108). The construction is sage-extensions' R_{Gamma_En} = "
        "Otilde+(T_Co) identification (results/issue359-tco-restricted-stabilizers.md, rows 1-2); no published source "
        "defines the group and none is claimed"
    ),
)
certificates.save(ROOT, held, tags=(TAG,))
print(f"authored {CARD} and certified {TAG} {FIELD} = {card_hash}")
