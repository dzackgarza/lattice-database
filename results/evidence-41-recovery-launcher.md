# #41: the recovery launcher reported no result because the image wrapper needs HOME

Reproduction and repair. The launcher's own result requirement (#22) was never in question: no guest
ran at all.

## What the sweep showed

`tests` sweep on the chat VM (2026-11-12 05:19, main `cfa35c3b24`, sage-extensions `5a9874e22ea18`,
recorded in `.scratch/stacksweep2.log` of that tree and quoted in lattice-database#38). Both tests of
`tests/test_recovery_launcher.py` failed, and the regression reported **every** case the same way:

    case normal:     launcher rc=1 (want 0), PYEXIT=absent, results=0
    case duplicate:  launcher rc=1 (want 1), PYEXIT=absent, results=0
    case incomplete: launcher rc=1 (want 1), PYEXIT=absent, results=0
    case short:      launcher rc=1 (want 1), PYEXIT=absent, results=0
    case raise:      launcher rc=1 (want 1), PYEXIT=absent, results=0
    case segv:       launcher rc=1 (want 1), PYEXIT=absent, results=0

`PYEXIT=absent` with `results=0` means the guest never printed a line, so the wrapper failed before
proot started rather than the guest behaving unexpectedly. The sweep also names where the tests ran:
the failed assertion records `CompletedProcess(args=['sh', '/repo/results/launcher-regression.sh'])`,
and `/repo` is the checkout's path **inside** the image. Those tests ran in the image, not on the host.

## The cause

`sage-image/run.sh` line 6-7:

    set -euo pipefail
    ROOT=${ROOT:-$HOME/sage-image/rootfs}
    PROOT=${PROOT:-$HOME/.udocker/bin/proot-x86_64}

and it runs its guest under the image's OCI environment, from `env.oci`, which **carries no HOME**.
Inside the image, HOME is unset, so the wrapper dies at line 7 under `set -u` before proot exists:

    $ run.sh ... /bin/sh -c 'sh results/launcher-regression.sh'    # inside the image
    HOME=[]
    /workspace/nucleus/work/home/sage-image/run.sh: line 7: HOME: unbound variable

That is the whole log of each case: no `PYEXIT=` line and no result, which is exactly the reported
`PYEXIT=absent, results=0`. Measured on this VM: the same regression on the host, with HOME set,
passed all six cases before any change. So the launcher was correct about what it requires, and the
environment it was run in never started a guest.

Inside the image the wrapper is present because the sweep binds the home that holds `sage-image/`, at
the same absolute path; a CI runner without that bind would still skip, as the test module says.

## Reproduction, before and after

| where | HOME | `results/verify-launcher.sh` before | after |
| --- | --- | --- | --- |
| host | set | REGRESSION PASS | REGRESSION PASS |
| host | unset | REGRESSION FAIL, six cases `PYEXIT=absent, results=0` | REGRESSION PASS |
| inside the image | unset | REGRESSION FAIL, `run.sh: line 7: HOME: unbound variable` | REGRESSION PASS |

The middle row is the same defect on the host: it is what the image run hit. `env -u HOME sh
results/launcher-regression.sh` reproduces the sweep's six lines exactly.

## The repair

`results/launcher-environment.sh` (new) resolves the wrapper's parts once, for the launcher and its
unrepaired counterpart: `SAGE_IMAGE` names the wrapper, and its rootfs and proot sit beside it
(`<wrapper dir>/rootfs`, `<wrapper dir>/../.udocker/bin/proot-x86_64`), overridable by `SAGE_ROOTFS`
and `SAGE_PROOT`, with the wrapper's own HOME-based paths as a fallback. They are passed to the
wrapper explicitly, so the wrapper no longer depends on HOME being set.

`results/verify-launcher.sh` additionally:

- names the first missing part before launching — the wrapper, its rootfs or proot — instead of
  reporting only that its own result was absent;
- writes that refusal into the log as well as stdout, so a caller reading the log finds the cause
  rather than a missing file, and creates the log's directory;
- prints the first line of the guest log when the run fails, so a wrapper or guest that stopped early
  reports what it said, not only `PYEXIT=absent`;
- reports an absent research checkout as a warning naming the path, since a Python guest imports the
  preamble through that bind, and does not refuse to launch over it;
- answers `--check` with that same answer and launches nothing, which is what
  `tests/test_recovery_launcher.py` now skips on, so a wrapper that cannot start is a named skip
  rather than a test failure.

`results/verify-launcher-unrepaired.sh` keeps its defect — it reports the wrapper's own status and
requires no result — and takes the same launch environment, so the two differ only in what they
require of the result.

## Checked

- `python3 -m pytest tests/test_recovery_launcher.py -q` on the host: **2 passed in 8.75s**.
- the same two tests inside the image, with HOME unset and the home bound at its host path (the
  sweep's configuration): **2 passed in 61.00s** — the repaired launcher's six cases and the
  unrepaired path's six, through nested proot.
- `env -u HOME sh results/launcher-regression.sh` on the host: REGRESSION PASS, and
  `results/launcher-regression.sh results/verify-launcher-unrepaired.sh`: REGRESSION FAIL with
  `{normal: 0, raise: 1, duplicate: 0, incomplete: 0, short: 0, segv: 0}`, the red pattern the second
  test asserts.
- the skip path names the missing part: with `SAGE_IMAGE=/nonexistent/run.sh`,
  `2 skipped … launcher: cannot run: the image wrapper is absent at /nonexistent/run.sh (SAGE_IMAGE
  names it)`.
- the normal case writes its results: `.scratch/lreg3/launcher-normal.log` holds
  `4ec0a9d032: 509 cards, 0 problems`, `b29b4ba832: 674 cards, 0 problems`, the summary line and
  `PYEXIT=0`.
- `just test`: 74 passed.

Not run: the complete suite (the whole-corpus read and `validation/test_build.py` need more memory
than this VM has, per #38), and `just test-push`, which inspects outgoing commits against a remote
named `origin` and this checkout's remote is `omm`.

## Still outside this repository

`sage-image/run.sh` expands `$HOME` under `set -u` while the image's OCI environment carries no HOME.
That file is outside the repositories this session can write to, so the wrapper keeps the hazard and
every in-repo caller now passes `ROOT` and `PROOT` in. A wrapper-side default that tolerates an unset
HOME, e.g. `${HOME:-/nonexistent}/sage-image/rootfs`, would remove it for other callers too.
