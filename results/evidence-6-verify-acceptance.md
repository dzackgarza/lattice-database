# #6: the verify acceptance, item by item

The issue's acceptance, verbatim: *a scheduled or dispatched `verify` run completes over every card,
with the memory ceiling it needed recorded in the workflow.*

## What can be read from here, and what cannot

The Actions API answers without a token on this public repository: runs, jobs, steps and check-run
annotations. Job **logs** do not — `/repos/…/actions/jobs/{id}/logs` and `/actions/runs/{id}/logs`
both answer `403 Must have admin rights to Repository`. So a shard's exit code is readable from here
and its printed peak is not, which is exactly the distinction item 2 turns on.

## Item 1 — a run completes over every card: **holds**

**The split covers the corpus.** `lattices/` holds 302,504 cards, and
`genus.in_shard` (`src/latticedb/genus.py:299`) is `certificates.tag_hash(tag) % count == index`.
Each card's tag matched exactly one of the sixteen shards; the shards hold 18,626–19,009 cards each
and 302,504 together.

**The dispatch rule is the same rule.** The `plan` job computes a tag's shard with the same
SHA-256 prefix modulo 16 (`.github/workflows/verify.yml:57`); it agrees with
`certificates.tag_hash(tag) % 16` on every tag tried, including `6JRR`, `029J`, `0268`, `0021`,
`5989`, `58S6`, `6JRS` and `00R2`.

**The runs.** Run `44078051011` (schedule, head `4c92ce1f89`, 2026-11-17, the newest `verify` run):
`plan` succeeded and **16 of 16** shard jobs ran *Verify lattice cards and certificate hashes* to
completion, each annotated `Process completed with exit code 1.` — no `137`, none cancelled. Run
`42844490886` (dispatch, `188412a150`) reads the same way. Exit 1 is the verifier refusing the
contradictions it found (`src/latticedb/cli.py:55`), which is what the acceptance asks for: the run
reports, it does not die.

**The gap this turn closed.** A shard's run could not say how many cards it read. `--shard i/n` runs
in the command's own process (`src/latticedb/checks/__init__.py:48`), and the line it printed named
neither the shard nor a count (`memory: … peak for this process`, cli.py:335 before), while the line
that carries the count (`… lattice cards structurally verified`, now `src/latticedb/cli.py:339`) is
never reached when a shard reports problems — and every shard of this tree has problems to report.
Probed on a fixture of sixteen cards, one from each shard, through the same command: all sixteen runs
printed exactly `memory: 0.4 GiB peak for this process` and nothing naming their cards. Now
(`src/latticedb/cli.py:332-337`):

```
memory: 0.4 GiB peak for 1 cards in shard 0/16
```

which the workflow's own log line and the new annotation carry. Test:
`tests/test_verification.py:57` (`test_a_shard_states_the_cards_it_verified_with_its_peak`).
The fixture reports eight `the related tag … is not in the corpus` problems, identically in every
shard, because those checks are corpus-wide (`src/latticedb/checks/__init__.py:67`); they are the
fixture's, not the cards'.

## Item 2 — the ceiling recorded in the workflow: **not met on `main`; the change is written but unlanded**

What stood: the workflow gave each shard 8 GiB of swap on top of the runner's memory
(`.github/workflows/verify.yml:23`) and said in a comment that each shard "reports the peak it
needed" (`:20`). The peak it *needed* was recorded nowhere in the repository: the only number is the
closing note on #6 — 14.2–14.6 GiB — and the logs that would carry it per shard answer 403 above.

`results/verify-peak-annotation.patch` records it and makes each run state its own:

- the `env:` comment now records the measured ceiling with its provenance
  (run `42844490886`, 14.2–14.6 GiB, and why the log could not be re-read);
- the verify step keeps the command's exit status (`1` for contradictions, `137` for a memory kill)
  and re-emits the shard's `memory:` line as a **job annotation**, which the run's API response
  carries without admin rights — so the next run's per-shard peaks are readable, and the number in
  the workflow can be checked instead of remembered.

`results/probe-6-verify-step.sh` runs that step's own shell, taken out of the workflow file, with the
Sage command replaced by a stub:

```
stub=reporting exit=1 notices=1
stub=clean exit=0 notices=1
stub=killed exit=137 notices=1
```

`::notice title=shard 3/16::memory: 14.6 GiB peak for 18958 cards in shard 3/16` is what the runner
would read. Against the unpatched file the probe reports `notices=0`, which is the gap itself.

**The workflow file is not on `main`.** This connection's GitHub App cannot push
`.github/workflows/verify.yml` (the same boundary that put `8055ad42a7` and `6f4784a604` on `main` as
patches), so the change travels as the patch above, to be landed by whoever holds that permission.
Until it lands, item 2 is recorded in the patch and in this file, not in the workflow.

## The ceiling has no scaling law, so none is offered

`results/probe-6-shard-peak.py` measures the two loads a shard does at the sizes this VM holds:

| cards | peak | | certificates | peak |
| --- | --- | --- | --- | --- |
| 2,000 | 0.44 GiB | | 9.9 MiB (78,865 entries) | 0.44 GiB |
| 12,000 | 0.54 GiB | | 39.3 MiB (313,260 entries) | 0.53 GiB |
| 40,000 | 1.12 GiB | | | |

The per-card cost is 10.5 KiB at the small end and 20.7 KiB between 12,000 and 40,000 — it
accelerates, and the last slope extrapolates to ≈6.3 GiB for 302,504 cards, near the 7.3 GiB
`src/latticedb/corpus.py:191` states for the full load. The certificate slope extrapolates to ≈0.9
GiB for the corpus's 2.4 million entries against the 9.08 GiB recorded for a full
`certificates.load` — a factor of ten this VM cannot resolve, because the full loads need about
fourteen GiB and it has six. So the workflow records the run's own peaks, not a fit.

## Not done here

- No run was dispatched by this turn; the evidence is read from runs already in the repository's
  Actions history.
- The full shard command was never run against `lattices/` from this VM — 14.6 GiB of peak against
  6 GiB available, the same wall as the runner's. The sixteen-card fixture is the smallest input that
  decides completion, the peak line and the status, and it is what was run.
- `.github/workflows/verify.yml` is unmodified on `main`.
