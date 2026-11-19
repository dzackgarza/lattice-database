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

from latticedb import certificates, checks, corpus, exceeded, failures, genus, records, sage_genus
from latticedb.catalogues import ArithmeticGroup
from latticedb.invariant_models import STANDARD_SUBGROUPS
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
    `integral.primitive_orbits`, `integral.discriminant_form`, its automorphism generators and its
    automorphism group order, and
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
    # The field is asked as its eight rows, one computation each (#7).
    assert [field for field in fields if genus.orbit_row_of(field) is not None] == [genus.orbit_row("primitive_orbits", row) for row in genus.STANDARD_SUBGROUPS]
    # One orbit of primitive isotropic vectors, e + f; U is even, so no vector of norm +-1.
    series = {"constant": 1, "z": [0, 0, 0, 0], "w": [0, 0, 0, 0]}
    genus.store(path, {"primitive_orbits": {group: series for group in ("O", "SO", "O+", "SO+", "Otilde", "SOtilde", "Otilde+", "SOtilde+")}})
    integral = corpus.load(tmp_path).entries[0].lattice.integral
    assert integral is not None and integral.primitive_orbits is not None
    assert set(integral.primitive_orbits) == {"O", "SO", "O+", "SO+", "Otilde", "SOtilde", "Otilde+", "SOtilde+"}
    assert integral.primitive_orbits["Otilde+"].constant == 1


def test_an_indefinite_card_asks_for_each_orbit_row_alone(tmp_path: Path) -> None:
    """#7: the eight rows are eight computations, so a subgroup that does not return costs its row.

    A request names a row, the card stores the rows that returned inside the field's block, and a
    row a failure quarantines is not asked again while the other rows still are.
    """
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    path = tmp_path / "lattices" / "0016.md"
    shutil.copy(REPOSITORY / "lattices" / "0016.md", path)
    document = frontmatter.load(str(path))
    metadata = corpus.front_matter(document)
    without("0016", "indefinite", metadata, certificates.Certificates(), "integral.primitive_orbits")
    path.write_text(records.record_text(metadata, document.content))
    lattice = corpus.load(tmp_path).entries[0].lattice
    asked = [field for request in genus.requests(corpus.load(tmp_path), derived(), {}, ("0016",)) for field in request["fields"]]
    assert [field for field in asked if genus.orbit_row_of(field) is not None] == [genus.orbit_row("primitive_orbits", row) for row in genus.STANDARD_SUBGROUPS]

    # The rows that returned are the field's rows; the ones that did not are simply not there.
    genus.store(path, {"primitive_orbits[O]": {"O": {"constant": 1, "z": [], "w": []}}})
    genus.store(path, {"primitive_orbits[SO]": {"SO": {"constant": 1, "z": [], "w": []}}})
    assert corpus.front_matter(corpus.read_card(path))["integral"]["primitive_orbits"] == {
        "O": {"constant": 1, "z": [], "w": []},
        "SO": {"constant": 1, "z": [], "w": []},
    }

    # A quarantined row is not asked; the rows that returned are not asked again either.
    blocked = genus.orbit_row("primitive_orbits", "SOtilde+")
    failures.record(tmp_path, genus.name("0016", blocked, "indefinite"), lattice, "did not return", "", 510.0)
    remaining = genus.orbit_rows_to_ask(lattice, "primitive_orbits", corpus.front_matter(corpus.read_card(path))["integral"]["primitive_orbits"], failures.load(tmp_path), {})
    assert blocked not in remaining
    assert genus.orbit_row("primitive_orbits", "O") not in remaining, "a stored row is not asked again"
    assert genus.orbit_row("primitive_orbits", "Otilde+") in remaining


