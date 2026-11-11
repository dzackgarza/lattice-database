# #37 rows 1-6 and 8 at main 64fd0e4d57: all seven pass in the image with a current sage-extensions

Measured on this VM, since GitHub Actions has started no job since 2026-11-12 00:51. One pytest call,
the seven node ids of #37's table that this repository owns, inside the image in the configuration of
`results/evidence-41-recovery-launcher.md`:

    run.sh -w /repo -b <chat checkout>:/repo -b <research checkout>:/repo/research -b $HOME:$HOME \
      /bin/sh -c 'HOME=/root; cd /repo; PYTHONPATH=/repo/research/src:/repo/src \
                  /sage/.venv/bin/python -m pytest <the seven ids> -v -p no:cacheprovider'

| # | node id | result |
| --- | --- | --- |
| 1 | `test_catalogue_schemas.py::test_an_arithmetic_group_generator_is_one_scale_one_self_isometry_of_its_lattice` | PASSED |
| 2 | `test_catalogue_schemas.py::test_the_coble_card_and_its_group_cards_state_only_their_defining_data` | PASSED |
| 3 | `test_certify_process.py::test_an_early_termination_does_not_blacklist_a_computation_for_a_whole_job` | PASSED |
| 4 | `test_geometric.py::test_k3_hodge_diamond_and_lattice_link_are_published` | PASSED |
| 5 | `test_geometric.py::test_symmetric_spaces_and_analytic_variety_are_published` | PASSED |
| 6 | `test_legacy_morphisms.py::test_imported_implicit_scales_become_explicit_without_changing_scaled_maps` | PASSED |
| 8 | `test_verification.py::test_a_shard_reports_the_problems_of_its_own_cards_only` | PASSED |

`7 passed in 65.85s`.

## The one stop, and why it is not a repair defect here

Run with the image's own baked sage-extensions (`/repos/sage-extensions` at `7b222e86214`), row 5 stops
after `site.build` renders the graph pages:

    src/latticedb/graphs.py:251 in properties
        hyperbolic = self._presents_mirrors() and invariants.is_acute_angled_hyperbolic_polytope_gram()
    /repos/sage-extensions/src/sage_extensions/categories/vinberg_invariants.py:343
        if any(gram[i, i] <= 0 for i in positions):
    TypeError: '<=' not supported between instances of 'OwnedJoinCategory.element_class'
               and 'OwnedJoinCategory.element_class'

The test needs that page: it asserts `"hyperbolic Coxeter polytope" in` the rendered
`graphs/hyperbolic-triangle-2-3-infinity.html`, and `graphs/hyperbolic-triangle-2-3-infinity.md` is the
one card stating mirror `norm_squared` and bond `gram` weights. The cause is in the preamble, not in
the call: `graphs.py` hands `FormModules(ZZ)(...)`'s own `gram_tensor()` to
`VinbergInvariantMatrices().from_root_gram`, and the tensor's entries are elements of the owned
rational field. Measured on that ring:

    1 == 0 -> False      1 == 1 -> True
    1 > 0  -> TypeError   1 <= 0 -> TypeError   QQ(-1)/2 < 0 -> TypeError

so `OwnedOrderedRings` does not make its own elements ordered. That is sage-extensions#307, whose red
test `tests/lattices/test_the_rational_hyperbolic_triangle_gram.sage` names this same TypeError and
`lattice-database#18`; its repair moves the comparisons into `OwnedOrderedRings.ElementMethods`
(`categories/rings/ring_foundation.py`) and is present at sage-extensions `523e797ab89` and at
`origin/main cb80e58`, so it is not a lattice-database repair defect. Binding that tree where the
image keeps its copy gives the seven passes in the table above, and the same probe answers
`1 > 0 -> True`.

The copy the image bakes in predates the repair; a VM run that does not bind a current sage-extensions
at `/repos/sage-extensions` reproduces the stop. CI does not use the baked copy: the Sage action
installs `research` and then `--requirements research/pyproject.toml`, which requires
`sage-extensions @ git+https://github.com/dzackgarza/sage-extensions` (main), and
`.github/actions/sage/provided.txt` excludes only `dzack-research`.

## Also recorded

- rows 1 and 2 were green at `6bd4baa097` (#34) and remain green at `64fd0e4d57`;
- `just test`: 74 passed;
- not run here: row 7, sage-extensions#347, and row 9, `validation/test_build.py`, which needs more
  memory than this VM has — run 43062460918 decides it.
