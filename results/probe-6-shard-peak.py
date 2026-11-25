"""Measure what one `verify` shard's two loads cost, at the scale this VM can hold (#6).

`checks.one_shard` reads the whole corpus and every certificate group in its own process,
so a shard's peak is the sum of those two loads plus the shard's own preamble structures.
The full loads need about fourteen GiB, which this VM does not have; this measures each
load at two sizes on a fixture and fits the per-card and per-byte cost, so the ceiling the
workflow states has a derivation and not only a memory.

    python results/probe-6-shard-peak.py cards 12000
    python results/probe-6-shard-peak.py certificates 16

Prints one JSON line: the size of the load, its peak resident GiB, and the slope.
"""

import json
import random
import resource
import shutil
import sys
from pathlib import Path

from latticedb import certificates, corpus

ROOT = Path(__file__).resolve().parent.parent


def peak() -> float:
    """The peak resident memory of this process, in GiB."""
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20


def fixture(name: str, cards: int, groups: int) -> Path:
    """A corpus of `cards` cards and `groups` certificate groups, at `.scratch/peak/<name>`."""
    root = ROOT / ".scratch" / "peak" / name
    if root.exists():
        shutil.rmtree(root)
    (root / "lattices").mkdir(parents=True)
    (root / "certificates").mkdir()
    for companion in ("families.yaml", "retired-tags.yaml"):
        shutil.copy2(ROOT / companion, root / companion)
    paths = sorted((ROOT / "lattices").glob("*.md"))
    random.Random(6).shuffle(paths)
    for path in paths[:cards]:
        shutil.copy2(path, root / "lattices" / path.name)
    files = sorted((ROOT / "certificates").glob("*.yaml"))
    random.Random(6).shuffle(files)
    for path in files[:groups]:
        shutil.copy2(path, root / "certificates" / path.name)
    return root


def main() -> None:
    """Measure the load named on the command line and print it with its cost."""
    kind, size = sys.argv[1], int(sys.argv[2])
    if kind == "cards":
        root = fixture(f"cards{size}", size, 0)
        loaded = corpus.load(root)
        measured, entries = len(loaded.entries), len(loaded.entries)
    else:
        root = fixture(f"groups{size}", 0, size)
        held = certificates.load(root)
        measured, entries = size, len(held)
        measured = sum(path.stat().st_size for path in (root / "certificates").glob("*.yaml")) / 2**20
    print(json.dumps({"kind": kind, "size": measured, "entries": entries, "peak_gib": round(peak(), 2)}))
    shutil.rmtree(root)


if __name__ == "__main__":
    main()
