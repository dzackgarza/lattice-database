#!/bin/sh
# Run a recovery check inside the published image and require its result, not the wrapper's silence.
#
# The image wrapper (`sage-image/run.sh`, proot) reports exit 0 when the guest process dies of a
# signal: measured on this VM, `python -c 'os.kill(os.getpid(), SIGSEGV)'` and the same with SIGKILL
# both return 0 through the wrapper, while `raise SystemExit(3)` and `os._exit(4)` return 3 and 4.
# So a wrapper exit of 0 says nothing about whether the work finished. This is the pattern
# research#749 repaired for its own launcher: echo the guest child's status inside the guest, where
# proot cannot touch it, and report success only when that status is 0 *and* the anchored result lines
# are present. The per-item lines must also be distinct: a guest that prints one item's result twice
# has produced none for the other, and a count alone would accept it (#22).
#
# The wrapper's own prerequisites are resolved here, and a missing one is named before the guest is
# started (#41). `sage-image/run.sh` expands `$HOME/sage-image/rootfs` and
# `$HOME/.udocker/bin/proot-x86_64` under `set -u`, and the image's OCI environment (`env.oci`)
# carries no HOME. A run of this launcher inside the image therefore died at the wrapper's line 7
# with `HOME: unbound variable`, before proot existed: the log held no `PYEXIT=` line and no result,
# and the report said only `PYEXIT=absent, results=0`. The rootfs and proot are found beside the
# wrapper that `SAGE_IMAGE` names, so the wrapper no longer needs HOME, and when either is absent the
# launcher says which one instead of reporting only its own failure. `results/launcher-environment.sh`
# resolves them for this launcher and its unrepaired counterpart. `--check` reports the same answer
# without launching anything, so a caller can skip rather than fail where the wrapper cannot run.
#
# usage: results/verify-launcher.sh LOG EXPECTED_RESULTS SCRIPT [ARGS...]
#        results/verify-launcher.sh --check
#   EXPECTED_RESULTS  how many per-item result lines the check must print
#   --check           name the first missing prerequisite and exit 1, or print where the wrapper,
#                     rootfs and proot are and exit 0; launches nothing
# The anchored patterns are the check's own result shape, overridable per check:
#   RESULT_RE   a per-item result line   (default: `<sha>: <n> cards, <m> problems`)
#   SUMMARY_RE  the one final summary    (default: `<n> problems in <m> recovered cards over <k> commits`)
# A check that cannot state its result in those two shapes cannot be launched through here, which is
# the point: the launcher requires the result rather than trusting an exit status.
#
# Where the parts come from: `results/launcher-environment.sh` resolves the wrapper (SAGE_IMAGE), the
# rootfs and proot it runs (SAGE_ROOTFS, SAGE_PROOT) and passes them in; RESEARCH_CHECKOUT names the
# research checkout the guest imports the preamble from, and its absence is reported but not fatal.
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
. "$REPO/results/launcher-environment.sh"
RESEARCH=${RESEARCH_CHECKOUT:-/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo}
RESULT_RE=${RESULT_RE:-'^[0-9a-f]{7,}: [0-9]+ cards, [0-9]+ problems$'}
SUMMARY_RE=${SUMMARY_RE:-'^[0-9]+ problems in [0-9]+ recovered cards over [0-9]+ commits$'}

# The first part the wrapper needs and does not have, or nothing when it can start a guest.
missing_prerequisite() {
  if [ ! -e "$IMAGE" ]; then
    echo "the image wrapper is absent at $IMAGE (SAGE_IMAGE names it)"
  elif [ ! -x "$IMAGE" ]; then
    echo "the image wrapper is not executable at $IMAGE (SAGE_IMAGE names it)"
  elif [ ! -d "$ROOT" ]; then
    echo "the image rootfs is absent at $ROOT (SAGE_ROOTFS names it; the wrapper reads \$HOME/sage-image/rootfs, and HOME is ${HOME:-unset})"
  elif [ ! -x "$PROOT" ]; then
    echo "proot is absent at $PROOT (SAGE_PROOT names it; the wrapper reads \$HOME/.udocker/bin/proot-x86_64, and HOME is ${HOME:-unset})"
  fi
}

if [ "${1:-}" = --check ]; then
  missing=$(missing_prerequisite)
  if [ -n "$missing" ]; then
    echo "launcher: cannot run: $missing"
    exit 1
  fi
  echo "launcher: ready (wrapper $IMAGE, rootfs $ROOT, proot $PROOT)"
  exit 0
fi

usage="usage: results/verify-launcher.sh LOG EXPECTED_RESULTS SCRIPT [ARGS...]"
LOG=${1:?"$usage"}
EXPECT=${2:?"$usage"}
SCRIPT=${3:?"$usage"}
shift 3
SCRIPT=${SCRIPT#"$REPO"/}

# A Python check runs under the image's interpreter; a shell check is run as it is.
case "$SCRIPT" in
  *.sh) RUNNER=/bin/sh ;;
  *)    RUNNER=/sage/.venv/bin/python ;;
esac

# Name what the launch needs and does not have, rather than reporting only that no result appeared.
# The refusal goes in the log as well as on stdout: a caller that reads the log would otherwise find
# no file at all and report a missing path instead of the missing part.
mkdir -p "$(dirname "$LOG")" 2>/dev/null || true
refuse() {
  echo "launcher: FAILURE (cannot start: $1)"
  printf 'launcher: FAILURE (cannot start: %s\n' "$1" >> "$LOG" 2>/dev/null || true
  exit 1
}
missing=$(missing_prerequisite)
[ -n "$missing" ] && refuse "$missing"
[ -f "$REPO/$SCRIPT" ] || refuse "the guest script is absent at $REPO/$SCRIPT"
if [ ! -d "$RESEARCH" ]; then
  echo "launcher: warning: the research checkout is absent at $RESEARCH, so /repo/research holds only what the image already has; RESEARCH_CHECKOUT names it"
fi

ROOT="$ROOT" PROOT="$PROOT" "$IMAGE" -w /repo \
  -b "$REPO:/repo" \
  -b "$RESEARCH:/repo/research" \
  /bin/sh -c 'interp=$1; shift; /usr/bin/env PYTHONPATH=/repo/research/src:/repo/src "$interp" -u "$@"; echo "PYEXIT=$?"' sh \
  "$RUNNER" "/repo/$SCRIPT" "$@" > "$LOG" 2>&1
prc=$?

pyexit=$(sed -n 's/^PYEXIT=//p' "$LOG" | tail -1)
results=$(grep -Ec "$RESULT_RE" "$LOG")
distinct=$(grep -E "$RESULT_RE" "$LOG" | sort -u | wc -l)
summary=$(grep -Ec "$SUMMARY_RE" "$LOG")

if [ "$pyexit" = 0 ] && [ "$results" -eq "$EXPECT" ] && [ "$distinct" -eq "$EXPECT" ] && [ "$summary" -eq 1 ]; then
  echo "launcher: SUCCESS (proot rc=$prc, PYEXIT=$pyexit, $results/$EXPECT results, all distinct, summary present)"
  exit 0
fi
echo "launcher: FAILURE (proot rc=$prc, PYEXIT=${pyexit:-absent}, results $results/$EXPECT with $distinct distinct, summary $summary)"
# A failed launch has to say what the wrapper or the guest said, or the cause is only in the log.
first=$(sed -n '1p' "$LOG")
if [ -n "$first" ]; then
  echo "launcher: the guest log begins: $first"
fi
exit 1
