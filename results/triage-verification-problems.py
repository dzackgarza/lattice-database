"""Classify each certificate contradiction the recovered tree shows: pre-existing or recovery-induced.

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \\
      /sage/.venv/bin/python results/triage-verification-problems.py results/evidence-20-verification.log

A contradiction is only meaningful as a pair: a card's value and the certificate that is supposed to
commit to it, read from the same revision. So for every `(card, field)` the production verifier
reports on the recovered tree, this reads the card *and* its own certificate shard from the revision
before the recovery (`934a1324ee`) and from the current tree, runs the repository's
`checks.records.problems` on each pair, and reports one of:

    pre-existing   the same contradiction is there before the recovery: not this item's doing
    recovered      it was there before and is gone now
    INDUCED        it is not there before and is here now: the recovery broke it
    neither        not reproduced on either pair (report the exact message; do not guess)

Old cards are never paired with new certificate shards, or the reverse.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from latticedb import certificates, checks, corpus

ROOT = Path(__file__).resolve().parent.parent
PRE = "934a1324ee"
PATTERN = re.compile(r"lattices/(?P<tag>[0-9A-Z]{4})\.md: (?P<field>[A-Za-z_.]+) contradicts")
EXTRA = {"families.yaml", "retired-tags.yaml"}


def reading(rev: str | None, tag: str) -> tuple[dict, dict]:
    """The card and its certificate shard as one revision states them; `None` means the working tree."""
    group = certificates.group(tag)
    names = [f"lattices/{tag}.md", f"certificates/{group}.yaml", *EXTRA]
    if rev is None:
        texts = {name: (ROOT / name).read_text() for name in names if (ROOT / name).exists()}
    else:
        done = subprocess.run(
            ["git", "-C", str(ROOT), "cat-file", "--batch"],
            input="".join(f"{rev}:{name}\n" for name in names).encode(), capture_output=True, check=True,
        ).stdout
        texts, position = {}, 0
        for name in names:
            end = done.index(b"\n", position)
            header = done[position:end].decode()
            position = end + 1
            if header.endswith("missing"):
                continue
            size = int(header.split()[-1])
            texts[name] = done[position:position + size].decode()
            position += size + 1
    return texts, group


def problems_at(rev: str | None, tag: str) -> list[str]:
    texts, group = reading(rev, tag)
    root = Path(tempfile.mkdtemp(dir=ROOT / ".scratch"))
    try:
        (root / "lattices").mkdir()
        (root / "certificates").mkdir()
        for name, document in texts.items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(document)
        return checks.records.problems(corpus.load(root), certificates.load(root))
    finally:
        shutil.rmtree(root)


def fields_in(problems: list[str]) -> set[str]:
    found = set()
    for problem in problems:
        match = PATTERN.search(problem)
        if match:
            found.add(match.group("field"))
    return found


def main(logs: list[str]) -> int:
    wanted: dict[str, set[str]] = {}
    for log in logs:
        for line in Path(log).read_text().splitlines():
            match = PATTERN.search(line)
            if match:
                wanted.setdefault(match.group("tag"), set()).add(match.group("field"))
    print(f"{len(wanted)} cards, {sum(len(fields) for fields in wanted.values())} contradicted fields reported\n")
    counts = {"pre-existing": 0, "recovered": 0, "INDUCED": 0, "neither": 0}
    for tag in sorted(wanted):
        before = fields_in(problems_at(PRE, tag))
        now = fields_in(problems_at(None, tag))
        for field in sorted(wanted[tag]):
            was, is_now = field in before, field in now
            verdict = (
                "pre-existing" if was and is_now
                else "recovered" if was and not is_now
                else "INDUCED" if not was and is_now
                else "neither"
            )
            counts[verdict] += 1
            print(f"{tag} {field:<52} before={str(was):<5} now={str(is_now):<5} {verdict}")
        extra = sorted(fields_in(problems_at(None, tag)) - wanted[tag])
        if extra:
            print(f"{tag}: also contradictory now, not in the log: {extra}")
    print()
    for verdict, count in counts.items():
        print(f"{verdict}: {count}")
    return 1 if counts["INDUCED"] else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
