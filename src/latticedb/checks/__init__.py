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


PROSE_KEYS = frozenset(
    {
        "references",
        "certifications",
        "aliases",
        "name",
        "latex",
        "citation",
        "abstract_structure",
        "description",
        "statement",
        "note",
        "related",
    }
)
"""The fields of a front matter whose strings are prose, a hash or a name, and never a tag, and `related`, which is
read without the other card: a card may be related to thousands and the check is only that each tag is a card.

A citation prints years and theorem numbers, and a tag is four characters from `0-9A-Z`, so reading a citation as a
reference would drag a card in for every numeral that happens to be a tag. Everything else is read as data, so a field
the schemas add later is read too: over-reading a card into a shard costs its memory, and under-reading it would make
its absence read as a reference problem.
"""


def referenced_tags(metadata: dict[str, object], tags: frozenset[str]) -> frozenset[str]:
    """Every lattice tag a record's front matter names, in any field but the prose ones."""
    found: set[str] = set()
    stack: list[object] = [metadata]
    while stack:
        value = stack.pop()
        if isinstance(value, str):
            if value in tags:
                found.add(value)
        elif isinstance(value, dict):
            stack.extend(item for key, item in value.items() if key not in PROSE_KEYS)
        elif isinstance(value, (list, tuple)):
            stack.extend(value)
    return frozenset(found)


CATALOGUE_DIRECTORIES = (
    "arithmetic-groups",
    "geometric-objects",
    "geometric-families",
    "graphs",
    "genera",
    "lattice-polytopes",
    "toric-varieties",
    "geometric-maps",
    "integral-local-systems",
    "picard-fuchs-operators",
    "moduli-problems",
    "lattice-families",
    "lie-groups",
)
"""Every catalogue `corpus.load` reads, in the order it reads them: each is read whole in every shard."""


def shard_closure(root: Path, tags: frozenset[str], cards: tuple[str, ...]) -> tuple[str, ...]:
    """Every card a shard's checks read: its own, and what they and the catalogues name, transitively.

    The checks compare records with the records they name, so a narrowed read has to be closed under naming or the
    absence of a named card reads as a reference problem. The catalogues are read whole in every shard and name the
    lattices they belong to (`arithmetic-groups/`, `geometric-objects/`, `graphs/`, `lattice-families/`), so their
    targets are part of the closure of every shard; a card's own references are read from its front matter, which is
    the same read `corpus.tags` makes. The closure is transitive: a named card naming a third one is loaded, and its
    own references are then checked by this shard as well, harmlessly and in every shard that reads it.
    """
    reached = set(cards)
    frontier = list(cards)
    for directory in CATALOGUE_DIRECTORIES:
        for path in sorted((root / directory).glob("*.md")):
            reached |= referenced_tags(corpus.front_matter(corpus.read_card(path)), tags)
    while frontier:
        tag = frontier.pop()
        path = root / "lattices" / f"{tag}.md"
        if not path.exists():
            continue
        for named in referenced_tags(corpus.front_matter(corpus.read_card(path)), tags):
            if named not in reached:
                reached.add(named)
                frontier.append(named)
    return tuple(sorted(reached & tags))


def one_shard(root: Path, shard: tuple[int, int]) -> tuple[int, list[str]]:
    """Verify the cards whose tag falls in `shard` of the corpus, in this process.

    The read is the shard's closure (`shard_closure`) rather than the corpus: those cards, the cards they and the
    catalogues name, and the certificates of those tags. What the union of the shards therefore checks is what one
    corpus-wide run checks, with two exceptions stated here rather than silently lost: a duplicate *Gram tensor* is
    still corpus-wide, read from the durable index (`records.duplicate_gram_problems`), while a duplicate *name* and
    a `hyperbolic_index` bound a morphism of another shard's card would supply are seen only within a shard's closure.
    """
    tags = frozenset(corpus.tags(root))
    cards = tuple(sorted(tag for tag in tags if genus.in_shard(tag, shard)))
    closure = shard_closure(root, tags, cards)
    loaded = corpus.load(root, tags=closure)
    held = certificates.load(root, tags=closure)
    selected = frozenset(cards)
    problems = [
        *records.duplicate_gram_problems(root, loaded, selected),
        *records.problems(loaded, held, selected),
        *relations.problems(loaded, root, selected, tags),
        *catalogues.problems(loaded),
    ]
    return len(selected), problems


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
