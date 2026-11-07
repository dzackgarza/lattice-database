"""Verify every card run 42363689427 recovered, one bounded process per chunk (#20).

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \\
      /sage/.venv/bin/python results/verify-current-chunks.py [--size 400] [--only INDEX]

This process only orchestrates: for each chunk it starts `results/verify-one-chunk.py` in a **separate
process**, which does the verification and records the result against the exact inputs it read (tree
commit and diff, card and certificate hashes, checker and verifier hashes, tag list). A chunk's record
is reused only when every one of those still matches, so a changed tree cannot inherit an old result.

Each chunk prints its own line and the run ends with the totals, which is what
results/verify-launcher.sh requires:

    chunk 3/23: 400 cards, 0 problems
    26 problems in 8999 recovered cards over 23 chunks

Nothing here reimplements a comparison: every verdict is `checks.records.problems`'s own, made in the
child process.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / ".scratch" / "verify-current-manifest.json"
ONE = ROOT / "results" / "verify-one-chunk.py"
COMMITS = (
    "4ec0a9d032", "b29b4ba832", "964395ab60", "4bafb3c10d", "1c07872a25", "e4586bd3ca", "b79a496a65",
    "9948ba5fac", "5d2e85df36", "06d674d450", "b3ce5ee40f", "28868d01f7", "a13524a39f", "e7e885b67e",
    "3b8fec51b9", "f49ed12c28",
)


def recovered_tags() -> list[str]:
    tags: set[str] = set()
    for commit in COMMITS:
        listing = subprocess.run(
            ["git", "-C", str(ROOT), "diff-tree", "--no-commit-id", "--name-only", "-r", commit],
            capture_output=True, text=True, check=True).stdout.splitlines()
        tags.update(Path(name).stem for name in listing if name.startswith("lattices/") and name.endswith(".md"))
    return sorted(tags)


def manifest(size: int) -> dict:
    """The chunk list, kept as it stands while the tag set is unchanged."""
    tags = recovered_tags()
    if MANIFEST.exists():
        held = json.loads(MANIFEST.read_text())
        if [tag for entry in held["chunks"] for tag in entry["tags"]] == tags:
            return held
    chunks = [{"tags": tags[i:i + size], "problems": None, "binding": None}
              for i in range(0, len(tags), size)]
    fresh = {"size": size, "tags": len(tags), "chunks": chunks}
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(fresh, indent=1, sort_keys=True))
    return fresh


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=400)
    parser.add_argument("--only", type=int, default=None, help="one chunk, 1-based")
    options = parser.parse_args()
    held = manifest(options.size)
    chunks = held["chunks"]
    total_problems = 0
    for index in range(len(chunks)):
        if options.only is not None and index != options.only - 1:
            continue
        chunk = chunks[index]
        # Always ask the child: it computes the binding for the inputs as they are now and decides
        # there whether its own record still describes them.
        run = subprocess.run([sys.executable, "-u", str(ONE), str(MANIFEST), str(index)])
        held = json.loads(MANIFEST.read_text())
        chunks = held["chunks"]
        chunk = chunks[index]
        if chunk["problems"] is None:
            print(f"chunk {index + 1}/{len(chunks)}: no result recorded (child exit {run.returncode})",
                  file=sys.stderr, flush=True)
            print(f"{total_problems} problems in {held['tags']} recovered cards over {len(chunks)} chunks")
            return 1
        total_problems += len(chunk["problems"])
    print(f"{total_problems} problems in {held['tags']} recovered cards over {len(chunks)} chunks", flush=True)
    return 1 if total_problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
