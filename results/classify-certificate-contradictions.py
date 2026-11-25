"""Split the pre-existing certificate contradictions by what is actually wrong with the pair.

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \\
      /sage/.venv/bin/python results/classify-certificate-contradictions.py results/evidence-20-verification.log

`checks.records.problems` reports one message, "contradicts its completed computation certificate",
for three different states of a card's field and its shard entry. The repair differs, so they are
separated here by recomputing the hash from the card's own stored value and Gram tensor:

    uncited      the shard's hash is exactly the hash of the stored value, and the card does not cite
                 it: the computation is finished and correct, the card's reference is missing.
    stale        the shard's hash is not the hash of the stored value: the certificate commits to a
                 value the card no longer states, so one of the two is out of date.
    unstated     the card states no value at all while the shard holds a certificate for the field.
    uncertified  the card cites a hash the shard does not hold.

Nothing is changed here: a contradiction is named with its state, so the owner decides between
re-stamping, re-citing and retracting.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import frontmatter
import yaml

from latticedb import certificates, corpus, genus

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r"lattices/(?P<tag>[0-9A-Z]{4})\.md: (?P<field>[A-Za-z_.]+) contradicts")


def classify(tag: str, field: str) -> tuple[str, str]:
    document = frontmatter.load(str(ROOT / "lattices" / f"{tag}.md"))
    metadata = document.metadata
    lattice = corpus.Lattice.model_validate(metadata)
    # A problem names the field by its local path, `<block>.<field>`; the genus maps the bare field.
    block_name, short = field.rsplit(".", 1)
    genus.stored_in(short, lattice.definiteness)
    block = metadata.get(block_name) or {}
    value = block.get(short)
    cited = (metadata.get("certifications") or {}).get(field)
    shard = yaml.load((ROOT / "certificates" / f"{certificates.group(tag)}.yaml").read_text(),
                      Loader=yaml.CSafeLoader) or {}
    entry = shard.get(genus.name(tag, short, lattice.definiteness)) or {}
    held = entry.get("hash")
    if value is None:
        return "unstated", f"card states no value; shard holds {str(held)[:12]}"
    if held is None:
        return "uncertified", f"card cites {str(cited)[:12]}; shard holds nothing"
    expected = certificates.certification_hash(
        genus.name(tag, short, lattice.definiteness), lattice, genus.certified_value(short, value, lattice)
    )
    if held == expected:
        if cited is None:
            return "uncited", f"shard {held[:12]} is this card's own value; the card cites nothing"
        if cited != held:
            return "stale-citation", (
                f"the card cites {cited[:12]} but the shard holds {held[:12]}, which is this card's own value"
            )
        return "contradiction", f"card and shard agree on {held[:12]} but the verifier still reports a difference"
    return "stale", f"shard {held[:12]} is not this value's hash {expected[:12]}"


def main(logs: list[str]) -> int:
    found: dict[str, set[str]] = {}
    for log in logs:
        for line in Path(log).read_text().splitlines():
            match = PATTERN.search(line)
            if match:
                found.setdefault(match.group("tag"), set()).add(match.group("field"))
    counts: dict[str, int] = {}
    for tag in sorted(found):
        for field in sorted(found[tag]):
            kind, detail = classify(tag, field)
            counts[kind] = counts.get(kind, 0) + 1
            print(f"{kind:<12} {tag} {field:<46} {detail}")
    print()
    for kind, count in sorted(counts.items(), key=lambda pair: -pair[1]):
        print(f"{kind}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
