"""Real process interruption preserves the certification queue's restart contract."""

from __future__ import annotations

import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest
import yaml

from latticedb import certificates, corpus, exceeded, failures, genus

REPOSITORY = Path(__file__).resolve().parent.parent


def prepare_card(root: Path, tag: str) -> Path:
    (root / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, root / corpus.FAMILIES_FILE)
    (root / corpus.RETIRED_FILE).write_text("{}\n")
    target = root / "lattices" / f"{tag}.md"
    shutil.copy(REPOSITORY / "lattices" / f"{tag}.md", target)
    return target


def hold_certificates(root: Path, tag: str, withhold: tuple[str, ...] = ()) -> None:
    """Copy the certificates this corpus holds for `tag` into the fixture's root.

    A copy of the card alone leaves every field of it pending, so the run recomputes
    them all before it reaches a search; the fixture holds the card's certificates, as
    `tests/test_catalogue_schemas.py` does (#34), and the searches are what is left.

    `withhold` names computations whose certificates the fixture leaves out, which is the state
    an interrupted run leaves: the card certified everywhere else and that computation uncomputed
    (#42).
    """
    held = {
        name: certificate
        for name, certificate in certificates.load(REPOSITORY, tags=[tag]).items()
        if name.split(" ", 1)[0] == tag and name not in withhold
    }
    certificates.save(root, held, tags=[tag])


def test_an_early_termination_does_not_blacklist_a_computation_for_a_whole_job(tmp_path: Path) -> None:
    prepare_card(tmp_path, "0016")
    # The roots of U span an index-two sublattice. The preamble's semi-decision
    # for roots generating all of U therefore keeps searching until interrupted.
    computation = genus.name("0016", "roots")
    # The corpus certifies what it can, so the two searches this test cuts are withheld from the
    # fixture: by 2026-11-18 the shard held both of them for 0016, and a run with nothing left to
    # ask exits before it reaches the search the test interrupts (run 44392454284).
    hold_certificates(tmp_path, "0016", withhold=(computation, genus.name("0016", "norms")))
    command = [sys.executable, "-m", "latticedb", "certify", "--minutes", "330", "--tag", "0016", "--root", str(tmp_path)]
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, start_new_session=True) as process:
        try:
            wait_until = time.monotonic() + 60
            while time.monotonic() < wait_until:
                if (tmp_path / exceeded.EXCEEDED_FILE).exists() and computation in exceeded.load(tmp_path):
                    break
                if process.poll() is not None:
                    output, _ = process.communicate()
                    raise AssertionError(f"certification ended before the requested computation started:\n{output}")
                time.sleep(0.01)
            else:
                raise AssertionError("certification did not announce the root search")
            os.killpg(process.pid, signal.SIGTERM)
            output, _ = process.communicate(timeout=30)
            assert process.returncode != 0, output
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate(timeout=30)

    loaded = corpus.load(tmp_path)
    lattice = loaded.entries[0].lattice
    interruptions = exceeded.load(tmp_path)
    assert not exceeded.is_exceeded(interruptions, computation, lattice)
    # The job ended it, not the death of its runner.
    assert not exceeded.was_lost(interruptions, computation, lattice)
    requested = genus.requests(loaded, certificates.load(tmp_path), interruptions, ("0016",))
    # The semi-decisions are a request of their own, after the fields that every procedure
    # returns (#14), so the search the job cut is the card's searches request.
    searches = next(request for request in requested if request.get("searches"))
    assert {"roots", "norms"} <= set(searches["fields"])


