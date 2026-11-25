# #43: the orbits of a cusp's root classes

The issue asks card 029J to carry, per Sterk cusp under `gamma-en-2`, "the orbits of the cusp's root classes in
$K_J = \eta_J^\perp/\mathbb{Z}\eta_J$ under the cusp stabilizer: the orbit count, one representative per orbit, and the
order of the transporter group", the same row on the T_Co card at cusps 3--5, each value "cited from a source that
proves it, or certified by computation. A count first seen in an agent report is not a value."

Two probes decide what can be stated. Neither of them is a computation of the counts.

## 1. The root family at each of the five cusps, from the card's Gram tensor

A wall $w$ of a chamber at the cusp $v$ lies in $v^\perp$, so its class in $K_J$ has $q([w]) = b(w, w)$, and two walls
give one class exactly when their difference is a rational multiple of $v$. So the roots of $K_J$ among the walls are
the walls of square $-2$, and this is decided by the card alone, in 0.1 s:
`tests/test_model.py::test_the_root_classes_of_the_enriques_cusps_are_the_walls_of_square_minus_two`.

| statement | page | walls | squares of the walls | roots of $K_J$ |
| --- | --- | --- | --- | --- |
| (4.3.5) | 19 | 12 | $-4$ | 0 |
| (4.3.6) | 21 | 10 | $-4, -2$ | 1 |
| (4.3.7) | 22 | 12 | $-4, -2$ | 2 |
| (4.3.8) | 23 | 11 | $-4, -2$ | 2 |
| (4.3.9) | 24 | 14 | $-4, -2$ | 4 |

The first cusp has no root class, so it has no row. The other four have 1, 2, 2 and 4 classes; a family of one class
has one orbit whatever the group does, and the other three need an inequivalence proof for every pair.

## 2. The owner's orbit call at the fourth cusp

`results/probe-43-cusp-root-class-orbits.py`, run in the pinned image with the current `sage-extensions` bound over
`/repos/sage-extensions`, at the card's own cusp vector for (4.3.8) (`results/evidence-43-owner-root-orbits.log`):

```
[    5.7s] Gamma_En,2 built
[    5.9s] reduction image at the card's cusp built
generators_are_certified_complete: False
generation_obstruction: the parabolic at the line 2*e_2 + e_3 - 4*e_4 - 5*e_5 - 7*e_6 - 10*e_7 - 8*e_8 - 6*e_9
  - 4*e_10 - 2*e_11 has no constructed generator family: parabolic_stabilizer_generators is stated for a primitive
  isotropic plane and refuses rank one, and the port's line stabilizer generators are not a computational route at
  Sterk's first Enriques cusp; the reflection subgroup of G_v is available through reflection_generators, whose
  chamber is the reflection part of G_v
[    5.9s] 11 classes of the walls, 2 of them roots of K_J
[   17.1s] 28 stabilizer generators
[  133.7s] 2 components, of sizes [1, 1]
RESULT {'statement': '4.3.8', 'wall_classes': 11, 'roots': 2, 'components': 2, 'sizes': [1, 1],
        'certified_complete': False}
```

The eleven wall classes and the two roots agree with probe 1. The orbit call returns two components of one class each,
and its own docstring (`sage_extensions/categories/isotropic_orbits.py`, `root_class_orbits`) says what that is: the
acting family is the certified reduction of the stabilizer's generators together with the reflections of the given
classes, it is not certified to generate $G_v$ at a primitive isotropic line, "so a component is an **identification**
... while a component of one class is *not* a proof of inequivalence."

The two components are therefore not a count of two orbits: they are two classes that this family does not identify.
`2` is the number the sage-extensions report measured, and the report states it as a measurement and not as a value.
Storing it, or the row's `orbit_count` derived from it, would be the count first seen in an agent report that the issue
forbids, and it would be minting a value the owner's own document says is undecided.

## What that leaves

- **No source** prints these orbit counts: Sterk prints the chambers, their diagrams and the cusp vectors, not the
  orbits of the root classes of $K_J$ under $\Gamma_v$.
- **No computation** certifies them while the stabilizer's generators are not certified at a line
  (sage-extensions#312): `generation_obstruction` names what is missing, and `latticedb certify` cannot ask the owner
  for a field the owner cannot decide.

So the field and its checks land, and the cards state no row. `integration` — the 029J rows and the T_Co rows — waits
on a certified generating family of $\Gamma_v$ at a primitive isotropic line, which is sage-extensions#312's work and
not this repository's.

One route that needs no complete family is worth recording, because it would decide the 0- and 1-class cusps today:
the number of $\Gamma_v$-orbits is at least the number of $O(K_J)$-orbits on the family and at most the number of
components the certified family gives, so a genus-level invariant that separates two root classes (the genus of
$r^\perp$ in $K_J$) closes the gap whenever the two numbers meet. That is a new computation in the preamble, not a
card edit, and it is not what this change does.

## The fields page renders the new row

`tests/validation/test_build.py` builds the whole site from the whole corpus (~10 min and several GiB), and in this
VM it was killed before its summary line. The one code path this change feeds there is the fields page's model list,
`site.fields()` -> `templates/fields.html.j2`, and that renders on its own, in 5.8 s, with the environment `site.build`
sets up (in the pinned image):

```
cusp_root_orbits True
orbits True
orbit_count True
representative False
classes False
transporter_order False
```

The three `True` are the fields of the row this change adds; the three `False` are the fields of the nested
`RootClassOrbit`, which the page does not list — as it does not list `ChamberWall`'s `name` and `vector` for a
`cusp_chambers` row. `test_the_fields_page_documents_every_field_of_a_record` walks the models `site.fields()`
yields, so it sees the row's fields and not the nested record's, and each of them is on the page.
