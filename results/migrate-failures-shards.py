"""Split the single `failures.yaml` ledger into the shards `failures/<group>.yaml` (issue #17).

Run once, from a checkout that still has the ledger:

    PYTHONPATH=src python3 results/migrate-failures-shards.py

It reads every entry (the ledger through `failures.load`, which also reads the legacy file), writes
the shards through `failures.save`, and reports the counts so the split can be checked against the
file it came from. It removes nothing: the ledger leaves the tree as a commit of its own.
"""
import sys
from pathlib import Path

sys.path.insert(0, "src")
from latticedb import failures  # noqa: E402

root = Path(".")
legacy = root / failures.LEGACY
before = failures.load(root)
print(f"ledger: {legacy.exists()} at {legacy.stat().st_size if legacy.exists() else 0} bytes")
print(f"entries read: {len(before)}")
failures.save(root, before)
shards = sorted((root / failures.DIRECTORY).glob("*.yaml"))
print(f"shards written: {len(shards)}, largest {max(path.stat().st_size for path in shards)} bytes")
after = failures.load(root)
assert set(after) == set(before), "the split lost or gained an entry"
assert all(after[key] == before[key] for key in before), "an entry changed in the split"
print("the shards hold exactly the entries the ledger held")
