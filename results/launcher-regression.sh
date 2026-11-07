#!/bin/sh
# Regression for results/verify-launcher.sh: a wrapper exit of 0 is not accepted as success (#20).
#
# The image wrapper reports 0 when its guest dies of a signal, so a check whose only evidence is
# "the outer command returned 0" accepts a died run. This runs the launcher over controlled cases
# and asserts, per case, the launcher's own return code -- the anchored result line and the guest
# child status it must see, exactly as research#749's launcher regression does.
#
# usage: results/launcher-regression.sh [WRAPPER]
#   WRAPPER defaults to the repaired launcher. The *same* assertions run against any wrapper, which
#   is how the unrepaired path is shown to fail: results/launcher-regression.sh
#   results/verify-launcher-unrepaired.sh must fail on the incomplete, short and signal cases while
#   its normal case still succeeds.
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
LAUNCHER=${1:-$REPO/results/verify-launcher.sh}
REPRO=$REPO/results/launcher-regression-repro.py
fail=0

# mode expected_rc what it proves
run_case() {
  mode=$1; want=$2; why=$3
  log=$REPO/.scratch/launcher-$mode.log
  tag=$(basename "$LAUNCHER" .sh)
  sh "$LAUNCHER" "$log" 2 "$REPRO" "$mode" > "$REPO/.scratch/$tag-$mode.out" 2>&1
  rc=$?
  pyexit=$(sed -n 's/^PYEXIT=//p' "$log" | tail -1)
  results=$(grep -Ec '^[0-9a-f]{7,}: [0-9]+ cards, [0-9]+ problems$' "$log")
  echo "case $mode: launcher rc=$rc (want $want), PYEXIT=${pyexit:-absent}, results=$results  [$why]"
  [ "$rc" -eq "$want" ] || { echo "REGRESSION FAIL: $mode gave rc $rc, wanted $want"; fail=1; }
}

run_case normal       0 "two results and the summary: the only case that may pass"
run_case incomplete   1 "two results, no summary: a clean exit must still fail"
run_case short        1 "one result of two: a clean exit must still fail"
run_case raise        1 "a nonzero guest status must fail"
run_case segv         1 "a signal death the wrapper reports as 0 must fail"

echo "wrapper: $(basename "$LAUNCHER")"
[ "$fail" -eq 0 ] && echo "REGRESSION PASS" || echo "REGRESSION FAIL"
exit $fail
