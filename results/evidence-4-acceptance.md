# #4: the acceptance, item by item

Issue #4 is closed and was accepted on 2026-11-09. This file records a re-check of its two acceptance
items against the tree as it stands, not a new claim of ownership over the unit.

Checked at `2d10112a85` (local `main`) and `88651884d3` (the tip of the connected repository's `main`):
`git diff 88651884d3 2d10112a85 -- src/latticedb/sage_genus.py tests/test_genus.py` is empty, so every
line quoted below is the same on both. Runtime: the pinned research image
(`ghcr.io/dzackgarza/sage:develop` rootfs, `/sage/.venv/bin/python` 3.14.10), with sage-extensions
`main` at `8b43451` bound at `/repos/sage-extensions` — the image's baked checkout is stale and still
fails at import (`ImportError: cannot import name 'QQ'`), which is the environment and not the code.

## 1. "serialize the value, not its text"

`_rational` builds the number from the value's own numerator and denominator, and nothing reads the
printed form:

- `src/latticedb/sage_genus.py:224` `_rational`, `:226`
  `number = Fraction(int(value.numerator()), int(value.denominator()))`.
- `src/latticedb/sage_genus.py:230` `_coefficients` and `:235` `_local_densities` are its two callers;
  the `local_density` call is `:238`.
- No `Fraction(str(...))` of an owner value remains in `src/` (`rg 'Fraction\(str' src/` → no match).

Decided on the smallest input that reaches it: $I_3=\langle1,1,1\rangle$ (the lattice of card `0022`),
asking the owner for one local density.

    m=1 type=sage_extensions.owned_category.OwnedJoinCategory.element_class str='(3)/(2)' num=3 den=2 rational='3/2'
       Fraction(str(value)) -> ValueError: Invalid literal for Fraction: '(3)/(2)'
    ...
    --- the real _local_densities path
    [{'prime': 2, 'densities': ['3/2', '3/2', 1, '3/4']}]

The other element class the argument type names — an owned ring element, here the $\theta$-series
coefficients — behaves the same way (`_coefficients -> [1, 6, 12, 8]`), so the numerator/denominator
route is not specific to the localization ring.

Probe: `results/probe-4-rational.py`; full output `results/evidence-4-rational.log`.

## 2. "a regression test feeds the real `_local_densities` path an owner element whose `str` is `(3)/(2)`"

- `tests/test_genus.py:537`
  `test_certification_stores_the_exact_two_adic_densities_of_the_sum_of_three_squares` runs
  `genus.certify` on `0022` (the card `I_3`), so the value passes through the worker, the real
  `_local_densities`, and the stored card; it asserts the stored densities at `:556` and the
  certificate's presence at `:557`.
- `tests/test_genus.py:525`
  `test_a_rational_is_serialized_from_its_numerator_and_denominator_never_its_text` pins the property
  directly, on the stand-in at `:509` whose `str` is `(3)/(2)`, and asserts `Fraction` rejects that
  text at `:529`.

The end-to-end test is what decides the item, and it decides it only if the old parser makes it red.
With `src/latticedb/sage_genus.py:226` set back to `number = Fraction(str(value))` and every other line
unchanged, in the same image:

    File "/repo/src/latticedb/sage_genus.py", line 238, in _local_densities
    File "/repo/src/latticedb/sage_genus.py", line 226, in _rational
      number = Fraction(str(value))
    ValueError: Invalid literal for Fraction: '(3)/(2)'
    FAILED tests/test_genus.py::test_a_rational_is_serialized_from_its_numerator_and_denominator_never_its_text
    FAILED tests/test_genus.py::test_certification_stores_the_exact_two_adic_densities_of_the_sum_of_three_squares
    2 failed, 46 deselected in 3.88s

Red log: `results/evidence-4-red.log`. With the committed line restored: `2 passed, 46 deselected in
4.49s` (`results/evidence-4-green.log`). The red run's failure is the reported one — run 42207160099's
`ValueError` at the localization element — and not a test-only artefact, because the value that raises
is the owner's.

## 3. "a dispatched `certify` run completes and writes at least one new certificate"

This connection can read the repository but cannot dispatch or read workflow runs through it; the
record below is read from GitHub's public Actions API and from the commits the run pushed.

- `certify` run `42370898252` (run number 53), `event: workflow_dispatch`,
  `created_at 2026-11-07T12:05:03Z`, `status: completed`, `conclusion: success`,
  `updated_at 2026-11-07T16:33:24Z`, head `9fa82dcb80`. That is after the fix (`1530ef6124`,
  2026-11-06T18:48Z) and after the end-to-end test (`b942f3815c`).
- Its last commit is `0b95411e26` (2026-11-07T16:32:49Z, `github-actions[bot]`), which adds
  `026E integral.local_densities` at `certificates/f1.yaml:28` and writes the value on the card at
  `lattices/026E.md:83`, with the card's hash at `lattices/026E.md:21`. The field that the string
  parser killed is the field that run certified.

The same holds at scale on the current tree: 122,184 `integral.local_densities` certificates exist
across 256 certificate group files (`rg -c '^[0-9A-Z]+ integral\.local_densities:' certificates/`).

## Not in this unit

- `genus.applies` (#8) is the other database-side piece the issue names; it is a separate unit.
- The `KeyError: ((1,), ())` from a different certification in run 42207160099 is named in the issue
  body but is not part of its acceptance. It was not reproduced here, and the owner-side failure the
  body says was filed on sage-extensions was not re-checked.
- No dispatch was made: the acceptance item is about a run that completed and wrote a certificate, and
  the record above establishes one.
