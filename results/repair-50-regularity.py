"""Restore the regularity decisions that stored certificates name and cards stopped stating (#50).

A certificate commits to the computation name, the Gram tensor and the stored result, so for a field
whose result is a decision — `definite.regular`, `definite.spinor_regular` — the certificate's hash
identifies the value among its possible ones: absent, true or false. This script reads every
certificate whose field is one a job may stop inside (`genus.SEMI_DECISIONS`), and, for each card
that no longer states the result, writes the value whose hash the certificate carries with the
citation of that certificate. A card where no candidate or more than one matches is refused, and the
run names it rather than guessing.

    PYTHONPATH=src python results/repair-50-regularity.py            # report only
    PYTHONPATH=src python results/repair-50-regularity.py --write    # write the cards
"""

import re
import sys
from pathlib import Path

import frontmatter
from pydantic import TypeAdapter

from latticedb import certificates, genus, storage
from latticedb.card_serialization import record_text
from latticedb.model import Lattice, Yaml

REPOSITORY = Path(__file__).resolve().parent.parent

NAME = re.compile(r"^([0-9A-Za-z]{4}) (\S+):$")
"""A certificate name: the tag, a space, and the block-and-field of the computation."""

CANDIDATES: tuple[tuple[str, bool], ...] = (("true", True), ("false", False))
"""The values a regularity certificate can name; a hash over the card's Gram tensor picks one."""


def ledger() -> dict[str, dict[str, tuple[str, str]]]:
    """Every certificate of a semi-decision field in `certificates/`, by card: field -> (hash, by)."""
    found: dict[str, dict[str, tuple[str, str]]] = {}
    for path in sorted((REPOSITORY / "certificates").glob("*.yaml")):
        tag = field = ""
        digest = by = ""
        for line in path.read_text().splitlines():
            matched = NAME.match(line)
            if matched:
                if tag and digest and field.rsplit(".", 1)[-1] in genus.SEMI_DECISIONS:
                    found.setdefault(tag, {})[field] = (digest, by)
                tag, field, digest, by = matched.group(1), matched.group(2), "", ""
            elif line.startswith("  hash: "):
                digest = line.removeprefix("  hash: ")
            elif line.startswith("  by: "):
                by = line.removeprefix("  by: ")
        if tag and digest and field.rsplit(".", 1)[-1] in genus.SEMI_DECISIONS:
            found.setdefault(tag, {})[field] = (digest, by)
    return found


def main(write: bool) -> int:
    restored = 0
    refused = 0
    for tag, held in sorted(ledger().items()):
        path = REPOSITORY / "lattices" / f"{tag}.md"
        document = frontmatter.load(str(path), encoding="utf-8")
        metadata: dict[str, Yaml] = TypeAdapter(dict[str, Yaml]).validate_python(document.metadata)
        lattice = Lattice.model_validate(metadata)
        citations = dict(lattice.certifications)
        changed = False
        for field, (digest, by) in sorted(held.items()):
            block_name, _, short = field.partition(".")
            block = dict(metadata.get(block_name) or {})
            value = block.get(short)
            if value is not None:
                computed = certificates.certification_hash(f"{tag} {field}", lattice, genus.certified_value(short, value, lattice))
                if computed != digest:
                    print(f"REFUSED {tag} {field}: the card states {value!r}, which is not the certificate's value")
                    refused += 1
                continue
            if short not in ("regular", "spinor_regular"):
                print(f"REFUSED {tag} {field}: a search of another field has no value to restore from a hash")
                refused += 1
                continue
            matching = [candidate for _, candidate in CANDIDATES if certificates.certification_hash(f"{tag} {field}", lattice, candidate) == digest]
            if len(matching) != 1:
                print(f"REFUSED {tag} {field}: the certificate names {matching}, not one value")
                refused += 1
                continue
            print(f"{tag} {field}: certificate {digest[:12]} names {matching[0]!r} ({by})")
            block[short] = matching[0]
            citations[field] = digest
            metadata[block_name] = _ordered(block, short, lattice)
            changed = True
        if not changed or not write:
            restored += changed
            continue
        metadata["certifications"] = citations
        text = record_text(metadata, document.content)
        if text != path.read_text():
            storage.write_text(path, text)
            print(f"{path.relative_to(REPOSITORY)}: written")
        restored += 1
    print(f"{restored} card(s) {'restored' if write else 'to restore'}, {refused} refused")
    return 1 if refused else 0


def _ordered(block: dict[str, Yaml], field: str, lattice: Lattice) -> dict[str, Yaml]:
    """The block with `field` in the model's own place: the line the card carried before it lost it."""
    model = genus.stored_in(field, lattice.definiteness)[1]
    return {key: block[key] for key in model.model_fields if key in block}


if __name__ == "__main__":
    sys.exit(main("--write" in sys.argv[1:]))
