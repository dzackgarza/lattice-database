"""Restore the citation each of the four cards' computed values already has a certificate for (#21).

The certificate commits to the computation name, the Gram tensor and the stored value, and not to
the card's `certifications` map, so a missing reference is repaired without recomputing anything:
the reference is the shard's own hash, and this script refuses to write a card whose stored value
does not hash to the entry it found.

    PYTHONPATH=src python results/repair-21-citations.py            # report only
    PYTHONPATH=src python results/repair-21-citations.py --write    # write the cards
"""

import sys
from pathlib import Path

import frontmatter
import yaml
from pydantic import TypeAdapter

from latticedb import certificates, storage
from latticedb.card_serialization import record_text
from latticedb.model import Lattice, Yaml

REPOSITORY = Path(__file__).resolve().parent.parent

CITED: dict[str, tuple[str, ...]] = {
    "0021": ("root_span.roots", "root_span.norms"),
    "0024": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
    "0026": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
    "0268": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
}
"""The cards of #21, and the block-qualified fields whose reference each lacked."""

RECURRED: dict[str, tuple[str, ...]] = {
    "0269": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
    "026A": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
    "02AI": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
    "028L": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
    "02A4": ("hyperbolic.reflective",),
    "02A9": ("hyperbolic.reflective", "root_span.roots", "root_span.norms"),
}
"""The same defect on cards certified by a run that pushed before the card merge driver landed.

Each value hashes to its shard's entry, exactly as #21's did; the reference is the whole repair.
"""


def front_matter(path: Path) -> dict[str, Yaml]:
    return TypeAdapter(dict[str, Yaml]).validate_python(frontmatter.load(str(path), encoding="utf-8").metadata)


def certified_value(field: str, value: Yaml) -> Yaml:
    """`genus.certified_value` for these fields: the computation commits to the stored value itself."""
    assert field not in {"automorphism_group_generator_morphisms", "primitive_orbits", "discriminant_orbits"}
    return value


def main(write: bool) -> int:
    held = certificates.load(REPOSITORY)
    restored = 0
    for tag, fields in {**CITED, **RECURRED}.items():
        path = REPOSITORY / "lattices" / f"{tag}.md"
        document = frontmatter.load(str(path), encoding="utf-8")
        metadata = front_matter(path)
        citations = dict(Lattice.model_validate(metadata).certifications)
        for qualified in fields:
            block_name, field = qualified.split(".", 1)
            block = metadata.get(block_name)
            value = block.get(field) if isinstance(block, dict) else None
            certificate = held.get(f"{tag} {qualified}")
            assert certificate is not None, f"{tag} {qualified}: the shard holds no certificate"
            recomputed = certificates.certification_hash(f"{tag} {block_name}.{field}", Lattice.model_validate(metadata), certified_value(field, value))
            assert certificate.hash == recomputed, f"{tag} {qualified}: the shard's hash is not the hash of the card's value"
            citations[qualified] = certificate.hash
            restored += 1
            print(f"{tag} {qualified}: {certificate.hash}")
        assert restored
        if not write:
            continue
        metadata["certifications"] = citations
        text = record_text(metadata, document.content)
        if text != path.read_text():
            storage.write_text(path, text)
            print(f"{path.relative_to(REPOSITORY)}: written")
    print(f"{restored} references {'restored' if write else 'to restore'}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--write" in sys.argv[1:]))
