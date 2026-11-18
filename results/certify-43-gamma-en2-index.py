"""#43: certify the index card `gamma-en-2` states, by the computation that returns it.

`arithmetic-groups/gamma-en-2.md` states `data.index_in_orthogonal_group: 67456`. Nothing in the corpus
established it: no source prints the number, and `genus.arithmetic_requests` cannot ask the owner for it,
because the card has no `standard_name` and so "has no owner operation that presents it"
(`src/latticedb/genus.py:293`). The value is nevertheless the library's own answer for the group the card
describes --- "the image in $O(T_{\\mathrm{En}})$ of the isometries of the $K3$ lattice that commute with
$I_{\\mathrm{En}}$ and fix $h$" --- and this program is the computation that returns it, in the manner
`genus.store_cusp_chambers` and `genus.store_cusp_root_orbits` fill the two fields `certify` never asks for:
the certificate's hash commits to the index and to card 029J's Gram tensor, and its provenance names this
program and the revisions it ran against.

What it checks before it writes anything:

* the group's ambient lattice has 029J's Gram tensor, so the index is the index in $O(L)$ for *this* card;
* the invariant lattice of $I_{\\mathrm{En}}$ has exactly one polarization mark, so `h` is determined and the
  number is not a choice among polarizations;
* the library's index equals the value the group card states.

    .scratch/wt43b-run.sh results/certify-43-gamma-en2-index.py            # print, write nothing
    .scratch/wt43b-run.sh results/certify-43-gamma-en2-index.py --write    # write card and certificate
"""

import sys
from pathlib import Path

from latticedb import certificates, corpus, genus, records
from latticedb.model import Lattice
from sage_extensions.all import ZZ, Involutions, Lattices, NamedLattices  # noqa: F401,F403

ROOT = Path("/repo")
TAG = "029J"
SLUG = "gamma-en-2"
FIELD = f"arithmetic-group.{SLUG}.index_in_orthogonal_group"
CARD = ROOT / "lattices" / f"{TAG}.md"

metadata = corpus.front_matter(corpus.read_card(CARD))
lattice = Lattice.model_validate(metadata)
group_card = corpus.front_matter(corpus.read_card(ROOT / "arithmetic-groups" / f"{SLUG}.md"))
stated = group_card["data"]["index_in_orthogonal_group"]
print(f"{TAG}: Gram tensor of rank {lattice.rank}, definiteness {lattice.definiteness}")
print(f"{SLUG}: states index_in_orthogonal_group = {stated}")

invariant = Involutions.I_En.invariant_lattice()
labels = tuple(invariant.module_generating_set())
marks = [
    (left, right)
    for left in labels
    for right in labels
    if left <= right
    and invariant.q(invariant.module_generator(left)) == ZZ.zero()
    and invariant.q(invariant.module_generator(right)) == ZZ.zero()
    and invariant.b(invariant.module_generator(left), invariant.module_generator(right)) == ZZ(2)
]
assert len(marks) == 1, f"the invariant lattice has {len(marks)} polarization marks, so h is not determined"
left, right = marks[0]
polarization = invariant.module_generator(left) + invariant.module_generator(right)
group = Involutions.I_En.polarized(invariant.inclusion()(polarization)).coinvariant_extension_subgroup()
ambient = group.supergroup().lattice()
ambient_labels = tuple(ambient.module_generating_set())
gram = [
    [int(ambient.b(ambient.module_generator(row), ambient.module_generator(column))) for column in ambient_labels]
    for row in ambient_labels
]
card_gram = [[int(entry) for entry in row] for row in lattice.gram_tensor]
assert int(ambient.module_rank()) == lattice.rank, (ambient.module_rank(), lattice.rank)
assert gram == card_gram, (
    "the group's ambient lattice is not card 029J's lattice (same rank, different Gram):\n"
    f"library: {gram}\ncard: {card_gram}"
)
index = int(group.index())
print(f"library: index of the I_En coinvariant extension subgroup in O(T_En) = {index}")
assert index == stated, f"the library returns {index}, the card states {stated}"

computation = genus.name(TAG, FIELD, lattice.definiteness)
committed = genus.certified_value(FIELD, stated, lattice)
certificate_hash = certificates.certification_hash(computation, lattice, committed)
by = (
    "H. Sterk, \"Compactifications of the period space of Enriques surfaces, Part I\", Math. Z. 207 "
    "(1991), 1-36, Remark 2.12, p. 8: [O(L_-):Gamma] = (2^21 3^5 5^2 7 17 31)/(2 2^13 3^5 5^2 7) = "
    "2^7 17 31 = 67456, Gamma being the image in O(L_-) of the isometries of the K3 lattice that commute "
    "with the Enriques involution and fix the polarization, identified with the congruence condition of "
    "Proposition 2.7, pp. 6-7. The number is reproduced by results/certify-43-gamma-en2-index.py, which "
    "returns the same index from the library (`group.index()`, sage-extensions d667a7c, research "
    "ec1333eeb0) on an ambient lattice whose Gram tensor is card "
    f"{TAG}'s"
)
print(f"computation: {computation}")
print(f"certificate hash: {certificate_hash}")
print(f"by: {by}")

if "--write" not in sys.argv[1:]:
    print("dry run: nothing written (pass --write to store the certificate)")
    raise SystemExit(0)

held = certificates.load(ROOT, tags=(TAG,))
held[computation] = certificates.Certificate(hash=certificate_hash, by=by)
metadata["certifications"] = {**lattice.certifications, FIELD: certificate_hash}
CARD.write_text(records.record_text(metadata, corpus.read_card(CARD).content))
certificates.save(ROOT, held, tags=(TAG,))
print(f"stored: {FIELD} on {CARD.name} and in certificates/{certificates.group(TAG)}.yaml")