def test_an_indefinite_card_requests_its_orbit_rows_and_its_automorphism_generators(tmp_path: Path) -> None:
    """#8: the request carries an owner extension to a card, and `applies` is one filter on it.

    U is indefinite, even, rank 2, hyperbolic index 1. Its automorphism generators are a field of
    `definite` in `BLOCKS` and are stored in `automorphisms` on this card, and its primitive orbit
    series is stored a row at a time in `integral`; the card states neither, so `certify` asks the
    owner for both. The queue a run works is `genus.requests`, so that is what this asserts: a
    predicate that answers True does not by itself put a field on the wire, and the acceptance of
    #8 is that the owner is asked.
    """
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    source = frontmatter.load(str(REPOSITORY / "lattices" / "0016.md"))
    metadata = corpus.front_matter(source)
    held = derived()
    without("0016", "indefinite", metadata, held, "integral.primitive_orbits", "automorphisms.automorphism_group_generator_morphisms")
    (tmp_path / "lattices" / "0016.md").write_text(records.record_text(metadata, source.content))
    requested = [field for request in genus.requests(corpus.load(tmp_path), held, {}, ("0016",)) for field in request["fields"]]
    assert "derive" not in requested, "a current derivation selects this card's fields, so the queue is the one a run works"
    assert "automorphism_group_generator_morphisms" in requested
    assert "automorphism_group_order" in requested, "O(U) is finite, and the order is a field of this card"
    assert {field for field in requested if field.startswith("primitive_orbits[")} == {
        genus.orbit_row("primitive_orbits", subgroup) for subgroup in STANDARD_SUBGROUPS
    }
    # `regular` is still withheld from this card, by the schema rather than by an owner limit: an
    # indefinite card has no `definite` block.
    assert "regular" not in requested


def test_a_field_is_withheld_by_its_block_and_by_the_two_domains_the_board_states() -> None:
    """#8, #29: the block a card cannot carry withholds a field, and so do two domains the board states.

    A2 is definite, even, rank 2; U is indefinite, even, rank 2 with hyperbolic index 1. The owner's
    domains — the discriminant sequence of a definite even card, the Eichler hypothesis of the
    discriminant orbits, the class count of a discriminant form — no longer withhold a request: an
    operation that refuses the card raises, `failures.record` quarantines that input, and the next run
    does not ask it again. Two rules do withhold. The spinor fields, because the refusal there is not
    survivable: the owner's own check ends the worker and then the run on a rank-2 card (#29), so the
    card is not asked outside that rank. And the discriminant-orbit series, because `theory/orbits.md`
    gives a definite card the other series: its orbits of primitive vectors are what `primitive_orbits`
    enumerates, and `discriminant_orbits` is asked of an indefinite card.
    """
    definite = Lattice.model_validate(frontmatter.load(str(REPOSITORY / "lattices" / "0012.md")).metadata)
    indefinite = Lattice.model_validate(frontmatter.load(str(REPOSITORY / "lattices" / "0016.md")).metadata)
    for field in (
        "primitive_orbits",
        "automorphism_group_generator_morphisms",
        "siegel_eisenstein_coefficients",
        "discriminant_sequence",
        "discriminant_form",
    ):
        assert genus.applies(field, definite), field
    for field in ("spinor_regular", "spinor_genus_count", "spinor_genera"):
        assert not genus.applies(field, definite), f"{field} is defined at rank at least 3, and 0012 has rank 2"
    assert not genus.applies("discriminant_orbits", definite), (
        "a definite card's orbits are the primitive vectors `primitive_orbits` enumerates, and the "
        "discriminant group's series is the indefinite card's"
    )
    assert genus.applies("discriminant_sequence", indefinite), "the owner refuses a definite-only operation by raising"
    assert genus.applies("discriminant_orbits", indefinite), "hyperbolic index 1 is the owner's to refuse"
    assert genus.applies("discriminant_form", indefinite), "the hyperbolic plane's discriminant group is trivial"
    assert genus.applies("discriminant_form", Lattice.model_validate(frontmatter.load(str(REPOSITORY / "lattices" / "3F4F.md")).metadata)), "|A_L| = 4323 is a cost of the call, not a block the card lacks"
    assert genus.applies("discriminant_form", Lattice.model_validate(frontmatter.load(str(REPOSITORY / "lattices" / "6JRX.md")).metadata)), "the corrected period lattice of degree 2 has |A_L| = 2"

    # The database's own facts still withhold: a block this card cannot carry, a field the owner
    # does not present, and the two orbit fields whose generators are not certified to generate a
    # cusp stabilizer.
    assert not genus.applies("roots", definite), "a definite card states its roots in `definite.roots`"
    assert not genus.applies("regular", indefinite), "an indefinite card has no `definite` block"
    for field in ("cusp_form_coordinates", "cusp_chambers", "cusp_root_orbits", "polarization_counts"):
        assert not genus.applies(field, definite), field


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


