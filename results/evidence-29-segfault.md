# #29: the segmentation fault, its cause, and what is still open

## The crash: two `libflint` builds in one process

`tests/test_bulk_sources.py` line 17 computed `int(fmpz_mat(quaternary.gram_tensor).det())`. In the
image, with `import sage.all` first — which is how the `tests` workflow starts its interpreter —
that call dies:

    Fatal Python error: Segmentation fault
      File "/repo/tests/test_bulk_sources.py", line 17 in test_nipp_tables_preserve_the_source_discriminants_and_group_orders
    ...
    /lib/x86_64-linux-gnu/libflint.so.19(fmpz_set+0x25)
    .../flint/types/fmpz_mat.cpython-314-x86_64-linux-gnu.so(+0x10d18)

The two libraries:

    python-flint 0.9.0 extension  ->  python_flint.libs/libflint-6839011d.so.24.0.0   (FLINT 3 build)
    Sage 11.0.beta5               ->  /lib/x86_64-linux-gnu/libflint.so.19.0.0      (FLINT 2.9 build)

`python-flint` ships its own FLINT under a mangled soname, but its `fmpz_set` resolves to the symbol
the process already loaded — Sage's `libflint.so.19` — so `fmpz_mat.det()` writes an FLINT 3 `fmpz`
through FLINT 2 code and the interpreter dies. Measured: the same expression succeeds in a process
that has **not** imported `sage.all` (`det: 4`), and segfaults in one that has.

## The repair

`tests/test_bulk_sources.py` now takes the determinant from the FLINT build the process already has:
Sage's own `matrix(ZZ, ...)` wherever `sage.all` is importable, `python-flint` only where it is not.
The assertion is the same equality against the source's stated discriminant, `(4, 4)` and `(2, 4)`.
`python-flint` is imported inside that branch, so the Sage process never loads the second build.

    $ python -c 'import sage.all, ...; pytest tests/test_bulk_sources.py'   # the workflow's order
    ......                                                                   [100%]
    6 passed in 25.66s                                       (before: exit 139 at the first test)

## The 70 minutes: named, not yet fixed

`tests/source_intake/test_hoehn_mason_source.py` runs in 0.53 s for its first test; the second,
`test_row_81_source_generators_are_the_seeded_self_isometries`, does not finish in 25 minutes. Its time
is one call, `hoehn_mason.automorphisms(leech, entry, record)` for the rank-19 record 02AQ, and a stack
dump after seven minutes puts it here:

    hoehn_mason._record_isometry -> hashimoto.basis_isometry -> FormModules...preserves_forms
      -> _form_square_commutes -> b -> _evaluate_by_bilinearity
      -> pure_tensor -> linear_combination -> _linear_combination_from_generator_coefficients

`preserves_forms` asks the form for every one of the 19×19 Gram entries, and the form of the subobject
`A ⊂ leech[1]` is a restriction/tensor presentation, so each entry is expanded through
`pure_tensor` instead of being read: seconds per entry, about 361 entries.

Attempted and rejected this turn: deciding the same question on `_numerical_form(target)`, the same
form rebuilt on its own Gram tensor. It did not shorten the run (still over 30 minutes), so the
remaining cost is on the source's side as well — `_formed(record.gram_tensor).twist(twist)` — and the
change was reverted rather than pushed unverified. A supporting defect: `sublattice.gram_matrix()`
raises `AttributeError: 'RestrictedScalarsModules.parent_class' object has no attribute
'matrix_space'`, so the subobject's form cannot be read as a matrix at all.

For the orchestrator to file against sage-extensions: `FormModules.Mor(...).preserves_forms` costs
O(rank²) tensor expansions on a subobject's form where the same decision on the Gram tensor is
immediate; and `gram_matrix()` fails on a formed module over restricted scalars.

## The preamble step: `13 passed`, exit 1

The owner's suite is run as a two-file selection from this repository, with its own `pyproject.toml`
`addopts`, which include `-p sage_extensions.testing.suite_budget`. That plugin grades the preamble
import, collection and each test's call phase against baselines recorded for sage-extensions' own full
suite, and ends the session nonzero when a gate fails after every test has passed — `13 passed in
55.63s` followed by exit 1.

`results/tests-workflow-owner-time-gates.patch` runs the contracts with `--no-time-gates`, the flag
that plugin documents for a run that is not its own suite. The contracts still run and still decide
the step. Verified here against sage-extensions main (32e116e) in the image: the selection runs in
5.32 s, and the one failure it reports is the owner's own —
`test_primitive_orbit_series_counts_primitive_isotropic_lines` raising
`TypeError: int() argument must be ... not 'OwnedJoinCategory.element_class'` inside
`sage_indefinite_port/indefinite/recursive.py:154` — so the step stays red until that is fixed
upstream, and no gate of ours is hiding it.
