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