def test_a_definite_binary_lattice_requests_regularity_and_no_spinor_field(
    tmp_path: Path,
) -> None:
    """#29: a rank-2 definite card is asked for `regular`, and for no spinor field.

    The owner defines the spinor fields at rank at least three and raises on this card, and that
    raise ends the worker and then the run, so the rank the card states is what withholds them and
    the card's other searches are asked as they were.
    """
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "0012.md", tmp_path / "lattices")
    fields = [field for request in genus.requests(corpus.load(tmp_path), derived(), {}, ()) for field in request["fields"]]
    assert "regular" in fields
    assert not {"spinor_regular", "spinor_genus_count", "spinor_genera"} & set(fields), (
        "the spinor fields are defined at rank at least three, and this card has rank 2"
    )


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
import json, os, signal, sys, time
for line in sys.stdin:
    request = json.loads(line)
    for field in request["fields"]:
        print(json.dumps({"tag": request["tag"], "started": [field]}), flush=True)
        if field == "raises":
            sys.exit(1)
        if field == "grows":
            time.sleep(60)
        if field == "dies":
            os.kill(os.getpid(), signal.SIGKILL)
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
    [values] = _pool(tmp_path, ["grows"])
    assert values["tag"] == "0012" and values["failed"] == "memory exhausted"
    # A killed worker is reported with what the run observed of the kill, not as an error (#46).
    killed = values["killed"]
    assert isinstance(killed, dict) and killed["by"] == "memory"
    assert killed["limit"] == int(2.0 * genus._meminfo("MemTotal"))
    assert isinstance(killed["peak"], int) and killed["peak"] > 0


