"""Computations that a certification job ended before they finished.

`exceeded.yaml` maps the name of a computation to the hash of that name and the
Gram tensor, with the seconds the computation had run when its job ended.

Certification writes zero elapsed seconds when a computation starts, checkpoints
its actual elapsed time every thirty seconds, and deletes it when it finishes.
Graceful termination writes a final checkpoint; a hard kill retains the latest
checkpoint. An entry that remains records unfinished work and its elapsed time. A computation that ran for at least `WINDOW_SECONDS` does not fit in
one job: certification holds it for manual triage. A computation that ran for less
was interrupted or started late, and the next job computes it first.

Entries are `lost` from the start of their computation until the job's final
checkpoint, and the job pushes its progress while it runs. An entry that is
still lost was running when its runner died; the next certification run recovers
it into the manual failure ledger before scheduling work.

A computation the run ended itself is a cost the same log records, not an error
that ends the run: when a worker is killed rather than returning a value or an
error, its entry also states what ended it (`killed_by`) and, when the run
measured them, the memory the worker held (`peak_bytes`) and the floor the run
keeps available (`limit_bytes`). The key names the card and the stage, as
`<tag> <stage>`, and `worker` is the stage of a worker that died before it
announced one.

The log is permanent. A changed Gram tensor changes the hash, so the entry no
longer applies. After a repair or an investigation that justifies retrying, use
``retry-computation`` to record the decision and release the matching input.
"""

from pathlib import Path

import yaml
from pydantic import Field, TypeAdapter

from latticedb import certificates, storage
from latticedb.model import Lattice, Record

EXCEEDED_FILE = "exceeded.yaml"

WINDOW_SECONDS = 5 * 60 * 60
"""The least running time that shows a computation does not fit in one job.

The certification workflow gives a job 330 minutes, so a computation that starts
first in its job runs for more than this before the timeout ends it.
"""


class Interruption(Record):
    hash: str = Field(description="SHA-256 digest of the computation name and Gram tensor.")
    seconds: int = Field(description="Seconds the computation had run when its job ended.")
    lost: bool = Field(default=False, description="Whether the runner died while the computation ran, so that it may have ended the job.")
    killed_by: str | None = Field(
        default=None,
        description="What ended the worker instead of a stored value or a raised error: `memory` when the run killed it to keep its memory floor, otherwise the signal that killed it. Absent when the job's own budget ended the run.",
    )
    peak_bytes: int | None = Field(
        default=None,
        description="Resident memory of the worker's process group when the run killed it for memory. Absent unless the run measured it, as it does when choosing the worker to kill.",
    )
    limit_bytes: int | None = Field(
        default=None,
        description="The memory the run keeps available to the machine; below it the run kills the worker holding the most.",
    )


Interruptions = dict[str, Interruption]


def load(root: Path) -> Interruptions:
    path = root / EXCEEDED_FILE
    if not path.exists():
        return {}
    return TypeAdapter(Interruptions).validate_python(yaml.load(path.read_text(), Loader=yaml.CSafeLoader) or {})


def save(root: Path, log: Interruptions) -> None:
    data = {name: entry.model_dump(exclude_defaults=True) for name, entry in sorted(log.items())}
    storage.write_text(root / EXCEEDED_FILE, yaml.dump(data, Dumper=yaml.CSafeDumper, sort_keys=False, allow_unicode=True))


def input_hash(name: str, lattice: Lattice) -> str:
    """Commit to one computation name and Gram tensor."""
    return certificates.certification_hash(name, lattice, None)


def seconds_run(log: Interruptions, name: str, lattice: Lattice) -> int | None:
    """The seconds this computation ran before a job ended it, if one did."""
    entry = log.get(name)
    if entry is None or entry.hash != input_hash(name, lattice):
        return None
    return entry.seconds


def was_lost(log: Interruptions, name: str, lattice: Lattice) -> bool:
    """Whether this computation was running when its runner died."""
    entry = log.get(name)
    return entry is not None and entry.lost and entry.hash == input_hash(name, lattice)


def is_exceeded(log: Interruptions, name: str, lattice: Lattice) -> bool:
    """Whether this computation ran for a whole job without finishing."""
    seconds = seconds_run(log, name, lattice)
    return seconds is not None and seconds >= WINDOW_SECONDS


def reason(interruption: Interruption) -> str:
    """What ended this computation, in the words the triage ledger records.

    A killed worker is named by what the run observed of it: the memory it held
    when the run killed it, the floor the run keeps available, or the signal
    that ended it. An entry that names no kill was ended by the job's budget.
    """
    if interruption.killed_by is None:
        return "worker or runner lost" if interruption.lost else "certification budget exhausted"
    if interruption.killed_by == "memory":
        held = "" if interruption.peak_bytes is None else f" at {interruption.peak_bytes / 2**30:.1f} GiB"
        floor = "" if interruption.limit_bytes is None else f" while the run kept {interruption.limit_bytes / 2**30:.1f} GiB free"
        return f"memory exhausted{held}{floor}"
    return f"worker killed by {interruption.killed_by}"
