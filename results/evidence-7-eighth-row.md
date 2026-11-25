# #7: the eighth T_Co row, landed by the database path

**Outcome: `integral.primitive_orbits` on 6JRR now states all eight rows — `O`, `SO`, `O+`, `SO+` at
$1$ and `Otilde`, `SOtilde`, `Otilde+`, `SOtilde+` at $527$ — under one certificate,
`4282656a7d42a5489e900ad120e0f39897cca2d71dabca91e1874feee4fca7b9`, which supersedes
`ed8a588f…` over seven.** The `SOtilde+` quarantine in `failures/e1.yaml` is released and resolved.
Nothing in this file is transcribed from a source or copied from an owner measurement into the card:
the stored value is what this database's own `certify` run returned on the stored Gram tensor.

## Which number came from which run

Three runs are involved, and they are not interchangeable.

1. `results/evidence-7/results.json` — the **seven-row** measurement
   (`results/evidence-7/probe-lines.py`, certify image, `sage_extensions` 34c9be8952, 2026-11-17).
   `O` 1 in 82.98 s, `SO` 1, `O+` 1, `SO+` 1 in 33.17 s, `Otilde` 527 in 30.94 s, `SOtilde` 527 in
   39.17 s, `Otilde+` 527 in 52.42 s; peak 1033 MiB. `SOtilde+` did not return: killed at ≥ 510 s and
   ≥ 9200 MiB. These are the seven values the card already stated.
2. **sage-extensions `dbf91e89`** (`origin/main` 2fb37d5), whose message carries the repair of
   sage-extensions#596 and its own measurement of all eight rows in one process at the owner's
   adopted runtime with the indefinite port at 54d12c2e: `O` 1, `SO` 1, `O+` 1, `SO+` 1 in 3.00 s,
   `Otilde` 527 in 93.10 s, `SOtilde` 527 in 64.83 s, `Otilde+` 527 in 74.05 s, **`SOtilde+` 527 in
   72.15 s**, all eight in 307.2 s at 1019 MiB. This is the owner's measurement of the owner's call.
   It was used as the expectation the card's own run had to reproduce; it is not the card's value and
   no certificate here commits to it.
3. **This turn's database run.** The row was released and then computed by this repository:

       just retry-computation 6JRR 'integral.primitive_orbits[SOtilde+]' --note '<#596 repair and its measurement>'
       latticedb certify --tag 6JRR --field primitive_orbits --phase fields --workers 1 --minutes 15

   in the pinned image (`dzackgarza/sage` revision `6301b4e4`, digest `sha256:332aebe9…`, Sage
   11.0.beta5, `/sage/.venv/bin/python` 3.14) with `sage_extensions` from a source checkout at **2fb37d5** (`origin/main`, carrying
   `dbf91e89`) bound at `/sage-ext` and first on `PYTHONPATH`, and this repository's `src` on it.
   The run printed

       6JRR {'primitive_orbits[SOtilde+]': {'SOtilde+': {'constant': 527, 'z': [], 'w': []}}}

   and took **179 s wall (2 m 59 s)**, exit 0. Only that row was asked: `orbit_rows_to_ask` skips a
   row whose series the card already states, so the seven certified rows were not recomputed and their
   values were not rewritten — the card's stored block gained one row.

## What was written

| path | change |
| --- | --- |
| `lattices/6JRR.md` | `integral.primitive_orbits.SOtilde+ = {constant: 527, z: [], w: []}`; `integral.primitive_orbits` → `4282656a…`; the two paragraphs describing the orbit block rewritten for eight rows |
| `certificates/e1.yaml` | the one hash `6JRR integral.primitive_orbits`, `ed8a588f…` → `4282656a…` (one line, `by: research preamble`) |
| `failures/e1.yaml` | `6JRR integral.primitive_orbits[SOtilde+]`: `open` → `resolved`, with the release note naming the repair |

`certificates/e1.yaml` was rewritten whole and every other entry in it is unchanged: the diff is one
line. The field's certificate is one hash over the row set (the schema has one `certifications` key per
field), so the eighth row necessarily re-mints the field's hash and nothing else.

## Post-conditions, checked

