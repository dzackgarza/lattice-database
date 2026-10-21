"""Certificates of completed computations.

`certificates/` maps the name of a computation to one hash of the
computation name, the Gram tensor, and the value stored on the card. The card
is the only place that stores the value itself. A name begins with the tag of
its card, and `certificates/<group>.yaml` holds the names whose tag falls in
`<group>`, one of `GROUPS` buckets of the tag's SHA-256 hash. No file outgrows a
Git host's limit, and a checkpoint rewrites only the groups whose cards changed.
Certification shards split the same hash (`genus.in_shard`), and `GROUPS` is a
multiple of the shard count, so no two shards write the same file.

A computation that does not finish has no certificate. Authored or seeded
card values have no certification status until the certification phase
computes them and writes a certificate, except a value that a seeded source
proves: its certificate names that source's citation, and the value is never
recomputed.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Iterable
from pathlib import Path

import yaml
from pydantic import Field, TypeAdapter

from latticedb import storage
from latticedb.model import Lattice, Record

CERTIFICATES_DIR = "certificates"


class Certificate(Record):
    hash: str = Field(
        description="SHA-256 digest of the computation name, Gram tensor, and certified card value.",
    )
    by: str = Field(description="The program that carried out the computation, with its version, or the citation of the source that proves the value.")


Certificates = dict[str, Certificate]


GROUPS = 256
"""The number of certificate files; a multiple of every certification shard count."""


def tag_hash(tag: str) -> int:
    """The hash of a card tag that places it in a certificate group and a certification shard."""
    return int.from_bytes(hashlib.sha256(tag.encode()).digest()[:8], "big")


def group(tag: str) -> str:
    """The certificate file of the card `tag`."""
    return f"{tag_hash(tag) % GROUPS:02x}"


def _group_of(name: str) -> str:
    return group(name.split(" ", 1)[0])


def load(root: Path) -> Certificates:
    held: Certificates = {}
    for path in sorted((root / CERTIFICATES_DIR).glob("*.yaml")):
        held.update(TypeAdapter(Certificates).validate_python(yaml.load(path.read_text(), Loader=yaml.CSafeLoader) or {}))
    return held


def save(root: Path, certificates: Certificates, tags: Iterable[str] | None = None) -> None:
    """Write the certificate groups of `tags`, or every group when `tags` is not given.

    Writing every group also removes the file of a group that no longer holds a certificate.
    """
    directory = root / CERTIFICATES_DIR
    groups: dict[str, Certificates] = {}
    for name, certificate in certificates.items():
        groups.setdefault(_group_of(name), {})[name] = certificate
    chosen = set(groups) if tags is None else {group(tag) for tag in tags}
    if tags is None and directory.exists():
        chosen |= {path.stem for path in directory.glob("*.yaml")}
    for name in sorted(chosen):
        path = directory / f"{name}.yaml"
        members = groups.get(name, {})
        if not members:
            if path.exists():
                path.unlink()
            continue
        data = {key: certificate.model_dump(exclude_none=True) for key, certificate in sorted(members.items())}
        directory.mkdir(exist_ok=True)
        storage.write_text(path, yaml.dump(data, Dumper=yaml.CSafeDumper, sort_keys=False, allow_unicode=True))


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def certification_hash(name: str, lattice: Lattice, value: object) -> str:
    """Commit to one computation name, Gram tensor, and stored result."""
    if lattice.gram_tensor is None:
        raise ValueError("a certification hash requires a stored Gram tensor")
    return digest(
        json.dumps(
            {
                "computation": name,
                "gram_tensor": [[str(entry) for entry in row] for row in lattice.gram_tensor],
                "result": value,
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            default=str,
        )
    )


def is_certified(
    certificates: Certificates,
    name: str,
    cited_hash: str | None,
    expected_hash: str,
) -> bool:
    """Whether the card cites the exact completed certificate for its stored result."""
    certificate = certificates.get(name)
    return cited_hash == expected_hash and certificate is not None and certificate.hash == cited_hash


def is_pending(
    certificates: Certificates,
    name: str,
    cited_hash: str | None,
    expected_hash: str,
) -> bool:
    """Whether the card lacks a completed certificate for its stored result."""
    return not is_certified(certificates, name, cited_hash, expected_hash)
