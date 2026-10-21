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

from latticedb import certificates, corpus, exceeded, genus

REPOSITORY = Path(__file__).resolve().parent.parent


def prepare_card(root: Path, tag: str) -> Path:
    (root / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, root / corpus.FAMILIES_FILE)
    (root / corpus.RETIRED_FILE).write_text("{}\n")
    target = root / "lattices" / f"{tag}.md"
    shutil.copy(REPOSITORY / "lattices" / f"{tag}.md", target)
    return target


def test_an_early_termination_does_not_blacklist_a_computation_for_a_whole_job(tmp_path: Path) -> None:
    prepare_card(tmp_path, "0016")
    command = [sys.executable, "-m", "latticedb", "certify", "--minutes", "330", "--tag", "0016", "--root", str(tmp_path)]
    # The roots of U span an index-two sublattice. The preamble's semi-decision
    # for roots generating all of U therefore keeps searching until interrupted.
    computation = genus.name("0016", "roots")
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
    assert "roots" in requested[0]["fields"]
    assert "norms" in requested[0]["fields"]


def test_finishing_a_previously_interrupted_computation_clears_its_log(tmp_path: Path) -> None:
    prepare_card(tmp_path, "0012")
    loaded = corpus.load(tmp_path)
    lattice = loaded.entries[0].lattice
    computation = genus.name("0012", "genus_class_count")
    exceeded.save(tmp_path, {computation: exceeded.Interruption(hash=exceeded.input_hash(computation, lattice), seconds=1)})
    genus.certify(tmp_path, loaded, {}, ("0012",), time.time() + 60)
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


def test_a_computation_killed_for_memory_is_run_last_by_the_next_job(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    prepare_card(tmp_path, "0012")
    worker = tmp_path / "worker.py"
    worker.write_text(
        "import json, sys, time\n"
        "request = json.loads(sys.stdin.readline())\n"
        'print(json.dumps({"tag": request["tag"], "started": [request["fields"][0]]}), flush=True)\n'
        "time.sleep(60)\n"
    )
    monkeypatch.setattr(genus, "WORKER", [sys.executable, str(worker)])
    # A reserve above the machine's memory is never available, so the worker is killed at once.
    monkeypatch.setattr(genus, "MEMORY_RESERVE", 2.0)
    loaded = corpus.load(tmp_path)
    first = genus.requests(loaded, {}, {}, ())[0]["fields"][0]
    with pytest.raises(ChildProcessError, match="memory exhausted"):
        genus.certify(tmp_path, loaded, {}, (), time.time() + 60)
    assert exceeded.was_lost(exceeded.load(tmp_path), genus.name("0012", first), loaded.entries[0].lattice)
