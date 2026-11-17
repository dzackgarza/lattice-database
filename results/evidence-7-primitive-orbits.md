# #7: the T_Co primitive isotropic line constants, measured

**Outcome: the seven rows that returned are stored and certified — `O`, `SO`, `O+`, `SO+` at 1 and
`Otilde`, `SOtilde`, `Otilde+` at 527 — and `SOtilde+` is quarantined in `failures/e1.yaml` with its
measured cost and its owner issue (sage-extensions#596).** Everything below is measured in the certify
image on the card's stored Gram tensor.

## The environment the measurement ran in

- Image: `dzackgarza/sage:develop`, revision `6301b4e4`, digest `sha256:332aebe9…`, Sage 11.0.beta5,
  Python 3.14.10 (`/sage/.venv/bin/python`), as the certify workflow's `docker run` gives it.
- `sage_extensions` imported from a source checkout at `34c9be89` (`origin/main`, the revision carrying
  #585, #586, #588, #592, #593) on `PYTHONPATH`. This is the repair the run-44077055181 blocker asks for:
  the image's own editable install at `/repos/sage-extensions` is 947 commits behind `origin/main`, and
  its `timing.current_commit()` needed a source tree with a `pyproject.toml`.
- `dzack_research` from the image's `/repos/research/src`, as `preamble`.
- The lattice is `Lattices(ZZ)(gram)` on `lattices/6JRR.md`'s stored `gram_tensor`, unmodified:
  rank 11, determinant −2048, signature (2, 9), even, Witt index 2. `timing.current_commit()` answers
  `34c9be895206eb7756de3411eb4d8b0d1c53b059`, so the record names the source it ran from.

## What the public call does, and what was run instead of it

`_primitive_isotropic_line_series` (owner, `categories/lattice_orbit_invariants.py`) builds the eight
subgroups from `L.Aut()`, `L.stable_orthogonal_group()`, `L.O_plus()` and `L.SO()` by intersection, and
stores, for each, `subgroup.isotropic_orbit_representatives(1).cardinality()` as the row's `constant`.
`L.primitive_orbit_series()` on an indefinite lattice is that function and nothing else.

That dict comprehension is one call: it returns when the eighth subgroup returns. `probe-lines.py` runs the
same eight bodies, one stage at a time, so a subgroup that does not return costs its own stage and not the
other seven.

## The constants

| subgroup | constant | seconds | peak MiB |
| --- | --- | --- | --- |
| `O` | 1 | 82.98 | 586 |
| `SO` | 1 | 0.02 | 586 |
| `O+` | 1 | 0.04 | 586 |
| `SO+` | 1 | 33.17 | 620 |
| `Otilde` | 527 | 30.94 | 845 |
| `SOtilde` | 527 | 39.17 | 922 |
| `Otilde+` | 527 | 52.42 | 1033 |
| `SOtilde+` | **not returned** | ≥ 510 (killed) | ≥ 9200 |

The seven that returned cost 238.7 s of wall clock and 1033 MiB peak in one process; the first row pays for
the ambient `O(L)` row (83 s) that the rest reuse. `O`, `SO`, `O+`, `SO+` are all 1 and the four stable
groups all 527, which is the split the issue's source assessment states; the numbers here are the
`isotropic_orbit_representatives(1).cardinality()` results, not the assessment.

The ambient row itself was measured separately (`probe-branch.py`): `L.Aut().isotropic_orbit_representatives(1)`
is **1** line, in 54.5 s at 560 MiB. That is why `O` is 1: `O(L)` is transitive on primitive isotropic
lines, and every further constant is that one orbit split by a subgroup.

## The eighth row

`SOtilde+ = Õ ∩ SO ∩ O⁺` does not return. Two independent runs:

- built as `(stable ∩ SO) ∩ O+` (the owner's own order) it reached 9.2 GiB RSS after 8.5 min, still growing
  at roughly 1 GiB a minute, on a 16 GiB machine; the run was killed there to keep the shared VM usable.
- built as `(stable ∩ O+) ∩ SO` it shows the same profile (2.3 GiB at 4 min 27 s, still growing).

The driver's own memory cap is `MEMORY_RESERVE = 0.1 × MemTotal`, i.e. the worker is `SIGKILL`ed when
`MemAvailable` falls below 1.6 GiB — about 14.4 GiB resident on a 16 GiB runner. The measured growth would
reach that floor rather than finish; the kill above was 3 GiB free, which is *stricter* than the driver, so
the row is open on the driver's cap too, and the run was not driven to the floor because driving it there
would have taken the VM's remaining memory from whatever else runs on it.

**Where it goes.** On this subgroup `isotropic_line_stabilizer_image` returns `None` for the single ambient
line (2.51 s), so the walk leaves the `splitting_isometries_from_line_class` route that `Otilde+` takes and
falls through to `exact_isotropic_stabilizer_generators` and `splitting_isometries`, which build and retain a
constructed transport per split line — 527 of them. `Otilde`, `SOtilde` and `Otilde+` each reach 527 in 31–52 s
at ≤ 1.03 GiB; only the doubly-restricted group takes the expensive branch. This is an owner-side cost, in
`sage_extensions`, not a database one: the database passes the subgroup it is given and nothing else.

## Line count, not vector count

The card needs `Γ`-orbits of primitive isotropic **lines**, and that is what returned. `isotropic_orbit_representatives(1)`
yields rank-one primitive isotropic **subobjects** — `lattice.primitive_isotropic_subobject(v)`, the
sublattice `ℤv`, which is what `_primitive_isotropic_line_series` itself names "primitive isotropic line
orbits" — so the number is a line count and not a vector count.

Here the two counts agree, and the card's own stored values say why: `A_L = (ℤ/2)^{11}`, so every class is
its own negative and every vector orbit is its own negative; `integral.discriminant_form.isotropic_classes`
is 528, and the zero class is not realised by a primitive vector because every entry of the stored Gram
tensor is even (so every divisibility is at least 2). 528 − 1 = 527 is the stable groups' constant, which
the walk reproduced without using that count.

## What was written, and how

The field is now askable per row. A request names a row — `primitive_orbits[Otilde]` in the request,
the `certifications` and `failures` keys, and the `exceeded` log — and the row is stored as that row of
`integral.primitive_orbits`, beside the rows stored before it. The field's certificate commits to the
rows the card states, through the same `orbit_projection` as before, and is minted again as each row
lands. A worker the run kills costs its own row, which is what `#46` already did for a field and what
`failures/e1.yaml` already recorded; nothing new was needed for the cost.

The rows are `_standard_subgroup`'s eight subgroups — the database's own vocabulary, stated with its
GHS citation — asked for `isotropic_orbit_representatives(1).cardinality()` through the owner. The
owner's `primitive_orbit_series` still computes the whole field on a definite card, where it is a
bounded search; the indefinite rows are asked one at a time.

Asked for at `certify --tag 6JRR --field primitive_orbits --phase fields --workers 1`, in the certify
image, on the stored Gram tensor, the seven unquarantined rows landed:

| row | constant | certificate |
| --- | --- | --- |
| `O`, `SO`, `O+`, `SO+` | 1 | one field certificate, `ed8a588feba9ac8f13ca410b7fdadc32da57e89b1ca3cc9daf4f53b47d5d1497`, over the seven rows |
| `Otilde`, `SOtilde`, `Otilde+` | 527 | as above |
| `SOtilde+` | absent | quarantined in `failures/e1.yaml`, `6JRR integral.primitive_orbits[SOtilde+]` |

The field's certificate is one hash over the row set, not one per row: the schema has one
`certifications` key per field, and `certified_value` commits to the rows stored.

## The row that did not return

`6JRR integral.primitive_orbits[SOtilde+]` is `open` in `failures/e1.yaml`, with the measured cost
(510 s, ≥ 9.2 GiB, killed) and the owner issue that carries the defect, **sage-extensions#596**:
`isotropic_line_stabilizer_image` answers `None` for the ambient `O(L)` row, which sends that subgroup
down the exact-stabilizer route. The entry was recorded from the measurement above rather than from a
driver run; the row was not driven to the driver's 1.6 GiB floor.

Because the row is quarantined, `requests()` does not ask it: a dispatch of `certify --tag 6JRR` costs
the seven rows (about four minutes) and stops there. When #596 is repaired, `just retry-computation 6JRR
'integral.primitive_orbits[SOtilde+]' --note ...` releases it, the field is missing an unblocked row, and
the next run asks that row alone.

## The request plan after the release

`just retry-computation 6JRR integral.primitive_orbits` was run with the measurement as its note, so the
field is asked again; the plan for `--phase fields` was

```
fields: ['primitive_orbits[O]', 'primitive_orbits[O+]', 'primitive_orbits[SO]', 'primitive_orbits[SO+]',
         'primitive_orbits[Otilde]', 'primitive_orbits[Otilde+]', 'primitive_orbits[SOtilde]',
         'arithmetic-group.otilde-plus-t-co.generator_morphisms']
fields: ['arithmetic-group.otilde-plus-t-co.index_in_orthogonal_group']
```

and with `--field primitive_orbits` the seven rows alone. The arithmetic-group fields of
`otilde-plus-t-co` are the ones that cost the run 44077055181 its budget; they are not part of this
item, and `--field` is what lets a dispatch ask this field without them.

Two rows' names carried a stale `exceeded` interruption from runs I stopped mid-flight; both were
released through `just retry-computation`, which is the triage the ledger exists for, and neither was a
mathematical failure.
