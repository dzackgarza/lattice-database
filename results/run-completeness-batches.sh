#!/bin/sh
# Run the #20 completeness comparison one shard per process, then report the run's totals.
#
# One process per snapshot bounds the memory (the whole-run process kept every revision's card and map
# text and was killed at status 137 after fourteen shards), and each shard's verdicts are recorded
# before the next starts, so this resumes where a previous run stopped: a shard already recorded is
# reprinted from the record rather than worked out again. The per-shard result lines and the final
# summary are exactly what results/verify-launcher.sh requires.
#
# usage: results/run-completeness-batches.sh [shard...]      (default: all sixteen)
set -u
REPO=$(cd "$(dirname "$0")/.." && pwd)
CHECK=$REPO/results/check-run-42363689427-complete.py
PY=${PYTHON:-python3}
shards=${*:-0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15}
for shard in $shards; do
  PYTHONPATH="$REPO/src" "$PY" -u "$CHECK" "$shard" || exit $?
done
PYTHONPATH="$REPO/src" "$PY" -u "$CHECK" --report
