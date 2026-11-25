# #37: the nine `tests` failures that stop in this repository

`tests` run `43007340416` (schedule, lattice-database `1224b1b184`, sage-extensions `dbe90c02ae`)
fails thirteen tests. Four stop in sage-extensions `primitive_orbit_series` on 026E and 0016 and are
sage-extensions#345; the nine below were reproduced at current main and each was traced to its owner.

Reproduction used the pinned image `ghcr.io/dzackgarza/sage:develop` (Sage 11.0.beta5, Python 3.14.10)
with a worktree of sage-extensions at `dbe90c02ae` — the revision of that run, not this VM's own
checkout — and `PYTHONPATH=<sage-extensions>/src:~/research/src:src`.

| Test | Stop at current main | Owner and cause | Repair |
| --- | --- | --- | --- |
| `test_catalogue_schemas.py::test_an_arithmetic_group_generator_is_one_scale_one_self_isometry_of_its_lattice` | passes | #34 (`6bd4baa097`): the fixture held no certificates, so every cited value of 0012 read as contradicting one | already landed |
| `test_catalogue_schemas.py::test_the_coble_card_and_its_group_cards_state_only_their_defining_data` | passes | #34 (`6bd4baa097`): the test pinned `"certifications" not in` a card that CI certified | already landed |
| `test_certify_process.py::test_an_early_termination_does_not_blacklist_a_computation_for_a_whole_job` | `certification did not announce the root search` | the test's fixture: a card copied without its certificates recomputes 0016's eight fields in 74 s before the searches, and cuts the run at 60 s | `bc38e6e43c` |
| `test_geometric.py::test_k3_hodge_diamond_and_lattice_link_are_published` | `KeyError: '0011'` at `site.py:530` | the site build: it resolved every `related` tag of a card through the loaded corpus, so a fixture of eight cards could not render `0001`, which relates to 58,337 cards | `88d7dbae57` |
| `test_geometric.py::test_symmetric_spaces_and_analytic_variety_are_published` | `KeyError: '0015'`, same line | same | `88d7dbae57` |
| `test_legacy_morphisms.py::test_imported_implicit_scales_become_explicit_without_changing_scaled_maps` | `git show 287b70c979…:lattices/0001.md` exits 128 | the test and `restore`: the migration read its pinned revision through `git`, and CI's checkout holds one commit | `7b04c3f6af` |
| `test_records.py::test_derive_computes_rational_definite_invariants_through_the_integral_twist` | `TypeError: unable to coerce <class 'fractions.Fraction'> to an integer` | sage-extensions: `QQ(Fraction(2, 3))` and `Lattices(QQ)` over a nested list of `Fraction` refuse a Python `Fraction` | issue text at `results/issue-sage-extensions-qq-fraction.md`; not posted, see below |
| `test_verification.py::test_a_shard_reports_the_problems_of_its_own_cards_only` | `assert [] == ()` | the test: `checks.run` returns `list[str]`, as its annotation says, and the test compared it to `()` | `d2662e4df8` |
| `validation/test_build.py::test_rows_render_only_stored_root_type_and_root_span_data` | `('D10', 'B10', 'B10(1/2)') == ('D10', 'B10', 'I_{10,0}')` | the test: three expectations name lattices the cards state under other, documented names; no card changed | `65157c27d6` |

## The rows that were already green

#34 (`6bd4baa097`) repaired both `test_catalogue_schemas.py` failures before this batch, and both pass
at current main with `dbe90c02ae`; they are in the table only to close the row they came from.

## The row whose stop is in sage-extensions

`QQ(Fraction(2, 3))` raises `TypeError: unable to coerce <class 'fractions.Fraction'> to an integer`
inside `ring_foundation.py`'s `source_element`, so `Lattices(QQ)` refuses the nested list of rational
values that `records.derive` hands it at `src/latticedb/records.py:320`. Reproduced through the public
calls only, at both `dbe90c02ae` and the newer `441519c`. This connection's GitHub App has no write
access to `dzackgarza/sage-extensions` — it cannot open an issue there — so the report is the file
`results/issue-sage-extensions-qq-fraction.md`, which carries the reproducer, the expected behaviour,
the database call that hits it and the run provenance. It has not been posted.

## What was measured, and what was not

Measured in the image at `dbe90c02ae`:

* `tests/test_geometric.py` 6 passed (was 2 failed).
* `tests/test_verification.py` 7 passed (was 1 failed).
* `tests/test_legacy_morphisms.py` 1 passed, and also in a copy of the tree whose repository holds a
  single commit and no history — the CI condition — where the test before this batch failed with
  `CalledProcessError … exit status 128`.
* `tests/test_certify_process.py::test_an_early_termination_does_not_blacklist_a_computation_for_a_whole_job`
  1 passed in 14.5 s (was `certification did not announce the root search` at 63.5 s).
* `genus.requests` for a fixture of 0016 that holds the card's 14 certificates: one request, the
  searches `["roots", "norms"]`; and `legacy_morphisms.restore(REPOSITORY, REPOSITORY)` returns `()`
  on main without touching a card, so the git-backed path still reads the pinned revision.

Not measured here:

* `tests/validation/test_build.py`: every test in it builds the full 302,504-card site and
  `corpus.load` holds about 7.5 GiB, which does not fit on this 15 GiB VM beside the other projects'
  work. The seven rows the repaired test reads were checked through `site.row` on the cards alone:
  0094 `E8`/`E8`, 0120 `D10`/`B10`/`B10(1/2)`, 0110 ``/`D8 A1`/`D8(2) + A1(4)`, 0016
  `<1>(2) + <1>(-2)`, 0151 `D12`/`D12`, 0150 `0`.
* `tests/test_records.py`: the file's other tests were not separated from the failing one here; the
  row's stop is the owner's and the module's state follows it.
* The rest of `tests/test_certify_process.py`: `test_a_search_that_never_ends_does_not_hold_back_other_cards`
  stops on sage-extensions#345 on this card, and `test_finishing_a_previously_interrupted_computation_clears_its_log`
  failed here only on its own 60 s budget under this VM's load; neither is one of the nine rows.
