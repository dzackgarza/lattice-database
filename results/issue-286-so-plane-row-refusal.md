# sage-extensions#286: the plane row of a determinant-kernel subgroup is refused on `T_Co`

**Not posted.** This connection cannot comment on `dzackgarza/sage-extensions`. The text below is the
report; it is one finding and one repair, both exact.

## What was called, and on what

`sage-extensions` at `0bbf022b6bf72e5a1d1f3267f3b7481fc19ba49f`, the adopted image
(`/sage/.venv/bin/python`, Sage 11.0.beta5, Python 3.14.10), on `T_Co = ⟨2⟩ ⊕ U(2) ⊕ E₈(−2)`'s
stored Gram tensor from `lattice-database` `lattices/6JRR.md`:

```python
L = Lattices(ZZ)(gram)          # rank 11, det −2048, signature (2, 9)
L.SO().cusps(2).cardinality()                      # raises
(L.O_plus().intersection(L.SO())).cusps(2).cardinality()   # raises
```

Both raise, in `sage_extensions/categories/orthogonal_quotients.py:4237`,
`_plane_orbit_from_parabolic_stabilizer`:

```
ValueError: the plane row of Integral lattice of rank 2 and signature (0, 0) under
{g in Orthogonal group O(Integral lattice of rank 11 and signature (2, 9)) : det(g)=1}
cannot be computed by the coset walk of the discriminant image: the subgroup cuts no
discriminant condition, or both a determinant and a spinor kernel at once, and the
walk's kernel-sign witness machinery lifts one sign coset only
```

The reach is `cusps(2)` → `_yield_subgroup_isotropic_orbit_representatives`
(`:4636`) → `_plane_orbit_from_parabolic_stabilizer` (`:4237`).

## Why this is an asymmetry and not a limit of the lattice

`_yield_subgroup_isotropic_orbit_representatives` tries `_plane_orbit_from_odd_stabilizer` before the
parabolic route, and that route's own guard (`:4157`) admits exactly one subgroup:

```python
if not (quotient.spinor_kernel and not quotient.determinant_kernel and not quotient._has_discriminant):
    return None
```

So on this lattice the four sign-only subgroups split unevenly, and the character data is the same
for all of them (`_has_discriminant` false, index 2 / 2 / 4):

| subgroup | `det` kernel | `sn` kernel | index | plane row |
| --- | --- | --- | ---: | --- |
| `O` | no | no | 1 | 1 (index-one branch) |
| `O+` | no | **yes** | 2 | 1, by the odd-stabilizer route |
| `SO` | **yes** | no | 2 | **refused** at `:4237` |
| `SO+` | **yes** | **yes** | 4 | **refused** at `:4237` |

Measured: the four rows of `finite_character_quotient()` are
`has_discriminant: false` for all three proper subgroups, `determinant_kernel` / `spinor_kernel` as
in the table.

The mathematics is not in question and is not offered as a repair: for a sign kernel the orbits are
the ambient ones, because the character-adjustment argument puts both sign characters in the
stabilizer of every primitive isotropic plane (research
`cor:coble-eight-standard-line-counts`), so the expected counts are 1, 1, 1, 1. What is missing is
the route: a determinant kernel of index two is the mirror image of `O⁺` and has the same
one-witness answer available — `plane_odd_character_witness` asked for the **determinant** character
instead of the spinor one — while today it lands on a route that refuses it.

## The repair this suggests, stated as one thing

Admit `SO` to `_plane_orbit_from_odd_stabilizer` by asking its guard for the character the subgroup
cuts — `determinant_kernel and not spinor_kernel and not _has_discriminant` — and take the odd
witness from the determinant image rather than the spinor image. `SO+`, which cuts both, stays
refused until the joint two-flip machinery exists; that is the honest scope, since the single-flip
witness covers one coset and the file already says so.

## What the consumer does meanwhile

`lattice-database` leaves the two rows empty, records both refusals in `failures/e1.yaml`
(disposition `open`, the owner's traceback as `stderr`), and asks for them no more; the public
operation's refusal is quoted in the prose of `lattices/6JRR.md`. Nothing is transcribed from the
theorem, and no local algorithm substitutes for the call.
