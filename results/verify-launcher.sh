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
#   EXPECTED_RESULTS  how many per-item result lines the script must print
#   the anchored line the script prints is `<N> problems in <M> recovered cards over <K> commits`
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
LOG=$1; EXPECT=$2; SCRIPT=$3; shift 3
# The script is named relative to the repository, which is mounted at /repo in the guest.
SCRIPT=${SCRIPT#"$REPO"/}
IMAGE=${SAGE_IMAGE:-/workspace/nucleus/work/home/sage-image/run.sh}
RESEARCH=${RESEARCH_CHECKOUT:-/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo}

"$IMAGE" -w /repo \
  -b "$REPO:/repo" \
  -b "$RESEARCH:/repo/research" \
  /bin/sh -c '/usr/bin/env PYTHONPATH=/repo/research/src:/repo/src /sage/.venv/bin/python -u "$@"; echo "PYEXIT=$?"' sh \
  "/repo/$SCRIPT" "$@" > "$LOG" 2>&1
prc=$?

pyexit=$(sed -n 's/^PYEXIT=//p' "$LOG" | tail -1)
results=$(grep -Ec '^[0-9a-f]{7,}: [0-9]+ cards, [0-9]+ problems$' "$LOG")
summary=$(grep -Ec '^[0-9]+ problems in [0-9]+ recovered cards over [0-9]+ commits$' "$LOG")

if [ "$pyexit" = 0 ] && [ "$results" -eq "$EXPECT" ] && [ "$summary" -eq 1 ]; then
  echo "launcher: SUCCESS (proot rc=$prc, PYEXIT=$pyexit, $results/$EXPECT results, summary present)"
  exit 0
fi
echo "launcher: FAILURE (proot rc=$prc, PYEXIT=${pyexit:-absent}, results $results/$EXPECT, summary $summary)"
exit 1
