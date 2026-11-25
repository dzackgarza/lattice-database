"""Split the single `failures.yaml` ledger into the shards `failures/<group>.yaml` (issue #17).

Run once, from a checkout that still has the ledger, naming it:

    PYTHONPATH=src python3 results/migrate-failures-shards.py failures.yaml

It reads every entry of that file, writes the shards through `failures.save`, and checks that the
shards hold exactly the entries the file held. The ledger is not a reader's format: `failures.load`
reads the shards, and this script is the only thing that reads the single file.
"""
import sys
from pathlib import Path

import yaml
from pydantic import TypeAdapter

sys.path.insert(0, "src")
from latticedb import failures  # noqa: E402

root = Path(".")
legacy = Path(sys.argv[1] if len(sys.argv) > 1 else "failures.yaml")
before = TypeAdapter(failures.Failures).validate_python(yaml.load(legacy.read_text(), Loader=yaml.CSafeLoader) or {})
print(f"ledger: {legacy} at {legacy.stat().st_size} bytes")
print(f"entries read: {len(before)}")
failures.save(root, before)
shards = sorted((root / failures.DIRECTORY).glob("*.yaml"))
print(f"shards written: {len(shards)}, largest {max(path.stat().st_size for path in shards)} bytes")
after = failures.load(root)
assert set(after) == set(before), "the split lost or gained an entry"
assert all(after[key] == before[key] for key in before), "an entry changed in the split"
print("the shards hold exactly the entries the ledger held")
