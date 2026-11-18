# #29: the three acceptance items, re-decided on main

Both upstream blockers the last comment on the issue names are closed, so each item can be decided
again:

- **dzackgarza/sage#25** (one `libflint` in the image) — closed 2026-11-12T16:08:41Z.
- **dzackgarza/sage-extensions#320** (`preserves_forms` on a formed submodule) — closed at
  `f4580f1684`, 2026-11-11T05:34:13Z.

**The tree.** `main` at `64896df0e6`, plus the four lines this turn adds at `tests/test_genus.py:495`,
`:521`, `:529` and `:682` (item 1, § "the one failure that was left").

**How it was measured.** In the pinned research image (`image.json` revision `6301b4e4…`, digest
`sha256:332aebe9…`), `/sage/.venv/bin/python` 3.14.10, `PYTHONPATH=research/src:src`, with
**sage-extensions main `64e04012`** bound at `/repos/sage-extensions`. The bind is not optional: the
image's baked checkout is `cf656f8c` and does not declare `QQ` (`src/sage_extensions/rings/__init__.py:165`
on main), so `src/latticedb/graphs.py:36` dies there with `ImportError: cannot import name 'QQ'`. That
is the stale image, not the code. The suite's collectors are the ones CI pins: `ai-review-ci` at
`e3ecc613`, `-p qc_sage_session -p qc_unique_inventory`.

## 1. A tests run completes the suite step: every collected test reports, no interpreter crash

The crash was `python-flint` 0.9.0's vendored FLINT 3 (`python_flint.libs/libflint-6839011d.so.24.0.0`)
resolving `fmpz_set` against the image's FLINT 2.9, which Sage links. Both halves are now decided:

- **The image holds one FLINT.** `import sage.all; from flint import fmpz_mat;
  fmpz_mat([[2,1],[1,2]]).det()` → `3`, exit 0 (before: SIGSEGV, exit 139). The vendored
  `site-packages/python_flint.libs/` directory is gone; the `.libs` directories present are `fpylll`,
  `gmpy2`, `igraph`, `lrcalc`, `numpy`, `pillow`, `pyzmq`, `scipy`.
- **The repository no longer asks for it.** `pyproject.toml:6-17` names no `python-flint`;
  `tests/test_bulk_sources.py:16` takes the determinant from Sage's own `matrix(ZZ, …)`;
  `tests/test_model.py:21` keeps `flint` in the `forbidden` tuple that `src/latticedb/*.py` is scanned
  against. (`research`'s own `pyproject.toml` still depends on `python-flint>=0.9`, so the library is
  installed in the CI venv; what changed is that nothing in this repository calls it, and the image can
  now load both.)

Deciding input — the test that died, at its new line, in the workflow's order (`import sage.all`
before pytest): `tests/test_bulk_sources.py:27` `test_nipp_tables_preserve_the_source_discriminants_and_group_orders`,
with the two determinants at `:30` and `:32`:

    $ pytest tests/test_bulk_sources.py
    8 passed in 2.49s        0.06s call  test_nipp_tables_preserve_the_source_discriminants_and_group_orders

8 and not 6 because the guard `_matrix_input` (`tests/test_bulk_sources.py:81`) landed with its two
tests (`:101`, `:111`): a ragged row, a float and a `bool` are named rather than handed to a
determinant. `results/probe-29-item1.log`.

**Collection.** `--co` over `tests` with the CI collectors: **327 tests collected, 0 collection
errors** (`results/probe-29-collect.log`). The six modules the step's comment names
(`.github/workflows/tests.yml:40`) no longer import `dz_research.preamble.categories` — no file under
`tests/` or `src/` names `dz_research` — so `--continue-on-collection-errors` is inert here.

**Every module on its own**, so that one crash or memory wall cannot hide another's reports: 30 test
modules, each in a fresh interpreter with a 4 GiB address-space cap (`results/probe-29-sweep.log`).
No module ended in a signal, and no interpreter crashed.

