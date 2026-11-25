"""Carry run 42363689427's new failure entries from its sixteen snapshots into the sharded ledger (#20).

    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/carry-run-42363689427-failures.py

The run predates the ledger's split into `failures/<group>.yaml`, so each shard's snapshot holds a
whole `failures.yaml`. The snapshots are commits made from the run's own patches, in the order of
`.scratch/recovery-42363689427/snapshots.txt`; the run's base commit is named below.

An entry the run wrote that the ledger does not hold is added. An entry the ledger already holds keeps
its disposition, which is the newer statement, but every attempt the run recorded that the ledger
does not already hold is added to its history: an attempt is identified by all it records -- hash,
Gram tensor, reason, stderr, duration, time, run URL and revisions -- and never by its position, so a
retry on a different input is a distinct attempt and the same attempt recorded twice is not. Attempts
are ordered by the time they were recorded, so a history stays chronological whichever of the two
recorded the later one.
"""
import subprocess
import sys
from pathlib import Path

import yaml
from pydantic import TypeAdapter

from latticedb import failures

ROOT = Path(__file__).resolve().parent.parent
BASE = "dde534ecd9d7c61af3800d20eb1635bc7541f38a"
SNAPSHOTS = [
    ("0", "794f18ea486199716478eba933de2af99e59a13d"),
    ("1", "402ec19330a9cdf29a430dc803f3588435902d3f"),
    ("2", "ca31ca0cfdde4e974fee2914571a8950cb40e213"),
    ("3", "ca10b320c1127eb1f58c2663a423db60071b99da"),
    ("4", "781b3856b747ee204dd159b3e88debadd98a82ed"),
    ("5", "e9771bbb1bd10151b6a206b5c0cc3cb02e153e08"),
    ("6", "639a22bbee78fff050fb78c41aaefe272a63a37f"),
    ("7", "05fd6bf6a875059b25fdc9a7aec1495f9134ce41"),
    ("8", "cdab7525ec8c1d7f985f0a0a0da7384e57ebf086"),
    ("9", "6bba243ef46d4c671679d16d750343a0c7fd95aa"),
    ("10", "47ed8f7071b8286f371ff810032c259cd4a2d8c9"),
    ("11", "fbfcfaa2507a1041dcd9649d1e58efca951c7e29"),
    ("12", "e64a3fc649a6ae25e877cb034dca453044a6aabe"),
    ("13", "8c042b15221077495dc9b858f4ff02306eed0acc"),
    ("14", "c0f123c2f8097c8e33c26753db9d99fd2bc93ba6"),
    ("15", "47e21ab79b354588abccad812ea1f1b12604682d"),
]


def ledger(rev: str) -> failures.Failures:
    # The last tree holding the whole ledger, which the run's base commit still has.
    text = subprocess.run(["git", "-C", str(ROOT), "show", f"{rev}:failures.yaml"],
                          capture_output=True, text=True, check=True).stdout
    return TypeAdapter(failures.Failures).validate_python(yaml.load(text, Loader=yaml.CSafeLoader) or {})


def attempt_key(attempt: "failures.Attempt") -> str:
    """The identity of one attempt: everything it records, never its position."""
    return attempt.model_dump_json()


def with_every_attempt(current: "failures.Failure", run_entry: "failures.Failure") -> "failures.Failure":
    """The current entry, its disposition kept, plus every attempt of the run it does not already hold.

    A newer disposition is a statement about the computation now; a distinct attempt is a fact about
    what happened. Keeping the first must not delete the second. The history stays chronological, so
    the order is by the time each attempt was recorded.
    """
    attempts = list(current.attempts)
    seen = {attempt_key(attempt) for attempt in attempts}
    for attempt in run_entry.attempts:
        if attempt_key(attempt) not in seen:
            attempts.append(attempt)
            seen.add(attempt_key(attempt))
    attempts.sort(key=lambda attempt: attempt.recorded_at)
    return current.model_copy(update={"attempts": attempts})


def main() -> int:
    base = ledger(BASE)
    current = failures.load(ROOT)
    print(f"base ledger {len(base)} entries; current sharded ledger {len(current)} entries")
    added = kept = same = carried = 0
    for shard, snapshot in SNAPSHOTS:
        entries = ledger(snapshot)
        delta = {key: entry for key, entry in entries.items() if base.get(key) != entry}
        new_here = 0
        for key in sorted(delta):
            entry = delta[key]
            if key not in current:
                current[key] = entry
                added += 1
                new_here += 1
                print(f"shard {shard}: added {key} ({entry.disposition}, {entry.attempts[-1].reason})")
            elif current[key] == entry:
                same += 1
            else:
                merged = with_every_attempt(current[key], entry)
                if merged == current[key]:
                    kept += 1
                    print(f"shard {shard}: {key} already holds every attempt ({current[key].disposition})")
                else:
                    current[key] = merged
                    carried += 1
                    print(f"shard {shard}: added {len(merged.attempts) - len(current[key].attempts)} "
                          f"attempt(s) to {key}, disposition kept as {merged.disposition} "
                          f"(the run's was {entry.disposition}); history now {len(merged.attempts)}")
        print(f"shard {shard}: {len(delta)} entries changed against the base, {new_here} newly added")
    failures.save(ROOT, current)
    written = failures.load(ROOT)
    assert written == current, "the sharded ledger does not hold what was saved"
    print(f"entries added {added}; existing entries given their missing attempts {carried}; "
          f"already holding every attempt {kept}; identical {same}; ledger now {len(written)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
