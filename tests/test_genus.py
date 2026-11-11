"""Fast checks of certification storage/request orchestration.

Mathematical contracts of the requested operations live in preamble tests;
lattice-db tests only the serialization/certificate behavior.
"""

import json
import shutil
import sys
import time
from fractions import Fraction
from pathlib import Path

import frontmatter
import pytest
import yaml

from latticedb import certificates, corpus, exceeded, genus, records, sage_genus
from latticedb.model import Lattice

REPOSITORY = Path(__file__).resolve().parent.parent


def derived() -> certificates.Certificates:
    """The repository's derive certificates, so a copied card requests the fields that apply to it."""
    held: certificates.Certificates = {}
    for tag in ("0012", "0016", "0026"):
        path = REPOSITORY / "certificates" / f"{certificates.group(tag)}.yaml"
        stored = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        held[f"{tag} derive"] = certificates.Certificate.model_validate(stored[f"{tag} derive"])
    return held


def without(tag: str, definiteness: str, metadata: dict, held: certificates.Certificates, *fields: str) -> None:
    """Remove `fields` from a copied card and from `held`, so the test states its own missing values.

    The corpus is certified by CI, so a field a card lacks today it holds tomorrow: 0016 now states
    `integral.primitive_orbits`, `integral.discriminant_form` and its automorphism generators, and
    0012 states its discriminant form. A test whose subject is "a missing field is requested and
    certified" must create that missing field, or it silently stops exercising certification. The
    field is given as its stored path, `<block>.<name>`; its value, its citation and its held
    certificate all go, so the card, its shard and the request agree. The values computed below are
    the mathematics, and they are unchanged.
    """
    for field in fields:
        block_name, short = field.split(".", 1)
        block = metadata.get(block_name)
        if isinstance(block, dict):
            block.pop(short, None)
        metadata.get("certifications", {}).pop(field, None)
        held.pop(genus.name(tag, short, definiteness), None)


def test_sparse_cards_do_not_block_computable_cards(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "0012.md", tmp_path / "lattices")
    (tmp_path / "lattices" / "9999.md").write_text("---\ntag: '9999'\nname: Sparse source card\nlatex: S\n---\n")
    requested = genus.requests(corpus.load(tmp_path), {}, {}, ())
    assert {request["tag"] for request in requested} == {"0012"}


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
    assert {request["tag"] for request in requested} == {"0012"}


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


def test_an_indefinite_card_requests_and_stores_the_eight_primitive_orbit_rows(
    tmp_path: Path,
) -> None:
    """#8: `integral.primitive_orbits` is asked on an indefinite card, not only on a definite one."""
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    path = tmp_path / "lattices" / "0016.md"
    shutil.copy(REPOSITORY / "lattices" / "0016.md", path)
    document = frontmatter.load(str(path))
    metadata = corpus.front_matter(document)
    # U = I_{1,1}: indefinite, even and unimodular, so its eight groups are one group. The corpus
    # certifies this field, so the test makes it missing in its own copy.
    assert metadata["definiteness"] == "indefinite"
    without("0016", "indefinite", metadata, certificates.Certificates(), "integral.primitive_orbits")
    path.write_text(records.record_text(metadata, document.content))
    assert "primitive_orbits" not in corpus.front_matter(corpus.read_card(path))["integral"]
    fields = [field for request in genus.requests(corpus.load(tmp_path), derived(), {}, ("0016",)) for field in request["fields"]]
    assert "primitive_orbits" in fields
    # One orbit of primitive isotropic vectors, e + f; U is even, so no vector of norm +-1.
    series = {"constant": 1, "z": [0, 0, 0, 0], "w": [0, 0, 0, 0]}
    genus.store(path, {"primitive_orbits": {group: series for group in ("O", "SO", "O+", "SO+", "Otilde", "SOtilde", "Otilde+", "SOtilde+")}})
    integral = corpus.load(tmp_path).entries[0].lattice.integral
    assert integral is not None and integral.primitive_orbits is not None
    assert set(integral.primitive_orbits) == {"O", "SO", "O+", "SO+", "Otilde", "SOtilde", "Otilde+", "SOtilde+"}
    assert integral.primitive_orbits["Otilde+"].constant == 1


