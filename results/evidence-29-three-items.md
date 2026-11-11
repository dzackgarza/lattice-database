# #29: the crash, the Hoehn–Mason minutes, and the exit that followed a passing preamble step

## 1. The crash: the input is well formed, and python-flint dies on it

With faulthandler enabled after Sage's import — `python -X faulthandler` cannot be used here, because
Sage's `cysignals` installs a signal handler through `signal.signal` and the option's wrapper makes that
raise `TypeError: signal handler must be signal.SIG_IGN, signal.SIG_DFL, or a callable object`:

    quaternary: type tuple, 4 rows of [4] entries, entry types ['int'], integral True, stated det 4
      calling fmpz_mat(gram).det() …
    Fatal Python error: Segmentation fault
      File "<string>", line 17 in <module>
      …
      /lib/x86_64-linux-gnu/libflint.so.19, at fmpz_set+0x25
      /sage/.venv/lib/python3.14/site-packages/flint/types/fmpz_mat.cpython-314-x86_64-linux-gnu.so, at +0x10d18

**The input is not the cause.** `nipp.quaternary(...)[0].gram_tensor` is a `tuple` of four `tuple`s of
four `int`s — square, integral, no bool, no `Fraction`, no Sage element. The crash is inside
`fmpz_mat`'s own construction: its `fmpz_set` resolves to `libflint.so.19` (the image's FLINT 2.9, which
Sage links) while **python-flint 0.9.0** ships `python_flint.libs/libflint-6839011d.so.24.0.0` (FLINT 3).
That is the image's dual-FLINT defect, filed as dzackgarza/sage#25; the library is not patched here.

Minimal reproduction, in the image:

    $ python -c "import sage.all; from flint import fmpz_mat; print(fmpz_mat(((2,0,0,1),(0,2,0,1),(0,0,2,1),(1,1,1,2))).det())"
    Segmentation fault (core dumped)          # without `import sage.all` it prints 4

The repository had already stopped calling it: `tests/test_bulk_sources.py` takes the determinant with
Sage's `matrix(ZZ, …)`, and `python-flint` is no longer a dependency. What this turn adds is the guard
the issue asks for, so a malformed transcription can never be mistaken for an engine defect:
`_matrix_input` checks that what the tables hand the determinant is a tuple of `len` equal rows of `int`
(bool excluded), the two NIPP matrices are checked with it, and a ragged row, a float and a bool are
each shown to be named. `tests/test_bulk_sources.py`: 8 passed in 36.10 s in the image.

The guard is green on this data and red on malformed data; it is not red on main, because the data was
never the defect — the owner of the crash is python-flint 0.9.0 in an image that loads two FLINTs.

## 2. The Hoehn–Mason seventy minutes: the owner expands a tensor per Gram entry

Measured in the image on row 81 of the Höhn–Mason tables (record `02AQ`, rank 19, a subobject of the
Leech lattice):

| call | time |
| --- | --- |
| `_leech_lattice` | 0.2 s |
| `_sublattice` (rank 19, with its inclusion) | 1.2 s |
| `source = _formed(record.gram_tensor).twist(1)` | 1.4 s |
| **one `b(x, x)` on the subobject** | **156.65 s** |
| one `b(x, x)` on the ambient Leech lattice | 0.014 s |

and the step is `hashimoto.basis_isometry`'s form-preservation decision:

    hoehn_mason.automorphisms                       src/latticedb/hoehn_mason.py:195
      hoehn_mason._record_isometry                  src/latticedb/hoehn_mason.py:177
        hashimoto.basis_isometry                    src/latticedb/hashimoto.py:157
          FormModules.Mor(...).preserves_forms      sage_extensions/.../form_modules.py:941
            _form_square_commutes                   sage_extensions/.../form_modules.py:349
              b                                     sage_extensions/.../form_modules.py:2120
                _evaluate_by_bilinearity            sage_extensions/.../module_morphisms.py:3393
                  pure_tensor                       sage_extensions/.../module_morphisms.py:3571
                    linear_combination              sage_extensions/.../framed_free_modules.py:329

`preserves_forms` asks the form for `rank²` = 361 Gram entries, and the form of a **subobject** answers
each by expanding the restriction through `pure_tensor`. It is the owner's defect, filed as
dzackgarza/sage-extensions#320, with this reproduction on that issue
(`results/evidence-sage-extensions-320.md`). No consumer-side change is made: rebuilding the owner's
object to answer the same question locally is a second code path for one decision, and was rejected in
review.

## 3. `13 passed` and exit 1: the owner's own post-run gate, and what remains

`sage_extensions/testing/suite_budget.py:106`:

    def pytest_sessionfinish(session, exitstatus):
        del exitstatus
        if _gated(session.config) and session.config.stash[_SLOW_CALLS]:
            session.exitstatus = pytest.ExitCode.TESTS_FAILED

Every selected test whose **call phase exceeded 20 s** is collected there, passed or failed, and the
hook overrides the session's status after the summary — so the step printed `13 passed` and exited 1.
The repair, landed as `6d023a6a58`, runs the contracts with `--no-time-gates`, the flag that plugin
documents for a run that is not its own suite; nothing runs after pytest in that step.

Verified here, warm bridge: with the gates on, a selection whose calls are short passes and exits 0
(`1 passed in 0.60s`, PYEXIT=0); with `--no-time-gates`, the full selection exits on its tests alone.
What remains is one of the owner's own contract tests failing inside the owner's code:

    tests/lattices/test_lattice_database_owner_contracts.sage::test_primitive_orbit_series_counts_primitive_isotropic_lines
    ValueError: primitive bounded orbit series requires a definite lattice, not Integral lattice of
    rank 5 and signature (2, 3)     sage_extensions/categories/lattice_orbit_invariants.py:136

13 of 13 apart from that one, and that one is a test asking for a series its own library refuses
(sage-extensions#286). Nothing in `.github/workflows/tests.yml` turns that into a failure; the owner's
test does.
