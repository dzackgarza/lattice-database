"""Durable manual triage of failed certification computations and their retries."""

from __future__ import annotations

import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal

import yaml
from pydantic import Field, TypeAdapter

from latticedb import exceeded, storage
from latticedb.model import Lattice, Record

FILE = "failures.yaml"


class Attempt(Record):
    hash: str
    gram_tensor: list[list[int | str]]
    reason: str
    stderr: str
    seconds: float
    recorded_at: datetime
    run_url: str | None
    database_revision: str | None
    research_revision: str | None


class Failure(Record):
    disposition: Literal["open", "retry", "resolved"]
    attempts: list[Attempt] = Field(min_length=1)
    notes: list[str] = Field(default_factory=list)


Failures = dict[str, Failure]


def load(root: Path) -> Failures:
    path = root / FILE
    if not path.exists():
        return {}
    return TypeAdapter(Failures).validate_python(yaml.load(path.read_text(), Loader=yaml.CSafeLoader) or {})


def save(root: Path, entries: Failures) -> None:
    storage.write_text(root / FILE, yaml.dump({key: value.model_dump() for key, value in sorted(entries.items())}, Dumper=yaml.CSafeDumper, sort_keys=False, allow_unicode=True))


def blocked(entries: Failures, computation: str, lattice: Lattice) -> bool:
    entry = entries.get(computation)
    return entry is not None and entry.disposition == "open" and entry.attempts[-1].hash == exceeded.input_hash(computation, lattice)


def record(root: Path, computation: str, lattice: Lattice, reason: str, stderr: str, seconds: float) -> Failure:
    """Append evidence and quarantine this input immediately, before continuing the queue."""
    assert lattice.gram_tensor is not None, (computation, lattice)
    entries = load(root)
    attempt = Attempt(
        hash=exceeded.input_hash(computation, lattice),
        gram_tensor=[[int(value) if value.denominator == 1 else str(value) for value in row] for row in lattice.gram_tensor],
        reason=reason,
        stderr=stderr,
        seconds=seconds,
        recorded_at=datetime.now(UTC),
        run_url=os.environ.get("LATTICEDB_RUN_URL"),
        database_revision=os.environ.get("LATTICEDB_REVISION"),
        research_revision=os.environ.get("LATTICEDB_RESEARCH_REVISION"),
    )
    entry = entries.get(computation)
    if entry is None:
        entry = Failure(disposition="open", attempts=[attempt])
    else:
        entry = Failure(disposition="open", attempts=[*entry.attempts, attempt], notes=entry.notes)
    entries[computation] = entry
    save(root, entries)
    return entry


def retry(root: Path, computation: str, note: str) -> None:
    """Release one computation after recording the triage decision; retain its history."""
    assert note.strip(), "Record the repair or reason for retrying this computation."
    entries = load(root)
    entry = entries[computation]
    assert entry.disposition == "open", (computation, entry.disposition)
    interruptions = exceeded.load(root)
    interruption = interruptions.get(computation)
    if interruption is not None and interruption.hash == entry.attempts[-1].hash:
        del interruptions[computation]
    exceeded.save(root, interruptions)
    entries[computation] = Failure(disposition="retry", attempts=entry.attempts, notes=[*entry.notes, f"{datetime.now(UTC).isoformat()}: {note}"])
    save(root, entries)


def resolve(root: Path, computation: str, lattice: Lattice) -> None:
    """A completed retry resolves its matching failure while preserving the evidence."""
    entries = load(root)
    entry = entries[computation]
    if entry.attempts[-1].hash == exceeded.input_hash(computation, lattice):
        entries[computation] = Failure(disposition="resolved", attempts=entry.attempts, notes=entry.notes)
        save(root, entries)


def recover(root: Path, lattices: dict[str, Lattice], interruptions: exceeded.Interruptions) -> Failures:
    """Promote prior full-window timeouts and lost workers into the manual queue."""
    entries = load(root)
    for computation, interruption in interruptions.items():
        tag = computation.split(" ", 1)[0]
        lattice = lattices.get(tag)
        if lattice is None or lattice.gram_tensor is None or interruption.hash != exceeded.input_hash(computation, lattice):
            continue
        if interruption.seconds < exceeded.WINDOW_SECONDS and not interruption.lost:
            continue
        entry = entries.get(computation)
        if entry is not None and entry.attempts[-1].hash == interruption.hash:
            continue
        reason = "worker or runner lost" if interruption.lost else "certification budget exhausted"
        entries[computation] = record(root, computation, lattice, f"{reason} (recovered from exceeded.yaml)", "", interruption.seconds)
    return entries
