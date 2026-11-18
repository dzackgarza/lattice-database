# #6: the verify acceptance, item by item

The issue's acceptance, verbatim: *a scheduled or dispatched `verify` run completes over every card,
with the memory ceiling it needed recorded in the workflow.*

## What can be read from here, and what cannot

The Actions API answers without a token on this public repository: runs, jobs, steps and check-run
annotations. Job **logs** do not — `/repos/…/actions/jobs/{id}/logs` and `/actions/runs/{id}/logs`
both answer `403 Must have admin rights to Repository`. A shard's exit code is therefore readable
from here and the peak it printed in its log was not, which is what item 2 turns on.

## Item 1 — a run completes over every card: **holds**

**The split covers the corpus.** `lattices/` holds 302,504 cards and `genus.in_shard` is
`certificates.tag_hash(tag) % count == index` (`src/latticedb/genus.py:299`). Every tag matched
exactly one of sixteen shards; the shards hold 18,626–19,009 cards each and 302,504 together.

**The dispatch rule is the same rule.** The `plan` job computes a tag's shard from the same SHA-256
prefix modulo 16 (`.github/workflows/verify.yml:57`), and it agrees with
`certificates.tag_hash(tag) % 16` on every tag tried (`6JRR`, `029J`, `0268`, `0021`, `5989`, `58S6`,
`6JRS`, `00R2`).

**The runs.** Run `44078051011` (schedule, head `4c92ce1f89`, 2026-11-17; still the newest `verify`
run when re-read on 2026-11-18): `plan` succeeded, and **16 of 16** shard jobs ran *Verify lattice
cards and certificate hashes* to completion with the annotation `Process completed with exit code
1.` — no `137` and none cancelled. Run `42844490886` (dispatch, `188412a150`) reads the same way.
Exit 1 is the verifier refusing the contradictions it found (`src/latticedb/cli.py:56`), which is
what the acceptance asks for: the run reports, it does not die.

**What a shard's run could not say, now fixed.** `--shard i/n` runs in the command's own process
(`src/latticedb/checks/__init__.py:48`), and its line named neither the shard nor a card count
(`memory: … peak for this process`), while the line that carries the count
(`src/latticedb/cli.py:345`) is never reached when a shard reports problems — and every shard of this
tree reports some. Sixteen shard runs over a sixteen-card fixture printed that line and nothing
naming their cards. Now (`src/latticedb/cli.py:336`):

```
memory: 0.3 GiB peak for 1 cards in shard 3/16
```

against the fixture, one card per shard. Test: `tests/test_verification.py:57`
(`test_a_shard_states_the_cards_it_verified_with_its_peak`). The fixture also reports eight
`the related tag … is not in the corpus` problems, identically in every shard, because those checks
are corpus-wide (`src/latticedb/checks/__init__.py:67`); they are the fixture's, not the cards'.

## Item 2 — the ceiling recorded in the workflow: the per-run record is now in the code; the number travels as a comment

What stood: the workflow gave each shard 8 GiB of swap on top of the runner's memory
(`.github/workflows/verify.yml:23`) and its comment claimed each shard "reports the peak it needed"
(`:20`). The peak it *needed* was recorded nowhere: the only number is the closing note on #6
(14.2–14.6 GiB), and the logs that would carry it per shard answer 403 above.

**The record now comes from the command, so it needs no workflow change to land.** Under Actions
(`GITHUB_ACTIONS=true`, which every runner sets) `latticedb verify` prints the peak line *and* emits
it as a workflow annotation (`src/latticedb/cli.py:339`), before it refuses its problems, so a shard
that finds contradictions still records what it needed:

```
memory: 0.3 GiB peak for 1 cards in shard 3/16
::notice title=shard 3/16::memory: 0.3 GiB peak for 1 cards in shard 3/16
```

from two real shard runs of the fixture (shards `0/16` and `3/16`, `GITHUB_ACTIONS=true`), on the
workflow as it stands — the plain `docker exec` step passes the annotation through. An annotation is
part of the run's API response, so the next scheduled run's per-shard peaks are readable where a job
log is not. Test: `tests/test_verification.py:62`, which asserts the notice under Actions and its
absence without.

**The number itself** is a comment in the workflow, recorded from run `42844490886` with its
provenance and with the 403 that stopped it being re-read from the logs:

```
env:
  # The ceiling a shard needs is recorded here, because its job log is not readable to everyone:
  # run 42844490886 … reported peaks of 14.2-14.6 GiB …
  SWAP_GIB: 8
```

That comment is `results/verify-peak-annotation.patch`; `git apply --check` succeeds against
`.github/workflows/verify.yml` on `main`. It travels as a patch because pushes that carry a
`.github/workflows` change have not landed through this connection: `8055ad42a7` removes exactly such
a change from `main`, and the same change arrives later as `70eedd9d65`, authored by the owner rather
than by the connection's identity.

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

- No run was dispatched by this turn; the run evidence is read from the repository's Actions history.
- The full shard command was never run against `lattices/` from this VM — 14.6 GiB of peak against
  6 GiB available, the same wall as the runner's. The sixteen-card fixture is the smallest input that
  decides completion, the peak line and the annotation.
