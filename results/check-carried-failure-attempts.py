"""Does the carried ledger hold every attempt run 42363689427 recorded, not just its disposition? (#20)

    PYTHONPATH=src python3 results/check-carried-failure-attempts.py

An entry can change for two independent reasons: the run recorded one more attempt at a computation
whose entry the ledger already had (so the ledger's disposition may still be the newer statement),
or it recorded a computation the ledger never had. Keeping the newer disposition must not discard a
distinct attempt. This compares attempt by attempt: an attempt is identified by everything it
records -- hash, Gram tensor, reason, stderr, seconds, time, run URL and revisions -- not by index,
because the same computation can be retried with a different input.
"""
import subprocess
import sys
from pathlib import Path

import yaml
from pydantic import TypeAdapter

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from latticedb import failures  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BASE = "dde534ecd9d7c61af3800d20eb1635bc7541f38a"
SNAPSHOTS = [
    ("0", "794f18ea486199716478eba933de2af99e59a13d"), ("1", "402ec19330a9cdf29a430dc803f3588435902d3f"),
    ("2", "ca31ca0cfdde4e974fee2914571a8950cb40e213"), ("3", "ca10b320c1127eb1f58c2663a423db60071b99da"),
    ("4", "781b3856b747ee204dd159b3e88debadd98a82ed"), ("5", "e9771bbb1bd10151b6a206b5c0cc3cb02e153e08"),
    ("6", "639a22bbee78fff050fb78c41aaefe272a63a37f"), ("7", "05fd6bf6a875059b25fdc9a7aec1495f9134ce41"),
    ("8", "cdab7525ec8c1d7f985f0a0a0da7384e57ebf086"), ("9", "6bba243ef46d4c671679d16d750343a0c7fd95aa"),
    ("10", "47ed8f7071b8286f371ff810032c259cd4a2d8c9"), ("11", "fbfcfaa2507a1041dcd9649d1e58efca951c7e29"),
    ("12", "e64a3fc649a6ae25e877cb034dca453044a6aabe"), ("13", "8c042b15221077495dc9b858f4ff02306eed0acc"),
    ("14", "c0f123c2f8097c8e33c26753db9d99fd2bc93ba6"), ("15", "47e21ab79b354588abccad812ea1f1b12604682d"),
]


def ledger(rev: str) -> failures.Failures:
    text = subprocess.run(["git", "-C", str(ROOT), "show", f"{rev}:failures.yaml"],
                          capture_output=True, text=True, check=True).stdout
    return TypeAdapter(failures.Failures).validate_python(yaml.load(text, Loader=yaml.CSafeLoader) or {})


def key(attempt: failures.Attempt) -> str:
    return attempt.model_dump_json()


def main() -> int:
    base = ledger(BASE)
    held = failures.load(ROOT)
    checked = missing_attempts = missing_entries = 0
    for shard, snapshot in SNAPSHOTS:
        entries = ledger(snapshot)
        shard_checked = shard_missing = 0
        for name, entry in entries.items():
            if base.get(name) == entry:
                continue
            checked += 1
            shard_checked += 1
            current = held.get(name)
            if current is None:
                missing_entries += 1
                shard_missing += 1
                print(f"shard {shard}: ABSENT entry {name}")
                continue
            present = {key(attempt) for attempt in current.attempts}
            for attempt in entry.attempts:
                if key(attempt) not in present:
                    missing_attempts += 1
                    shard_missing += 1
                    print(f"shard {shard}: {name} lacks the attempt {attempt.recorded_at} "
                          f"({attempt.reason}); ledger has {len(current.attempts)}, the run had {len(entry.attempts)}")
        print(f"shard {shard}: {shard_checked} changed entries checked, {shard_missing} without every attempt", flush=True)
    print(f"\n{checked} changed entries checked; {missing_entries} absent, {missing_attempts} attempts not carried")
    return 1 if missing_entries or missing_attempts else 0


if __name__ == "__main__":
    raise SystemExit(main())
