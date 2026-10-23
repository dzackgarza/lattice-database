"""Failed computations remain reproducible and quarantined until explicitly released."""

from __future__ import annotations

import shutil
import sys
import time
from pathlib import Path

import pytest
import yaml

from latticedb import certificates, corpus, genus

REPOSITORY = Path(__file__).resolve().parent.parent


def specimen_certificates() -> certificates.Certificates:
    path = REPOSITORY / "certificates" / f"{certificates.group('0012')}.yaml"
    stored = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
    return {key: certificates.Certificate.model_validate(value) for key, value in stored.items() if key.startswith("0012 ")}


def specimen(root: Path) -> corpus.Corpus:
    (root / "lattices").mkdir()
    shutil.copy(REPOSITORY / "lattices/0012.md", root / "lattices/0012.md")
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, root / corpus.FAMILIES_FILE)
    (root / corpus.RETIRED_FILE).write_text("{}\n")
    return corpus.load(root)


def test_worker_startup_failure_is_persisted_and_requires_explicit_retry(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    loaded = specimen(tmp_path)
    # A missing worker module is a real subprocess startup failure, before any
    # mathematical operation starts. Its stderr must survive outside the CI log.
    monkeypatch.setattr(genus, "WORKER", [sys.executable, "-m", "latticedb.unavailable_worker"])
    monkeypatch.setenv("LATTICEDB_RUN_URL", "https://github.com/dzackgarza/lattice-database/actions/runs/39753434335")
    with pytest.raises(ChildProcessError):
        genus.certify(tmp_path, loaded, {}, (), time.time() + 30)
    assert (tmp_path / "failures.yaml").exists(), "worker failure was discarded instead of queued for triage"

    from latticedb import failures

    queued = failures.load(tmp_path)["0012 worker"]
    assert queued.disposition == "open"
    assert "latticedb.unavailable_worker" in queued.attempts[-1].stderr
    assert queued.attempts[-1].run_url.endswith("/39753434335")
    assert queued.attempts[-1].gram_tensor == [[2, -1], [-1, 2]]
    # A second nightly run must leave the failed input alone.
    genus.certify(tmp_path, loaded, {}, (), time.time() + 30)
    assert len(failures.load(tmp_path)["0012 worker"].attempts) == 1
    failures.retry(tmp_path, "0012 worker", "Reproduce the startup error after repairing the worker environment.")
    with pytest.raises(ChildProcessError):
        genus.certify(tmp_path, loaded, {}, (), time.time() + 30)
    repeated = failures.load(tmp_path)["0012 worker"]
    assert repeated.disposition == "open"
    assert len(repeated.attempts) == 2
    assert "repairing the worker environment" in repeated.notes[-1]


def test_failed_operation_is_quarantined_by_input_without_blocking_other_work(tmp_path: Path) -> None:
    from latticedb import exceeded, failures

    loaded = specimen(tmp_path)
    lattice = loaded.entries[0].lattice
    held = {key: value for key, value in specimen_certificates().items() if key.endswith(" derive")}
    computation = genus.name("0012", "discriminant_sequence")
    failures.record(tmp_path, computation, lattice, "memory exhausted", "Unable to allocate 21.7 GiB", 42)
    requested = genus.requests(loaded, held, {}, (), failed=failures.load(tmp_path))
    fields = {field for request in requested for field in request["fields"]}
    assert "discriminant_sequence" not in fields
    assert "genus_class_count" in fields
    changed = lattice.model_copy(update={"gram_tensor": ((4, -2), (-2, 4))})
    assert not failures.blocked(failures.load(tmp_path), computation, changed)

    exceeded.save(tmp_path, {computation: exceeded.Interruption(hash=exceeded.input_hash(computation, lattice), seconds=18001)})
    failures.retry(tmp_path, computation, "Preamble implementation now uses less memory.")
    assert computation not in exceeded.load(tmp_path)
    fields = {field for request in genus.requests(loaded, held, exceeded.load(tmp_path), (), failed=failures.load(tmp_path)) for field in request["fields"]}
    assert "discriminant_sequence" in fields
    failures.resolve(tmp_path, computation, lattice)
    resolved = failures.load(tmp_path)[computation]
    assert resolved.disposition == "resolved"
    assert resolved.attempts[-1].reason == "memory exhausted"


def test_successful_retry_computes_and_resolves_its_failure(tmp_path: Path) -> None:
    from latticedb import failures

    loaded = specimen(tmp_path)
    lattice = loaded.entries[0].lattice
    held = specimen_certificates()
    computation = genus.name("0012", "integer_valued")
    held.pop(computation)
    failures.record(tmp_path, computation, lattice, "exit status 1", "Previous worker environment failed.", 1)
    failures.retry(tmp_path, computation, "Run the real preamble operation in the repaired environment.")
    genus.certify(tmp_path, loaded, held, ("0012",), time.time() + 30)
    entry = failures.load(tmp_path)[computation]
    assert entry.disposition == "resolved"
    assert len(entry.attempts) == 1
    assert entry.notes
    stored = corpus.front_matter(corpus.read_card(tmp_path / "lattices/0012.md"))
    assert stored["form"]["integer_valued"] is True
    assert stored["certifications"]["form.integer_valued"] == certificates.load(tmp_path)[computation].hash


def test_previous_timeouts_and_lost_workers_enter_manual_triage(tmp_path: Path) -> None:
    from latticedb import exceeded, failures

    loaded = specimen(tmp_path)
    lattice = loaded.entries[0].lattice
    timeout = genus.name("0012", "discriminant_sequence")
    lost = genus.name("0012", "genus_class_count")
    exceeded.save(tmp_path, {
        timeout: exceeded.Interruption(hash=exceeded.input_hash(timeout, lattice), seconds=18241),
        lost: exceeded.Interruption(hash=exceeded.input_hash(lost, lattice), seconds=30, lost=True),
    })
    # No process needs to run to recover an already committed interruption.
    genus.certify(tmp_path, loaded, {}, (), time.time())
    queued = failures.load(tmp_path)
    assert set(queued) == {timeout, lost}
    assert all(entry.disposition == "open" for entry in queued.values())
    assert queued[timeout].attempts[-1].seconds == 18241
    assert "exceeded.yaml" in queued[lost].attempts[-1].reason


def test_a_later_completed_certificate_resolves_recovered_failure(tmp_path: Path) -> None:
    from latticedb import failures

    loaded = specimen(tmp_path)
    lattice = loaded.entries[0].lattice
    computation = genus.name("0012", "integer_valued")
    failures.record(tmp_path, computation, lattice, "worker or runner lost", "", 60)
    # Another runner may finish before the triage-ledger repair is deployed.
    genus.certify(tmp_path, loaded, specimen_certificates(), ("0012",), time.time())
    assert failures.load(tmp_path)[computation].disposition == "resolved"
