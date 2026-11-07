#!/bin/sh
# Run a recovery check inside the published image and require its result, not the wrapper's silence.
#
# The image wrapper (`sage-image/run.sh`, proot) reports exit 0 when the guest process dies of a
# signal: measured on this VM, `python -c 'os.kill(os.getpid(), SIGSEGV)'` and the same with SIGKILL
# both return 0 through the wrapper, while `raise SystemExit(3)` and `os._exit(4)` return 3 and 4.
# So a wrapper exit of 0 says nothing about whether the work finished. This is the pattern
# research#749 repaired for its own launcher: echo the guest child's status inside the guest, where
# proot cannot touch it, and report success only when that status is 0 *and* the anchored result line
# is present.
#
# usage: results/verify-launcher.sh LOG EXPECTED_RESULTS SCRIPT [ARGS...]
#   EXPECTED_RESULTS  how many per-item result lines the check must print
# The anchored patterns are the check's own result shape, overridable per check:
#   RESULT_RE   a per-item result line   (default: `<sha>: <n> cards, <m> problems`)
#   SUMMARY_RE  the one final summary    (default: `<n> problems in <m> recovered cards over <k> commits`)
# A check that cannot state its result in those two shapes cannot be launched through here, which is
# the point: the launcher requires the result rather than trusting an exit status.
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
LOG=$1; EXPECT=$2; SCRIPT=$3; shift 3
SCRIPT=${SCRIPT#"$REPO"/}
IMAGE=${SAGE_IMAGE:-/workspace/nucleus/work/home/sage-image/run.sh}
RESEARCH=${RESEARCH_CHECKOUT:-/workspace/nucleus/work/projects/p-f1594a14bfb1401c85c6ee2525d7ac43/../p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo}
RESEARCH=${RESEARCH_CHECKOUT:-/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo}
RESULT_RE=${RESULT_RE:-'^[0-9a-f]{7,}: [0-9]+ cards, [0-9]+ problems$'}
SUMMARY_RE=${SUMMARY_RE:-'^[0-9]+ problems in [0-9]+ recovered cards over [0-9]+ commits$'}

# A Python check runs under the image's interpreter; a shell check is run as it is.
case "$SCRIPT" in
  *.sh) RUNNER=/bin/sh ;;
  *)    RUNNER=/sage/.venv/bin/python ;;
esac

"$IMAGE" -w /repo \
  -b "$REPO:/repo" \
  -b "$RESEARCH:/repo/research" \
  /bin/sh -c 'interp=$1; shift; /usr/bin/env PYTHONPATH=/repo/research/src:/repo/src "$interp" -u "$@"; echo "PYEXIT=$?"' sh \
  "$RUNNER" "/repo/$SCRIPT" "$@" > "$LOG" 2>&1
prc=$?

pyexit=$(sed -n 's/^PYEXIT=//p' "$LOG" | tail -1)
results=$(grep -Ec "$RESULT_RE" "$LOG")
summary=$(grep -Ec "$SUMMARY_RE" "$LOG")

if [ "$pyexit" = 0 ] && [ "$results" -eq "$EXPECT" ] && [ "$summary" -eq 1 ]; then
  echo "launcher: SUCCESS (proot rc=$prc, PYEXIT=$pyexit, $results/$EXPECT results, summary present)"
  exit 0
fi
echo "launcher: FAILURE (proot rc=$prc, PYEXIT=${pyexit:-absent}, results $results/$EXPECT, summary $summary)"
exit 1
