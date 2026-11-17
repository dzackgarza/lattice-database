#!/usr/bin/env bash
# Push the values this shard has certified so far to main.
#
# Certification keeps writing the worktree while this runs, so the snapshot is taken through a
# separate index; nothing here resets, checks out or stages into the worktree certification writes.
# Each push carries the change since the last snapshot that reached main, so a runner that dies
# loses only what followed it.
#
# The commit is made *on* the main it is pushed onto and pushed as a fast-forward, so this shard's
# change is never rebased onto a base that has moved and Git has no cherry-pick to conflict on. A
# path that main also changed since this shard's last push is merged here, one path at a time, by
# the driver `.gitattributes` names for it; a driver that cannot merge it is this shard's named
# failure, not a conflict Git reports and every later tick retries (#47).
#
# Usage: persist.sh <shard>/<shards> [final]
set -euo pipefail

label="$1"
final="${2:-}"
state="$GITHUB_WORKSPACE/.persist"
mkdir -p "$state/merge"
# A card holds every field of one lattice, and the fields run and the searches run both hold fields
# of it, so its citations must merge key by key: a whole-file resolution to either side drops the
# other run's references, which leaves a certificate in `certificates/` that its card no longer
# cites (#21). `.gitattributes` names both drivers; they run in the image, whose interpreter holds
# the preamble and the schema.
workspace="$(git rev-parse --show-toplevel)"
python_path="$workspace/research/src:$workspace/src"
# A configuration that already names a driver decides how the merge runs — the regression test drives
# these files with the interpreter of the process it runs in — and this script supplies its own only
# where there is none.
if [ -z "$(git config --get merge.keyed-map.driver || true)" ]; then
  git config merge.keyed-map.driver "docker exec -i --workdir \"\$PWD\" --env PYTHONPATH=$python_path sage-env /sage/.venv/bin/python -m latticedb merge-keyed-map %O %A %B"
fi
if [ -z "$(git config --get merge.card-map.driver || true)" ]; then
  git config merge.card-map.driver "docker exec -i --workdir \"\$PWD\" --env PYTHONPATH=$python_path sage-env /sage/.venv/bin/python -m latticedb card_merge %O %A %B"
fi
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
if [ "${#selection[@]}" -eq 0 ]; then
  echo "No path this checkout holds is on main; nothing to push."
  exit 0
fi

# What this run wrote: the worktree against the commit it checked out, untracked files included. A
# path outside this set is another shard's work, only as old as this checkout, and carrying it would
# revert theirs (#47).
mapfile -t written < <(
  git diff --name-only --no-renames HEAD -- "${selection[@]}"
  git ls-files --others --exclude-standard -- "${selection[@]}"
)
# Union with what an earlier tick wrote: a ledger this run pushed and has since rewritten without
# its own resolved entry holds the content it checked out, and that rewrite is still its own.
mapfile -t mine < <(
  {
    printf '%s\n' "${written[@]}"
    cat "$state/written" 2>/dev/null || true
  } | sed '/^$/d' | sort -u
)
if [ "${#mine[@]}" -gt 0 ]; then
  printf '%s\n' "${mine[@]}" > "$state/written"
fi
# This shard's change since its last push: the paths its run wrote that also differ from the commit
# that reached main last.
mapfile -t changed < <(
  comm -12 <(printf '%s\n' "${mine[@]}") <(
    {
      git diff --name-only --no-renames "$pushed" -- "${selection[@]}"
      git ls-files --others --exclude-standard -- "${selection[@]}"
    } | sort -u
  )
)
if [ "${#changed[@]}" -eq 0 ]; then
  echo "No newly completed computations."
  exit 0
fi

# The command Git would run as this path's merge driver, with Git's own `%O %A %B` filled in.
driver_command() {
  local path="$1" base="$2" ours="$3" theirs="$4" driver command
  driver="$(git check-attr merge -- "$path" | sed 's/^[^:]*: merge: //')"
  if [ -z "$driver" ] || [ "$driver" = "unspecified" ] || [ "$driver" = "unset" ]; then
    echo "no merge driver is named for it by .gitattributes"
    return 1
  fi
  command="$(git config --get "merge.$driver.driver" || true)"
  if [ -z "$command" ]; then
    echo "the $driver merge driver is not configured: set merge.$driver.driver"
    return 1
  fi
  command="${command//%O/\"$base\"}"
  command="${command//%A/\"$ours\"}"
  command="${command//%B/\"$theirs\"}"
  printf '%s' "$command"
}

