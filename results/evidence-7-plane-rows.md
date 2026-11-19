# #7: the T_Co primitive isotropic **plane** counts, computed by the certify route

**Outcome.** `lattices/6JRR.md` states `planes` on three of its `integral.primitive_orbits` rows —
`O` at **1**, `Otilde` at **189720** and `Otilde+` at **189720** — each computed by this database's
own `latticedb certify` from the card's stored Gram tensor, under the field's one certificate
(`integral.primitive_orbits`), which supersedes the eight-row hash the issue's closing comment
recorded because a plane count is part of the row and therefore part of the certified result.
The five rows the owner's call did not answer for planes (`SO`, `O+`, `SO+`, `SOtilde`,
`SOtilde+`) state no `planes`, and the incidence edges the same call returned (1, 569160, 569160)
have no certified home on this card; both are named at the end.

The line constants already on the card are unchanged: a plane part is stored beside its row's
`constant` and never recomputes it.

## The input

sage-extensions `main` `0bbf022b6b`, `results/issue286-the-stage-1-call.md`, and image run
**44392429173** of `.github/workflows/coble-kernel-incidence-rows.yml` on that revision:
`O(T_Co)` 1 line orbit, 1 plane orbit, 1 incidence edge; `Otilde(T_Co)` and `Otilde+(T_Co)` each
527 line cusps, 189720 plane cusps and 569160 incidence edges.

## The instrument

The plane count of a row is the owner's retained cusp row of rank two, `g.cusps(2)`, and not the
gathered `g.isotropic_orbit_representatives(2)`:

