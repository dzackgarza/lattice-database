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


def verify(commit: str) -> tuple[int, list[str]]:
    """The production certificate checks over the cards one commit touched, in their own corpus."""
    tags = touched_tags([commit])
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
        return len(tags), checks.records.problems(loaded, held)
    finally:
        shutil.rmtree(root)


def main(commits: list[str]) -> int:
    """One commit at a time, so a run's memory is one commit's corpus and each result is printed."""
    total_cards = total_problems = 0
    for commit in commits:
        cards, problems = verify(commit)
        total_cards += cards
        total_problems += len(problems)
        print(f"{commit}: {cards} cards, {len(problems)} problems", flush=True)
        for problem in problems:
            print("   ", problem.replace(str(ROOT), ""), flush=True)
    print(f"\n{total_problems} problems in {total_cards} recovered cards over {len(commits)} commits")
    return 1 if total_problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
