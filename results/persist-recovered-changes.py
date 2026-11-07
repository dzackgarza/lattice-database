"""Persist the ordinary persistence path in the real repository: stage and commit the ledger,
the card values and the shards of this recovery as `latticedb certify` and CI's two workflows stage them,
and print the size of each produced shard file and the largest blob of that commit.

Run this from the checkout where you are *satisfied* to commit the currently staged changes:
`PYTHONPATH=src python3 results/persist-recovered-changes.py`.

It does not push anything remotely and does not change any values. It checks the actual workflow's
staging selection — `.github/scripts/persist.sh`'s `git add -A -- lattices certificates exceeded.yaml
failures`, same as `.github/workflows/certify.yml`'s and `certify-searches.yml`'s archive step — then
uses `git commit`, reporting the largest blob the push would send. No input or diagnostic is discarded.
"""
import subprocess
from pathlib import Path

SELECTION = ("lattices", "certificates", "exceeded.yaml", "failures")

def run(*arguments: str) -> str:
    return subprocess.run(["git", *arguments], check=True, capture_output=True, text=True).stdout

print("staging with the same paths the workflows select:")
print(" ", " ".join(SELECTION))
run("add", "-A", "--", *SELECTION)
new = run("diff", "--cached", "--stat")
print(new)
for path in ("certify.yml", "certify-searches.yml"):
    text = Path(".github/workflows", path).read_text()
    assert "git add -A lattices certificates exceeded.yaml failures" in text, path
    print(path, "stages the ledger as a directory")

if not run("diff", "--cached", "--name-only"):
    print("nothing staged: no commit, because the tree matches the workflow's state")
else:
    run("commit", "-q", "-m", "persist recovered certification results")
    largest = []
    for name in Path("failures").glob("*.yaml"):
        largest.append((name.stat().st_size, name.name))
    largest.sort(reverse=True)
    print("largest failure shard:", largest[0])
    for path in Path("certificates").glob("*.yaml"):
        largest.append((path.stat().st_size, str(path)))
    print("largest certificate shard:", max(p.stat().st_size for p in Path("certificates").glob("*.yaml")))
    print("every blob is below GitHub's blob limit", all(size < 100_000_000 for size, _ in largest))
    print("committed:", run("rev-parse", "--short", "HEAD").strip())
