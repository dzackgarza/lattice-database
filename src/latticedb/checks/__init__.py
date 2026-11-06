"""Read-only verification of stored lattice-db claims.

`corpus.load` reads each file and checks that it has the shape of its schema.
Every question that needs two records, or a record and the family, the retired
tags or the catalogues is asked here only when it is a storage/reference question.
Mathematical validity is queried through the corresponding preamble object; no
mathematical algorithm is implemented here.
Archived intake sources are provenance for how cards were seeded. Nothing here writes.

A run verifies the cards of one shard in a process of its own (`SHARDS` of them,
`--shard i/n` for one). The whole corpus is read, because a claim is checked
against the cards it names, but each process holds the preamble structures of its
own shard only: the preamble memoizes every structure it constructs in
process-wide caches that it never releases, so one process that verified every
card of this corpus outgrew the runner and was killed for memory (exit 137, run
42206179575) (#6).
"""

from __future__ import annotations

import json
import resource
import subprocess
import sys
from pathlib import Path

from latticedb import certificates, corpus, genus
from latticedb.checks import catalogues, records, relations

SHARDS = 8
"""How many processes verify the corpus, each holding the structures of its own shard.

The corpus is about 1.7 GB of card text in 302,497 cards, and `corpus.load`
validates all of it in every process: read once, the models cost about 7.5 GiB.
What a shard removes is the sum of the preamble's structures for the other
shards' cards. Raise it when a shard's reported peak approaches the runner's
memory.
"""


def run(root: Path, shard: tuple[int, int] | None = None) -> tuple[int, list[str]]:
    """Run stored-card verification without changing cards, one process per shard of the corpus.

    `shard` verifies that shard in this process; without it every shard is verified
    in a process of its own, one after another. A corpus no larger than the shard
    count is one shard, so a small corpus is not read once per shard.
    """
    if shard is not None:
        return one_shard(root, shard)
    count = len(list((root / "lattices").glob("*.md")))
    shards = max(1, min(SHARDS, count))
    verified = 0
    found: dict[str, None] = {}
    for index in range(shards):
        cards, problems = in_its_own_process(root, index, shards)
        verified += cards
        for problem in problems:
            found.setdefault(problem, None)
    return verified, list(found)


def one_shard(root: Path, shard: tuple[int, int]) -> tuple[int, list[str]]:
    """Verify the cards whose tag falls in `shard` of the corpus, in this process."""
    loaded = corpus.load(root)
    held = certificates.load(root)
    cards = frozenset(entry.lattice.tag for entry in loaded.entries if genus.in_shard(entry.lattice.tag, shard))
    problems = [
        *records.shared_gram_problems(loaded),
        *records.problems(loaded, held, cards),
        *relations.problems(loaded, root, cards),
        *catalogues.problems(loaded),
    ]
    return len(cards), problems


def in_its_own_process(root: Path, index: int, count: int) -> tuple[int, list[str]]:
    """The problems a fresh process finds in shard `index` of `count` and the cards it verified.

    The process reports its peak memory on standard error, which the caller leaves
    attached so that a run's log records it. A process that ends without a report is
    one problem and not a silent pass: a shard killed for memory must not read as
    verified cards.
    """
    process = subprocess.Popen(
        [sys.executable, "-m", "latticedb.verify_shard"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    assert process.stdin is not None and process.stdout is not None
    output, _ = process.communicate(json.dumps({"root": str(root), "index": index, "count": count}) + "\n")
    verified = 0
    found: list[str] = []
    for line in output.splitlines():
        if not line.strip():
            continue
        reported = json.loads(line)
        if isinstance(reported, str):
            found.append(reported)
        else:
            verified = int(reported["verified"])
    if process.returncode != 0:
        found.append(f"verification of shard {index}/{count} ended with exit status {process.returncode}")
    return verified, found


def report(root: Path) -> tuple[str, ...]:
    """Every problem of the corpus under `root`, one line each."""
    return tuple(run(root)[1])


def peak() -> str:
    """The peak resident memory of this process, as the ceiling the verification needed."""
    return f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.1f} GiB"
