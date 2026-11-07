# The image wrapper reports 0 when its guest dies of a signal

Recorded while recovering run 42363689427 (#20). Reproduction and scope only; no claim about what
killed any particular process.

## Reproduction on this VM

`sage-image/run.sh` (proot launcher; `exec proot ... /usr/bin/env -i ... "$@"`) with a guest that
does one thing and stops:

| guest | wrapper exit |
| --- | --- |
| `python -c 'raise SystemExit(3)'` | 3 |
| `python -c 'os._exit(4)'` | 4 |
| `python -c 'print("header"); raise SystemExit(1)'` | 1 |
| `python -c 'os.kill(os.getpid(), SIGSEGV)'` | **0** |
| `python -c 'os.kill(os.getpid(), SIGKILL)'` | **0** |

So an ordinary exit code is carried through and a signal death is not: the wrapper reports success.
Anything whose only evidence is "the outer command returned 0" accepts a guest that was killed.

## Observed in this session

Background job `jmw6ug2ma` ran

    run.sh -w /repo -b "$PWD:/repo" -b <research>:/repo/research \
      /usr/bin/env PYTHONPATH=... /sage/.venv/bin/python -u results/verify-run-42363689427.py <16 commits>

and ended, per the job record, **exit 0 after 11 min 36 s**, with its whole output being one line:

    16 commits, 8999 cards touched

No per-commit result, no final summary, no traceback. The same run under the per-commit verifier
prints a `<commit>: <n> cards, <m> problems` line per commit as it goes and a summary at the end, so
a completed run cannot look like this. What killed the guest is **not established**: a masked
signal death is one explanation and the mechanism above is independent of which signal it was, but
no process or kernel evidence of a particular cause was collected, and none is claimed.

## The owner's repaired pattern

`sage-extensions`-adjacent work in research#749 diagnosed the same masking and repaired its launcher
(`computations/reports/cusp-run-launcher.sh`): run the child inside the guest and echo `PYEXIT=$?`
there, where proot cannot rewrite it, then report success only when that status is 0 **and** an
anchored result line is present, and otherwise exit nonzero. Its regression
(`computations/reports/cusp-launcher-regression.sh`) asserts, per controlled case, the launcher's
return code, the exact guest status, and the presence or absence of the anchored line for
`normal`, `incomplete`, `raise`, `segv` and `exit3`.

`results/verify-launcher.sh` applies that pattern here, and `results/launcher-regression.sh` holds it
to five cases, including a clean exit with a missing summary and a SIGSEGV death:
`results/evidence-20-launcher-regression.log` shows `REGRESSION PASS`.

## Filed where

**lattice-database#22**, under #20 with a blocked-by edge: the recovery launcher's incomplete-result
success. Its body records this controlled reproduction, the ordinary-exit propagation, and that the
original cause is unknown. The repair and this regression belong to #22; #20 stays the recovered card
values and certificates. The wrapper itself (`$HOME/sage-image/run.sh`) is outside the repositories
this session can write to, and this session's GitHub connection cannot publish issues, so the
upstream half is recorded in the issue body rather than filed separately.

## Suggested upstream description

> **Title:** the image wrapper reports exit 0 when its guest dies of a signal
>
> `sage-image/run.sh` returns 0 for a guest killed by SIGSEGV or SIGKILL, while it carries an
> ordinary `SystemExit(3)` and `os._exit(4)` through. Observed as job `jmw6ug2ma`: 11 min 36 s,
> exit 0, output a single header line, no traceback and no final result. Adopt research#749's
> repaired pattern (`computations/reports/cusp-run-launcher.sh`): echo the guest child's status inside
> the guest and require it to be 0 together with an anchored result line before reporting success.
> Reproduction and the case table are in `results/image-wrapper-defect.md` of the lattice-database
> checkout.
