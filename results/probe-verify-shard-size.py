"""The gate's shard: how many cards a shard names, and what reading them costs.

`checks.one_shard` reads the whole corpus and every certificate, which this VM cannot hold (#6 records the same for
the runner). This measures the alternative — the shard's own cards plus the cards they name — before any check is
rewired to it.

    .scratch/wt43d-run.sh -u results/probe-verify-shard-size.py [shard]
"""

import resource
import sys
import time
from pathlib import Path

from latticedb import certificates, corpus, genus

ROOT = Path("/repo")
INDEX = int(sys.argv[1]) if len(sys.argv) > 1 else 0
COUNT = 16
start = time.time()


def peak() -> str:
    return f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.2f} GiB"


tags = corpus.tags(ROOT)
shard = tuple(tag for tag in tags if genus.in_shard(tag, (INDEX, COUNT)))
print(f"[{time.time() - start:6.1f}s] {len(tags)} tags, {len(shard)} in shard {INDEX}/{COUNT}; peak {peak()}", flush=True)


def named(metadata: dict) -> set[str]:
    """Every tag a card names: its morphism targets and the cards it says it is related to."""
    found = set()
    for morphism in metadata.get("morphisms") or []:
        target = morphism.get("target") if isinstance(morphism, dict) else None
        if isinstance(target, str):
            found.add(target)
    for related in metadata.get("related") or []:
        if isinstance(related, str):
            found.add(related)
    return found


closure = set(shard)
for tag in shard:
    metadata = corpus.front_matter(corpus.read_card(ROOT / "lattices" / f"{tag}.md"))
    closure |= named(metadata)
print(f"[{time.time() - start:6.1f}s] the shard names {len(closure) - len(shard)} further cards; peak {peak()}", flush=True)

loaded = corpus.cards(ROOT, sorted(closure))
print(f"[{time.time() - start:6.1f}s] read {len(loaded.entries)} cards; peak {peak()}", flush=True)
held = certificates.load(ROOT, tags=sorted(closure))
print(f"[{time.time() - start:6.1f}s] read {len(held)} certificates; peak {peak()}", flush=True)
print(f"RESULT: shard {INDEX}/{COUNT}: {len(shard)} cards, closure {len(closure)}, certificates {len(held)}, peak {peak()}", flush=True)