def test_a_worker_killed_by_a_signal_is_reported_with_its_signal(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A container out-of-memory kill reaches the driver as SIGKILL and no traceback (#46)."""
    monkeypatch.setattr(genus, "WORKER", [sys.executable, str(tmp_path / "worker.py")])
    assert _pool(tmp_path, ["dies"]) == [{"tag": "0012", "failed": "killed by signal 9", "killed": {"by": "signal 9"}}]


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
    # The queue carries every field of an odd ternary card; this test's subject is the density.
    assert "local_densities" in genus.requests(loaded, held, {}, ("0022",))[0]["fields"]
    genus.certify(tmp_path, loaded, held, ("0022",), time.time() + 120, fields=("local_densities",))
    # Oracle: the density of t at 2 for x^2 + y^2 + z^2 is #{x in (Z/2^k)^3 : x.x = t mod 2^k} / 2^(2k),
    # counted for k = 6; the count is constant from k = 5 on.
    expected = ["3/2", "3/2", 1, "3/4", "3/2", "3/2", 0, "3/4", "3/2", "3/2", 1, "1/2"]
    assert frontmatter.load(str(path)).metadata["integral"]["local_densities"] == [{"prime": 2, "densities": expected}]
    assert genus.name("0022", "local_densities") in certificates.load(tmp_path)


def test_certification_stores_an_indefinite_card_automorphism_generators(tmp_path: Path) -> None:
    """#8: U's card is asked for the order of $O(L)$ and its generators, and certifies both."""
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
    without(
        "0016",
        "indefinite",
        metadata,
        held,
        "integral.discriminant_form",
        "automorphisms.automorphism_group_generator_morphisms",
        # `8474ec98` certified the order on card 0016, so the test creates the missing value it asks for.
        "automorphisms.automorphism_group_order",
    )
    path.write_text(records.record_text(metadata, document.content))
    loaded = corpus.load(tmp_path)
    # U is even and unimodular, so its discriminant form is trivial but stated: |O(q)| = 1, one
    # isotropic class and one orbit. The card does not state it, so certify asks for it.
    assert {
        "automorphism_group_order",
        "automorphism_group_generator_morphisms",
        "discriminant_form",
    } <= {field for request in genus.requests(loaded, held, {}, ("0016",)) for field in request["fields"]}
    genus.certify(
        tmp_path,
        loaded,
        held,
        ("0016",),
        time.time() + 240,
        fields=("automorphism_group_order", "automorphism_group_generator_morphisms", "discriminant_form"),
    )
    card = corpus.front_matter(corpus.read_card(path))
    # The group is stated in `automorphisms`: its order, which is finite for U, and its generators.
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
    # The order the owner states is the order those generators span, and it is certified with them.
    assert card["automorphisms"]["automorphism_group_order"] == 4
    assert genus.name("0016", "automorphism_group_order", "indefinite") in certificates.load(tmp_path)
    assert genus.name("0016", "automorphism_group_generator_morphisms", "indefinite") in certificates.load(tmp_path)


def test_certification_keeps_a_root_lattice_integer_valued(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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
    assert {"integer_valued", "discriminant_form"} <= set(genus.requests(loaded, held, {}, ("0012",))[0]["fields"])
    genus.certify(tmp_path, loaded, held, ("0012",), time.time() + 120, fields=("integer_valued", "discriminant_form"))
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


def test_a_computed_chamber_is_certified_by_its_program_and_joins_no_reference(tmp_path: Path) -> None:
    """#36: a chamber no source prints cites none; its certificate names the operation and its revision."""
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "0125.md", tmp_path / "lattices")
    path = tmp_path / "lattices" / "0125.md"
    document = frontmatter.load(str(path))
    held: certificates.Certificates = {}
    without("0125", "integral", document.metadata, held, "integral.cusp_chambers")
    path.write_text(records.record_text(corpus.front_matter(document), document.content))
    references = list(corpus.front_matter(corpus.read_card(path))["references"])

    row = {
        "walls": [{"name": "w_1", "vector": [0, -1]}, {"name": "w_2", "vector": [1, -1]}],
        "wall_count": 2,
        "gram": [["-4", "2"], ["2", "-4"]],
        "diagram": [{"a": "w_1", "b": "w_2", "order": 4}],
        "ideal_vertices": 1,
    }
    by = "computed, not cited: fundamental_chamber(max_roots=20, max_decompositions=2000) at sage-extensions deadbeef."
    genus.store_cusp_chambers(path, "O", [row], by, held)
    metadata = corpus.front_matter(corpus.read_card(path))
    stored = metadata["integral"]["cusp_chambers"]["O"][0]
    assert (stored.get("statement"), stored.get("printed_page"), stored.get("reference")) == (None, None, None), (
        "a computed chamber states no source"
    )
    assert metadata["references"] == references, "a computed row joins no citation to the card"
    lattice = Lattice.model_validate(metadata)
    computation = genus.name("0125", "cusp_chambers", lattice.definiteness)
    digest = certificates.certification_hash(computation, lattice, genus.certified_value("cusp_chambers", metadata["integral"]["cusp_chambers"], lattice))
    assert lattice.certifications["integral.cusp_chambers"] == digest == held[computation].hash
    assert held[computation].by == by, "the certificate names the program, not a source"
    assert genus.store_cusp_chambers(path, "O", [row], by, held) is None and corpus.front_matter(corpus.read_card(path))["certifications"]["integral.cusp_chambers"] == digest, (
        "writing the same row twice is the same certificate"
    )


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


def coble_corpus(root: Path) -> Path:
    """The Coble card with its two arithmetic-group cards, and nothing else."""
    (root / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, root / corpus.FAMILIES_FILE)
    (root / corpus.RETIRED_FILE).write_text("{}\n")
    shutil.copy(REPOSITORY / "lattices" / "6JRR.md", root / "lattices")
    (root / "arithmetic-groups").mkdir()
    for slug in ("otilde-t-co", "otilde-plus-t-co"):
        shutil.copy(REPOSITORY / "arithmetic-groups" / f"{slug}.md", root / "arithmetic-groups")
    return root


def certify_index(root: Path, slug: str, index: int) -> certificates.Certificates:
    """Store an index on the group card and its matching certificate on the lattice card."""
    path = root / "arithmetic-groups" / f"{slug}.md"
    document = frontmatter.load(str(path))
    document.metadata["data"] = {**(document.metadata.get("data") or {}), "index_in_orthogonal_group": index}
    path.write_text(frontmatter.dumps(document))
    card = root / "lattices" / "6JRR.md"
    lattice_document = frontmatter.load(str(card))
    lattice = Lattice.model_validate(corpus.front_matter(lattice_document))
    field = f"{genus.ARITHMETIC_PREFIX}{slug}.index_in_orthogonal_group"
    computation = genus.name("6JRR", field, lattice.definiteness)
    digest = certificates.certification_hash(computation, lattice, index)
    lattice_document.metadata["certifications"] = {**(lattice_document.metadata.get("certifications") or {}), field: digest}
    card.write_text(frontmatter.dumps(lattice_document))
    return {computation: certificates.Certificate(hash=digest, by="test")}


def requested_fields(root: Path, held: certificates.Certificates) -> set[str]:
    # `corpus.cards` is what `latticedb certify --tag 6JRR` loads, so the request is built from it.
    return {field for request in genus.requests(corpus.cards(root, ("6JRR",)), held, {}, ("6JRR",)) for field in request["fields"]}


def test_a_per_tag_load_carries_the_arithmetic_group_cards_of_its_lattices(tmp_path: Path) -> None:
    """The tag-scoped reader #30 introduced must give the group cards a certification request needs."""
    root = coble_corpus(tmp_path)
    other = root / "arithmetic-groups" / "gamma-en-2.md"
    other.write_text(frontmatter.dumps(frontmatter.load(str(REPOSITORY / "arithmetic-groups" / "gamma-en-2.md"))))
    loaded = corpus.cards(root, ("6JRR",))
    assert [entry.value.slug for entry in loaded.arithmetic_groups] == ["otilde-plus-t-co", "otilde-t-co"]
    assert corpus.cards(root, ("6JRR",)).families == {}


def test_the_coble_card_requests_the_index_and_generators_of_its_group_cards(tmp_path: Path) -> None:
    """#7: the two group cards state an index and generators, and both are asked from this card's Gram tensor."""
    root = coble_corpus(tmp_path)
    requested = genus.requests(corpus.cards(root, ("6JRR",)), {}, {}, ("6JRR",))
    fields = {field for request in requested for field in request["fields"]}
    assert {
        "arithmetic-group.otilde-t-co.index_in_orthogonal_group",
        "arithmetic-group.otilde-t-co.generator_morphisms",
        "arithmetic-group.otilde-plus-t-co.index_in_orthogonal_group",
        "arithmetic-group.otilde-plus-t-co.generator_morphisms",
    } <= fields
    groups = {(str(group["slug"]), str(group["standard_name"])) for request in requested for group in request.get("arithmetic_groups", [])}
    assert groups == {("otilde-t-co", "Otilde"), ("otilde-plus-t-co", "Otilde+")}
    assert genus.name("6JRR", "arithmetic-group.otilde-t-co.index_in_orthogonal_group") == "6JRR arithmetic-group.otilde-t-co.index_in_orthogonal_group"


def test_a_completed_arithmetic_group_index_is_not_requested_again(tmp_path: Path) -> None:
    """A matching completed certificate is reused, and a different stored index is computed again."""
    root = coble_corpus(tmp_path)
    held = certify_index(root, "otilde-t-co", 46998591897600)
    fields = requested_fields(root, held)
    assert "arithmetic-group.otilde-t-co.index_in_orthogonal_group" not in fields
    assert "arithmetic-group.otilde-t-co.generator_morphisms" in fields
    changed = frontmatter.load(str(root / "arithmetic-groups" / "otilde-t-co.md"))
    changed.metadata["data"] = {**(changed.metadata.get("data") or {}), "index_in_orthogonal_group": 2}
    (root / "arithmetic-groups" / "otilde-t-co.md").write_text(frontmatter.dumps(changed))
    assert "arithmetic-group.otilde-t-co.index_in_orthogonal_group" in requested_fields(root, held)


def test_a_computed_generator_is_stored_once_as_a_self_isometry_of_the_lattice(tmp_path: Path) -> None:
    """The matrix is a `morphisms` entry of the lattice card; the group card states its name."""
    root = coble_corpus(tmp_path)
    matrix = [[1 if row == column else 0 for column in range(11)] for row in range(11)]
    stored = genus.store_arithmetic_group(root, "6JRR", "otilde-plus-t-co", {"index_in_orthogonal_group": 93997183795200, "generator_morphisms": [matrix]})
    lattice = Lattice.model_validate(corpus.front_matter(corpus.read_card(root / "lattices" / "6JRR.md")))
    self_isometries = [morphism for morphism in lattice.morphisms if morphism.target == "6JRR" and morphism.scale == 1]
    # The card already states the 126 generators of O(L) that CI certified, so the test counts the
    # matrix it stored once among them rather than the whole `morphisms` list.
    stored_once = [morphism for morphism in self_isometries if morphism.matrix == tuple(tuple(row) for row in matrix)]
    assert len(stored_once) == 1
    group = ArithmeticGroup.model_validate(corpus.front_matter(corpus.read_card(root / "arithmetic-groups" / "otilde-plus-t-co.md")))
    assert group.data.generator_morphisms == (stored_once[0].name,)
    assert group.data.index_in_orthogonal_group == 93997183795200
    assert dict(stored) == {"generator_morphisms": [matrix], "index_in_orthogonal_group": 93997183795200}
    # The name is what the certificate commits to indirectly: it commits to the matrix.
    assert genus.certified_value("arithmetic-group.otilde-plus-t-co.generator_morphisms", list(group.data.generator_morphisms or ()), lattice) == [matrix]


def test_a_stated_arithmetic_group_value_without_its_computation_is_a_verification_problem(tmp_path: Path) -> None:
    """A group card states what a completed computation returned, or it states nothing."""
    root = coble_corpus(tmp_path)
    path = root / "arithmetic-groups" / "otilde-t-co.md"
    document = frontmatter.load(str(path))
    data = dict(document.metadata.get("data") or {})
    # This test isolates the index certificate.  The fixture's real card also
    # carries generator_morphisms, whose independent certificate is deliberately
    # not copied into this temporary corpus.
    data.pop("generator_morphisms", None)
    data["index_in_orthogonal_group"] = 46998591897600
    document.metadata["data"] = data
    path.write_text(frontmatter.dumps(document))
    card = root / "lattices" / "6JRR.md"
    lattice_document = frontmatter.load(str(card))
    certifications = dict(lattice_document.metadata.get("certifications") or {})
    certifications.pop("arithmetic-group.otilde-t-co.generator_morphisms", None)
    lattice_document.metadata["certifications"] = certifications
    card.write_text(frontmatter.dumps(lattice_document))
    problems = checks.records.problems(corpus.load(root), {}, frozenset({"6JRR"}))
    assert any("arithmetic group otilde-t-co: the stated index_in_orthogonal_group" in problem for problem in problems), problems
    held = certify_index(root, "otilde-t-co", 46998591897600)
    assert not any("arithmetic group otilde-t-co:" in problem for problem in checks.records.problems(corpus.load(root), held, frozenset({"6JRR"})))


def test_the_arithmetic_group_index_is_the_order_of_the_finite_character_image() -> None:
    r"""#7: `[O(L):Gamma]` is the owner's finite character image, not a coset enumeration.

    Every standard subgroup is a kernel, or an intersection of kernels, of characters into finite
    groups, so `O(L)/Gamma` embeds in the finite product of their images and the index is the
    quotient of two finite orders. On a specimen whose discriminant group is small enough for the
    owner to also walk the cosets, both answers agree; on 6JRR the coset space of
    $\widetilde O(T_{\mathrm{Co}})$ has 46998591897600 points, which is exactly the finite order
    $|O(A_L,q)|$ that answers without enumerating them.
    """
    from sage_extensions.categories.lattices import Lattices
    from sage_extensions.rings import ZZ as owned_integers

    lattice = Lattices(owned_integers)([[2, 1], [1, 2]])
    assert int(lattice.discriminant_group().orthogonal_group().cardinality()) == 2
    for standard, cosets in (("Otilde", 2), ("Otilde+", 4)):
        group = sage_genus._standard_subgroup(lattice, standard)
        assert int(group.index()) == cosets
        assert sage_genus._arithmetic_group_value(group, "index_in_orthogonal_group") == cosets


def test_the_enriques_group_states_the_index_its_certificate_establishes() -> None:
    r"""#43: card 029J's `gamma-en-2` index is established, not merely stated.

    `genus.arithmetic_requests` cannot ask the owner for this one: the group is defined by a source,
    has no `standard_name`, and "has no owner operation that presents it" (`genus.py:293`), so
    `certify` never requests it while `checks.records.arithmetic_problems` reports a stated value
    nothing establishes. The value is the library's own answer --- the index in $O(T_{\mathrm{En}})$
    of the coinvariant extension subgroup of the Enriques involution --- and
    `results/certify-43-gamma-en2-index.py` is the computation that returns it, with the certificate's
    hash committing to the index and to this card's Gram tensor. This test states that the card and
    the certificate still agree, so a changed value must bring a new hash.
    """
    root = Path(__file__).resolve().parent.parent
    held = certificates.load(root, tags=("029J",))
    loaded = corpus.cards(root, ("029J",))
    entry = next(entry for entry in loaded.entries if entry.lattice.tag == "029J")
    assert checks.records.arithmetic_problems(loaded, held, entry) == []
    group = next(card.value for card in loaded.arithmetic_groups if card.value.slug == "gamma-en-2")
    assert group.data.index_in_orthogonal_group == 67456
    field = "arithmetic-group.gamma-en-2.index_in_orthogonal_group"
    computation = genus.name("029J", field, entry.lattice.definiteness)
    certificate = held[computation]
    assert entry.lattice.certifications[field] == certificate.hash
    assert certificate.by is not None
    assert "Remark 2.12, p. 8" in certificate.by and "2^7 17 31" in certificate.by


def test_a_local_density_prints_the_text_a_fraction_rejects() -> None:
    """#4: the value `_local_densities` receives prints `(3)/(2)`, stated on the owner's own object.

    The end-to-end test above states the value the card stores; this states the premise, so item 2
    cannot pass silently when the preamble's printing changes. It sits at the end of the file, after
    every test that starts a certify worker, because it loads the preamble into this process and a
    worker started afterwards has less memory and time to run in.
    """
    from sage_extensions.categories.lattices import Lattices
    from sage_extensions.rings import ZZ as owned_integers

    card = frontmatter.load(str(REPOSITORY / "lattices" / "0022.md")).metadata
    density = Lattices(owned_integers)(card["gram_tensor"]).genus().local_density(2, 1)
    assert str(density) == "(3)/(2)"
    with pytest.raises(ValueError):
        Fraction(str(density))
    assert sage_genus._rational(density) == "3/2"
