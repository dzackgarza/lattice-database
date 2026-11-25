"""Regression for #17 through the application, not through source-text inspection.

Runs `results/regression-recovery-defects.py` inside the supported image. The test doesn't stub Sage,
projections, or the verifier's required values.
"""
import subprocess
import sys
from pathlib import Path


def test_recovery_with_a_retained_attempt_and_then_a_deletion_fails() -> None:
    artifacts = Path("attachments/you-work-the-github-s6pa/extracted/openmath-certify-42326648686")
    if not artifacts.is_dir():
        # Supported acceptance requires the retained run's data and the owner runtime.
        import pytest
        pytest.skip("the retained run artifacts must be attached")
    root = Path(__file__).resolve().parent.parent
    verifier = root / "results" / "verify-recovered-values.py"
    subprocess.run(
        [sys.executable, str(root / "results" / "regression-recovery-defects.py"), str(verifier)],
        check=True,
        cwd=root,
    )


def test_a_missing_owned_field_from_a_retained_patch_must_prevent_recovery_acceptance() -> None:
    """Exercise `git apply` on one artifact and omission detection through the real verifier."""
    root = Path(__file__).resolve().parent.parent
    artifacts = root / "attachments/you-work-the-github-s6pa/extracted/openmath-certify-42326648686"
    if not artifacts.is_dir():
        import pytest
        pytest.skip("retained run artifacts must be attached")
    subprocess.run(
        [sys.executable, str(root / "results" / "regression-recovery-coverage.py"),
         str(root / "results" / "verify-recovered-values.py")],
        check=True,
        cwd=root,
    )
