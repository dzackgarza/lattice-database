# #20: run 42363689427's conflict, reproduced through the persistence path, and its values on main

Run 42363689427 (schedule, `dde534ecd9`, 2026-11-07 10:22:31Z–16:11:43Z) computed sixteen shards and
failed all sixteen persistence steps. This records the conflict the path produced, the repair to the
path, and the verification that the run's computed values are on main.

## The artifacts

    $ curl -sS https://api.github.com/repos/dzackgarza/lattice-database/actions/runs/42363689427/artifacts
    RFC 200, "total_count": 16
    certification-42363689427-1-shard-0 … -15, "expired": false      (every one)

They have **not** expired. Downloading them needs a credential this connection does not hold —
`GET …/actions/artifacts/13579919839/zip` without one answers **401** — so the extraction made on
2026-11-07 is what it is, with one defect of its own worth stating: three of its sixteen patch files
are **0 bytes** (`shard-1`, `shard-5`, `shard-13`). Those three were applied as commits
`b29b4ba832`, `e4586bd3ca`, `e7e885b67e`, all in main's history, so their content is on main and
verifiable there; the empty files are a lost local copy, not a lost patch. Nothing in
`.scratch/recovery-42363689427/` was deleted.

## The conflict, reproduced

Each patch applies cleanly to its own base (`certification-base.txt` = `dde534ecd9`). Taking shard 0's
patch, staging it exactly as `persist.sh` stages (`lattices certificates exceeded.yaml failures.yaml`
at that revision), committing the snapshot with `git commit-tree -p $pushed`, and cherry-picking it
onto main as the script does:

    $ git cherry-pick -X theirs 017081ff06ce5eb13d069c5e995dbb5350563c49
    Auto-merging certificates/00.yaml … certificates/f0.yaml
    Auto-merging exceeded.yaml
    CONFLICT (modify/delete): failures.yaml deleted in HEAD and modified in 017081ff06
      (feat: certify computed card values (shard 0/16)). Version … of failures.yaml left in tree.
    Auto-merging lattices/0268.md
    error: could not apply 017081ff06… 
    cherry-pick exit: 1

One conflict, and no merge driver can resolve it: **`failures.yaml` no longer exists on main.** #17
replaced the single ledger file with the sharded `failures/` directory, and a shard that started
before that split still holds — and stages — the retired file. Git reports modify/delete, `-X theirs`
does not apply to it, and every later snapshot carries the same file, so the shard reports
`Computed values conflict with main; the next snapshot retries them.` for the whole of its life. That
is the message all sixteen steps printed.

## The repair to the persistence path

`persist.sh` now stages only the paths the shard's checkout holds **and current main tracks**, and
names the ones it skipped:

    git fetch --quiet origin main
    for path in lattices certificates exceeded.yaml failures failures.yaml; do
      [ -e "$path" ] || continue
      if git rev-parse --quiet --verify "FETCH_HEAD:$path" >/dev/null; then selection+=("$path")
      else skipped+=("$path"); fi
    done
    ::warning::main no longer tracks …; this run started before it was retired, so the snapshot does not carry it.

The same selection guards the other direction: the old checkout has no `failures/`, and `git add -A`
on a pathspec that matches nothing aborts the script (`fatal: pathspec 'failures' did not match any
files`, which is how a checkout of `dde534ecd9` behaves against today's selection).

Verified on the same shard and the same base, with the selection as the script now computes it:

    selection: lattices certificates exceeded.yaml
    skip (retired on main): failures.yaml
    snapshot c20b67c327c88cdaec67686e039029e037410713
    $ git cherry-pick c20b67c327
    [detached HEAD b858423913] snapshot: shard 0, fixed selection
    exit: 0, 0 conflicted paths

## The values: on main already, value for value

For each shard, its recovered content (the patch applied to `dde534ecd9`, or for shards 1, 5 and 13 the
commit that applied it) was compared with main: every certificate entry by `(key, hash)`, every card by
its front-matter fields.

| shard | ledger entries | cards | differing | absent |
| --- | --- | --- | --- | --- |
| 0 | 148,768 same | 509 cards, 26,839 values | 0 | 0 |
| 1 | 438,652 same | 1,245 cards, 64,292 values | 0 | 0 |
| 2 | 169,771 same | 694 cards, 36,764 values | 0 | 0 |
| 3 | 159,444 same | — | 0 | 0 |
| 4 | 156,861 same | 537 cards, 28,412 values | 0 | 0 |
| 5 | 1,040,197 same | 3,688 cards, 193,531 values | 0 | 0 |
| 6 | 153,055 same | 679 cards, 35,882 values | 0 | 0 |
| 7 | 158,192 same | 458 cards, 24,264 values | 1 | 0 |
| 8 | 139,505 same | 691 cards, 36,641 values | 0 | 0 |
| 9 | 158,447 same | 545 cards, 28,808 values | 0 | 0 |
| 10 | 138,084 same | 441 cards, 23,340 values | 0 | 0 |
| 11 | 154,714 same | 566 cards, 29,993 values | 0 | 0 |
| 12 | 143,023 same | 463 cards, 24,488 values | 0 | 0 |
| 13 | 2,134,880 same | 7,984 cards, 420,909 values | 0 | 0 |
| 14 | 159,519 same | 521 cards, 27,594 values | 0 | 0 |
| 15 | 155,630 same | 556 cards, 29,432 values | 1 | 0 |

**Nothing of this run is absent from main.** A certificate's hash is a function of the computation
name, the Gram tensor and the stored value, so the later certifying runs recomputed the same values and
wrote the same hashes: the run's output reached main through them even though its own persistence
steps never landed.

The two differences are the *valid concurrent results* the issue says to keep, and main's are the newer
ones:

    shard 7   6JRY integral.primitive_orbits   main  eba45974e533…  by: J. Scattone, Mem. AMS 374
    shard 15  6JRX integral.primitive_orbits   main  10326525e21e…  by: J. Scattone, Mem. AMS 374

Both were re-certified **by citation** in `089400ef44` ("Scattone's Lambda_2 and Lambda_4 with the
cited plane-orbit counts of O"), which replaced this run's computed row with the source's stated one.
Neither is a loss.

## What the recovery does, and does not, change

It changes no value: there is nothing missing to add and nothing correct to replace. It changes the
persistence path, so that the conflict that stopped sixteen steps cannot happen again. Replaying an
archived snapshot *today* is deliberately not done: the card merge driver takes the incoming side for a
key both sides changed, so an old snapshot would revert newer values — which is why the recovery is
this verification rather than a re-application.
