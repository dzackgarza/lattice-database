Closing #7: both acceptance clauses are met, and the generation half is met as **recorded not
supplied**. Values and hashes below are the ones on main after this change.

**1. `integral.primitive_orbits` on `lattices/6JRR.md`: all eight standard subgroups, one certificate.**

| row | constant |
| --- | --- |
| `O`, `SO`, `O+`, `SO+` | 1 |
| `Otilde`, `SOtilde`, `Otilde+`, `SOtilde+` | 527 |

certificate `4282656a7d42a5489e900ad120e0f39897cca2d71dabca91e1874feee4fca7b9` (`6JRR integral.primitive_orbits`,
`certificates/e1.yaml`), superseding `ed8a588feba9ac8f13ca410b7fdadc32da57e89b1ca3cc9daf4f53b47d5d1497`,
which covered seven rows. The eighth row is the one that was quarantined: sage-extensions#596 repaired
the line stabilizer's sign space (`dbf91e893d80`), the row was released with
`just retry-computation 6JRR 'integral.primitive_orbits[SOtilde+]'`, and
`latticedb certify --tag 6JRR --field primitive_orbits --phase fields --workers 1` in the pinned image
with sage-extensions `2fb37d5` returned 527 for the stored Gram tensor in 179 s, exit 0. The other
seven rows were not recomputed and their values did not change; `failures/e1.yaml` now records that
quarantine as `resolved`.

**2. The two arithmetic-group cards: index certified, generators recorded as not supplied.**

- `arithmetic-groups/otilde-t-co.md`, `[O(T_Co) : Õ(T_Co)] = 46998591897600 = |O(A_{T_Co}, q)|`,
  certificate `682c595c52447cd1add71138601fe9259fd3e5e868e05a646a95e0b27c3225f1`.
- `arithmetic-groups/otilde-plus-t-co.md`, `[O(T_Co) : Õ⁺(T_Co)] = 93997183795200 = 2|O(A_{T_Co}, q)|`,
  certificate `326145ccf46247778eb506416cb6c6985eedf61029060ff4497597e2c3f8a3b0`, with
  `parent_group: otilde-t-co`.

Both indices are read from the finite orthogonal group of the discriminant form, not from the coset
space. `data.generator_morphisms` is absent on both cards, and no certificate on 6JRR claims one:
`sage-extensions#597` settles the generation half by proof rather than by a measurement — Õ(T_Co) is
the principal congruence subgroup of level 2, rank_2(T_Co) = 0 where Kneser's theorem needs rank_2 ≥ 6,
Gritsenko–Hulek–Sankaran's Proposition 3.4 needs two hyperbolic planes, and Allcock's Bertini-involution
family is stated for Λ(2) of rank 10 — and the only route left, the Schreier family over
46998591897600 cosets, did not return in 600 s (4607 MiB and rising, exit 124 of its own timeout).
The reason and the issue are now stated in the prose of both group cards and in the paragraph of
`lattices/6JRR.md` that lists them; the two computations are quarantined in `failures/e1.yaml` so that
scheduled runs stop paying for them, and either can be released with `just retry-computation`.

**What this comment does not claim.** `latticedb verify` over the affected cards is a corpus- or
shard-scoped run (`checks.one_shard` loads the whole corpus), so it is the certify/verify workflow's
line and not something this change ran. What was run on the three cards is their own component checks:
`checks.records.problems(..., {"6JRR"})` and `checks.relations.problems(..., {"6JRR"})` both return 0,
and the scoped catalogue pass reports only that the two group cards' `ambient_lie_group: o-2-9` is
absent from the tag-scoped read, which reads no `lie-groups/` cards.

Evidence: `results/evidence-7-eighth-row.md`, `results/evidence-7-primitive-orbits.md`,
`results/evidence-7-arithmetic-group-index.md`. Tests: `tests/test_genus.py`, `tests/test_failures.py`,
`tests/test_persist.py`, `tests/test_catalogue_schemas.py` — 74 passed, 1 pre-existing failure
(`test_persist.py::test_shards_push_progress_repeatedly_without_touching_their_worktrees`, failing
identically at the parent commit `0f28d1ef3b`).
