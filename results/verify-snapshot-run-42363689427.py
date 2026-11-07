"""Each snapshot's certificates held to the values and tensors in that same snapshot (#20).

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \\
      /sage/.venv/bin/python results/verify-snapshot-run-42363689427.py [shard...]

A certificate is a hash of one computation name, one Gram tensor and one field projection, so a
snapshot's `certificates/<group>.yaml` entry is only evidence if the value and tensor beside it in
that same snapshot are what it was computed from. This materialises, per snapshot, just the cards the
snapshot changed and their own certificate groups, and runs the repository's
`checks.records.problems` -- the certificate half of `latticedb verify` -- over them.

It is deliberately not a reimplementation: no comparison is written here. The subset corpus is what
the run's own cards need, and nothing else of the corpus is read, because a whole-corpus load does
not finish in one process.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from latticedb import certificates, checks, corpus

ROOT = Path(__file__).resolve().parent.parent
BASE = "dde534ecd9d7c61af3800d20eb1635bc7541f38a"
SNAPSHOTS = [
    ("0", "794f18ea486199716478eba933de2af99e59a13d"), ("1", "402ec19330a9cdf29a430dc803f3588435902d3f"),
    ("2", "ca31ca0cfdde4e974fee2914571a8950cb40e213"), ("3", "ca10b320c1127eb1f58c2663a423db60071b99da"),
    ("4", "781b3856b747ee204dd159b3e88debadd98a82ed"), ("5", "e9771bbb1bd10151b6a206b5c0cc3cb02e153e08"),
    ("6", "639a22bbee78fff050fb78c41aaefe272a63a37f"), ("7", "05fd6bf6a875059b25fdc9a7aec1495f9134ce41"),
    ("8", "cdab7525ec8c1d7f985f0a0a0da7384e57ebf086"), ("9", "6bba243ef46d4c671679d16d750343a0c7fd95aa"),
    ("10", "47ed8f7071b8286f371ff810032c259cd4a2d8c9"), ("11", "fbfcfaa2507a1041dcd9649d1e58efca951c7e29"),
    ("12", "e64a3fc649a6ae25e877cb034dca453044a6aabe"), ("13", "8c042b15221077495dc9b858f4ff02306eed0acc"),
    ("14", "c0f123c2f8097c8e33c26753db9d99fd2bc93ba6"), ("15", "47e21ab79b354588abccad812ea1f1b12604682d"),
]


def contents(rev: str, paths: list[str]) -> dict[str, str]:
    """The contents of `paths` at `rev`, in one batched read."""
    if not paths:
        return {}
    done = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "--batch"],
        input="".join(f"{rev}:{path}\n" for path in paths).encode(), capture_output=True, check=True,
    ).stdout
    found: dict[str, str] = {}
    position = 0
    for path in paths:
        end = done.index(b"\n", position)
        header = done[position:end].decode()
        position = end + 1
        if header.endswith("missing"):
            continue
        size = int(header.split()[-1])
        found[path] = done[position:position + size].decode()
        position += size + 1
    return found


def verify(shard: str, snapshot: str) -> list[str]:
    changed = subprocess.run(["git", "-C", str(ROOT), "diff", "--name-only", BASE, snapshot],
                             capture_output=True, text=True, check=True).stdout.split()
    cards = [path for path in changed if path.startswith("lattices/") and path.endswith(".md")]
    groups = sorted({certificates.group(Path(path).stem) for path in cards})
    wanted = [*cards, *(f"certificates/{group}.yaml" for group in groups),
              f"certificates/cf.yaml", "families.yaml", "retired-tags.yaml"]
    if "certificates/17.yaml" in changed:
        wanted.append("certificates/17.yaml")
    files = contents(snapshot, sorted(set(wanted)))
    root = Path(tempfile.mkdtemp(dir=ROOT / ".scratch"))
    (root / "lattices").mkdir()
    (root / "certificates").mkdir()
    for path, document in files.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(document)
    try:
        loaded = corpus.load(root)
        held = certificates.load(root)
        return checks.records.problems(loaded, held)
    finally:
        shutil.rmtree(root)


def main(wanted: list[str]) -> int:
    total = 0
    for shard, snapshot in SNAPSHOTS:
        if wanted and shard not in wanted:
            continue
        problems = verify(shard, snapshot)
        total += len(problems)
        print(f"shard {shard:>2} ({snapshot[:8]}): {len(problems)} problems", flush=True)
        for problem in problems[:8]:
            print("   ", problem)
        if len(problems) > 8:
            print(f"    ... and {len(problems) - 8} more")
    print(f"\n{total} certificate-pairing problems across the snapshots checked")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