def test_the_database_asks_the_owner_on_every_card_of_the_operations_class() -> None:
    """#8: a request is withheld by the schema's block and by the domain the owner states.

    A2 is definite, even, rank 2; U is indefinite, even, rank 2 with hyperbolic index 1. What
    the database withheld by a guess at the owner's power rather than by its stated domain is
    asked: the automorphism generators on the indefinite card, in `automorphisms`, and
    `primitive_orbits` on both. The owner's stated limits still hold — spinor genera need rank
    at least three, the discriminant sequence a definite even card, the discriminant orbits an
    even card of hyperbolic index at least two — and a definite block field is not asked on an
    indefinite card, which cannot store it.
    """
    definite = Lattice.model_validate(frontmatter.load(str(REPOSITORY / "lattices" / "0012.md")).metadata)
    indefinite = Lattice.model_validate(frontmatter.load(str(REPOSITORY / "lattices" / "0016.md")).metadata)
    assert genus.applies("primitive_orbits", definite) and genus.applies("primitive_orbits", indefinite)
    assert genus.applies("automorphism_group_generator_morphisms", definite) and genus.applies("automorphism_group_generator_morphisms", indefinite)
    assert genus.applies("siegel_eisenstein_coefficients", definite)
    assert genus.applies("discriminant_sequence", definite)
    assert not genus.applies("spinor_regular", definite), "spinor regularity needs rank at least three"
    assert not genus.applies("spinor_genus_count", definite), "spinor genera need rank at least three"
    assert not genus.applies("discriminant_sequence", indefinite), "a definite even card is the domain"
    assert not genus.applies("discriminant_orbits", indefinite), "hyperbolic index 1 is outside the Eichler hypothesis"
    assert not genus.applies("regular", indefinite), "an indefinite card cannot carry the definite block"
    assert not genus.applies("automorphism_group_order", indefinite)
    assert not genus.applies("roots", definite), "a definite card states its roots in `definite.roots`"
    assert not genus.applies("cusp_form_coordinates", definite), "the owner does not present it"
    assert genus.applies("discriminant_form", Lattice.model_validate(frontmatter.load(str(REPOSITORY / "lattices" / "0016.md")).metadata)), "the hyperbolic plane's discriminant group is trivial"
    assert not genus.applies("discriminant_form", Lattice.model_validate(frontmatter.load(str(REPOSITORY / "lattices" / "3F4F.md")).metadata)), "|A_L| = 4323 is above the owner's bound of 4096"
    assert genus.applies("discriminant_form", Lattice.model_validate(frontmatter.load(str(REPOSITORY / "lattices" / "6JRX.md")).metadata)), "the corrected period lattice of degree 2 has |A_L| = 2"
    assert genus.applies("discriminant_form", definite), "A_2 has three classes to partition"


def test_a_card_without_an_integral_block_requests_no_primitive_orbits() -> None:
    """The database's own fact: a value has no block to be stored in on this card."""
    lattice = Lattice.model_validate({"tag": "9998", "name": "Half-integral", "latex": "H", "gram_tensor": [["1/2"]]})
    assert lattice.integral is None
    assert not genus.applies("primitive_orbits", lattice)


def test_the_plane_count_enters_the_certified_orbit_result_only_when_it_is_stated() -> None:
    """#3: a row that states `planes` commits to it, and a row written before the field keeps its hash."""
    without = genus.certified_value("primitive_orbits", {"O": {"constant": 2, "z": [0, 1], "w": [0, 1]}})
    assert without == {"O": {"constant": 2, "z": [0, 1], "w": [0, 1]}}
    with_planes = genus.certified_value("primitive_orbits", {"O": {"constant": 2, "planes": 2, "reference": {"citation": "Sterk"}}})
    assert with_planes == {"O": {"constant": 2, "z": None, "w": None, "planes": 2}}


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
    fields = [field for request in genus.requests(corpus.load(tmp_path), derived(), {}, ()) for field in request["fields"]]
    assert "regular" in fields
    assert "spinor_regular" not in fields


def test_a_definite_binary_lattice_requests_its_genus_series_siegel_product_and_local_conditions(
    tmp_path: Path,
) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "0012.md", tmp_path / "lattices")
    request = genus.requests(corpus.load(tmp_path), derived(), {}, ())[0]
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


