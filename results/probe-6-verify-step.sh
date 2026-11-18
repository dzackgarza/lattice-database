#!/usr/bin/env bash
# Run the verify step's own shell with the Sage command replaced by a stub (#6).
#
# The step must pass a shard's exit status through (1 for contradictions, 137 for a memory kill)
# and re-emit the shard's `memory:` line as a job annotation, which the run's API response carries
# where a job log needs repository-admin rights. This takes the `run:` block out of the workflow
# file itself, so what is exercised is the text that will run, not a copy of it.
#
#   bash results/probe-6-verify-step.sh
set -euo pipefail
here=$(cd "$(dirname "$0")/.." && pwd)
scratch="$here/.scratch/verify-step"
rm -rf "$scratch"
mkdir -p "$scratch"

python3 - "$here/.github/workflows/verify.yml" "$scratch/step.sh" <<'PY'
import re
import sys

import yaml

workflow, destination = sys.argv[1], sys.argv[2]
steps = yaml.safe_load(open(workflow))["jobs"]["cards"]["steps"]
script = next(step["run"] for step in steps if step["name"] == "Verify lattice cards and certificate hashes")
swapped, count = re.subn(r"docker exec .*?2>&1 \| tee shard\.log", '"$STUB" 2>&1 | tee shard.log', script, flags=re.S)
assert count == 1, "the step no longer runs the command in one pipeline through tee"
# The runner substitutes `${{ … }}` before the shell sees the step, so this does the same.
swapped = swapped.replace("${{ matrix.shard }}", "3")
open(destination, "w").write(swapped)
PY

stub() {
    local name=$1
    shift
    printf '%s\n' '#!/usr/bin/env bash' "$@" > "$scratch/$name"
    chmod +x "$scratch/$name"
}
stub reporting 'printf "memory: 14.6 GiB peak for 18958 cards in shard 3/16\n" >&2' 'printf "0268 integral.genus_class_count: contradicts its completed computation certificate\n" >&2' 'exit 1'
stub clean 'printf "memory: 14.2 GiB peak for 18900 cards in shard 4/16\n" >&2' 'exit 0'
stub killed 'printf "memory: 3.1 GiB peak for 12 cards in shard 9/16\n" >&2' 'exit 137'

for name in reporting clean killed; do
    status=0
    ( cd "$scratch" && SHARDS=16 STUB="./$name" bash --noprofile --norc -eo pipefail step.sh > "out-$name.txt" 2>&1 ) || status=$?
    notice=$(grep -c '^::notice title=shard ' "$scratch/out-$name.txt" || true)
    echo "stub=$name exit=$status notices=$notice"
done
