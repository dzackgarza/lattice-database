#!/usr/bin/env bash
# Push the values this shard has certified so far to main.
#
# Certification keeps writing the worktree while this runs, so the snapshot is taken
# through a separate index and integrated in a separate worktree; neither touches the
# files certification writes. Each push carries the change since the last snapshot that
# reached main, so a runner that dies loses only what followed it.
#
# Usage: persist.sh <shard>/<shards> [final]
set -euo pipefail

label="$1"
final="${2:-}"
state="$GITHUB_WORKSPACE/.persist"
mkdir -p "$state"
# A card holds every field of one lattice, and the fields run and the searches run both hold fields
# of it, so its citations must merge key by key: a whole-file resolution to either side drops the
# other run's references, which leaves a certificate in `certificates/` that its card no longer
# cites (#21). `.gitattributes` names both drivers; they run in the image, whose interpreter holds
# the preamble and the schema.
workspace="$(git rev-parse --show-toplevel)"
python_path="$workspace/research/src:$workspace/src"
git config merge.keyed-map.driver "docker exec -i --workdir \"\$PWD\" --env PYTHONPATH=$python_path sage-env /sage/.venv/bin/python -m latticedb merge-keyed-map %O %A %B"
git config merge.card-map.driver "docker exec -i --workdir \"\$PWD\" --env PYTHONPATH=$python_path sage-env /sage/.venv/bin/python -m latticedb.card_merge %O %A %B"
# A periodic push still running when certification ends finishes before the final one.
exec 9>"$state/lock"
flock 9
grep -qxF '/.persist/' .git/info/exclude || echo '/.persist/' >> .git/info/exclude
pushed="$(cat "$state/pushed" 2>/dev/null || git rev-parse HEAD)"

# A path main has retired cannot be merged from an older checkout. `failures.yaml` was replaced by
# the sharded `failures/` ledger (#17), so a shard that started before that split stages a file main
# no longer tracks: Git reports modify/delete, no merge driver can resolve it, and every later
# attempt fails the same way (#20 — run 42363689427's sixteen persistence steps). The same holds in
# the other direction for a checkout that predates a path main now tracks. Stage only the paths this
# checkout holds *and* current main tracks, and name the ones skipped.
git fetch --quiet origin main
selection=()
skipped=()
for path in lattices certificates exceeded.yaml failures failures.yaml; do
  [ -e "$path" ] || continue
  if git rev-parse --quiet --verify "FETCH_HEAD:$path" >/dev/null; then
    selection+=("$path")
  else
    skipped+=("$path")
  fi
done
if [ "${#skipped[@]}" -gt 0 ]; then
  echo "::warning::main no longer tracks ${skipped[*]}; this run started before it was retired, so the snapshot does not carry it."
fi
GIT_INDEX_FILE="$state/index" git read-tree "$pushed"
GIT_INDEX_FILE="$state/index" git add -A -- "${selection[@]}"
tree="$(GIT_INDEX_FILE="$state/index" git write-tree)"
if [[ "$tree" == "$(git rev-parse "$pushed^{tree}")" ]]; then
  echo "No newly completed computations."
  exit 0
fi
snapshot="$(git commit-tree "$tree" -p "$pushed" -m "feat: certify computed card values (shard $label)")"

worktree="$state/main"
[[ -d "$worktree" ]] || git worktree add --quiet --detach "$worktree" "$pushed"
picked=""
for attempt in $(seq 1 30); do
  git -C "$worktree" fetch --quiet origin main
  # A push killed with its step can leave a cherry-pick in progress.
  git -C "$worktree" cherry-pick --abort 2>/dev/null || true
  git -C "$worktree" reset --quiet --hard FETCH_HEAD
  picked=""
  # Shards own disjoint cards and certificate files; a card's lines, exceeded.yaml and the ledger
  # merge key by key through the drivers above, so an overlapping writer's keys survive this push.
  # A conflict the drivers cannot merge is a defect: the next snapshot retries it.
  if ! git -C "$worktree" cherry-pick "$snapshot" >/dev/null; then
    git -C "$worktree" cherry-pick --abort
    echo "::error::Computed values conflict with main; the next snapshot retries them."
    break
  fi
  picked=1
  if git -C "$worktree" push --quiet origin HEAD:main; then
    echo "$snapshot" > "$state/pushed"
    echo "Pushed $(git diff --name-only "$pushed" "$snapshot" | wc -l) changed files (attempt $attempt)."
    exit 0
  fi
  sleep $(( RANDOM % 20 + 1 ))
done
if [[ -n "$final" ]]; then
  # Only a commit on current main may be pushed: an older tree would revert workflow files.
  branch="certify-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}-${label%%/*}"
  if [[ -n "$picked" ]] && git -C "$worktree" push --quiet origin "HEAD:refs/heads/$branch"; then
    echo "::error::Could not push to main; the computed values are on branch $branch and in the uploaded patch."
  else
    echo "::error::Could not integrate computed values; recover the uploaded certification patch."
  fi
fi
exit 1
