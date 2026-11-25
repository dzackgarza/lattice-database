"""#22 through the real recovery path: the launcher of record, the image wrapper and a controlled guest.

`results/verify-launcher.sh` is the launcher the #20 recovery checks run under: it starts the check
inside the published image and reports success only when the guest's own status says 0, every
expected per-item result is there and distinct, and the final summary is present. It has to be that
way because the image wrapper (`sage-image/run.sh`, proot) reports 0 for a guest killed by a signal
while carrying an ordinary exit code through, so an outer status is not evidence that the work
finished (`results/image-wrapper-defect.md`, job jmw6ug2ma).

These run `results/launcher-regression.sh`, which launches six controlled guests through a launcher
and asserts that launcher's own return code per case:

- the launcher of record passes all six: a complete run, one item reported twice, a missing summary,
  a missing item, a nonzero guest status and a guest killed by SIGSEGV;
- the unrepaired launch path (`results/verify-launcher-unrepaired.sh`, the pattern the launcher had
  before the repair) fails the four incomplete and death cases, so the regression is not the assertion
  that a shell script can exit 0.

Where the launcher cannot start a guest the tests skip, and the launcher's own `--check` names the
part that is missing (the wrapper, its rootfs or proot): a CI runner has the container image, not
this VM's proot launcher, and the launcher is not what those runners use. `--check` also covers #41,
where the suite ran inside the image with the wrapper present but `$HOME` unset, so the wrapper died
at its own line 7 before proot and every case reported an absent status and no result.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPOSITORY = Path(__file__).resolve().parent.parent

REPAIRED = REPOSITORY / "results" / "verify-launcher.sh"
UNREPAIRED = REPOSITORY / "results" / "verify-launcher-unrepaired.sh"
REGRESSION = REPOSITORY / "results" / "launcher-regression.sh"

CASES = ("normal", "duplicate", "incomplete", "short", "raise", "segv")


def launcher_refusal() -> str | None:
    """Why `results/verify-launcher.sh` cannot start a guest here, or None when it can.

    The launcher owns the rule, so the tests ask it rather than guessing from the wrapper's presence:
    `--check` names the first part it needs and does not have (the wrapper, its rootfs or proot) and
    launches nothing. A wrapper that is present but cannot start is not a test failure (#41).
    """
    checked = subprocess.run(
        ["sh", str(REPAIRED), "--check"], capture_output=True, text=True, check=False
    )
    if checked.returncode == 0:
        return None
    return checked.stdout.strip() or f"launcher --check exited {checked.returncode}"


REFUSAL = launcher_refusal()

requires_image = pytest.mark.skipif(REFUSAL is not None, reason=REFUSAL or "")


def run_regression(tmp_path: Path, launcher: Path | None = None) -> subprocess.CompletedProcess[str]:
    """Run the launcher regression, keeping its logs out of the checkout."""
    command = ["sh", str(REGRESSION)] + ([str(launcher)] if launcher is not None else [])
    return subprocess.run(
        command,
        cwd=REPOSITORY,
        capture_output=True,
        text=True,
        env={**os.environ, "LAUNCHER_LOG_DIR": str(tmp_path)},
        check=False,
    )


def reported(output: str) -> dict[str, int]:
    """Each case's launcher return code, as the regression reports it."""
    found: dict[str, int] = {}
    for line in output.splitlines():
        if not line.startswith("case "):
            continue
        mode, _, rest = line[len("case ") :].partition(": launcher rc=")
        found[mode] = int(rest.split(" ", 1)[0])
    return found


@requires_image
def test_the_recovery_launcher_requires_every_result_and_the_guest_status(tmp_path: Path) -> None:
    """The launcher of record passes the complete run and every incomplete or dying one it must refuse."""
    finished = run_regression(tmp_path)
    assert "REGRESSION PASS" in finished.stdout, finished.stdout + finished.stderr
    assert finished.returncode == 0
    assert reported(finished.stdout) == {mode: (0 if mode == "normal" else 1) for mode in CASES}


@requires_image
def test_the_regression_fails_on_the_unrepaired_launch_path(tmp_path: Path) -> None:
    """The same cases, on the pre-fix path: it accepts a run that died and a run that lost an item."""
    finished = run_regression(tmp_path, UNREPAIRED)
    assert "REGRESSION FAIL" in finished.stdout, finished.stdout + finished.stderr
    assert finished.returncode != 0
    assert reported(finished.stdout) == {
        "normal": 0,
        "raise": 1,
        "duplicate": 0,
        "incomplete": 0,
        "short": 0,
        "segv": 0,
    }, "the complete run passes and an ordinary nonzero status propagates; every other case is accepted"
