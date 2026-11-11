"""Restore the regularity values that stored certificates name and the cards stopped stating (#23).

A certificate commits to the computation name, the Gram tensor and the stored result, so for a field
whose result is a decision — `definite.regular`, `definite.spinor_regular` — the certificate's hash
identifies the value among its possible ones: absent, true or false. This script takes each named
card's own certificate shard, and writes the value whose hash the certificate carries, with the
citation, refusing any card where no candidate or more than one matches.

    PYTHONPATH=src python results/repair-23-regularity.py            # report only
    PYTHONPATH=src python results/repair-23-regularity.py --write    # write the cards
"""

import sys
from pathlib import Path

import frontmatter
import yaml
from pydantic import TypeAdapter

from latticedb import certificates, corpus, genus, storage
from latticedb.card_serialization import record_text
from latticedb.certificates import Certificates
from latticedb.model import Lattice, Yaml

REPOSITORY = Path(__file__).resolve().parent.parent

STATES: dict[str, tuple[str, ...]] = {
    "0023": ("regular", "spinor_regular"),
    "02AE": ("regular", "spinor_regular"),
    "02AF": ("regular", "spinor_regular"),
    "02AG": ("regular", "spinor_regular"),
    "02AH": ("regular", "spinor_regular"),
    "02AN": ("regular", "spinor_regular"),
    "02BQ": ("regular",),
    "02BS": ("regular",),
    "02BT": ("regular",),
}
"""Each card of the contradiction report, and the regularity fields its shard certifies."""

CANDIDATES = (("absent", None), ("true", True), ("false", False))


def main(write: bool) -> int:
    restored = 0
    for tag, fields in STATES.items():
        path = REPOSITORY / "lattices" / f"{tag}.md"
        document = frontmatter.load(str(path), encoding="utf-8")
        metadata: dict[str, Yaml] = TypeAdapter(dict[str, Yaml]).validate_python(document.metadata)
        held = TypeAdapter(Certificates).validate_python(
            yaml.load((REPOSITORY / "certificates" / f"{certificates.group(tag)}.yaml").read_text(), Loader=yaml.CSafeLoader) or {}
        )
        lattice = Lattice.model_validate(metadata)
        block = dict(metadata.get("definite") or {})
        citations = dict(lattice.certifications)
        changed = False
        for field in fields:
            computation = genus.name(tag, field, lattice.definiteness)
            entry = held.get(computation)
            assert entry is not None, f"{tag} {field}: the shard holds no certificate"
            matching = [name for name, value in CANDIDATES if certificates.certification_hash(computation, lattice, value) == entry.hash]
            assert len(matching) == 1, f"{tag} {field}: the certificate names {matching}, not one value"
            name = matching[0]
            assert name != "absent", f"{tag} {field}: its certificate commits to an absent value, so there is nothing to restore"
            value = dict(CANDIDATES)[name]
            assert block.get(field) in (None, value), f"{tag} {field}: the card states {block.get(field)!r}, the certificate {value!r}"
            print(f"{tag} {field}: certificate {entry.hash[:12]} names {value!r}")
            block[field] = value
            citations[f"definite.{field}"] = entry.hash
            changed = True
        if not changed or not write:
            continue
        metadata["definite"] = block
        metadata["certifications"] = citations
        text = record_text(metadata, document.content)
        if text != path.read_text():
            storage.write_text(path, text)
            print(f"{path.relative_to(REPOSITORY)}: written")
        restored += 1
    print(f"{restored} card(s) {'restored' if write else 'to restore'}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--write" in sys.argv[1:]))