def test_a_cut_search_resumes_first_among_the_searches_not_before_the_other_fields(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    for tag in ("0012", "0016"):
        shutil.copy(REPOSITORY / "lattices" / f"{tag}.md", tmp_path / "lattices")
    loaded = corpus.load(tmp_path)
    a2 = next(entry.lattice for entry in loaded.entries if entry.lattice.tag == "0012")
    computation = genus.name("0012", "regular")
    log = {computation: exceeded.Interruption(hash=exceeded.input_hash(computation, a2), seconds=60)}
    requested = genus.requests(loaded, derived(), log, ())
    # Both cards' finishing fields come first by size; A2's cut search leads the searches.
    assert [request["tag"] for request in requested] == ["0016", "0012", "0012", "0016"]
    assert not any(request.get("resumed") for request in requested)
    assert requested[2]["fields"][0] == "regular"


def test_a_computation_running_when_its_runner_died_comes_after_everything_else(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    for tag in ("0012", "0016"):
        shutil.copy(REPOSITORY / "lattices" / f"{tag}.md", tmp_path / "lattices")
    loaded = corpus.load(tmp_path)
    a2 = next(entry.lattice for entry in loaded.entries if entry.lattice.tag == "0012")
    computation = genus.name("0012", "genus_symbol")
    log = {computation: exceeded.Interruption(hash=exceeded.input_hash(computation, a2), seconds=600, lost=True)}
    requested = genus.requests(loaded, derived(), log, ())
    assert requested[-1]["tag"] == "0012" and requested[-1]["fields"] == ["genus_symbol"]
    assert all("genus_symbol" not in request["fields"] for request in requested[:-1] if request["tag"] == "0012")
    assert not any(request.get("resumed") for request in requested)


def test_resumed_requests_leave_one_worker_to_the_rest(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    worker = tmp_path / "worker.py"
    worker.write_text(FAKE_WORKER)
    monkeypatch.setattr(genus, "WORKER", [sys.executable, str(worker)])

    def request(tag: str, field: str, resumed: bool) -> genus.Request:
        made: genus.Request = {"tag": tag, "gram": [[2]], "integral": True, "fields": [field], "series_bound": 1}
        return {**made, "resumed": True} if resumed else made

    # Two resumed computations that never finish lead the queue of two workers.
    queue = [request("0001", "grows", True), request("0002", "grows", True), request("0003", "genus_symbol", False)]
    stream = genus.computed(queue, time.time() + 10, 2)
    finished = [values for values in stream if "checkpoint" not in values and "started" not in values and "deadline" not in values]
    assert finished == [{"tag": "0003", "genus_symbol": True}]


def test_shards_partition_the_cards() -> None:
    tags = [f"{number:04d}" for number in range(1, 200)]
    shards = [[tag for tag in tags if genus.in_shard(tag, (index, 4))] for index in range(4)]
    assert sorted(tag for shard in shards for tag in shard) == tags
    assert all(shards)


def test_smaller_cards_come_first_and_every_card_precedes_the_searches(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    for tag in ("0012", "0016", "0026"):
        shutil.copy(REPOSITORY / "lattices" / f"{tag}.md", tmp_path / "lattices")
    # U and A2 are derived; II_{1,2} is held underived, so its search request carries
    # its record, from which the worker selects the searches that apply.
    held = {computation: certificate for computation, certificate in derived().items() if computation != "0026 derive"}
    requested = genus.requests(corpus.load(tmp_path), held, {}, ())
    # U has determinant -1 and A2 determinant 3, both of rank 2; II_{1,2} has rank 3.
    assert [request["tag"] for request in requested] == ["0016", "0012", "0026"] * 2
    finishing, searches = requested[:3], requested[3:]
    assert not any(set(request["fields"]) & genus.SEMI_DECISIONS for request in finishing)
    assert finishing[2]["fields"][0] == "derive"
    assert all(set(request["fields"]) <= genus.SEMI_DECISIONS for request in searches)
    assert "roots" in searches[0]["fields"]
    assert "record" in searches[2] and "derive" not in searches[2]["fields"]


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


def test_an_underived_seeded_card_requests_its_invariants_with_its_derivation(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "3999.md", tmp_path / "lattices")
    # A seeded card states its rank but none of the hypotheses that derivation supplies.
    requested = genus.requests(corpus.load(tmp_path), {}, {}, ())
    assert requested[0]["fields"][0] == "derive"
    assert "genus_symbol" in requested[0]["fields"]


class Printed:
    """A preamble rational whose printed form is the one a Fraction rejects: `(3)/(2)`."""

    def __init__(self, numerator: int, denominator: int) -> None:
        self._numerator, self._denominator = numerator, denominator

    def numerator(self) -> int:
        return self._numerator

    def denominator(self) -> int:
        return self._denominator

    def __str__(self) -> str:
        return f"({self._numerator})/({self._denominator})"


def test_a_rational_is_serialized_from_its_numerator_and_denominator_never_its_text() -> None:
    """#4: the owner prints a localized rational as `(3)/(2)`, and the card stores the value `3/2`."""
    with pytest.raises(ValueError):
        # The printed form is not a number: reading it was the defect.
        Fraction(str(Printed(3, 2)))
    assert sage_genus._rational(Printed(3, 2)) == "3/2"
    assert sage_genus._rational(Printed(6, 3)) == 2
    assert sage_genus._rational(Printed(-9, 6)) == "-3/2"
    # The value classes the adapter receives keep the pair they were given, so the reduction happens here.
    assert sage_genus._rational(Printed(0, 5)) == 0


def test_certification_stores_the_exact_two_adic_densities_of_the_sum_of_three_squares(tmp_path: Path) -> None:
    # The preamble prints a local density as `(3)/(2)`; the card stores the rational `3/2`.
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    path = tmp_path / "lattices" / "0022.md"
    document = frontmatter.load(str(REPOSITORY / "lattices" / "0022.md"))
    del document.metadata["integral"]["local_densities"]
    del document.metadata["certifications"]["integral.local_densities"]
    path.write_text(records.record_text(corpus.front_matter(document), document.content))
    stored = yaml.load((REPOSITORY / "certificates" / f"{certificates.group('0022')}.yaml").read_text(), Loader=yaml.CSafeLoader)
    held = {name: certificates.Certificate.model_validate(value) for name, value in stored.items() if name.startswith("0022 ")}
    del held["0022 integral.local_densities"]
    loaded = corpus.load(tmp_path)
    assert genus.requests(loaded, held, {}, ("0022",))[0]["fields"] == ["local_densities"]
    genus.certify(tmp_path, loaded, held, ("0022",), time.time() + 120)
    # Oracle: the density of t at 2 for x^2 + y^2 + z^2 is #{x in (Z/2^k)^3 : x.x = t mod 2^k} / 2^(2k),
    # counted for k = 6; the count is constant from k = 5 on.
    expected = ["3/2", "3/2", 1, "3/4", "3/2", "3/2", 0, "3/4", "3/2", "3/2", 1, "1/2"]
    assert frontmatter.load(str(path)).metadata["integral"]["local_densities"] == [{"prime": 2, "densities": expected}]
    assert genus.name("0022", "local_densities") in certificates.load(tmp_path)


def test_certification_stores_an_indefinite_card_automorphism_generators(tmp_path: Path) -> None:
    """#8: U's O(L) is infinite, so its card is asked for the generators alone and certifies them."""
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    path = tmp_path / "lattices" / "0016.md"
    document = frontmatter.load(str(REPOSITORY / "lattices" / "0016.md"))
    # The orbit series of U: one orbit of primitive isotropic vectors, e + f, and no vector of
    # norm +-1 because U is even.
    series = {"constant": 1, "z": [0, 0, 0, 0], "w": [0, 0, 0, 0]}
    metadata = corpus.front_matter(document)
    metadata["integral"] = {**metadata["integral"], "primitive_orbits": {group: dict(series) for group in ("O", "SO", "O+", "SO+", "Otilde", "SOtilde", "Otilde+", "SOtilde+")}}
    lattice = Lattice.model_validate(metadata)
    stored = yaml.load((REPOSITORY / "certificates" / f"{certificates.group('0016')}.yaml").read_text(), Loader=yaml.CSafeLoader)
    held = {name: certificates.Certificate.model_validate(value) for name, value in stored.items() if name.startswith("0016 ")}
    # Every value already on the card carries its certificate, so the generators are the only field
    # this card is asked for.
    citations = dict(metadata["certifications"])
    for field in genus.BLOCKS:
        block_name = genus.stored_in(field, "indefinite")[0]
        block = metadata.get(block_name)
        value = block.get(field) if isinstance(block, dict) else None
        if field == "automorphism_group_generator_morphisms" or value is None:
            continue
        computation = genus.name("0016", field, "indefinite")
        digest = certificates.certification_hash(computation, lattice, genus.certified_value(field, value, lattice))
        held[computation] = certificates.Certificate(hash=digest, by="test")
        citations[f"{block_name}.{field}"] = digest
    metadata["certifications"] = citations
    # The corpus certifies both fields this test is about, so the test removes them from its own copy:
    # the generators and the discriminant form are the two it asks certify to compute.
    without("0016", "indefinite", metadata, held, "integral.discriminant_form", "automorphisms.automorphism_group_generator_morphisms")
    path.write_text(records.record_text(metadata, document.content))
    loaded = corpus.load(tmp_path)
    # U is even and unimodular, so its discriminant form is trivial but stated: |O(q)| = 1, one
    # isotropic class and one orbit. The card does not state it, so certify asks for it.
    assert [field for request in genus.requests(loaded, held, {}, ("0016",)) for field in request["fields"]] == ["automorphism_group_generator_morphisms", "discriminant_form"]
    genus.certify(tmp_path, loaded, held, ("0016",), time.time() + 120)
    card = corpus.front_matter(corpus.read_card(path))
    # The group is stated by generators alone: no order field, and no `definite` block.
    assert "definite" not in card
    certified = Lattice.model_validate(card)
    assert certified.automorphisms is not None
    names = certified.automorphisms.automorphism_group_generator_morphisms
    assert names is not None and len(names) == 2
    stored_morphisms = {morphism.name: morphism.matrix for morphism in certified.morphisms if morphism.target == "0016" and morphism.scale == 1}
    matrices = [stored_morphisms[name] for name in names]
    # A generating set is not canonical, so the test states the contract and not a chosen set:
    # every stored matrix is an isometry of the card's Gram tensor, and the group they generate
    # is O(U), of order 4.
    gram = [[0, 1], [1, 0]]

    def product(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
        return [[sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

    def preserves(matrix: list[list[int]]) -> bool:
        conjugated = [[sum(matrix[i][k] * gram[k][l] * matrix[j][l] for k in range(2) for l in range(2)) for j in range(2)] for i in range(2)]
        return conjugated == gram

    assert all(preserves(matrix) for matrix in matrices), "a stored generator is not an isometry of U"
    identity = [[1, 0], [0, 1]]
    generated = {tuple(entry for row in identity for entry in row)}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for matrix in matrices:
            image = product(matrix, current)
            key = tuple(entry for row in image for entry in row)
            if key not in generated:
                generated.add(key)
                frontier.append(image)
    assert len(generated) == 4, f"the stored generators span a group of order {len(generated)}, not |O(U)| = 4"
    assert "automorphism_group_order" not in card["automorphisms"]
    assert genus.name("0016", "automorphism_group_generator_morphisms", "indefinite") in certificates.load(tmp_path)


def test_certification_keeps_a_root_lattice_integer_valued(tmp_path: Path) -> None:
    # A2 has Gram tensor [[2, -1], [-1, 2]]: every entry is an integer, so its form is integer-valued.
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    path = tmp_path / "lattices" / "0012.md"
    document = frontmatter.load(str(REPOSITORY / "lattices" / "0012.md"))
    stored = yaml.load((REPOSITORY / "certificates" / f"{certificates.group('0012')}.yaml").read_text(), Loader=yaml.CSafeLoader)
    held = {name: certificates.Certificate.model_validate(value) for name, value in stored.items() if name.startswith("0012 ")}
    del held[genus.name("0012", "integer_valued")]
    # Both fields this test names are missing in its own copy: A_2's discriminant form is certified on
    # the corpus's own card, so the test removes it and its held certificate here.
    without("0012", "definite", document.metadata, held, "form.integer_valued", "integral.discriminant_form")
    path.write_text(records.record_text(corpus.front_matter(document), document.content))
    loaded = corpus.load(tmp_path)
    # A_2 is even with three classes, so its discriminant form's three invariants are asked too.
    assert genus.requests(loaded, held, {}, ("0012",))[0]["fields"] == ["integer_valued", "discriminant_form"]
    genus.certify(tmp_path, loaded, held, ("0012",), time.time() + 120)
    assert frontmatter.load(str(path)).metadata["form"]["integer_valued"] is True
    assert genus.name("0012", "integer_valued") in certificates.load(tmp_path)


def test_a_primitive_orbit_row_is_stored_and_certified_by_its_citations(tmp_path: Path) -> None:
    """A cited row joins the field under its group key, and one certificate names every citation."""
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "029J.md", tmp_path / "lattices")
    path = tmp_path / "lattices" / "029J.md"
    reference = {
        "citation": "H. Sterk, \"Compactifications of the period space of Enriques surfaces, Part I\", "
        "Math. Z. 207 (1991), 1-36, Theorem 4.0.1, p. 55.",
        "url": "https://doi.org/10.1007/BF02571383",
    }
    held: certificates.Certificates = {}
    genus.cite_orbit_row(path, "SOtilde", {"constant": 3}, reference, held)

    metadata = corpus.front_matter(corpus.read_card(path))
    series_of_group = metadata["integral"]["primitive_orbits"]
    assert series_of_group["SOtilde"] == {"constant": 3}
    assert {"O", "gamma-en-2", "Otilde+"} <= set(series_of_group), "the rows already on the card stay"
    assert reference in [dict(entry) for entry in metadata["references"]], "the citation joins the card"
    lattice = Lattice.model_validate(metadata)
    computation = genus.name("029J", "primitive_orbits", lattice.definiteness)
    digest = certificates.certification_hash(
        computation,
        lattice,
        genus.certified_value("primitive_orbits", series_of_group, lattice),
    )
    assert lattice.certifications["integral.primitive_orbits"] == digest
    assert held[computation].hash == digest
    assert held[computation].by.startswith(reference["citation"]), "this row's citation leads the provenance"
    assert "Sterk" in held[computation].by and "Dutour" in held[computation].by, "the other cited rows are named too"

    with pytest.raises(AssertionError, match="the source proves"):
        genus.cite_orbit_row(path, "O", {"constant": 3}, reference, held)


def test_a_cusp_chamber_row_is_added_without_dropping_or_contradicting_a_stored_one(tmp_path: Path) -> None:
    """#33, #35: the chamber writer takes the rows a source proves on top of the ones the card holds.

    Sterk's five statements are one source and were transcribed in two batches, and a figure of it was
    read twice: the row at (4.3.9) gained its fourteenth wall when Fig. 12 was read again. A stored row
    keeps its cusp, statement, page and figure and every wall it states, so a fuller reading may add a
    wall; a lost wall, a changed page, or a dropped cusp stops the writer instead of replacing the row.
    """
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "029J.md", tmp_path / "lattices")
    path = tmp_path / "lattices" / "029J.md"
    rows = corpus.front_matter(corpus.read_card(path))["integral"]["cusp_chambers"]["gamma-en-2"]
    reference = {"citation": "H. Sterk, \"Compactifications of the period space of Enriques surfaces, Part I\", Math. Z. 207 (1991), 1-36, Section 4.3."}
    by = f"{reference['citation']} The Gram matrix, the Coxeter diagram and the wall count are the card's form on those walls."

    def read_further(row: dict, lost: str) -> dict:
        """The same chamber row without one wall: its walls, Gram matrix and diagram shrink together."""
        keep = [i for i, wall in enumerate(row["walls"]) if wall["name"] != lost]
        return {
            **row,
            "walls": [row["walls"][i] for i in keep],
            "wall_count": len(keep),
            "gram": [[row["gram"][i][j] for j in keep] for i in keep],
            "diagram": [edge for edge in row["diagram"] if lost not in (edge["a"], edge["b"])],
        }

    document = frontmatter.load(str(path))
    held: certificates.Certificates = {}
    without("029J", "integral", document.metadata, held, "integral.cusp_chambers")
    path.write_text(records.record_text(corpus.front_matter(document), document.content))

    genus.cite_cusp_chambers(path, "gamma-en-2", rows[:1], reference, by, held)
    assert [row["statement"] for row in corpus.front_matter(corpus.read_card(path))["integral"]["cusp_chambers"]["gamma-en-2"]] == ["4.3.5"]

    genus.cite_cusp_chambers(path, "gamma-en-2", rows[:2], reference, by, held)
    metadata = corpus.front_matter(corpus.read_card(path))
    assert [row["statement"] for row in metadata["integral"]["cusp_chambers"]["gamma-en-2"]] == ["4.3.5", "4.3.6"], (
        "a further statement of the same source adds its row to the stored one"
    )
    lattice = Lattice.model_validate(metadata)
    computation = genus.name("029J", "cusp_chambers", lattice.definiteness)
    digest = certificates.certification_hash(
        computation,
        lattice,
        genus.certified_value("cusp_chambers", metadata["integral"]["cusp_chambers"], lattice),
    )
    assert lattice.certifications["integral.cusp_chambers"] == digest == held[computation].hash, "the one hash commits to both rows"

    # (4.3.9) as Fig. 12 is read now, and the same row as it read before its fourteenth wall was found.
    full = next(row for row in rows if row["statement"] == "4.3.9")
    short = read_further(full, "\\alpha_8")
    assert short["wall_count"] == full["wall_count"] - 1
    genus.cite_cusp_chambers(path, "gamma-en-2", [rows[0], rows[1], short], reference, by, held)
    genus.cite_cusp_chambers(path, "gamma-en-2", [rows[0], rows[1], full], reference, by, held)
    stored = {row["statement"]: row for row in corpus.front_matter(corpus.read_card(path))["integral"]["cusp_chambers"]["gamma-en-2"]}
    assert stored["4.3.9"]["wall_count"] == full["wall_count"], "a fuller reading of the same figure adds its wall"
    assert [wall["name"] for wall in stored["4.3.9"]["walls"]] == [wall["name"] for wall in full["walls"]]

    with pytest.raises(AssertionError, match="dropped or moved"):
        genus.cite_cusp_chambers(path, "gamma-en-2", [rows[0], rows[1], short], reference, by, held)
    altered = {**full, "printed_page": 25}
    with pytest.raises(AssertionError, match="changes its printed_page"):
        genus.cite_cusp_chambers(path, "gamma-en-2", [rows[0], rows[1], altered], reference, by, held)
    with pytest.raises(AssertionError, match="not among the rows proved now"):
        genus.cite_cusp_chambers(path, "gamma-en-2", rows[1:2], reference, by, held)
    assert [row["statement"] for row in corpus.front_matter(corpus.read_card(path))["integral"]["cusp_chambers"]["gamma-en-2"]] == ["4.3.5", "4.3.6", "4.3.9"], (
        "a refused write leaves the card as it was"
    )


def test_the_queue_separates_the_terminating_fields_from_the_searches() -> None:
    """#14: a run takes one phase, so a dispatched run does not wait on a schedule run's search."""
    terminating = {"tag": "0012", "fields": ["integer_valued"]}
    search = {"tag": "029J", "fields": ["roots", "norms"], "searches": True}
    queue = [terminating, search]
    assert genus.in_phase(queue, None) == queue, "both phases, in the queue's order"
    assert genus.in_phase(queue, False) == [terminating]
    assert genus.in_phase(queue, True) == [search]


def test_the_owner_s_orbit_counts_are_emitted_as_their_exact_cardinalities(capsys: pytest.CaptureFixture[str]) -> None:
    """#16: the emitter writes the owner's own counts, on the owner's own series for 026E.

    The per-tag run of 01:00Z read `TypeError: Object of type Cardinalities.parent_class is not JSON
    serializable` at `primitive_orbits -> O -> constant`. This asks the owner for that series and emits
    it through the adapter's own `_emit` and `VALUES["primitive_orbits"]`: every group's constant is
    the cardinality's `finite_value()`, which is what the card then stores.
    """
    series = _cardinality_series()
    with pytest.raises(TypeError, match="not JSON serializable"):
        sage_genus._emit("026E", {"primitive_orbits": series})

    sage_genus._emit("026E", {"primitive_orbits": sage_genus.VALUES["primitive_orbits"](_CardinalityLattice(series))})
    emitted = json.loads(capsys.readouterr().out.strip().splitlines()[-1])["primitive_orbits"]
    assert sorted(emitted) == sorted(series)
    for group, row in series.items():
        assert emitted[group]["constant"] == row["constant"].finite_value()
        assert isinstance(emitted[group]["constant"], int)


def test_the_converted_orbit_counts_are_what_the_card_stores_and_reads_back(tmp_path: Path) -> None:
    """#16: the value the adapter emits is the value the card stores, and a reader reads it.

    The counts come from the owner's own series for 026E — its `Cardinalities` element for each group —
    and #15's lesson is that a stored value the reader refuses stops every certify job before a
    computation, so the stored form is asserted through `corpus.read_card` and through the
    certificate's projection of it.
    """
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "026E.md", tmp_path / "lattices")
    path = tmp_path / "lattices" / "026E.md"

    series = _cardinality_series()
    genus.store(path, {"primitive_orbits": sage_genus.VALUES["primitive_orbits"](_CardinalityLattice(series))})
    stored = corpus.front_matter(corpus.read_card(path))
    lattice = Lattice.model_validate(stored)
    assert lattice.integral is not None and lattice.integral.primitive_orbits is not None
    for group, row in series.items():
        assert lattice.integral.primitive_orbits[group].constant == row["constant"].finite_value()
    projection = genus.certified_value("primitive_orbits", stored["integral"]["primitive_orbits"])
    for group, row in series.items():
        assert projection[group]["constant"] == row["constant"].finite_value()

def _regularity_card(tmp_path: Path) -> Path:
    """A card that states a semi-decision result and cites its certificate."""
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    source = frontmatter.load(str(REPOSITORY / "lattices" / "0023.md"))
    metadata = {key: value for key, value in source.metadata.items() if key in ("tag", "name", "latex", "gram_tensor", "rank", "definite", "certifications")}
    metadata["definite"] = {**(metadata.get("definite") or {}), "regular": True, "spinor_regular": True}
    metadata["certifications"] = {**(metadata.get("certifications") or {}), "definite.regular": "aa" * 32, "definite.spinor_regular": "bb" * 32}
    path = tmp_path / "lattices" / "0023.md"
    path.write_text(records.record_text(metadata, source.content))
    return path


def test_a_derivation_keeps_a_result_another_computation_wrote(tmp_path: Path) -> None:
    """#23: the derivation writes its own blocks, and does not delete the fields of other computations.

    The record a run derives from is its read of the card when the card was queued; a semi-decision
    written during the run is not in it, and writing the derivation alone deleted the value while its
    certificate stayed in `certificates/`.
    """
    path = _regularity_card(tmp_path)
    stored = corpus.front_matter(corpus.read_card(path))
    # the derivation as a stale run produces it: the blocks rebuilt, without the regularity results
    derived = dict(stored)
    derived["definite"] = {"minimum": 1, "kissing_number": 6}
    derived["certifications"] = {"derive": "cc" * 32}
    kept = genus.keep_other_computations(path, derived)
    assert kept["definite"]["regular"] is True
    assert kept["definite"]["spinor_regular"] is True
    assert kept["definite"]["minimum"] == 1, "the derivation's own values win"
    assert kept["certifications"]["definite.regular"] == "aa" * 32
    assert kept["certifications"]["definite.spinor_regular"] == "bb" * 32
    assert kept["certifications"]["derive"] == "cc" * 32


def test_a_derivation_of_another_lattice_carries_nothing_over(tmp_path: Path) -> None:
    """A derivation whose Gram tensor differs is another lattice, and its blocks are its own."""
    path = _regularity_card(tmp_path)
    derived = {**corpus.front_matter(corpus.read_card(path)), "gram_tensor": [[2, 0], [0, 2]], "definite": {"minimum": 2}, "certifications": {}}
    kept = genus.keep_other_computations(path, derived)
    assert kept["definite"] == {"minimum": 2}
    assert "definite.regular" not in kept["certifications"]


class _CardinalityLattice:
    """A lattice stand-in that answers with the owner's series already computed for 026E."""

    def __init__(self, series: dict[str, object]) -> None:
        self._series = series

    def primitive_orbit_series(self, bound: int | None = None) -> dict[str, object]:
        return self._series


def _cardinality_series() -> dict[str, object]:
    """The owner's primitive-orbit series for 026E, computed as `certify` asks for it."""
    from sage.all import ZZ
    from sage_extensions.categories.lattices import Lattices

    record = frontmatter.load(str(REPOSITORY / "lattices" / "026E.md")).metadata
    return Lattices(ZZ)(Lattice.model_validate(record).gram_tensor).primitive_orbit_series()


def test_the_owner_s_orbit_counts_are_cardinalities_that_json_refuses() -> None:
    """#16: the value `certify` must store is a `Cardinalities` element, and `json` cannot emit it.

    This is the reported failure, on the owner's own object for 026E: not a stub, and not a printed
    form. The emitter's conversion is what turns it into the card's number.
    """
    from sage_extensions.categories.sets.cardinals import Cardinal

    series = _cardinality_series()
    constant = series["O"]["constant"]
    assert isinstance(constant, Cardinal)
    with pytest.raises(TypeError, match="Cardinalities"):
        json.dumps(series)
    assert constant.is_finite() is True
    assert constant.finite_value() == 1


def test_a_finite_cardinality_is_serialized_as_the_owner_s_exact_value() -> None:
    """The count a card stores is the owner's `finite_value`, not a cast and not a printed form."""
    from sage_extensions.categories.sets.cardinals import cardinal

    assert sage_genus._orbit_count(cardinal(7)) == 7
    assert sage_genus._orbit_count(cardinal(0)) == 0


def test_a_countably_infinite_count_is_the_count_the_owner_states() -> None:
    """`aleph0` is written where the owner says the cardinal is countably infinite."""
    from sage_extensions.categories.sets.cardinals import aleph0

    assert sage_genus._orbit_count(aleph0) == "aleph0"


def test_a_cardinality_beyond_aleph0_is_not_recorded_as_aleph0() -> None:
    """A cardinal the owner states to be uncountable has no count this schema states."""
    from sage_extensions.categories.sets.cardinals import continuum

    with pytest.raises(ValueError, match="uncountable"):
        sage_genus._orbit_count(continuum)