# Merge one path main and this shard both changed, and answer the blob to stage. A failure here
# answers a reason on stderr and is this shard's, with the path named.
merged_blob() {
  local path="$1" key base ours theirs command blob
  key="$(printf '%s' "$path" | tr '/' '_')"
  base="$state/merge/$key.base"
  ours="$state/merge/$key.ours"
  theirs="$state/merge/$key.theirs"
  : > "$base"
  git show "$pushed:$path" > "$base" 2>/dev/null || true
  git show "FETCH_HEAD:$path" > "$ours"
  : > "$theirs"
  if [ -e "$path" ]; then
    cp -- "$path" "$theirs"
  fi
  if ! command="$(driver_command "$path" "$base" "$ours" "$theirs")"; then
    printf '%s\n' "$command" >&2
    return 1
  fi
  # Git runs a merge driver in the worktree's root, and a driver configured elsewhere resolves
  # that directory as `$PWD`.
  if ! ( cd "$workspace" && eval "$command" ); then
    echo "its merge driver failed" >&2
    return 1
  fi
  blob="$(git hash-object -w --path "$path" "$ours")"
  printf '%s' "$blob"
}

# Stage this shard's change against the main `FETCH_HEAD` names, for one attempt. Answers 2 when a
# path cannot be merged and 3 when staging itself failed; both end the tick as this shard's.
stage_attempt() {
  local path blob main_blob base_blob deleted
  GIT_INDEX_FILE="$state/index" git read-tree FETCH_HEAD || { echo "cannot read main's tree" >&2; return 3; }
  for path in "${changed[@]}"; do
    main_blob="$(git rev-parse --quiet --verify "FETCH_HEAD:$path" || true)"
    base_blob="$(git rev-parse --quiet --verify "$pushed:$path" || true)"
    deleted=""
    if [ ! -e "$path" ]; then
      deleted=1
    fi
    if [ -n "$base_blob" ] && [ -n "$main_blob" ] && [ "$main_blob" = "$base_blob" ]; then
      # Main has not touched it since this shard's last push, so this shard's copy is the change.
      :
    elif [ -z "$main_blob" ] && [ -n "$base_blob" ]; then
      echo "::warning::shard $label: main no longer tracks $path; the snapshot leaves it out, as Git cannot merge a path main retired." >&2
      continue
    elif [ -n "$deleted" ] && [ -n "$main_blob" ]; then
      echo "::error::shard $label: this run deleted $path and main changed it after this shard's last push; the deletion is not on main and the run continues." >&2
      return 2
    elif [ -n "$deleted" ]; then
      GIT_INDEX_FILE="$state/index" git update-index --force-remove -- "$path" || return 3
      continue
    elif [ -n "$main_blob" ] || [ -n "$base_blob" ]; then
      # Both sides changed it: merge it here, so a driver that cannot run is named rather than left
      # to Git, which reports it as a conflict with no side to it (#47).
      if ! blob="$(merged_blob "$path")"; then
        echo "::error::shard $label: $path could not be merged with main, so the values this shard certified since its last push are not on main; the run continues and the path stays this shard's." >&2
        return 2
      fi
      GIT_INDEX_FILE="$state/index" git update-index --add --cacheinfo "100644,$blob,$path" || return 3
      continue
    fi
    blob="$(git hash-object -w --path "$path" "$path")" || return 3
    GIT_INDEX_FILE="$state/index" git update-index --add --cacheinfo "100644,$blob,$path" || return 3
  done
  return 0
}

snapshot=""
for attempt in $(seq 1 30); do
  git fetch --quiet origin main
  status=0
  stage_attempt || status=$?
  if [ "$status" -eq 2 ] || [ "$status" -eq 3 ]; then
    break
  fi
  tree="$(GIT_INDEX_FILE="$state/index" git write-tree)"
  if [ "$tree" = "$(git rev-parse "FETCH_HEAD^{tree}")" ]; then
    echo "No newly completed computations."
    exit 0
  fi
  snapshot="$(git commit-tree "$tree" -p FETCH_HEAD -m "feat: certify computed card values (shard $label)")"
  if git push --quiet origin "$snapshot:refs/heads/main"; then
    echo "$snapshot" > "$state/pushed"
    echo "Pushed $(git diff --name-only "$pushed" "$snapshot" | wc -l) changed files (attempt $attempt)."
    exit 0
  fi
  # Main moved under the push. Nothing is rebased and nothing is forced: the next attempt stages
  # this shard's change again, against the main main now has.
  sleep $(( RANDOM % 20 + 1 ))
done
if [[ -n "$final" ]]; then
  # Only a commit on current main may be pushed: an older tree would revert workflow files.
  branch="certify-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}-${label%%/*}"
  if [[ -n "$snapshot" ]] && git push --quiet origin "$snapshot:refs/heads/$branch"; then
    echo "::error::shard $label: main did not take this shard's progress; the values are on branch $branch and in the uploaded patch."
  else
    echo "::error::shard $label: the values this shard certified since its last push are not on main; recover them from the uploaded certification patch."
  fi
fi
exit 1
