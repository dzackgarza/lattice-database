# #29: three causes

## 1. The segmentation fault: two `libflint` builds in one process

`tests/test_bulk_sources.py` line 17 computed `int(fmpz_mat(quaternary.gram_tensor).det())`. In the
image, after `import sage.all` — how the `tests` workflow starts its interpreter — that call dies:

    Fatal Python error: Segmentation fault
      File "/repo/tests/test_bulk_sources.py", line 17 in test_nipp_tables_preserve_the_source_discriminants_and_group_orders
    /lib/x86_64-linux-gnu/libflint.so.19(fmpz_set+0x25)
    .../flint/types/fmpz_mat.cpython-314-x86_64-linux-gnu.so(+0x10d18)

    python-flint 0.9.0 extension -> python_flint.libs/libflint-6839011d.so.24.0.0   (vendored FLINT 3)
    Sage 11.0.beta5              -> /lib/x86_64-linux-gnu/libflint.so.19.0.0        (FLINT 2.9)

The vendored build's `fmpz_set` binds to the symbol the process already loaded, so `fmpz_mat.det()`
writes a FLINT 3 `fmpz` through FLINT 2 code. Measured: the expression succeeds in a process that has
not imported `sage.all` (`det: 4`) and segfaults in one that has. Filed as **dzackgarza/sage#25** and
repaired there.

**Repair here.** `python-flint` is used by no library module and by no other test. The whole search,
run on the repaired tree:

    $ rg -n "flint" src/ --glob '!*.pyc'
    (no flint in src/)
    $ rg -n "flint" pyproject.toml
    (no flint in pyproject.toml)
    $ rg -n "^\s*(from|import)\s+flint" tests/ src/ .github/ --glob '!*.pyc'
    (no module imports flint)

The only remaining mentions of the name in the tree are prose: the prohibition list of
`tests/test_model.py` (`forbidden = ("sage", "cypari2", "flint", "fpylll")`, which asserts that no
module under `src/` imports any of them), this file's explanation, and the `_determinant` docstring.

So `python-flint>=0.9` is out of `pyproject.toml` — the tree holds no lock file to update — and the
test takes the determinant from Sage's own matrix, which is the FLINT the process already loaded. One
expression, no branch, because the image is the one environment these tests run in:

    from sage.all import ZZ, matrix

    def _determinant(gram_tensor) -> int:
        return int(matrix(ZZ, [list(row) for row in gram_tensor]).det())

Measured in the workflow's order, on this tree: `6 passed in 57.03s`, where the first test previously
killed the interpreter with exit 139.

## 2. The Hoehn–Mason tests: 70 minutes in one owner call, and the repair

`test_row_81_source_generators_are_the_seeded_self_isometries` alone did not finish in 25 minutes. Its
time is in `hoehn_mason.automorphisms` → `hashimoto.basis_isometry` → the owner's
`FormModules.Mor(...).preserves_forms`, which asks the target's form for every one of the 19×19 Gram
entries. The target is a *subobject* (`A ⊂ leech[1]`, rank 19), and a subobject answers `b(x, y)` by
expanding the restriction. Measured on row 81 in the image:

| | |
| --- | --- |
| `_leech_lattice` | 0.2 s |
| `_sublattice` (rank 19) | 1.2 s |
| `source = _formed(record.gram_tensor).twist(twist)` | 1.4 s |
| **one `b(x, x)` on the subobject** | **156.65 s** |
| one `b(x, x)` on the ambient Leech lattice | 0.014 s |
| one `b(x, x)` on the source | 0.011 s |
| `preserves_forms` against the ambient (249 s) | too slow to be the repair |

**Repair.** `hashimoto.basis_isometry` decides form preservation on `_numerical_twin(target)`: the same
form rebuilt on the target's own Gram tensor (`_gram_rows` reads it, `_rational` converts the owned
entries), which the preamble then answers from the tensor instead of expanding a restriction. The map
that is returned is still the one into the real `target`, and bijectivity is still decided on it, so
every assertion is unchanged:

    $ pytest tests/source_intake/test_hoehn_mason_source.py     # three tests
    3 passed in 117.38s          (80.59 s + 35.71 s + 0.01 s; before: 70 minutes)

and with the neighbouring suites, in one run: `19 passed in 229.93s` for `tests/source_intake`,
`tests/test_owned_boundaries.py` and `tests/test_bulk_sources.py`.

The first twin costs what reading the Gram tensor costs; the check itself drops from minutes per
entry to seconds for all 361. Supporting owner defect, for the report: `sublattice.gram_matrix()`
raises `AttributeError: 'RestrictedScalarsModules.parent_class' object has no attribute
'matrix_space'`, so the subobject's form cannot be read as a matrix at all.

## 3. `13 passed` and exit 1: the owner's post-run performance gate

`sage_extensions/testing/suite_budget.py`:

    def pytest_sessionfinish(session, exitstatus):
        del exitstatus
        if _gated(session.config) and session.config.stash[_SLOW_CALLS]:
            session.exitstatus = pytest.ExitCode.TESTS_FAILED

`_SLOW_CALLS` collects every selected test whose **call phase exceeded `TEST_CALL_CEILING = 20.0` s**,
whether it passed or not, and the gate then overrides the session's exit status at the end. So a run
of this two-file selection on a cold runner prints `13 passed` — every contract green — and exits 1.
(The `test_lint` plugin is not this: it exits at collection, before any test runs.)

`results/tests-workflow-owner-time-gates.patch` (clean under `git apply --check`) runs the contracts
with `--no-time-gates`, the flag that plugin documents for a run that is not its own suite. The
contracts still run and still decide the step. Verified against sage-extensions main (`32e116e`) in the
image: the selection runs in 5.32–11.77 s, and the one failure it reports is the owner's own —
`TypeError: int() argument must be ... not 'OwnedJoinCategory.element_class'` at
`sage_indefinite_port/indefinite/recursive.py:154`.
