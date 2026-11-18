"""Verification checks stated claims without requiring enrichment to finish."""

from __future__ import annotations

from pathlib import Path

import pytest

from latticedb import certificates, checks, corpus, records
from latticedb.cli import app
from latticedb.model import Lattice, Yaml


def write_card(root: Path, fields: dict[str, Yaml]) -> Path:
    (root / "lattices").mkdir()
    (root / corpus.FAMILIES_FILE).write_text("{}\n")
    (root / corpus.RETIRED_FILE).write_text("{}\n")
    path = root / "lattices" / "0001.md"
    path.write_text(records.record_text({"tag": "0001", "name": "Sparse card", "latex": "S", **fields}, "A source claim."))
    return path


@pytest.mark.parametrize(
    "fields",
    [
        {},
        {"gram_tensor": [[2]]},
        {"rank": 1, "integral": {"parity": "even"}},
        {"rank": 1, "gram_tensor": [[2]], "integral": {"parity": "even"}},
    ],
)
def test_unknown_fields_do_not_make_a_valid_card_a_verification_error(tmp_path: Path, fields: dict[str, Yaml]) -> None:
    write_card(tmp_path, fields)
    assert checks.report(tmp_path) == ()


def test_partial_cards_still_have_their_completed_certificates_checked(tmp_path: Path) -> None:
    path = write_card(tmp_path, {"gram_tensor": [[2]], "integral": {"parity": "even", "genus_class_count": 1}})
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    lattice = Lattice.model_validate(metadata)
    digest = certificates.certification_hash("0001 integral.genus_class_count", lattice, 1)
    metadata["certifications"] = {"integral.genus_class_count": digest}
    path.write_text(records.record_text(metadata, document.content))
    certificates.save(tmp_path, {"0001 integral.genus_class_count": certificates.Certificate(hash=digest, by="test")})
    assert checks.report(tmp_path) == ()

    metadata["integral"] = {"parity": "even", "genus_class_count": 2}
    path.write_text(records.record_text(metadata, document.content))
    assert any("contradicts its completed computation certificate" in problem for problem in checks.report(tmp_path))


def test_a_certificate_without_its_defining_gram_tensor_is_an_error(tmp_path: Path) -> None:
    write_card(tmp_path, {"certifications": {"integral.genus_class_count": "0" * 64}})
    assert any("certificate" in problem.lower() and "Gram tensor" in problem for problem in checks.report(tmp_path))


def test_a_shard_states_the_cards_it_verified_with_its_peak(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """#6: a shard's peak line names the shard and its card count, before any problem refuses the run."""
    write_card(tmp_path, {})
    mine = certificates.tag_hash("0001") % 2
    app(["verify", "--shard", f"{mine}/2", "--root", str(tmp_path)], result_action="return_value")
    assert f"for 1 cards in shard {mine}/2" in capsys.readouterr().out


def test_a_shard_on_a_runner_annotates_the_peak_a_log_alone_would_not_expose(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    """#6: under Actions the peak line is also an annotation, which reads back where a job log does not."""
    write_card(tmp_path, {})
    mine = certificates.tag_hash("0001") % 2
    arguments = ["verify", "--shard", f"{mine}/2", "--root", str(tmp_path)]
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    app(arguments, result_action="return_value")
    plain = capsys.readouterr().out
    assert "::notice" not in plain
    assert f"memory: " in plain and f"for 1 cards in shard {mine}/2" in plain
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    app(arguments, result_action="return_value")
    annotated = capsys.readouterr().out
    assert f"::notice title=shard {mine}/2::memory: " in annotated
    assert f"for 1 cards in shard {mine}/2" in annotated


def test_a_shard_reports_the_problems_of_its_own_cards_only(tmp_path: Path) -> None:
    """#6: the shards partition the cards, and each run checks the cards of its own shard."""
    path = write_card(tmp_path, {"gram_tensor": [[2]], "rank": 1})
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    metadata["certifications"] = {"integral.genus_class_count": "0" * 64}
    path.write_text(records.record_text(metadata, document.content))
    mine = certificates.tag_hash("0001") % 2
    assert any("contradicts its completed computation certificate" in problem for problem in checks.run(tmp_path, (mine, 2))[1])
    # `checks.run` returns the problems as the list its annotation documents, so a shard
    # with nothing to report returns none of them.
    assert checks.run(tmp_path, (1 - mine, 2))[1] == []
    assert checks.run(tmp_path, (mine, 2))[0] == 1