`checks.records.problems(corpus.cards(root, ("6JRR",)), certificates.load(root, ("6JRR",)), {"6JRR"})`
→ **0 problems**, over the card, its two arithmetic-group cards and their certificates; the card now
lists the eight rows `{'O': 1, 'SO': 1, 'O+': 1, 'SO+': 1, 'Otilde': 527, 'SOtilde': 527,
'Otilde+': 527, 'SOtilde+': 527}`. `checks.relations.problems(loaded, root, {"6JRR"})` → 0.
`checks.catalogues.problems(loaded)` on this tag-scoped load reports 2: both group cards' `ambient Lie
group o-2-9 is not in the corpus`, which is a property of the scoped read (`corpus.cards` reads the
lattice, its group cards and nothing else; `lie-groups/o-2-9.md` exists) and not of these cards.

Not run, and why: `latticedb verify` is corpus- or shard-scoped (`checks.one_shard` starts with
`corpus.load(root)`, 7.3 GiB of cards and 9 GiB of certificates, and this VM reports 9–11 GiB free), so
"`latticedb verify` on the affected cards" is the CI shard's line to produce, not one this turn can.
`checks.records.shared_gram_problems` is corpus-wide for the same reason.

## Tests

`pytest tests/test_genus.py tests/test_failures.py tests/test_persist.py tests/test_catalogue_schemas.py
-q` in the same image: **74 passed, 1 failed** —
`tests/test_persist.py::test_shards_push_progress_repeatedly_without_touching_their_worktrees`, which
fails on a `git cherry-pick` conflict inside `.github/scripts/persist.sh` in its own temporary
repository. It fails identically on a pristine worktree at `0f28d1ef3b`, the parent of this change, so
it is not this change's: the test never reads a lattice card, and the defect is pre-existing.

## The generators of the two groups: recorded as not supplied

`sage-extensions#597` closes the generation half with a proof rather than a measurement:
$\widetilde O(T_{\mathrm{Co}})$ is the principal congruence subgroup of level $2$, and every published
generation statement fails a hypothesis — $\mathrm{rank}_2(T_{\mathrm{Co}}) = 0$ against Kneser's
$\mathrm{rank}_2 \ge 6$, Gritsenko–Hulek–Sankaran's Proposition 3.4 needing two hyperbolic planes,
Allcock's Bertini family stated for $\Lambda(2)$ of rank $10$ — while the one route left, the Schreier
family over $46998591897600$ cosets, did not return in 600 s (4607 MiB, rising, exit 124). The owner's
`stable_orthogonal_group_generators` now refuses that lattice with the failing hypothesis named
(`2c441da`).

So `data.generator_morphisms` stays absent on both group cards, and the cards say so with the reason
and the issue: `arithmetic-groups/otilde-t-co.md`, `arithmetic-groups/otilde-plus-t-co.md`, and the
paragraph of `lattices/6JRR.md` that lists the attached groups. No generator set was written and no
`index()` was called: the two indices stay as they were certified,
`46998591897600` (`682c595c…`) and `93997183795200` (`326145cc…`).

## The one ledger entry this turn adds, and why

With the orbit row resolved, the fields phase of `certify --tag 6JRR` asked exactly one computation:

    phase fields ['arithmetic-group.otilde-plus-t-co.generator_morphisms']

That is the same impossible enumeration as the parent group's, whose entry
(`6JRR arithmetic-group.otilde-t-co.generator_morphisms`) is already `open` in `failures/e1.yaml`, and
leaving one of the pair quarantined and the other asked would spend a scheduled job — the previous one
died at 5609 s and 14 GiB — on a computation #597 proves cannot return a generating family. So it is
recorded as `open` with the probe as its evidence, in the shape the `SOtilde+` row's entry already has
(`reason` "did not return: …", `stderr` naming the measurement rather than a worker traceback,
`seconds: 600`). After that entry the fields phase of `certify --tag 6JRR` asks nothing, and the
searches phase still asks the semi-decisions `roots` and `norms`, which are their own item.

This one is a judgement call and is reversible with one command:
`just retry-computation 6JRR 'arithmetic-group.otilde-plus-t-co.generator_morphisms' --note …`.