| module | exit | reported |
| --- | --- | --- |
| `tests/source_intake/test_hashimoto_source.py` | 0 | 3 passed in 1.02s |
| `tests/source_intake/test_hoehn_mason_source.py` | 0 | 3 passed in 3.72s |
| `tests/source_intake/test_nebe_sloane_source.py` | 0 | 19 passed in 4.21s |
| `tests/test_bulk_sources.py` | 0 | 8 passed in 2.13s |
| `tests/test_card_merge.py` | 0 | 5 passed in 1.67s |
| `tests/test_catalogue_schemas.py` | 0 | 17 passed in 11.89s |
| `tests/test_certify_process.py` | 0 | 8 passed in 233.97s |
| `tests/test_certify_reads.py` | 0 | 5 passed in 10.16s |
| `tests/test_construction_corpus.py` | 0 | 6 passed in 25.80s |
| `tests/test_corpus.py` | 1 | 20 passed, then `MemoryError` writing the cache under the 4 GiB cap |
| `tests/test_cusp_root_orbits.py` | 0 | 5 passed in 11.26s |
| `tests/test_failures.py` | 0 | 9 passed in 257.99s |
| `tests/test_geometric.py` | 0 | 6 passed in 89.24s |
| `tests/test_graphs.py` | 0 | 2 passed in 4.32s |
| `tests/test_hashimoto.py` | 0 | 2 passed in 7.24s |
| `tests/test_keyed_merge.py` | 0 | 2 passed in 30.96s |
| `tests/test_legacy_morphisms.py` | 0 | 1 passed in 7.53s |
| `tests/test_merge.py` | 0 | 3 passed in 4.36s |
| `tests/test_model.py` | 0 | 73 passed in 18.59s |
| `tests/test_morphism_scale.py` | 0 | 8 passed in 108.73s |
| `tests/test_nikulin_triples.py` | 0 | 5 passed in 845.58s |
| `tests/test_owned_boundaries.py` | 0 | 3 passed in 7.24s |
| `tests/test_persist.py` | 0 | 5 passed in 50.26s |
| `tests/test_rational_forms.py` | 0 | 4 passed in 2.82s |
| `tests/test_records.py` | 0 | 16 passed in 197.53s |
| `tests/test_recovery_launcher.py` | 0 | 2 passed in 145.55s |
| `tests/test_scattone_cards.py` | 0 | 2 passed in 8.07s |
| `tests/test_site_formatting.py` | 0 | 2 passed in 0.98s |
| `tests/test_verification.py` | 0 | 9 passed in 70.85s |
| `tests/test_verify_recovery.py` | 0 | 2 passed in 1343.45s |

`tests/test_corpus.py`'s one failure is the memory wall, not an assertion: its last test,
`tests/test_corpus.py:363` `test_the_stored_corpus_loads_through_the_reader_that_every_workflow_starts_with`,
is the untagged load of the whole repository — 7.29 GiB measured on this tree — and it died at the
4 GiB cap with `MemoryError` raised from `_pytest/cacheprovider.py:227` at session finish.

### The one failure that was left: the run's own memory reserve, not the code

`tests/test_genus.py` in the sweep reported four failures in its first 35 tests, and two of them
reproduced alone, on this VM at 1.4 GiB available:

    FAILED tests/test_genus.py::test_a_card_continues_on_a_new_worker_after_one_computation_fails
      tests/test_genus.py:491  AssertionError: at index 1 diff:
        {'tag': '0012', 'failed': 'memory exhausted', 'killed': {'by': 'memory', ...}}
        != {'tag': '0012', 'failed': 'exit status 1'}
    FAILED tests/test_genus.py::test_a_worker_killed_by_a_signal_is_reported_with_its_signal
      tests/test_genus.py:514  AssertionError: at index 0 diff:
        {'tag': '0012', 'failed': 'memory exhausted', 'killed': {'by': 'memory', 'peak': 0, ...}}
        != {'tag': '0012', 'failed': 'killed by signal 9', 'killed': {'by': 'signal 9'}}

`results/probe-29-genus-workers-before.log`. The cause is `genus.computed`'s own reserve:
`src/latticedb/genus.py:554` `reserve = int(MEMORY_RESERVE * _meminfo("MemTotal"))` (0.1 by default,
`genus.py:504`) and `genus.py:639` `if candidates and _meminfo("MemAvailable") < reserve:` → SIGKILL of
the largest worker, reported as `"memory exhausted"` (`genus.py:663-665`). On a runner whose free memory
dips below a tenth of its total, that kill preempts the failure each of these tests is about — so their
verdict is decided by how loaded the machine is, not by the code under test.

Four tests now pin the reserve out of the way; the one test whose subject *is* the reserve keeps
`MEMORY_RESERVE = 2.0` (`tests/test_genus.py:506`), and each pin says so:

