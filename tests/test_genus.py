"""Fast checks of certification storage/request orchestration.

Mathematical contracts of the requested operations live in preamble tests;
lattice-db tests only the serialization/certificate behavior.
"""

import shutil
import sys
import time
from pathlib import Path

import frontmatter
import pytest

from latticedb import certificates, corpus, exceeded, genus, records
from latticedb.model import Lattice

REPOSITORY = Path(__file__).resolve().parent.parent


def test_sparse_cards_do_not_block_computable_cards(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "0012.md", tmp_path / "lattices")
    (tmp_path / "lattices" / "9999.md").write_text("---\ntag: '9999'\nname: Sparse source card\nlatex: S\n---\n")
    requested = genus.requests(corpus.load(tmp_path), {}, {}, ())
    assert [request["tag"] for request in requested] == ["0012"]


def test_gram_only_card_queues_derivation_before_invariants(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    source = frontmatter.load(str(REPOSITORY / "lattices" / "0012.md"))
    metadata = {key: source.metadata[key] for key in ("tag", "name", "latex", "gram_tensor")}
    (tmp_path / "lattices" / "0012.md").write_text(records.record_text(metadata, source.content))
    requested = genus.requests(corpus.load(tmp_path), {}, {}, ())
    assert requested[0]["fields"][0] == "derive"
    assert requested[0]["record"] == metadata


def test_selected_card_certification_does_not_verify_unrelated_morphisms(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    for tag in ("0012", "0016", "0026"):
        shutil.copy(REPOSITORY / "lattices" / f"{tag}.md", tmp_path / "lattices")
    path = tmp_path / "lattices" / "0016.md"
    document = frontmatter.load(str(path))
    del document.metadata["morphisms"][0]["scale"]
    path.write_text(records.record_text(corpus.front_matter(document), document.content))
    requested = genus.requests(corpus.load(tmp_path), {}, {}, ("0012",))
    assert [request["tag"] for request in requested] == ["0012"]


def test_a_computed_series_of_orbits_replaces_its_prefix_and_preserves_the_authored_tail(
    tmp_path: Path,
) -> None:
    path = tmp_path / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    document = frontmatter.load(str(path))
    document.metadata["integral"]["primitive_orbits"] = {
        "O": {
            "constant": 0,
            "z": [None, 1, 9, 9, 7, 8],
            "reference": {"citation": "source"},
        }
    }
    path.write_text(frontmatter.dumps(document))
    genus.store(
        path,
        {"primitive_orbits": {"O": {"constant": 0, "z": [0, 1, 0, 0], "w": [0, 0, 0, 0]}}},
    )
    stored = frontmatter.load(str(path)).metadata["integral"]["primitive_orbits"]["O"]
    assert stored["z"] == [0, 1, 0, 0, 7, 8]
    assert stored["w"] == [0, 0, 0, 0]
    assert stored["reference"] == {"citation": "source"}


def test_orbit_certificate_value_excludes_source_only_tail_and_reference() -> None:
    stored = {
        "O": {
            "constant": 0,
            "z": [0, 1, 0, 0, 7, 8],
            "w": [0, 0, 0, 0, 9],
            "reference": {"citation": "A source."},
        }
    }
    assert genus.certified_value("primitive_orbits", stored) == {
        "O": {
            "constant": 0,
            "z": [0, 1, 0, 0],
            "w": [0, 0, 0, 0],
        }
    }


def test_a_missing_value_is_written(tmp_path: Path) -> None:
    path = tmp_path / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    document = frontmatter.load(str(path))
    del document.metadata["integral"]["genus_class_count"]
    path.write_text(frontmatter.dumps(document))
    genus.store(path, {"genus_class_count": 1})
    assert frontmatter.load(str(path)).metadata["integral"]["genus_class_count"] == 1


def test_a_stored_value_that_differs_is_replaced(tmp_path: Path) -> None:
    path = tmp_path / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    genus.store(path, {"automorphism_group_order": 6})
    assert frontmatter.load(str(path)).metadata["definite"]["automorphism_group_order"] == 6


def test_a_certified_value_is_not_requested(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    source = frontmatter.load(str(REPOSITORY / "lattices" / "0012.md"))
    metadata = corpus.front_matter(source)
    lattice = Lattice.model_validate(metadata)
    derive_hash = certificates.certification_hash("0012 derive", lattice, records.derived_projection(metadata))
    held = {"0012 derive": certificates.Certificate(hash=derive_hash, by="test")}
    card_certifications: dict[str, str] = {"derive": derive_hash}
    for field, (block_name, _) in genus.BLOCKS.items():
        block = metadata.get(block_name)
        value = block.get(field) if isinstance(block, dict) else None
        if value is None:
            continue
        computation = genus.name("0012", field)
        certificate_hash = certificates.certification_hash(computation, lattice, genus.certified_value(field, value, lattice))
        card_certifications[f"{block_name}.{field}"] = certificate_hash
        held[computation] = certificates.Certificate(hash=certificate_hash, by="test")
    metadata["certifications"] = card_certifications
    (tmp_path / "lattices" / "0012.md").write_text(records.record_text(metadata, source.content))
    loaded = corpus.load(tmp_path)
    requests = genus.requests(loaded, held, {}, ("0012",))
    pending_fields = {field for request in requests for field in request["fields"]}
    assert "derive" not in pending_fields
    assert "genus_symbol" not in pending_fields
    assert "genus_class_count" not in pending_fields
    assert "automorphism_group_order" not in pending_fields

    changed = frontmatter.load(str(tmp_path / "lattices" / "0012.md"))
    changed.metadata["integral"]["genus_class_count"] = 2
    (tmp_path / "lattices" / "0012.md").write_text(records.record_text(corpus.front_matter(changed), changed.content))
    loaded = corpus.load(tmp_path)
    assert "genus_class_count" in genus.requests(loaded, held, {}, ("0012",))[0]["fields"]


def test_a_definite_binary_lattice_requests_regularity_and_no_spinor_regularity(
    tmp_path: Path,
) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "0012.md", tmp_path / "lattices")
    fields = genus.requests(corpus.load(tmp_path), {}, {}, ())[0]["fields"]
    assert "regular" in fields
    assert "spinor_regular" not in fields


def test_a_definite_binary_lattice_requests_its_genus_series_siegel_product_and_local_conditions(
    tmp_path: Path,
) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "0012.md", tmp_path / "lattices")
    request = genus.requests(corpus.load(tmp_path), {}, {}, ())[0]
    assert request["series_bound"] == 12
    fields = request["fields"]
    for field in (
        "genus_theta_series",
        "theta_series_cuspidal_component",
        "local_densities",
        "siegel_eisenstein_coefficients",
        "anisotropic_primes",
        "local_representations",
    ):
        assert field in fields
    assert "cusp_form_coordinates" not in fields


def test_a_computation_that_outran_a_job_is_skipped_and_a_cut_one_runs_first(
    tmp_path: Path,
) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    for tag in ("0011", "0012"):
        shutil.copy(REPOSITORY / "lattices" / f"{tag}.md", tmp_path / "lattices")
    loaded = corpus.load(tmp_path)
    lattices = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    fields = genus.requests(loaded, {}, {}, ())[1]["fields"]
    assert "genus_symbol" in fields and fields[-1] != "genus_symbol"

    def logged(tag: str, field: str, seconds: int) -> tuple[str, exceeded.Interruption]:
        computation = genus.name(tag, field)
        return computation, exceeded.Interruption(hash=exceeded.input_hash(computation, lattices[tag]), seconds=seconds)

    log = dict(
        [
            logged("0012", "genus_class_count", exceeded.WINDOW_SECONDS),
            logged("0012", fields[-1], 60),
        ]
    )
    requested = genus.requests(loaded, {}, log, ())
    assert requested[0]["tag"] == "0012"
    assert requested[0]["fields"][:2] == ["derive", fields[-1]]
    assert "genus_class_count" not in requested[0]["fields"]
    assert "genus_class_count" in requested[1]["fields"]


def test_shards_partition_the_cards() -> None:
    tags = [f"{number:04d}" for number in range(1, 200)]
    shards = [[tag for tag in tags if genus.in_shard(tag, (index, 4))] for index in range(4)]
    assert sorted(tag for shard in shards for tag in shard) == tags
    assert all(shards)


def test_smaller_cards_come_first_and_semi_decisions_end_each_card(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    for tag in ("0012", "0016", "0026"):
        shutil.copy(REPOSITORY / "lattices" / f"{tag}.md", tmp_path / "lattices")
    requested = genus.requests(corpus.load(tmp_path), {}, {}, ())
    # U has determinant -1 and A2 determinant 3, both of rank 2; II_{1,2} has rank 3.
    assert [request["tag"] for request in requested] == ["0016", "0012", "0026"]
    for request in requested:
        semi = [index for index, field in enumerate(request["fields"]) if field in genus.SEMI_DECISIONS]
        assert semi == list(range(len(request["fields"]) - len(semi), len(request["fields"])))
    assert "roots" in requested[0]["fields"]


FAKE_WORKER = """
import json, sys, time
for line in sys.stdin:
    request = json.loads(line)
    for field in request["fields"]:
        print(json.dumps({"tag": request["tag"], "started": [field]}), flush=True)
        if field == "raises":
            sys.exit(1)
        if field == "grows":
            time.sleep(60)
        print(json.dumps({"tag": request["tag"], field: True}), flush=True)
    print(json.dumps({"tag": request["tag"], "done": True}), flush=True)
"""


def _pool(tmp_path: Path, fields: list[str]) -> list[dict[str, object]]:
    worker = tmp_path / "worker.py"
    worker.write_text(FAKE_WORKER)
    request: genus.Request = {"tag": "0012", "gram": [[2]], "integral": True, "fields": fields, "series_bound": 1}
    stream = genus.computed([request], time.time() + 60, 1)
    return [values for values in stream if "checkpoint" not in values and "started" not in values]


def test_a_card_continues_on_a_new_worker_after_one_computation_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(genus, "WORKER", [sys.executable, str(tmp_path / "worker.py")])
    assert _pool(tmp_path, ["genus_symbol", "raises", "regular"]) == [
        {"tag": "0012", "genus_symbol": True},
        {"tag": "0012", "failed": "exit status 1"},
        {"tag": "0012", "regular": True},
    ]


def test_the_largest_worker_is_killed_when_memory_runs_low(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(genus, "WORKER", [sys.executable, str(tmp_path / "worker.py")])
    # A reserve above the machine's memory is never available, so the worker is killed at once.
    monkeypatch.setattr(genus, "MEMORY_RESERVE", 2.0)
    assert _pool(tmp_path, ["grows"]) == [{"tag": "0012", "failed": "memory exhausted"}]


def test_a_worker_that_fails_before_computing_is_not_replaced(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(genus, "WORKER", [sys.executable, "-c", "raise SystemExit(3)"])
    requests: list[genus.Request] = [{"tag": tag, "gram": [[2]], "integral": True, "fields": ["genus_symbol"], "series_bound": 1} for tag in ("0011", "0012")]
    stream = genus.computed(requests, time.time() + 60, 1)
    assert [values for values in stream if "checkpoint" not in values] == [{"tag": "0011", "failed": "exit status 3"}]