def test_finishing_a_previously_interrupted_computation_clears_its_log(tmp_path: Path) -> None:
    """An interruption record is cleared by the run that finishes its computation.

    #42: the fixture is the state an interrupted run leaves — 0012 certified everywhere except the
    one computation whose record `exceeded.yaml` holds — and the budget covers a worker's start plus
    that computation, which is about 10 s here. With the card's other certificates absent the run
    recomputes its 24 fields at about 5.5 s each; the budget then ends it inside a later field
    (`integral.modular_scale` started at 89 s of a 60 s budget, measured), and that field's record
    correctly stays, because the run did start it and did not finish it.
    """
    prepare_card(tmp_path, "0012")
    loaded = corpus.load(tmp_path)
    lattice = loaded.entries[0].lattice
    computation = genus.name("0012", "genus_class_count")
    hold_certificates(tmp_path, "0012", withhold=(computation,))
    exceeded.save(tmp_path, {computation: exceeded.Interruption(hash=exceeded.input_hash(computation, lattice), seconds=1)})
    # The card's other values are certified and this one is pending, so the queue asks for it alone.
    assert [request["fields"] for request in genus.requests(loaded, certificates.load(tmp_path), exceeded.load(tmp_path), ("0012",))] == [["genus_class_count"]]
    genus.certify(tmp_path, loaded, certificates.load(tmp_path), ("0012",), time.time() + 300)
    assert exceeded.load(tmp_path) == {}
    assert computation in certificates.load(tmp_path)


def test_an_interrupted_certificate_write_preserves_completed_certificates(tmp_path: Path) -> None:
    held = {"0012 derive": certificates.Certificate(hash="b" * 64, by="previous computation")}
    certificates.save(tmp_path, held)
    group = tmp_path / certificates.CERTIFICATES_DIR / f"{certificates.group('0012')}.yaml"
    before = group.read_bytes()
    result = subprocess.run([sys.executable, str(REPOSITORY / "tests/fixtures/interrupted_certificate_write.py"), str(tmp_path)], capture_output=True, text=True)
    assert result.returncode == 27, result.stderr
    assert group.read_bytes() == before
    assert certificates.load(tmp_path) == held
    assert list((tmp_path / certificates.CERTIFICATES_DIR).iterdir()) == [group]


def test_a_search_that_never_ends_does_not_hold_back_other_cards(tmp_path: Path) -> None:
    prepare_card(tmp_path, "0016")
    shutil.copy(REPOSITORY / "lattices" / "0012.md", tmp_path / "lattices")
    loaded = corpus.load(tmp_path)
    lattices = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    # A cut root search on U is resumed first; its semi-decision never returns.
    log = {genus.name("0016", field): exceeded.Interruption(hash=exceeded.input_hash(genus.name("0016", field), lattices["0016"]), seconds=60) for field in ("roots", "norms")}
    exceeded.save(tmp_path, log)
    genus.certify(tmp_path, loaded, {}, (), time.time() + 150, workers=2)
    held = certificates.load(tmp_path)
    assert genus.name("0012", "genus_symbol") in held
    assert genus.name("0016", "roots") in exceeded.load(tmp_path)


def test_certificates_are_saved_in_the_groups_of_their_tags(tmp_path: Path) -> None:
    held = {
        "0012 derive": certificates.Certificate(hash="a" * 64, by="computed"),
        "3999 derive": certificates.Certificate(hash="b" * 64, by="computed"),
    }
    certificates.save(tmp_path, held)
    directory = tmp_path / certificates.CERTIFICATES_DIR
    names = {certificates.group("0012") + ".yaml", certificates.group("3999") + ".yaml"}
    assert {path.name for path in directory.iterdir()} == names
    held["0013 derive"] = certificates.Certificate(hash="c" * 64, by="computed")
    other = directory / f"{certificates.group('3999')}.yaml"
    untouched = other.stat().st_mtime_ns
    # A checkpoint names the cards that changed, and rewrites only their groups.
    certificates.save(tmp_path, held, {"0013"})
    assert other.stat().st_mtime_ns == untouched
    assert certificates.load(tmp_path) == held
    del held["3999 derive"]
    certificates.save(tmp_path, held)
    assert "3999 derive" not in certificates.load(tmp_path)


def test_no_two_shards_write_the_same_certificate_group() -> None:
    tags = [f"{number:04d}" for number in range(1, 4000)]
    owners: dict[str, set[int]] = {}
    for tag in tags:
        shard = next(index for index in range(16) if genus.in_shard(tag, (index, 16)))
        owners.setdefault(certificates.group(tag), set()).add(shard)
    assert all(len(shards) == 1 for shards in owners.values())


