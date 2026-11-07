"""The production certificate checks over every card run 42363689427 recovered, on the current tree.

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/verify-current-chunks.py [--size 400] [--state PATH]

The whole recovered set cannot be verified in one process: a corpus load holds every card and the
preamble keeps every structure it builds (that is why `latticedb verify` shards), and the single
process that tried it here died after one line of output. So the set is verified in chunks of cards,
each in its own process, and every chunk prints its own result:

    chunk 3/23: 400 cards, 0 problems

A chunk's corpus holds only that chunk's cards and the certificate groups they need, which is the
same code CI runs (`checks.records.problems`, the certificate half of `latticedb verify`) applied to
a subset the process can finish. Chunks already recorded in the state file are skipped, so a run cut
short by a job's limit resumes instead of starting again; the final summary names the totals:

    0 problems in 8999 recovered cards over 23 chunks

Nothing here reimplements a comparison: every verdict is `checks.records.problems`'s own.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from latticedb import certificates, checks, corpus

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / ".scratch" / "verify-current-state.json"
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


def verify(tags: list[str]) -> list[str]:
    groups = sorted({certificates.group(tag) for tag in tags})
    root = Path(tempfile.mkdtemp(dir=ROOT / ".scratch"))
    try:
        (root / "lattices").mkdir()
        (root / "certificates").mkdir()
        shutil.copy(ROOT / corpus.FAMILIES_FILE, root / corpus.FAMILIES_FILE)
        shutil.copy(ROOT / corpus.RETIRED_FILE, root / corpus.RETIRED_FILE)
        for group in groups:
            shutil.copy(ROOT / "certificates" / f"{group}.yaml", root / "certificates" / f"{group}.yaml")
        for tag in tags:
            shutil.copy(ROOT / "lattices" / f"{tag}.md", root / "lattices" / f"{tag}.md")
        loaded = corpus.load(root)
        held = certificates.load(root)
        return checks.records.problems(loaded, held)
    finally:
        shutil.rmtree(root)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=400)
    parser.add_argument("--state", type=Path, default=STATE)
    options = parser.parse_args()

    tags = recovered_tags()
    chunks = [tags[i:i + options.size] for i in range(0, len(tags), options.size)]
    done: dict[str, int] = json.loads(options.state.read_text()) if options.state.exists() else {}
    total_problems = 0
    for index, chunk in enumerate(chunks, 1):
        key = f"{index}/{len(chunks)}"
        if key in done:
            total_problems += done[key]
            print(f"chunk {key}: {len(chunk)} cards, {done[key]} problems (recorded)", flush=True)
            continue
        problems = verify(chunk)
        total_problems += len(problems)
        done[key] = len(problems)
        options.state.parent.mkdir(parents=True, exist_ok=True)
        options.state.write_text(json.dumps(done, indent=1, sort_keys=True))
        print(f"chunk {key}: {len(chunk)} cards, {len(problems)} problems", flush=True)
        for problem in problems:
            print("   ", problem.replace(str(ROOT), ""), flush=True)
    print(f"\n{total_problems} problems in {len(tags)} recovered cards over {len(chunks)} chunks", flush=True)
    return 1 if total_problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
