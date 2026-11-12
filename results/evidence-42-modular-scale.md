# #42: the record is right, the test's run was too big for its budget

Reproduced in the image at main `64fd0e4d57` with the current sage-extensions tree at
`/repos/sage-extensions`. The record CI saw is the one this run leaves: hash `b503be4ac852fc44…`,
`seconds=0`, `lost=False`.

## The order of the fields, and the budget at each

The test's own fixture (a copy of `0012` and no certificates), `genus.certify(root, loaded, {},
("0012",), time.time() + 60)`:

    queue: request 0  fields (24): derive, genus_class_count, integer_valued, elementary_primes,
                       genus_symbol, overlattice_count, spinor_genus_count, spinor_genera,
                       hyperbolic_index, automorphism_group_order,
                       automorphism_group_generator_morphisms, discriminant_sequence,
                       discriminant_form, primitive_orbits, cusp_chambers, discriminant_orbits,
                       modular_scale, genus_theta_series, theta_series_cuspidal_component,
                       cusp_form_coordinates, siegel_eisenstein_coefficients, anisotropic_primes,
                       local_representations, local_densities
           request 1  searches: reflective, regular, spinor_regular, roots, norms

    [ 31.46s | left  28.54s] 0012 derive
    [ 36.75s | left  23.25s] 0012 {'integer_valued': True}
    [ 41.87s | left  18.13s] 0012 {'genus_class_count': 1}
    [ 47.85s | left  12.15s] 0012 {'elementary_primes': [3]}
    [ 53.51s | left   6.49s] 0012 {'genus_symbol': 'II_{2,0} (2: 1^-2; 3: 1^-1 3^-1)'}
    [ 59.66s | left   0.34s] 0012 {'overlattice_count': 1}
    [ 65.46s | left  -5.46s] 0012 {'hyperbolic_index': 0}
    [ 71.42s | left -11.42s] 0012 {'automorphism_group_order': 12, …}
    [ 77.05s | left -17.05s] 0012 {'discriminant_sequence': …}
    [ 83.40s | left -23.40s] 0012 {'discriminant_form': …}
    [ 89.00s | left -29.00s] 0012 {'primitive_orbits': …}
    [ 89.00s | left -29.00s] Certification time budget exhausted

    log after the run: {'0012 integral.modular_scale': Interruption(hash='b503be4ac852fc44…',
                                                                    seconds=0, lost=False)}

So the run reaches `integral.modular_scale`, announces it started, and the budget ends the run inside
it: the final checkpoint writes the entry with the seconds it had run, which is 0 because the
announcement and the end fall in the same second. **The record is correct** — the computation started
and did not finish, which is what `exceeded.py` documents ("a computation that ran for less was
interrupted or started late, and the next job computes it first").

The cause is the size of the run the test starts: 24 fields at about 5.5 s each (≈130 s) plus a
searches request, in a 60 s budget. Measured with a budget that fits the card — the same fixture and
`time.time() + 600` — the run finishes every field and `regular`, and the log ends **empty**
(131.77 s, `{}`).

## The repair (the test's owner)

The fixture is now the state an interrupted run leaves, and the run is sized to it:

- `hold_certificates(root, tag, withhold=…)` copies the card's certificates except the computations
  named in `withhold`; the test withholds `0012 integral.genus_class_count`, the computation its
  `exceeded.yaml` record names;
- the test passes that held dict to `genus.certify`, as the API takes it, instead of `{}`;
- the budget is 300 s, which covers a worker's start plus one computation; the run finishes as soon
  as the work is done, so the budget costs nothing when it passes.
- both assertions are unchanged, and one is added: the queue asks for exactly `["genus_class_count"]`,
  so a fixture that would recompute more says so before the log assertion does.

Measured with that fixture: queue `[['genus_class_count'], False]`; the value stored at 9.39 s; the log
`{}`; `0012 integral.genus_class_count` certified; 10.05 s in total.

## Checked

- `tests/test_certify_process.py::test_finishing_a_previously_interrupted_computation_clears_its_log`
  in the image: **1 passed in 12.24s**.
- the whole file in the image: `1 failed, 6 passed in 222.78s`. The failure is
  `test_a_search_that_never_ends_does_not_hold_back_other_cards`, which this change does not touch
  (it uses `prepare_card` and `genus.certify` directly, and the helper's new keyword defaults to
  none). It stops inside the preamble: with the current tree,
  `orthogonal_quotients.py:2118 _line_orbit_from_divided_classes` →
  `ValueError: no primitive isotropic vector of … has divisor 1 and divided class -[1]`; with the
  image's baked copy, `definite_lattices.py:294 _square_shell` → `AttributeError: 'int' object has no
  attribute 'parent'`. It passed in run 43062460918, so it is a venue difference between this VM's
  preamble and CI's, and it is not #42's test.
- `just test`: 74 passed.