KILLED_WORKER = """
import json, sys, time
request = json.loads(sys.stdin.readline())
print(json.dumps({"tag": request["tag"], "started": [request["fields"][0]]}), flush=True)
time.sleep(60)
"""


def test_a_computation_killed_for_memory_records_its_cost_instead_of_raising(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """#46: a worker the run kills is a recorded cost, not the exception that ended the run.

    The kill is driven at the boundary the driver sees: a worker that announces its stage
    and does not return, under a memory reserve the machine can never meet (#2 of #46 asks
    for this). The real worker cannot be made to exhaust a runner's memory in a fast test,
    and the driver is not given a smaller limit for one run here.
    """
    prepare_card(tmp_path, "0012")
    worker = tmp_path / "worker.py"
    worker.write_text(KILLED_WORKER)
    monkeypatch.setattr(genus, "WORKER", [sys.executable, str(worker)])
    # A reserve above the machine's memory is never available, so the worker is killed at once.
    monkeypatch.setattr(genus, "MEMORY_RESERVE", 2.0)
    loaded = corpus.load(tmp_path)
    lattice = loaded.entries[0].lattice
    first = genus.requests(loaded, {}, {}, ())[0]["fields"][0]
    computation = genus.name("0012", first)
    before = (tmp_path / "lattices/0012.md").read_bytes()
    # The run ends without raising: what it spent is a row, not a failure of the run.
    genus.certify(tmp_path, loaded, {}, (), time.time() + 60)
    interruption = exceeded.load(tmp_path)[computation]
    assert interruption.killed_by == "memory"
    assert interruption.limit_bytes == int(2.0 * genus._meminfo("MemTotal"))
    assert isinstance(interruption.peak_bytes, int) and interruption.peak_bytes > 0
    assert interruption.lost, "the next job must recover a killed computation into triage"
    assert (tmp_path / "lattices/0012.md").read_bytes() == before, "a killed computation writes no field"
    # The recorded cost is respected: the next job promotes it to the ledger and computes nothing.
    genus.certify(tmp_path, loaded, {}, (), time.time() + 60)
    assert failures.load(tmp_path)[computation].disposition == "open"
    assert exceeded.reason(exceeded.load(tmp_path)[computation]).startswith("memory exhausted")


def test_the_certify_command_exits_zero_when_a_worker_is_killed(tmp_path: Path) -> None:
    """#46: the command reports a killed worker and exits 0; only a worker that failed raises.

    The kill is simulated at the boundary the driver sees, as in the test above: the child
    process sets the worker to a program that announces its stage and never returns, and
    the memory reserve to twice the machine, so the driver kills it. No knob is added to the
    driver for a test; the real worker cannot be limited to a runner's memory here.
    """
    prepare_card(tmp_path, "0012")
    worker = tmp_path / "worker.py"
    worker.write_text(KILLED_WORKER)
    bootstrap = tmp_path / "bootstrap.py"
    bootstrap.write_text(
        "import sys\n"
        "from latticedb import cli, genus\n"
        "genus.MEMORY_RESERVE = 2.0\n"
        f"genus.WORKER = [sys.executable, {str(worker)!r}]\n"
        "cli.main()\n"
    )
    loaded = corpus.load(tmp_path)
    computation = genus.name("0012", genus.requests(loaded, {}, {}, ())[0]["fields"][0])
    before = (tmp_path / "lattices/0012.md").read_bytes()
    completed = subprocess.run(
        [sys.executable, str(bootstrap), "certify", "--tag", "0012", "--minutes", "1", "--root", str(tmp_path)],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert "ChildProcessError" not in completed.stdout + completed.stderr
    assert exceeded.load(tmp_path)[computation].killed_by == "memory"
    assert (tmp_path / "lattices/0012.md").read_bytes() == before
    assert failures.load(tmp_path)[computation].attempts[-1].reason == "memory exhausted"
