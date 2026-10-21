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
# A periodic push still running when certification ends finishes before the final one.
exec 9>"$state/lock"
flock 9
grep -qxF '/.persist/' .git/info/exclude || echo '/.persist/' >> .git/info/exclude
pushed="$(cat "$state/pushed" 2>/dev/null || git rev-parse HEAD)"

GIT_INDEX_FILE="$state/index" git read-tree "$pushed"
GIT_INDEX_FILE="$state/index" git add -A -- lattices certificates exceeded.yaml
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
  # Shards own disjoint cards and certificate files; exceeded.yaml merges key by key.
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
