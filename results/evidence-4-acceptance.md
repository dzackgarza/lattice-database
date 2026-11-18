# #4: the acceptance, item by item, decided

Issue #4 is closed and was accepted on 2026-11-09. This file re-decides its `Accepted when` sentence
item by item, then the body's remaining clauses, on the tree as it stands. Runtime throughout: the
pinned research image (`ghcr.io/dzackgarza/sage:develop` rootfs, `/sage/.venv/bin/python` 3.14.10,
`PYTHONPATH=research/src:src`), with sage-extensions `main` at `8b43451` bound at
`/repos/sage-extensions` — the image's baked checkout is stale and still fails at import
(`ImportError: cannot import name 'QQ'`), which is the environment and not the code. Host: 4 cores,
15 GiB, load average 30 while these ran.

Line numbers are those of the pushed tree (`src/latticedb/sage_genus.py` and `tests/test_genus.py` are
unchanged between `88651884d3`, `cef9c85209` and `88651884d3`'s descendants that touch only cards).

## Item 1 — "serialize the value, not its text": holds

`_rational` builds the number from the value's own numerator and denominator, and nothing reads the
printed form:

- `src/latticedb/sage_genus.py:224` `_rational`; the construction at `:226`
  `Fraction(int(value.numerator()), int(value.denominator()))`.
- Its two callers: `_coefficients` `:230`, `_local_densities` `:235`, the owner call at `:238`.
- `rg 'Fraction\(str' src/` → no match.

Smallest input that reaches it: $I_3=\langle1,1,1\rangle$ (card `0022`), one local density.

    m=1 type=sage_extensions.owned_category.OwnedJoinCategory.element_class str='(3)/(2)' num=3 den=2 rational='3/2'
       Fraction(str(value)) -> ValueError: Invalid literal for Fraction: '(3)/(2)'
    --- the real _local_densities path
    [{'prime': 2, 'densities': ['3/2', '3/2', 1, '3/4']}]

(`results/evidence-4-rational.log:2-3` and the last line; probe `results/probe-4-rational.py`.) The
other element class the annotation names — an owned ring element, the $\theta$-series coefficients —
takes the same route (`_coefficients -> [1, 6, 12, 8]`), so this is not specific to the localization
ring.

**No guard and no fallback**, the body's own requirement, measured on four non-rationals
(`results/evidence-4-clauses.log:1-5`): `1.5`, `'3/2'`, `None`, `[1]` each raise
`AttributeError: ... has no attribute 'numerator'` at `:226`. There is no `try`/`except` anywhere in
`src/latticedb/sage_genus.py` (`rg -n '^\s*(try|except)\b'` → no match), and `_run` `:369` is
`_start`, `values = compute()`, `_emit`, return: an owner raise ends the worker, as its docstring says.

## Item 2 — "a regression test feeds the real `_local_densities` path an owner element whose `str` is `(3)/(2)`": holds

- `tests/test_genus.py:563`
  `test_certification_stores_the_exact_two_adic_densities_of_the_sum_of_three_squares` runs
  `genus.certify(tmp_path, loaded, held, ("0022",), time.time() + 120)` at `:587`, so the value passes
  through the worker and the real `_local_densities`; it asserts the stored densities at `:591` and
  the certificate at `:592`.
- `tests/test_genus.py:551` pins the property directly against the stand-in at `:535`, whose `__str__`
  is `(3)/(2)`, and asserts `Fraction` rejects that text.

The item is decided by the red run. With `src/latticedb/sage_genus.py:226` set back to
`number = Fraction(str(value))` and nothing else changed:

    File "/repo/src/latticedb/sage_genus.py", line 238, in _local_densities
    File "/repo/src/latticedb/sage_genus.py", line 226, in _rational
      number = Fraction(str(value))
    ValueError: Invalid literal for Fraction: '(3)/(2)'
    FAILED tests/test_genus.py::test_a_rational_is_serialized_from_its_numerator_and_denominator_never_its_text
    FAILED tests/test_genus.py::test_certification_stores_the_exact_two_adic_densities_of_the_sum_of_three_squares

(`results/evidence-4-red.log`.) With the committed line: `2 passed, 47 deselected in 64.17s`, run
against the pushed test file (`results/evidence-4-green.log`).

**The premise is asserted in the suite, in `tests/test_owner_rational_text.py:29`**
(`test_a_local_density_prints_the_text_a_fraction_rejects`): it builds the owner's genus for card
`0022`, asserts `str(density) == "(3)/(2)"`, that `Fraction` rejects that text, and that `_rational`
stores `3/2` — so the premise cannot rot silently if the owner's printing changes.

It is a module of its own because it loads the preamble into the test process, and the same assertion
in the wrong place costs a certify test its budget. Both placements were measured before this one:

- inside the end-to-end test, before `genus.certify`: the deadline at `tests/test_genus.py:587`
  (`time.time() + 120`) expired — `Certification time budget exhausted` after 179.87 s, against
  `2 passed in 59.63s` for the same file without it on the same host at load average 30;
- as its own test inside `tests/test_genus.py`: the certify worker was killed for memory,
  `memory: 1.6 GiB available; 0022 holds 0.2 GiB` (`1 failed, 2 passed in 82.64s`);
- as this module, the pair with that certify test passes in either order — 33.04 s with the premise
  test first, 40.50 s with the certify test first, at load average 17.75 on 15 GiB with 4 GiB free.

It runs in `justfile:108` (`just test-certification`), after `tests/test_genus.py`, so the worker never
meets the process's high-water mark. The certification workflow states its test files on one line that a
push from this connection cannot change (the connected app has no `workflows` permission), so that
one-line addition is checked and left unapplied in `results/certification-tests-4-premise.patch`
(`git apply --check` passes against the pushed workflow).

## Item 3 — "a dispatched `certify` run completes and writes at least one new certificate": holds

Read from GitHub's public Actions API and from the commits the run pushed; this connection cannot
dispatch or read workflow runs.

- `certify` run `44077055181` (run number 65): `event: workflow_dispatch`, `status: completed`,
  `conclusion: success`, 2026-11-17T11:46:41Z → 17:26:02Z, head `4c92ce1f89`.
- Its commit `b89236bf09` writes `6JRR integral.local_densities` at `certificates/e1.yaml:31406`, the
  value on the card at `lattices/6JRR.md:124`, and the card's hash at `lattices/6JRR.md:20` — the field
  the string parser killed.
- The earlier dispatched run `42370898252` (run 53, `conclusion: success`, 2026-11-07T12:05:03Z →
  16:33:24Z) wrote `026E integral.local_densities` at `certificates/f1.yaml:28`, value at
  `lattices/026E.md:83`.
- Scale on the current tree: 122,184 `integral.local_densities` certificates in 256 group files
  (`rg -c '^[0-9A-Z]+ integral\.local_densities:' certificates/`).

The issue's Result sentence also claims the **scheduled** run: runs 60 (2026-11-14) and 61 (2026-11-15)
are `completed/success`; run 66 started 2026-11-17T12:00:08Z and was `in_progress` when read at
23:07:17Z, so the newest scheduled run is not claimed complete here.

## Body clause — an undecided answer stores nothing: holds

`case _: return None` at `:192` (`_reflective` `:183`), `:203` (`_regular` `:196`) and `:214`
(`_spinor_regular` `:207`), and `genus.store` drops such a value at `src/latticedb/genus.py:789-790`
(`for key, value in values.items(): if value is None: continue`). Measured: storing
`{"local_densities": None, "genus_symbol": None}` over card `0022` leaves `local_densities` absent from
the card (`results/evidence-4-clauses.log:6-8`).

## Body clause — research and sage-extensions tracked at `main`: holds, the quoted lines have drifted

The body cites "`pyproject.toml` line 17; `.github/actions/sage/action.yml` line 9". Today:
`pyproject.toml:16` is `"dzack-research @ git+https://github.com/dzackgarza/research"` (unpinned), and
the step that installs it together with its requirements is `.github/actions/sage/action.yml:33-42`
(`uv pip install --requirements research/pyproject.toml`); `action.yml:9` is the `research` *checkout*,
not the install. sage-extensions reaches the run through research's own dependency, at `main`, which is
what the body's claim needs.

## Body clause — the second database-side piece, `genus.applies`: not changed here

`src/latticedb/genus.py:125` `applies(field, lattice)`. It is #8's unit and no line of it was touched by
this fix; it stays the filter between a card's fields and the owner calls the database makes.

## Body clause — the `KeyError: ((1,), ())` read in this unit: decided, owner-side, now green

The record already in the repository is `results/evidence-19/unrelated-preexisting-failures.log:6`. The
KeyError is Sage's cache wrapper re-raising, `sage/misc/cachefunc.pyx:1965` (`return cache[k]`); the
underlying raise is the owner's `AttributeError: 'int' object has no attribute 'parent'` at
`sage_extensions/categories/definite_lattices.py:294`, reached from the database at
`src/latticedb/records.py:240` (`_definite` → `reflective_root_system_components()`). No database parse
is in that path: the key never existed because the owner's computation raised.

At sage-extensions `8b43451` the line that raised is `definite_lattices.py:441`
(`engine_target = SageZZ(_engine_element(target.parent(), target))`), its caller is `:502`, and the two
tests that recorded the failure now pass: `tests/test_records.py::test_derive_computes_the_dual_gram_tensor`
and `tests/test_verification.py::test_a_shard_reports_the_problems_of_its_own_cards_only`, `2 passed in
4.40s`. So the strand closes as owner-side, with no database change owed.

## Files

- `tests/test_owner_rational_text.py` — item 2's premise, on the owner's own object, asserted in the
  suite; listed in `justfile:108`.
- `results/certification-tests-4-premise.patch` — the same listing for
  `.github/workflows/certification-tests.yml`, checked and unapplied (no `workflows` permission here).
- `results/probe-4-rational.py`, `results/evidence-4-rational.log` — item 1 on the owner's object.
- `results/probe-4-clauses.py`, `results/evidence-4-clauses.log` — no fallback; undecided stores nothing.
- `results/evidence-4-red.log`, `results/evidence-4-green.log` — item 2's red and green runs.

No line of `src/` is changed by this record.
