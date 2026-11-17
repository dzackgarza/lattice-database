# #7: the T_Co primitive isotropic line constants, measured

**Outcome: seven of the eight constants returned; `SOtilde+` did not, so no card value and no certificate
were written.** The field is one computation and the driver writes it only when the whole call returns.
Everything below is measured in the certify image on the card's stored Gram tensor.

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

## Why the card is unchanged

`integral.primitive_orbits` is one preamble computation, and `genus.store` writes a field only from a
completed computation; the call did not complete. Two alternatives were rejected:

- writing the seven values with a `null` for `SOtilde+` would store a certified, partial field: the
  certificate would commit to a value no run produced, `requests()` would then see a matching stored value and
  a held certificate and never ask again, and the issue states the rule this breaks — *a pending computation
  has no certificate*.
- the finite discriminant route does not replace it: `integral.discriminant_orbits` does not apply to this
  card (`integral.hyperbolic_index` is 0, and that field's Eichler hypothesis needs at least 2).

So `lattices/6JRR.md` keeps its fourteen certified fields, `integral.primitive_orbits` stays absent, and
`failures/e1.yaml` keeps `6JRR integral.primitive_orbits` open, which is also why a dispatch of
`certify --tag 6JRR` does not currently request the field at all.

## What the next dispatch knows

- Seven rows: about 4 minutes and 1.03 GiB in one worker, on four cores.
- Eighth row: unbounded on the current owner revision; expect the driver's 1.6 GiB memory floor.
- The eight rows are one computation, so nothing lands until the eighth returns.
