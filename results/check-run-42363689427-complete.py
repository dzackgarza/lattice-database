"""Every value, certificate and diagnostic run 42363689427 completed is present on main (#20).

    python3 results/check-run-42363689427-complete.py            # pure YAML and git, no image

The run's sixteen per-shard patches are read through commits made from them, each against the run's
own base commit dde534ecd9. For each snapshot, only the field paths it actually *changed* against
that base are considered: a field the run did not touch is not this check's business, and asking the
corpus to equal an old snapshot would make every later correction look like a loss.

Three outcomes per changed path, and nothing else:

    PRESENT   main holds exactly what the run computed -- `recovery_comparison.same`, which is
              position-exact for lists (a reordered Gram row, a permuted morphism matrix or a lost
              duplicate coefficient is a difference) and key-exact for mappings.
    DIFFERENT main holds another value for the same field. Never silently accepted: each such path
              must be named in `results/evidence-20-supersessions.yaml` with the reason it is a
              later, reviewed statement, and is then counted as a supersession.
    ABSENT    main has no such value at all. This is the failure the check exists for.

Certificates are compared as the pair they are: a shard entry for a computation name is exactly
`{hash, by}`, and the hash means something only against the field projection and Gram tensor it was
computed from. That pairing is checked by `results/verify-run-42363689427.py`, which runs the
repository's own `checks.records.problems` -- on the current tree, and with `--revision` on each
snapshot's own cards and certificate shards. This script checks presence, not pairing.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml
from pydantic import TypeAdapter

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from recovery_comparison import MISSING, at, changed_leaves, same  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BASE = "dde534ecd9d7c61af3800d20eb1635bc7541f38a"
SUPERSESSIONS = ROOT / "results" / "evidence-20-supersessions.yaml"
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
CACHE: dict[tuple[str, str], str | None] = {}


def fetch(rev: str, paths: list[str]) -> None:
    """Read `paths` at `rev` in one `git cat-file --batch`, not one process per path."""
    wanted = [path for path in paths if (rev, path) not in CACHE]
    if not wanted:
        return
    done = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "--batch"],
        input="".join(f"{rev}:{path}\n" for path in wanted).encode(), capture_output=True, check=True,
    ).stdout
    position = 0
    for path in wanted:
        end = done.index(b"\n", position)
        header = done[position:end].decode()
        position = end + 1
        if header.endswith("missing"):
            CACHE[(rev, path)] = None
            continue
        size = int(header.split()[-1])
        CACHE[(rev, path)] = done[position:position + size].decode()
        position += size + 1


def text(rev: str, path: str) -> str | None:
    fetch(rev, [path])
    return CACHE[(rev, path)]


def front_matter(document: str) -> dict:
    return yaml.load(document.split("---", 2)[1], Loader=yaml.CSafeLoader) or {}


def mapping(document: str | None) -> dict:
    return (yaml.load(document, Loader=yaml.CSafeLoader) or {}) if document else {}


def main() -> int:
    from latticedb import failures

    reviewed = mapping(SUPERSESSIONS.read_text()) if SUPERSESSIONS.exists() else {}
    present = superseded = 0
    absent: list[str] = []
    unreviewed: list[str] = []
    differing: list[str] = []
    held = failures.load(ROOT)
    for shard, snapshot in SNAPSHOTS:
        paths = subprocess.run(["git", "-C", str(ROOT), "diff", "--name-only", BASE, snapshot],
                               capture_output=True, text=True, check=True).stdout.split()
        fetch(snapshot, paths)
        fetch(BASE, paths)
        cards = [path for path in paths if path.startswith("lattices/") and path.endswith(".md")]
        maps = [path for path in paths if path.startswith("certificates/") or path == "exceeded.yaml"]
        shard_present = shard_superseded = 0
        for path in cards:
            after, before = text(snapshot, path), text(BASE, path)
            if after is None:
                continue
            current_path = ROOT / path
            if not current_path.exists():
                absent.append(f"{path}: the card the run certified is gone")
                continue
            current = front_matter(current_path.read_text())
            for field, wanted in changed_leaves(front_matter(before) if before else {}, front_matter(after)).items():
                got = at(current, field)
                key = f"{path}: {field}"
                if got is MISSING:
                    absent.append(key)
                elif same(got, wanted):
                    present += 1
                    shard_present += 1
                else:
                    differing.append(f"{key} -- run: {str(wanted)[:70]!r} / main: {str(got)[:70]!r}")
                    if key in reviewed:
                        superseded += 1
                        shard_superseded += 1
                    else:
                        unreviewed.append(key)
        for path in maps:
            after, before = mapping(text(snapshot, path)), mapping(text(BASE, path))
            current = mapping((ROOT / path).read_text()) if (ROOT / path).exists() else {}
            for name, wanted in changed_leaves(before, after).items():
                got = at(current, name)
                key = f"{path}: {name}"
                if got is MISSING:
                    absent.append(key)
                elif same(got, wanted):
                    present += 1
                    shard_present += 1
                else:
                    differing.append(f"{key} -- run: {str(wanted)[:70]!r} / main: {str(got)[:70]!r}")
                    if key in reviewed:
                        superseded += 1
                        shard_superseded += 1
                    else:
                        unreviewed.append(key)
        run_entries = TypeAdapter(failures.Failures).validate_python(mapping(text(snapshot, "failures.yaml")))
        base_entries = TypeAdapter(failures.Failures).validate_python(mapping(text(BASE, "failures.yaml")))
        for name, wanted in run_entries.items():
            if base_entries.get(name) == wanted:
                continue
            key = f"failures: {name}"
            got = held.get(name)
            if got is None:
                absent.append(key)
            elif got == wanted:
                present += 1
            else:
                differing.append(f"{key} -- run: {wanted.disposition} / main: {got.disposition}")
                if key in reviewed:
                    superseded += 1
                else:
                    unreviewed.append(key)
        print(f"shard {shard:>2}: {len(cards)} cards, {len(maps)} map files, "
              f"{shard_present} present, {shard_superseded} superseded", flush=True)
    for problem in absent:
        print("ABSENT:", problem)
    for problem in differing:
        print("DIFFERENT:", problem)
    for problem in unreviewed:
        print("UNREVIEWED:", problem)
    print(f"\n{present} changed paths present exactly, {superseded} reviewed supersessions, "
          f"{len(differing)} differing ({len(unreviewed)} unreviewed), {len(absent)} absent")
    return 1 if absent or unreviewed else 0


if __name__ == "__main__":
    raise SystemExit(main())
