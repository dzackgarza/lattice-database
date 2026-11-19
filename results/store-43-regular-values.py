"""#43: give the eight definite cards the `regular` values their own certificates commit to.

The gate reports, on eight definite cards, `definite.regular` and `definite.spinor_regular` as contradicting a
completed computation certificate: the certificate holds a hash and the card states neither the value nor the
citation. The field is `bool | "true under GRH"`, so the hash determines which of three values the computation
returned --- `certificates.certification_hash` over each candidate commits to the card's Gram tensor and the
computation's name --- and that is how the value is recovered here: it is read out of the certificate, not chosen, and
the card then cites the certificate it now states.

Nothing in `certificates/` is written: the entries already exist. `regular` and `spinor_regular` are not part of
`records.derived_projection`, so the `<tag> derive` certificate does not move either.

    .scratch/wt43e-run.sh -u results/store-43-regular-values.py            # print, write nothing
    .scratch/wt43e-run.sh -u results/store-43-regular-values.py --write    # write the eight cards
"""

import sys
from pathlib import Path

from latticedb import certificates, corpus, records, storage
from latticedb.model import Lattice

ROOT = Path("/repo")
TAGS = ("02LP", "3ICA", "02BW", "02O9", "02YE", "0353", "03UB", "04R0")
CANDIDATES = (True, False, "true under GRH")

held = certificates.load(ROOT, tags=TAGS)
pending: list[tuple[str, str, object, str]] = []
for tag in TAGS:
    path = ROOT / "lattices" / f"{tag}.md"
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    lattice = Lattice.model_validate(metadata)
    for short in ("regular", "spinor_regular"):
        field = f"definite.{short}"
        certificate = held.get(f"{tag} {field}")
        if certificate is None or certificate.hash is None:
            print(f"{tag} {field}: no completed certificate, left alone")
            continue
        matches = [
            value
            for value in CANDIDATES
            if certificates.certification_hash(f"{tag} {field}", lattice, value) == certificate.hash
        ]
        if len(matches) != 1:
            raise SystemExit(f"{tag} {field}: the certificate commits to {matches}, which is not one value")
        value = matches[0]
        stated = (metadata.get("definite") or {}).get(short)
        cited = metadata.get("certifications", {}).get(field)
        if stated == value and cited == certificate.hash:
            print(f"{tag} {field}: states {value!r} and cites it, nothing to do")
            continue
        if stated is not None and stated != value:
            raise SystemExit(f"{tag} {field}: the card states {stated!r} and the certificate commits to {value!r}")
        print(f"{tag} {field}: certificate commits to {value!r}; card states {stated!r}, cites {cited!r}")
        pending.append((tag, field, value, certificate.hash))

print(f"{len(pending)} card fields to write")
if "--write" not in sys.argv[1:]:
    print("dry run: nothing written (pass --write to store the values)")
    raise SystemExit(0)

for tag, field, value, certificate_hash in pending:
    path = ROOT / "lattices" / f"{tag}.md"
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    block = dict(metadata.get("definite") or {})
    block[field.split(".", 1)[1]] = value
    metadata["definite"] = block
    metadata["certifications"] = {**metadata.get("certifications", {}), field: certificate_hash}
    storage.write_text(path, records.record_text(metadata, document.content))
    print(f"wrote {tag} {field} = {value!r}")
