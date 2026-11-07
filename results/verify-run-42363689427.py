"""Verify the cards a recovery commit touched, through the repository's own certificate checks.

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/verify-run-42363689427.py <commit>...

`checks.records.problems` is the half of `latticedb verify` that compares every cited field of a card
with its completed certificate, recomputing the hash from the stored Gram and the stored value. A
scratch corpus holding only the touched cards and their own certificate groups keeps the run to what
the recovery changed, and it is the same code CI runs.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from latticedb import certificates, checks, corpus

ROOT = Path(__file__).resolve().parent.parent


def touched_tags(commits: list[str]) -> list[str]:
    tags: set[str] = set()
    for commit in commits:
        listing = subprocess.run(
            ["git", "-C", str(ROOT), "diff-tree", "--no-commit-id", "--name-only", "-r", commit],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
        for name in listing:
            if name.startswith("lattices/") and name.endswith(".md"):
                tags.add(Path(name).stem)
    return sorted(tags)


def main(commits: list[str]) -> int:
    tags = touched_tags(commits)
    print(f"{len(commits)} commits, {len(tags)} cards touched")
    groups = sorted({certificates.group(tag) for tag in tags})
    with tempfile.TemporaryDirectory(dir=ROOT / ".scratch") as scratch:
        root = Path(scratch)
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
        problems = checks.records.problems(loaded, held)
    for problem in problems:
        print(problem)
    print(f"{len(problems)} problems in {len(tags)} recovered cards over {len(groups)} certificate groups")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
