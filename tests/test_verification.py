"""Verification checks stated claims without requiring enrichment to finish."""

from __future__ import annotations

from pathlib import Path

import pytest
from latticedb import certificates, checks, corpus, records
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