- `tests/test_genus.py:495` — `test_a_card_continues_on_a_new_worker_after_one_computation_fails`
- `tests/test_genus.py:521` — `test_a_worker_killed_by_a_signal_is_reported_with_its_signal`
- `tests/test_genus.py:529` — `test_a_worker_that_fails_before_computing_is_not_replaced`
- `tests/test_genus.py:682` — `test_certification_keeps_a_root_lattice_integer_valued` (it failed under
  a forced reserve with `KeyError: 'integer_valued'` at `tests/test_genus.py:697`: the killed worker
  never wrote the field the test then reads)

Deciding input, both runs on a modelled loaded runner (`-p force_reserve`, which sets
`genus.MEMORY_RESERVE = 2.0` before the session, above this VM's free memory), over those five tests:

    HEAD as it is:      3 failed, 2 passed, 44 deselected in 28.74s      exit 1
    with the four pins: 5 passed, 45 deselected in 58.80s                exit 0

`results/probe-29-genus-red.log`, `results/probe-29-genus-green.log`. The pin does not weaken an
assertion: no test in the file asserts the reserve's message except the one that sets it to 2.0.

### What the sweep did not measure

- `tests/test_genus.py` stopped in its 36th test,
  `test_the_owner_s_orbit_counts_are_emitted_as_their_exact_cardinalities` (`tests/test_genus.py:840`),
  which did not return within 45 minutes on this VM under load; tests 37–49 of that module were not
  measured here. That is a slow test, not a crash — the module's earlier tests reported.
- `tests/test_stored_records.py` and `tests/validation/test_build.py` were not run: they open
  `certificates.load(REPOSITORY)` (`tests/test_stored_records.py:58`, 9.08 GiB measured) and
  `corpus.load(ROOT)` (`tests/validation/test_build.py:22`, 7.29 GiB), and this VM had 1.2–3.1 GiB
  available throughout while other projects' jobs held ~6 GiB.
- `tests/validation/test_construction.py` was still running (20 minutes, no test reported) when the
  sweep was stopped by hand; not measured.

**The run itself.** The `tests` workflow is `schedule` and `workflow_dispatch` only
(`.github/workflows/tests.yml:2-5`) and this connection has no dispatch, so the end-to-end decision is
the next scheduled run. The last `tests` run is `44077175689` (schedule, 2026-11-17T11:47:31Z, head
`4c92ce1f89`), red at step 7 ("Run every lattice database test…") and step 9 ("Validate preamble owner
contracts").

On the pushed commit `86bc85f9d4` there is no `tests` run; the only runs on it are `pages`
(`44251285303`, cancelled by its own concurrency group) and **Certification regression tests**
(`44251285213`, push, 2026-11-18T06:26:00Z, **failure**), whose single suite step runs
`.github/workflows/certification-tests.yml:34-39`:

    tests/test_genus.py tests/test_failures.py tests/test_persist.py tests/test_corpus.py

in one process, in 22m42s (06:27:40-06:50:22), on the same image and the same collector as the `tests`
workflow. Its failure is not this change's: every run of that workflow on 2026-11-18 is red — the
twelve newest are `44206527418`, `44206530392`, `44217873313`, `44221212515` (cancelled),
`44235241685`, `44243823221`, `44245524701`, `44246820134`, `44247491925`, `44247706774`,
`44251285213`, and one still running — across commits `39f5a36843` to `86bc85f9d4`, several of them
older than the pins above installed here today.

What that run failed on cannot be read from this connection: the run has **0 artifacts**, the job log
(`/actions/jobs/{id}/logs`) answers **403** anonymously, and its check-run annotations carry only the
exit status (`Process completed with exit code 1`, step 5). Reading it needs `actions: read` on the
repository; making the `tests` workflow itself run needs `actions: write` (dispatch). Neither is held
here, so neither the cause of that red nor item 1's end-to-end decision is decided in this file.

## 1b. The suite step must terminate: a per-test ceiling, thread method

Run `44268649907` (`workflow_dispatch`, head `3e233c6c9b`, 2026-11-18T08:37:49Z — `main`, with both of
this issue's commits as ancestors) entered step 7, "Run every lattice database test, including Sage
sessions and source intake", at 08:46:53Z and **was still inside it 88 minutes later** with steps 8–10
`pending`; it was cancelled at 10:08:38Z having produced no verdict. A step that never returns is the
same defect class as the segfault this issue names — the run does not terminate — and it leaves item 1
with nothing to read.

**Repair** (`pyproject.toml`, `[tool.pytest.ini_options]`): every test is bounded.

    timeout = 1800
    timeout_method = "thread"

and `pytest-timeout>=2.4` is now declared in this repository's own `dev` group; before this it reached
the image only through `research`'s dev group, so nothing here said the option was supported.

*Why the thread method.* The signal method raises inside the test, which only helps code that returns
to Python — the case that hangs is a call that never does (Sage/FLINT/pari inside a worker). The thread
method cannot interrupt either, but on the ceiling it dumps every thread's stack and ends the run, so
the log carries the test that hung, by name, and the step ends inside its budget instead of being
killed by the job timeout with no output.

Proven on a test that never returns, ceiling 5 s:

    $ pytest -q --timeout=5 --timeout-method=thread .scratch/test_hang_demo.py
    +++++++++++++++++++++++++++++++++++ Timeout ++++++++++++++++++++++++++++++++++++
    ...
      File "/repo/.scratch/test_hang_demo.py", line 5, in test_this_one_never_returns
        time.sleep(600)
    +++++++++++++++++++++++++++++++++++ Timeout ++++++++++++++++++++++++++++++++++++
    EXIT=1

`results/probe-29-timeout-demo.log`. The ceiling does not disturb the selection: `--collect-only` on
`tests/test_card_merge.py` collects 5 tests with no "Unknown config option" warning.

*Why 1800 s.* Above the slowest legitimate test measured on this tree (1343 s,
`tests/test_verify_recovery.py`, on a loaded 4-core VM with other projects holding ~6 GiB) and 30
minutes, far inside the step's `timeout-minutes: 350`. A segfault needs no ceiling to be named: pytest
enables `faulthandler`, and the crash this issue opened with was reported that way — `File
"/repo/tests/test_bulk_sources.py", line 17 in test_nipp_tables_preserve_the_source_discriminants_and_group_orders`.

**What the ceiling catches first on this tree.** The same selection run locally with a 300 s ceiling
(`--timeout=300 --timeout-method=thread`, `results/probe-29-timeout-sweep.log`) ended 14m26s in and
named one test:

    File "/repo/tests/test_corpus.py", line 371, in test_the_stored_corpus_loads_through_the_reader_that_every_workflow_starts_with
      loaded = corpus.load(ROOT)
    File "/repo/src/latticedb/corpus.py", line 253, in load
      document = read_card(path)
    File "/repo/src/latticedb/corpus.py", line 63, in read_card
      return frontmatter.load(path, handler=_CARD_YAML)

That is the whole-corpus read — 7.29 GiB, measured at 421 s when the VM is quiet — not a hang, and it is
why the committed ceiling is 1800 s and not the 300 s this probe used: the step's non-termination is
most plausibly this same memory-bound read thrashing inside a 16 GB runner that already holds the
suite's other loads, and a ceiling below the read's cost would fail the suite on a slow runner instead
of naming a hang.

**The ceiling in CI.** Run `44284006493` (`workflow_dispatch`, head `193234cebe`, the commit that adds
the ceiling) entered step 7 at 10:27:10Z and **ended it at 11:26:17Z — 59 minutes, exit code 1** — with
the job completing at 11:26:37Z, well inside its `timeout-minutes: 350`. The run before it, without the
ceiling, sat 88 minutes inside the same step with steps 8–10 `pending` and was cancelled with no
verdict. The step now terminates and hands pytest's own exit status up.

What that exit status contains is not readable from this connection: the run has **0 artifacts**, and
the run-log, the job-log and the job's own log endpoint each answer **403** anonymously. `exit code 1`
is what pytest reports for failing tests and also what the thread method's `os._exit(1)` produces
(`pytest_timeout.py:542`), so which tests failed — or whether the ceiling itself fired — is in that log
and needs `actions: read`. The first failing frame of this run is therefore not quoted here.

## 1c. The frame, from the repository owner's reading of that log, and the three costs behind it

The frame, quoted from the job log: the run did not fail on a test's assertion but on the ceiling,
inside the pandoc call of the site build —

    tests/validation/test_build.py:28  built -> site.build(ROOT, target)
    src/latticedb/site.py:520          markdown_to_html([... entries, pages, theory])
    src/latticedb/site.py:377          [convert(text) for text in texts]
    src/latticedb/site.py:374          subprocess.run(command, input=text, capture_output=True, text=True, check=True)
                                       ++++++++++++++++++ Timeout ++++++++++++++++++

Measured on this tree, in the pinned image:

| | |
| --- | --- |
| texts `build` converts | 302,504 cards + 8 pages + 11 theory = **302,523** |
| one pandoc call | **12.0 ms** bare, **11.8 ms** over 200 real cards |
| the whole corpus, one process per text | **59 minutes** of process starts alone |
| the build's marginal cost per card | **35.75 ms** (500 cards 54.1 s, 2,000 cards 107.7 s; fixed overhead 36 s) |
| the whole site at that rate | **≈181 minutes** |

A profile of the 2,000-card build splits the marginal cost: `corpus.read_card` 26 ms per card; the
page's Jinja render 41 ms, of which 16 ms is the owner's
`quadratic_hypersurface_zeta_factorization` (sage-extensions `lattice_zeta_invariants.py:36`, called
3,988 times for 2,000 cards); `site.broken_links` 36 ms per page. So the count is the problem and no
ceiling value fixes it: the whole-corpus build is hours, not minutes.

**It could not finish at all, at any speed.** `site.build` refuses a page whose link reaches nothing,
and one card wrote its links to the wrong directory: `lattices/0125.md` said
`../arithmetic-groups/g-e.html` and `../arithmetic-groups/h-e.html` where the builder writes
`arithmetic-group/` (singular, `site.py:508`). Its first frame was
`tag/0125.html: ../arithmetic-groups/g-e.html`. Repaired at `lattices/0125.md:567`, `:569`, `:571`.

**The fixture now builds a bounded corpus** (`tests/validation/test_build.py`): the twelve tags the
module asserts on, every lattice their morphisms reach, every lattice an arithmetic-group or lie-group
card names, the two collection pages it asserts on (`even-unimodular.md`, `root-lattices.md`), and the
small content directories — instead of all 302,504 cards. Every assertion is unchanged; only the corpus
the builder is given shrinks.

    $ pytest tests/validation/test_build.py
    17 passed in 70.80s

`results/probe-29-build-bounded.log`. The 1800 s ceiling is now two and a half orders of magnitude away
from what this fixture costs.

**What was tried and reverted.** Converting the texts in chunks (one pandoc process per 512 texts,
joined by an HTML comment, split on the same comment) is 30× faster — 0.08 s for 200 texts against
2.55 s — but pandoc deduplicates heading identifiers within one document, so `morphism-provenance-to-027e`
came back as `…-027e-2`, `…-3`: the site's anchors would change. The change is not in this tree; with
the bounded corpus the 59 minutes never arises here.

## 2. The Hoehn–Mason tests run in the time of an ordinary unit test

The 70 minutes were one owner call: `hoehn_mason.automorphisms` (`src/latticedb/hoehn_mason.py:195`)
opens with `_record_isometry` (`:174`), which asks `hashimoto.basis_isometry`
(`src/latticedb/hashimoto.py:144`) for its verdict, which is `form_morphisms.preserves_forms(module_map)`
at **`src/latticedb/hashimoto.py:156`**. On row 81 the target is a formed submodule of the Leech
lattice over restricted scalars, and the owner answered each of its 19×19 Gram entries by expanding the
restriction: one `b(x, x)` measured 156.65 s.

The cause is the owner's and is fixed there: sage-extensions#320, closed at `f4580f1684`, with the
owner's own measurement of `preserves_forms(R, A)` on 02AQ at **1.04 s** against no return within
1500 s. No consumer change is made here — the alternative, deciding the same question on a rebuilt twin
of the target, was landed at `0b6e8d0ce1` and reverted at `587d56febe`; `hashimoto.py:156` still decides
on the target the caller gave it.

Measured now:

    $ pytest tests/source_intake/test_hoehn_mason_source.py
    3 passed in 3.74s
      2.42s call  test_row_81_source_generators_are_the_seeded_self_isometries   (:33)
      0.83s call  test_row_81_source_inclusion_is_the_seeded_leech_embedding    (:44)
      0.01s call  test_row_81_entry_is_read_from_the_stored_ancillary_file     (:25)

and with its neighbours, `tests/source_intake` + `tests/test_bulk_sources.py` +
`tests/test_owned_boundaries.py`: **36 passed in 8.84 s** (the same trio was 19 passed in 229.93 s
before the owner's fix, and the Hoehn–Mason file alone was 70 minutes in CI).
`results/probe-29-item2.log`, `results/probe-29-item3.log`.

## 3. The preamble step exits 0 when its tests pass

The step printed `13 passed` and exited 1 because of the owner's post-run performance gate, not a test:
`src/sage_extensions/testing/suite_budget.py:139-144` overwrites `session.exitstatus` with
`ExitCode.TESTS_FAILED` whenever a selected test's call phase, the star import or collection exceeded
its ceiling — passed or not. `.github/workflows/tests.yml:80` runs the step with `--no-time-gates`, the
flag that plugin documents for a run that is not its own suite (`suite_budget.py:54`, applied at `:141`).

Deciding input: the same passing selection with the gate armed against a ceiling it cannot meet
(`-o time_gate_call_ceiling=0.001`), and with the flag:

    gates armed:       1 passed in 0.72s    exit=1
    --no-time-gates:   1 passed in 0.87s    exit=0

`results/probe-29-gate-on.log`, `results/probe-29-gate-off.log`. So the step's exit status is the
tests' own. On the step's real selection the current state is **1 failed, 12 passed in 8.71 s**, exit 1
(`results/probe-29-item3.log`), and the failure is the owner's own contract inside the owner's own
library, not this repository's:

    tests/lattices/test_lattice_database_owner_contracts.sage:93
    Lattices(ZZ)([[1, 0], [0, -1]]).integral_hyperbolic_index()
      sage_extensions/categories/lattices.py:6734 integral_hyperbolic_index
      sage_extensions/categories/lattices.py:6872 hyperbolic_index
      sage_extensions/categories/lattices.py:6765 _direct_hyperbolic_splitting
      sage_extensions/categories/lattices.py:10875 hyperbolic_partner
        for residue in projection.codomain():
    AttributeError: '_SelectedFinitePresentationModules.parent_class[_PresentedModule].ObjectType'
                  object has no attribute 'list'

The step is therefore red on a test and not on a performance gate; item 3 is the gate, and it is
decided by the two runs above.

## Not done here

- No dispatched `tests` run (no `workflows` permission on this connection): item 1's end-to-end
  decision waits for the schedule.
- The owner's failing contract test above has no issue number from this session (no issue-creation
  permission); it is named by file and line so it can be filed where it belongs.

## 1d. The dispatched run after the build fix: still red, and what could not be read

Run `44304988129` (`workflow_dispatch`, head `0ab2ba44`, one commit above `dc80815d70`, 2026-11-18T12:33Z)
completed **failure** at 13:49:14Z:

| step | from | to | conclusion |
| --- | --- | --- | --- |
| 6 Provision the shared Sage environment | 12:44:40Z | 12:50:29Z | success |
| 7 Run every lattice database test… | 12:50:29Z | 13:48:56Z | **failure, exit 1** |
| 9 Validate preamble owner contracts | 13:48:59Z | 13:49:09Z | failure, exit 1 |

Step 7 again ended inside the job's 350-minute budget — 58 minutes, against 59 for the run before the
build fix — so the step terminates, but it is not green and its content is not readable here: **0
artifacts**, and the run-log, job-log and job-log-by-id endpoints each answer **403** anonymously.

What that leaves open is item 1's "every collected test reported", and it is not decidable from
outside: `exit 1` is pytest's status for failing tests and the thread method's `os._exit(1)`
(`pytest_timeout.py:542`) alike, and the frame that would distinguish them is in that log. Two readings
fit the numbers, and the evidence does not separate them:

- the suite ran to the end in 58 minutes and reported genuine failures — item 1 met as written;
- the 1800 s ceiling fired on a test reached about 28 minutes in, so the step ended 58 minutes in with
  one test named and the tests after it unreported — item 1 narrowed to that test.

The build is not that test: after `dc80815d70` the site build is 70 s (`results/probe-29-build-bounded.log`),
and `tests/validation/test_build.py` no longer carries a whole-corpus fixture. The remaining
memory-bound candidates, both measured on this tree before, are the whole-corpus reads —
`tests/test_corpus.py:363` (`corpus.load(ROOT)`, 7.29 GiB, 421 s quiet) and
`tests/test_stored_records.py:58` (`certificates.load(REPOSITORY)`, 9.08 GiB, 556 s) — which on a
16 GB runner already holding the suite's other loads can take far longer than they do on a quiet one.
