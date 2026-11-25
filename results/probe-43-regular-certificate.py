"""#43: which value do the orphan `regular` certificates commit to?

The gate now reports, on eight definite cards, `definite.regular` and `definite.spinor_regular` as "contradicts its
completed computation certificate": the certificate exists and the card states no value. The field is a
`bool | "true under GRH"`, so the hash commits to one of three values and the value can be *read* out of the
certificate rather than guessed. This prints, per card and field, which candidate the stored hash equals.

    .scratch/wt43e-run.sh -u results/probe-43-regular-certificate.py
"""

from pathlib import Path

from latticedb import certificates, corpus
from latticedb.model import Lattice

ROOT = Path("/repo")
TAGS = ("02LP", "3ICA", "02BW", "02O9", "02YE", "0353", "03UB", "04R0")
CANDIDATES = (True, False, "true under GRH")

held = certificates.load(ROOT, tags=TAGS)
found: dict[str, list[str]] = {}
for tag in TAGS:
    metadata = corpus.front_matter(corpus.read_card(ROOT / "lattices" / f"{tag}.md"))
    lattice = Lattice.model_validate(metadata)
    for field in ("definite.regular", "definite.spinor_regular"):
        computation = f"{tag} {field}"
        certificate = held.get(computation)
        if certificate is None or certificate.hash is None:
            found.setdefault(tag, []).append(f"{field}: no certificate")
            continue
        matches = [
            value
            for value in CANDIDATES
            if certificates.certification_hash(computation, lattice, value) == certificate.hash
        ]
        stated = (metadata.get("definite") or {}).get(field.split(".")[1])
        found.setdefault(tag, []).append(f"{field}: commits to {matches!r}, card states {stated!r}")
for tag, lines in found.items():
    for line in lines:
        print(f"{tag}: {line}")
