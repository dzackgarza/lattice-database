# #28: eight runners at once, and each shard reads only its own tags

## The bound, from the job times of 2026-11-08 to 2026-11-10

    run 42471750708  (11-08, ce097a80)  16 shard jobs, longest 344 min, median 341, 5,464 runner-min
    run 42611380402  (11-09, 304b00b0)  16 shard jobs, longest 344 min, median 341, 5,467 runner-min
    run 42806751744  (11-10, b0e2f38f52) 16 shard jobs, longest 343 min, median 341, 5,460 runner-min

Each shard is a runner for ~5 h 41 min, and the run's total is ~91 runner-hours, so the total work is
fixed and only the concurrency decides the wall time:

| runners held at once | wall time | runners left for the account |
| --- | --- | --- |
| 16 (as dispatched) | 5 h 41 min | none |
| **8** | **11 h 10 min** (two waves) | 8 or more |
| 6 | 15 h 12 min | 10 |
| 4 | 22 h 41 min | 12 — and the next 03:17 run would find this one still going |

Eight is the largest concurrency that halves the runners and the smallest that keeps a run inside a
day, well clear of the next scheduled run. `.github/workflows/certify.yml` carries
`max-parallel: 8` on the matrix since `98a6505039`, so **no workflow change is needed in this turn**;
the shards, their `timeout-minutes: 350`, and the `--minutes 330 --shard i/16 --phase fields` each job
runs are unchanged, so the certified values and the total work are unchanged.

## What each shard reads now

Every shard used to read the whole corpus before its first computation — `corpus.load` (302,504 cards,
7.29 GiB, 421 s) and `certificates.load` (2,449,746 entries, 9.08 GiB, 556 s) — although `genus.certify`
certifies only the tags its shard holds. `cli.certify` now reads what the shard can certify:

    visible = tags the run names, else the tags `genus.in_shard` gives the shard
    loaded  = corpus.cards(root, visible)
    held    = certificates.load(root, visible)

and `certificates.save` receives the same tags, so a group is always written from a full read of it.

Measured on the full repository in the image, shard 0 of 16:

| | before | after |
| --- | --- | --- |
| tags listed | — | 18,988 in 3.1 s |
| cards read | 302,504 in 421 s | 18,988 in 30.4 s |
| certificate entries | 2,449,746 in 556 s | 149,405 in 7.4 s |
| load before the first computation | **556 s (9 min 16 s), 9.08 GiB peak** | **40.9 s, 0.83 GiB peak** |

So a shard's 344 minutes become ~335, and a run's two waves ~11 h 10 min rather than 11 h 28 min. The
peak falls from 9.08 GiB to 0.83 GiB, which is the difference between a shard that is one runner's
memory and one that is not.

## The test

`tests/test_certify_reads.py`, run in the image (5 passed):

- `test_a_shard_reads_only_the_tags_it_holds` — a shard of a scheduled run hands the queue its own tags
  and opens no other card's file;
- `test_the_whole_corpus_shard_still_reads_every_card` — `--shard 0/1` is the whole corpus and reads it;
- with #30's three tests beside them: a tag request reads one card, two tags read two, and a run
  without either reads the corpus.
