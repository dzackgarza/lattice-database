"""#43: the stored checks of card 029J alone, through the corpus's own tagged readers.

`latticedb verify --shard 0/16` is one process that loads every card and every certificate
(`latticedb/checks/__init__.py:64`-`:65` -> `corpus.load` -> `certificates.load`), which the
repository measures at 7.29 GiB and 9.08 GiB and this VM cannot hold; the tagged readers `#30`
added are what a per-tag request may use instead (`corpus.cards`, `certificates.load(tags=...)`).
This runs the same checks on the one card this issue is about, so a green line here is a
statement about 029J and not about the corpus.

    .scratch/wt-run.sh results/verify-43-scoped.py
"""

from pathlib import Path

from latticedb import certificates, corpus
from latticedb.checks import catalogues, records, relations

ROOT = Path("/repo")
TAGS = ("029J", "6JRR")
GROUPS = ("o-t-en", "so-t-en", "o-plus-t-en", "so-plus-t-en", "otilde-t-en",
          "sotilde-t-en", "otilde-plus-t-en", "sotilde-plus-t-en", "gamma-en-2")
"""The arithmetic-group cards of 029J, whose certificates carry its indices."""

loaded = corpus.cards(ROOT, TAGS)
held = certificates.load(ROOT, tags=(*TAGS, *GROUPS))
cards = frozenset(entry.lattice.tag for entry in loaded.entries)
problems = [
    *records.shared_gram_problems(loaded),
    *records.problems(loaded, held, cards),
    *relations.problems(loaded, root=ROOT, cards=cards),
    *catalogues.problems(loaded),
]
print(f"cards read: {sorted(cards)}")
print(f"certificate groups read: {len(held)}")
print(f"arithmetic-group certificates asked for: {GROUPS}")
print(f"problems: {len(problems)}")
for problem in problems:
    print(" -", problem)