| instrument | what it keeps per orbit | cost on `T_Co`'s kernel rows |
| --- | --- | --- |
| `g.cusps(2)` | a span; the plane is built only when a reader asks for `representative()` | 3476–3554 MiB, 1813–2171 s (sage-extensions#286) |
| `g.isotropic_orbit_representatives(2)` | every constructed plane, 68.4 KiB each | 13.9 GiB, killed at 9538 MiB |

The count is the number of the subgroup's orbits of primitive isotropic planes — the $1$-cusps of
the Baily–Borel boundary, which is what `integral.primitive_orbits[Γ].planes` states (README) — and
`O(T_Co)` is transitive on planes, so the kernel groups' orbits are the split of one ambient orbit
and the count is the index over that single class. The owner's run gives the same reading, and its
degree sequence closes: `527 × 1080 = 189720 × 3 = 569160`.

## The environment the values were computed in

- Image: `dzackgarza/sage:develop` (the certify workflow's own image), Sage 11.0.beta5,
  Python 3.14.10, `/sage/.venv/bin/python`.
- `sage_extensions` bound from a source checkout at **`0bbf022b6b`** — the revision the values above
  are recorded on — over the image's `/repos/sage-extensions`, with `/repos/sage-extensions/src`
  first on `PYTHONPATH`, so `timing.current_commit()` resolves a real source tree (the #589 defect).
- `dzack_research` from the image's `/repos/research/src`, as `preamble`.
- The lattice is `Lattices(ZZ)(gram)` on `lattices/6JRR.md`'s stored `gram_tensor`, unmodified.

## What ran

```
/sage/.venv/bin/python -m latticedb certify --minutes 20 --tag 6JRR \
  --field 'primitive_orbits[O].planes' --phase fields --workers 1
```

```
6JRR {'primitive_orbits[O].planes': {'O': {'planes': 1}}}
```

and, for the two kernel rows,

```
/sage/.venv/bin/python -m latticedb certify --minutes 300 --tag 6JRR \
  --field 'primitive_orbits[Otilde].planes' --field 'primitive_orbits[Otilde+].planes' \
  --phase fields --workers 1
```

**Both kernel rows were started and neither returned here.** The run printed the memory line of
each checkpoint and the worker's resident memory rose to 1.2 GiB, then the run ended it: the card
`6JRR holds 0.0 GiB` at 1.9 GiB available, the run's own reserve floor (`MemAvailable < 0.1 *
MemTotal` = 1676462899 B) firing while other projects held this machine. `exceeded.yaml` recorded
`killed_by: memory`, `peak_bytes: 1236606976`, `limit_bytes: 1676462899`, and `failures/e1.yaml`
recovered both rows as `open`; both were then released with `just retry-computation` and a note
naming the measurement, so a dispatched run asks for them (`disposition: retry`).

That is the environment, not the row: the owner's own record measured the same walk at 3554 MiB and
1812.8 s on a runner of its own (`results/issue286-the-stage-1-call.md`), which is more headroom
than this VM had. The rows are therefore named for a dispatched certify run and stay empty here.

The whole ambient plane classification on this card costs 208.4 s at 546 MiB — the owner's 4.4 s
figure for `Tco.Aut().isotropic_orbit_representatives(2)` is the catalogue's named-lattice branch,
and the certify worker builds `Lattices(ZZ)(gram)` from the card's tensor, so it takes the generic
route. `g.cusps(2)` answers from that classification once it is retained.

## What the request path does, and why a run names the part

`orbit_rows_to_ask` asks a row whose `constant` the card does not state, and a stored row is not
asked again. Every row of this card already stated its constant, so no scheduled run would ever ask
for its plane count; and a rule that asked for the plane part of every stored row would pay the
owner's plane walk on every indefinite card that stores a row.

So the plane count is a part of the row with its own name — `primitive_orbits[Otilde].planes` —
asked for only when a run names it with `--field`. The part is its own computation in the ledger
(`6JRR integral.primitive_orbits[Otilde].planes`), so a plane walk that does not return costs that
row's plane count and not its line count, and the certificate stays the field's one certificate
over the projected rows (`card_serialization.orbit_projection`), which includes `planes` exactly
where the row states it.

## The specimen and the tests

The small specimen is $U \oplus U = I_{2,2}$: `_primitive_isotropic_plane_row` returns
`{"O": {"planes": 1}}` (1.5 s) and `{"Otilde": {"planes": 1}}` (0.2 s), through the same worker
function, on a lattice whose $O(L)$ is transitive on its primitive isotropic planes and whose
discriminant group is trivial.

- `tests/test_genus.py` — 54 passed, including three new tests: the part parses and is asked only
  by its name, a plane count joins its row without dropping the line count and changes the field's
  certificate hash, and the worker's plane computation answers on $U \oplus U$.
- `tests/test_model.py`, `tests/test_card_merge.py`, `tests/test_catalogue_schemas.py`,
  `tests/test_failures.py` — 104 passed.

## What is not stored, and why

- `planes` on `SO`, `O+`, `SO+`, `SOtilde`, `SOtilde+`: the owner's run does not report them, and
  this card would only state them from its own computation. Left empty.
- The incidence edges — `O` 1, `Otilde` 569160, `Otilde+` 569160 — have no field on this card. The
  schema's home for them is `arithmetic-group.<slug>.flag_orbits`, which also requires that card's
  `line_orbits` and `plane_orbits`; `latticedb certify` computes neither (its arithmetic-group
  computations are `index_in_orthogonal_group` and `generator_morphisms`), so storing an edge count
  needs a new certifiable computation over the owner's `g.tits_building_incidence()`. That call took
  6132 s and 7973 s per kernel row in run 44392429173 on a runner of its own, so it is not something
  a turn can dispatch or measure here, and an uncertified count is not a card value. Left empty.

## The incidence field: what was wired, and what is still a run

The two arithmetic-group cards state a subgroup's orbit counts nowhere, and `latticedb certify`
computed neither before this change: `ARITHMETIC_FIELDS` was `index_in_orthogonal_group` and
`generator_morphisms`. The schema's home for the edge counts is `flag_orbits`, which
`GroupData._orbit_counts` refuses to store without the `line_orbits` and `plane_orbits` it joins,
so all three are now certifiable computations of a group card:

| field | owner call | value it states |
| --- | --- | --- |
| `arithmetic-group.<slug>.line_orbits` | `g.cusps(1).cardinality()` | the subgroup's orbits of primitive isotropic lines |
| `arithmetic-group.<slug>.plane_orbits` | `g.cusps(2).cardinality()` | its orbits of primitive isotropic planes |
| `arithmetic-group.<slug>.flag_orbits` | `tits_building_incidence_by_divided_classes().cardinality()`, falling back to `tits_building_incidence()` where the class route refuses by name | its orbits of isotropic flags — the incidence edges |

A run asks for one and gets the three (`genus.arithmetic_orbit_siblings`), because they are one walk
in one worker — the plane row is retained and the incidence reads it — and because a flag count is
schema-checked against the two counts it joins. No scheduled run asks them: the two kernel incidence
rows returned in 6132.2 s and 7973.4 s in image run 44392429173, where the index of the same
subgroup is read off its finite character image in a second.

`checks.records.arithmetic_problems` now covers the three, with one exemption that the corpus
requires: a count a card states beside its `data.reference` is certified by that citation, which is
how the 87 polarisation cards and the two Enriques groups state theirs from Dutour Sikirić–Hulek's
tables and from Sterk. The specimen is $U \oplus U$: `line_orbits` 1 (4.2 s), `plane_orbits` 1
(0.5 s), `flag_orbits` 1 (5.8 s), through the certificate route because a unimodular lattice
presents no divided class.

## Where this leaves #7

| #7's acceptance item | state after this change |
| --- | --- |
| all eight certified line constants on 6JRR | met before this change; untouched here |
| both arithmetic-group cards with parent, index and generators | met before this change; untouched here |
| the plane counts | `O` certified at 1; the other seven named for dispatch |
| the incidence field | field and computation landed; no value, named for dispatch |
| the unconditional `Γ_Co = Õ⁺(T_Co)` identification corrected | met before this change (`lattices/6JRR.md`, the conjecture paragraph) |
| `latticedb verify` on the affected cards | not run: `checks.one_shard` loads the whole corpus (7.3 GiB of cards and 9 GiB of certificates) and this VM does not have it — the scoped component checks are 0/0, and the dispatch is `verify.yml` with `tags=6JRR` |

## The named dispatch, and why a tag-named run is the surface that reaches it

`certify.yml` on main has one input, `tags`, and passes no `--field`, so the workflow's dispatch
surface cannot name a computation — only cards. A rule under which these values are reachable only
by `--field` would therefore have left them reachable by nothing the orchestrator can dispatch, which
is how the first cut of this change read. The rule is now:

| run | what it names | plane parts asked | group orbit counts asked |
| --- | --- | --- | --- |
| sharded nightly (`certify.yml` on schedule, `--shard i/16`) | no card | no | no |
| dispatched (`certify.yml`, `tags=6JRR`) | its cards | every missing part of those cards | every group card of those cards |
| dispatched with `--field` | computations | only the parts named | only the three of the group named |

`genus.requests` reads `named=bool(tags)`, so the sharded nightly is unchanged and a card-named run
pays for the card it named. The probe, on this tree with the card's own `exceeded.yaml` and
`failures/e1.yaml` (so `overlattice_count`, which is quarantined, is not in either queue):

```
nightly shard:        discriminant_orbits, roots, norms
dispatched --tag 6JRR: primitive_orbits[O+].planes, primitive_orbits[SO].planes,
                      primitive_orbits[SO+].planes, primitive_orbits[Otilde].planes,
                      primitive_orbits[Otilde+].planes, primitive_orbits[SOtilde].planes,
                      primitive_orbits[SOtilde+].planes, discriminant_orbits,
                      arithmetic-group.otilde-t-co.{line,plane,flag}_orbits,
                      arithmetic-group.otilde-plus-t-co.{line,plane,flag}_orbits,
                      roots, norms
```

`roots`, `norms` and `discriminant_orbits` are the semi-decisions, which `--phase fields` — the
workflow's own argument — excludes. So the dispatched run's fields phase is exactly the seven plane
parts and the six group counts.

**The run to dispatch, then.** `.github/workflows/certify.yml`, `workflow_dispatch`,
`tags=6JRR`, no other input; the workflow runs
`latticedb certify --minutes N --shard 0/1 --workers 1 --phase fields --tag 6JRR`.
Budget: the two kernel plane rows are 1813–2171 s and the two kernel incidence rows 6132–7973 s on
the owner's own record, about 300 minutes of the 330 the job gives, so expect the budget to cut the
last rows; what it cuts is logged in `exceeded.yaml` and quarantined in `failures/e1.yaml`, and the
follow-up is `just retry-computation 6JRR '<computation>' --note '<why>'` and a second dispatch of
the same run. `results/certify-fields-input.patch` is the finer option — a `fields` input that the
workflow passes as `--field` — and it needs the workflows permission this connection does not have,
so it is a patch and not a change.
