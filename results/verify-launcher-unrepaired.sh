#!/bin/sh
# The unrepaired launch path, kept as the red counterpart of results/verify-launcher.sh (#22).
#
# This is exactly the pattern job jmw6ug2ma used: call the image wrapper and report its status as the
# result. It carries an ordinary exit code through and reports 0 for a guest killed by a signal, so
# the same regression that the repaired launcher passes must fail here -- on the incomplete, short
# and signal cases -- while its normal case still succeeds. Without that, the regression would be
# proving nothing but that a shell script can exit 0.
#
# The launch environment is the repaired launcher's, from results/launcher-environment.sh, so this
# path differs from it only in what it requires of the guest's result: it starts the same guest and
# reports the wrapper's own status. Without the shared resolution the wrapper cannot start where HOME
# is unset (#41), and the regression would be red for the wrong reason.
#
# usage: results/verify-launcher-unrepaired.sh LOG EXPECTED_RESULTS SCRIPT [ARGS...]
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
. "$REPO/results/launcher-environment.sh"
LOG=$1; EXPECT=$2; SCRIPT=$3; shift 3
SCRIPT=${SCRIPT#"$REPO"/}
RESEARCH=${RESEARCH_CHECKOUT:-/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo}

ROOT="$ROOT" PROOT="$PROOT" "$IMAGE" -w /repo \
  -b "$REPO:/repo" \
  -b "$RESEARCH:/repo/research" \
  /usr/bin/env PYTHONPATH=/repo/research/src:/repo/src /sage/.venv/bin/python -u "/repo/$SCRIPT" "$@" > "$LOG" 2>&1
prc=$?

echo "unrepaired launcher: wrapper rc=$prc (no result is required of the output)"
exit "$prc"
