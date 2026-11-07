"""Lightweight regressions for the two real image-exposed defects, without importing Sage.

`recovered_failures` and `genus`'s owned certificate functions are checked by the supported image;
these inspect the command itself's own control flow so that certificates whose computation is `derive`
do not enter a block/field split and so an artifact's failure attempts are asserted, not loaded unused.
"""
from pathlib import Path

import yaml


def test_the_derive_certificate_has_no_block_field_split_and_its_certificate_is_looked_up() -> None:
    """Regression: `name == "<tag> derive` must hit `records.derived_projection` first."""
    text = Path("results/verify-recovered-values.py").read_text()
    derive_first = text.index('if name.endswith(" derive"):')
    split_call = text.index('block, field = name[len(f"{tag} "):].split(".", 1)')
    assert derive_first < split_call, "block/field split precedes the derive branch"
    assert '(current_card.get("certifications") or {}).get("derive")' in text
    assert 'if actual_hash :=' not in text


def test_each_artifact_added_failure_is_checked_in_the_storage_model() -> None:
    """Regression: original attempt hashes and their model records are compared, not loaded and dropped."""
    import ast

    text = Path("results/verify-recovered-values.py").read_text()
    tree = ast.parse(text)
    all_names = {
        node.id for node in ast.walk(tree)
        if isinstance(node, ast.Name)
    } | {
        node.attr for node in ast.walk(tree)
        if isinstance(node, ast.Attribute)
    }
    assert "Fail" not in all_names
    uses = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name)
        and node.value.id == "recovered_failures"
    ]
    assert uses, "`recovered_failures` is loaded but never read"
    # Failure/Attempt validation and attempt-hash equality are exercised on the original values.
    assert "failures.load" in text
    assert "model_validate" in text
    assert "original failure attempt" in text


def test_0066_artifact_transliteration_for_the_reviewed_path() -> None:
    """The artifact used by #17 genuinely contains a record named TAG derive."""
    root = Path("attachments/you-work-the-github-s6pa/extracted/openmath-certify-42326648686")
    if not root.exists():
        import pytest
        pytest.skip("retained artifacts not attached")
    additions = []
    for artifact in sorted(root.iterdir()):
        if not artifact.is_dir():
            continue
        tag = artifact.name.split("-")[-1]
        contents = (artifact / "certification.patch").read_text()
        additions.extend(
            line[1:] for line in contents.splitlines()
            if line[:1] == "+" and line.startswith(f"+{tag} derive:")
        )
    assert additions, "no artifact's additions contain a TAG derive certificate"
    assert all(name.endswith(":") for name in additions), "each TAG derive entry is a bare computation"
    assert all("." not in name[len(tag):].strip() for name in additions), "there is no block.field suffix on TAG derive"

