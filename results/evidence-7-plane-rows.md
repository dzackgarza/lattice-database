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
| `latticedb verify` on the affected cards | **run**, 2026-11-19: `latticedb verify --shard 1/16`, the shard holding 6JRR, 18910 cards at a 3.6 GiB peak; no problem on 6JRR or either group card, and the shard's twelve problems are `definite.regular` contradictions on seven other cards (see below) |

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

## The two sign-kernel rows and the two determinant-kernel rows (2026-11-19)

`certify --tag 6JRR --field 'primitive_orbits[SO].planes' --field 'primitive_orbits[O+].planes'
--field 'primitive_orbits[SO+].planes' --phase fields --workers 1`, `--minutes 45`, image run of this
turn at sage-extensions `0bbf022b6b`, exit 1:

| row | outcome | the call |
| --- | --- | --- |
| `O+` | **1**, stored | `L.O_plus().cusps(2).cardinality()` |
| `SO` | refused by the owner | `L.SO().cusps(2).cardinality()` raises `ValueError` at `orthogonal_quotients.py:4237` |
| `SO+` | refused by the owner | `(L.O_plus() & SO()).cusps(2).cardinality()` raises the same |

So `integral.primitive_orbits` on `6JRR` now states `planes` on two rows, `O` and `O+`, both 1, under
field certificate `f0a9d428…` (superseding `15dcbad2…`). The two refusals are in `failures/e1.yaml`
with the owner's traceback, so neither a dispatch nor a nightly asks them again; the finding and the
repair it suggests are in `results/issue-286-so-plane-row-refusal.md`.

The cause is one guard, and it is the owner's: `_plane_orbit_from_odd_stabilizer` is admitted only
for `spinor_kernel and not determinant_kernel and not _has_discriminant`, so `O+` is decided by a
one-witness route and `SO`/`SO+` fall through to `_plane_orbit_from_parabolic_stabilizer`, which
refuses every sign-only subgroup. `SO` is `O+`'s mirror and the same one-witness answer is available
to it from the determinant image.

**The queue a `tags=6JRR` dispatch asks now** (the two refusals quarantined, so skipped):

```
primitive_orbits[Otilde].planes   primitive_orbits[Otilde+].planes
primitive_orbits[SOtilde].planes  primitive_orbits[SOtilde+].planes
arithmetic-group.otilde-t-co.{line,plane,flag}_orbits
arithmetic-group.otilde-plus-t-co.{line,plane,flag}_orbits
```

four kernel plane walks and two kernel incidence walks, against the same 330-minute budget.

## The four kernel rows: which the walk can decide, and the two local stops (2026-11-19)

The guard `_plane_orbit_from_parabolic_stabilizer` reads before it walks is the subgroup's finite
character quotient, so the walkable class is decidable without paying a walk. Measured on the stored
Gram tensor at sage-extensions `0bbf022b6b`, one process:

| row | index | `_has_discriminant` | det kernel | spinor kernel | parabolic route refuses | probe |
| --- | ---: | --- | --- | --- | --- | ---: |
| `Otilde` | 46998591897600 | true | no | no | no | 1.5 s |
| `SOtilde` | 93997183795200 | true | **yes** | no | no | 32.0 s |
| `Otilde+` | 93997183795200 | true | no | **yes** | no | 6.7 s |
| `SOtilde+` | — | — | — | — | unreachable | killed at 676 s |

`SOtilde+` did not reach the guard: its quotient was killed as the fourth quotient of that same
process, so the probe was repeated alone, in a fresh process, and killed again after **594 s**. That
is not accumulation, and an earlier measurement at the #596 epoch saw the subgroup pass 9.2 GiB RSS
after 510 s and keep growing. The row is now `open` in `failures/e1.yaml` with this measurement, so
neither a nightly nor a dispatch pays it.

## The two local stops on `Otilde`'s walk

`certify --tag 6JRR --field 'primitive_orbits[Otilde].planes' --phase fields --workers 1`,
`--minutes 100`, image run of this turn:

| attempt | wall | worker peak | the run's reserve floor | free memory on this VM | outcome |
| --- | ---: | ---: | ---: | ---: | --- |
| earlier turn | 677 s | 1236606976 B | 1676462899 B | 1.9 GiB available | worker ended, card untouched, exit 0 |
| this turn | 1054 s | 1065508864 B | 1676462899 B | 1.5 GiB available | worker ended, card untouched, exit 0 |

Both are `killed_by: memory` in `exceeded.yaml`, and both were released with
`just retry-computation` and a note carrying the measurement, so the row is `disposition: retry` and
a dispatched run asks it. The stop is the host's and not the row's: the owner's record measures this
row at 3476 MiB and 2171.0 s alone on a runner, and this VM had three other projects' jobs holding
between 4 and 15 GiB throughout.

**What is left for the dispatch, then, is three plane parts and six group counts** — not four plane
parts: `SOtilde+` is now quarantined for a reason that is not a walk.

## The two group cards' line counts, and why the three counts are not a bundle (2026-11-19)

Two of the group-card counts were computed this turn, and the first attempt showed a defect in my
own wiring rather than in the owner's cost.

| run | field | instrument | outcome |
| --- | --- | --- | --- |
| 1st | `arithmetic-group.otilde-t-co.line_orbits` | `g.cusps(1)` (span row) | **527**, stored |
| 1st | `arithmetic-group.otilde-plus-t-co.line_orbits` | `g.cusps(1)` | killed at 55 s, 636657664 B peak, reserve floor |
| 2nd | `arithmetic-group.otilde-plus-t-co.line_orbits` | `g.isotropic_orbit_representatives(1)` | **527**, stored |

A **line** is one vector and its span, so the gathered row is the cheap instrument and the span row
is the expensive one — the mirror image of the plane case, where the span row is cheap because a
plane's construction and retention is what costs. The lattice card's own line row already used the
gathered route; my `line_orbits` used `g.cusps(1)` and paid for it on the second subgroup. Fixed in
`sage_genus._arithmetic_group_value`, and the two stored values stand either way: a certificate
commits to the computation's name, Gram tensor and value, not to the instrument inside it.

**The dependency is the schema's, and only the schema's.** A flag count is stored only beside the
two counts it joins (`GroupData._orbit_counts`), so naming `flag_orbits` asks `line_orbits` and
`plane_orbits`. Naming a line count asks the line count. Until this turn the three were one bundle in
`genus.requests`, which meant a 31–52 s value could not be had without paying a 1813–2171 s walk, and
one kill lost all three; `arithmetic_orbit_dependencies` now states the dependency that exists.

**Where the two cards stand:** `line_orbits: 527` on both, certified
(`arithmetic-group.otilde-t-co.line_orbits`, `arithmetic-group.otilde-plus-t-co.line_orbits`) — the
theorem's number and the lattice card's row. `plane_orbits` and `flag_orbits` remain unstated for
both, and are the two kernel plane walks plus the two incidence walks of the dispatch.

## The kernel plane walk, third attempt

`Otilde`'s plane row, `--minutes 120`, at load 2.1 with 10 GiB available when it started:

| attempt | wall | worker peak | reserve floor | free memory at the end |
| --- | ---: | ---: | ---: | ---: |
| 1 | 677 s | 1236606976 B | 1676462899 B | 1.9 GiB |
| 2 | 1054 s | 1065508864 B | 1676462899 B | 1.5 GiB |
| 3 | 426 s | 1295683584 B | 1676462899 B | 1.8 GiB |

Three attempts, three ends at the run's own reserve floor, never by the row: the worker's peak never
approached the owner's 3476 MiB because the host's *available* memory was taken by other projects
before the walk reached it. The row is released again with this measurement and stays for the
dispatch; I will not attempt it a fourth time on this VM, because the stop is now measured three ways
and repeating it spends the VM to learn nothing.

## `latticedb verify` on the cards #7 changed (2026-11-19)

```
/sage/.venv/bin/python -m latticedb verify --shard 1/16
memory: 3.6 GiB peak for 18910 cards in shard 1/16
```

`sage-extensions` `0bbf022b6b`, the image's `/repos/research/src` as the preamble, the repository at
`a79c8b5a1b`. Shard `1/16` is the shard `6JRR` falls in (`certificates.tag_hash("6JRR") % 16 == 1`),
so the run covers 6JRR, `arithmetic-groups/otilde-t-co.md`, `arithmetic-groups/otilde-plus-t-co.md`
and every card they name, through `records.problems`, `relations.problems`, the duplicate-Gram index
and the catalogue checks.

**On the cards #7 changed: no problem.** The run's twelve problems are all one class on seven other
cards, all `definite`:

| card | problem |
| --- | --- |
| `02XN`, `03EP`, `05VD`, `06NV`, `06O4` | `definite.regular` **and** `definite.spinor_regular` each contradict its completed computation certificate |
| `3ICJ`, `3ICR` | `definite.regular` contradicts its completed computation certificate |

Those are the class the #7 comments already name on `02C3`, `02DC`, `02EI` and `0394`; they are not
this issue's cards and nothing here changes them. The run therefore exits 1 on the shard, and the
shard's redness is theirs — the affected cards' clause of #7 is what this run establishes, and it
holds.

The earlier statement that this could not be run is now stale in one specific way: `checks.one_shard`
**does** read only the shard's closure (`corpus.load(root, tags=shard_closure(...))`), which is why
18910 cards cost 3.6 GiB here rather than the 7.5 GiB the whole corpus cost in the runs that died.
The dispatch named for a wider check is still `verify.yml` with `tags=6JRR`, which verifies that shard
in CI.

## `Otilde+`'s kernel plane row returns: 189720 (2026-11-19)

```
latticedb certify --minutes 120 --tag 6JRR --field 'primitive_orbits[Otilde+].planes' \
  --phase fields --workers 1
6JRR {'primitive_orbits[Otilde+].planes': {'Otilde+': {'planes': 189720}}}
```

Started 07:12:26 UTC at load 0.98 with 10.7 GiB available — the quietest window this VM has offered —
and the value was stored by 07:47:51, so about 2000 s, at a 3.3 GiB card footprint (the owner's own
record: 1812.8 s at 3554 MiB on a runner). `integral.primitive_orbits` now states `planes: 189720` on
row `Otilde+` under field certificate `a3371f82…`, superseding `f0a9d428…`; the eight line constants,
`O`'s 1 and `O+`'s 1 were not recomputed.

The value is the theorem's `thm:coble-plane-orbit-counts` (2) for `K ∩ O⁺` and the count image run
`44392429173` reports for `Õ⁺(T_Co)`, and it is the computation, not the comparison, that put it on
the card.

**Why this one returned where three attempts at `Otilde` did not.** Nothing about the row: the walk
never exceeded 3.3 GiB either. The host had 6.9–7.3 GiB available throughout, so the run's own
1676462899 B reserve floor never fired. The three `Otilde` attempts were each killed when *other
projects* took the machine down to 1.5–1.9 GiB available, and the walks were at 1.0–1.3 GiB at the
time in every case. Same row, same machine, different tenant load.

**What this leaves in the field:** `planes` on `Otilde` and `SOtilde` (both reachable, both 189720 by
the theorem, neither computed here), `planes` on `SOtilde+` (unreachable: its character quotient
alone does not return), and `plane_orbits` and `flag_orbits` on the two group cards. `SOtilde` is now
the row worth one attempt in a quiet window, being the same walk that just returned.

## The lemma behind the four kernel plane counts, decided on this card (2026-11-19)

**Lemma.** Let `K = ker rho_{T_Co}`. For every primitive isotropic plane `P` of `T_Co` the stabilizer
of `P` in `K` maps onto `{±1}²` under `(det, sn_R)`. Hence `K`, `K ∩ SO`, `K ∩ O⁺` and `K ∩ SO⁺`
have the same orbits of primitive isotropic planes, and the four kernel rows of
`integral.primitive_orbits` have one plane count between them.

**Sources, by printed page.**

- D. Dolgachev, S. Kondō, *The rationality of the moduli spaces of Coble surfaces and of nodal
  Enriques surfaces*, Izv. Math. **77**:3 (2013): §2, printed p. 510 — the conventions (the lattice,
  its signature, the discriminant kernel $\widetilde O$); §3 eq. (3.6) with Proposition 3.2, printed
  p. 513 — `N = ⟨2⟩ ⊕ E(2)` and the moduli space.
- D. Dutour Sikirić, K. Hulek, *Moduli of polarised Enriques surfaces — computational aspects*,
  J. London Math. Soc. **110** (2024), arXiv:2302.01679, Lemma 3.6, printed p. 22 — the double-coset
  reduction through the finite image, which is what lets a character kernel's orbits be read as the
  ambient orbit's split.
- The two sign pairs are the ones research's `cor:coble-eight-standard-line-counts` proof exhibits for
  the line case; this is the plane case of the same character argument.

**The check.** `results/verify-7-plane-sign-witnesses.py`, on `lattices/6JRR.md`'s stored Gram tensor
at sage-extensions `0bbf022b6b`, with the owner's own membership predicates for every subgroup:

| witness (card's basis) | fixes the standard plane | `O` | `SO` | `O⁺` | `Õ = K` | `SÕ` | `Õ⁺` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| negate ⟨2⟩ | yes | ✓ | – | – | ✓ | – | – |
| negate `U(2)` | yes | ✓ | ✓ | – | ✓ | ✓ | – |
| negate `E8(−2)` | yes | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

All three are diagonal with ±1 entries, so each fixes the hyperbolic block's span as a set; each is
in `Õ`, so each lies in the stabilizer inside `K` of that plane. Their character pairs are
`(−1,−1)`, `(+1,−1)` and `(+1,+1)`, and `(−1,−1)·(+1,−1) = (−1,+1)`, so the three generate all four
pairs — inside `K ∩ Stab(P₀)` for the standard plane `P₀`.

**Why that is every plane and not one.** `O(T_Co)` is transitive on the primitive isotropic planes of
`T_Co`, which this card's own computation returns as the ambient row `O.planes = 1` (208.4 s on the
stored Gram). For any plane `P` pick `g ∈ O(T_Co)` with `gP₀ = P`; then
`g K g⁻¹ = K` and `g Stab_K(P₀) g⁻¹ = Stab_K(P)`, so the conjugated witnesses exhibit the same four
pairs at `P`.

**What it settles and what it does not.** It settles that the four kernel rows have one plane count
between them, so `SOtilde`'s walk, when it runs, must return `Otilde+`'s 189720 — and it explains why
the card's `SOtilde+` row can stay empty for a reason that is not the arithmetic (its character
quotient does not build here) while the count itself is not in doubt. It does not put a value on any
row: a card states what its own computation returned, and only `Otilde+`'s walk has returned.

## The flag count's arithmetic, and what it rests on (2026-11-19)

**Lemma.** The incidence relation between `K`'s line cusps and its plane cusps is $(1080,3)$-biregular,
so it has $527 \cdot 1080 = 189720 \cdot 3 = 569160$ edges, and the number of isotropic-flag orbits of
`K` is `569160`.

**Sources, by printed page.**

- D. Dutour Sikirić, K. Hulek, *Moduli of polarised Enriques surfaces — computational aspects*,
  J. London Math. Soc. **110** (2024), arXiv:2302.01679, Lemma 3.6, printed p. 22 — the double-coset
  reduction of a character kernel's orbits to the finite image, which is what makes the line and
  plane orbits countable at all.
- D. Dolgachev, S. Kondō, *The rationality of the moduli spaces of Coble surfaces and of nodal
  Enriques surfaces*, Izv. Math. **77**:3 (2013), §2 printed p. 510 and §3 eq. (3.6) with
  Proposition 3.2, printed p. 513 — `T_Co`, its signature, and its discriminant kernel `K`.

**The arithmetic, checked against the card's own numbers** (`results/probe-flag-arithmetic.py`,
`results/evidence-7-plane-rows.md` above holds the run):

```
isotropic_subgroups     23715  = 527 * 270 / 6
line_degree              1080  = 135 * 8 stars per plane
plane_degree                3  = the three nonzero divided classes of a plane (F2^2)
527 * 1080            = 569160
189720 * 3            = 569160
edges_close              true
```

The two degrees are the sources' numbers, not this run's: `135` is the number of order-four isotropic
subgroups of `A_{T_Co}` through a given nonzero isotropic class, `8` is the number of stars of such a
subgroup, and `3` is immediate because a primitive isotropic plane's divided classes are `P/2P ≅ F₂²`,
whose nonzero elements are exactly the classes of the plane's primitive vectors.

**What this does not establish.** The edge count is a count of *pairs of orbits*; that it equals the
number of *flag orbits* needs the injectivity of the forgetful map — distinct `K`-flag orbits have
distinct endpoint pairs, because a flag orbit is named by its divided class data (plane decorated plus
one nonzero class) — and that is the source's statement, not a computation here. Nor is `flag_orbits`
a card value on either group card: the incidence walk is 6132–7973 s per kernel row and has not run
here.

**Why it is worth recording anyway.** It fixes what the two group cards' `flag_orbits` must be when
their walks return — `569160` — and it double-checks `189720` from the line side, so a returned plane
count that did not close against `527 \cdot 1080` would be a disagreement worth reporting rather than
a value to store.

## `SOtilde`'s plane row: attempted once, ended by the host (2026-11-19)

```
latticedb certify --minutes 120 --tag 6JRR --field 'primitive_orbits[SOtilde].planes' \
  --phase fields --workers 1
```

Started 08:41 UTC with 9.4 GiB available. The worker reached 1.1 GiB and the run ended it at
`seconds: 566`, `peak_bytes: 1130909696`, `limit_bytes: 1676462899` — the reserve floor again, with
the host at 2.9 GiB available after other projects took the machine. Released with that measurement
so a dispatched run asks it; the count it must return is 189720 by the sign lemma above.

The four kernel rows now have four attempts between them and one returned: `Otilde+` in 2000 s, at
3.3 GiB, on a host that kept 6.9–7.3 GiB free.

| row | attempts | outcome |
| --- | ---: | --- |
| `Otilde+` | 1 | **189720**, 2000 s, 3.3 GiB |
| `Otilde` | 3 | ended at 677 s, 1054 s, 426 s; 1.0–1.3 GiB peak |
| `SOtilde` | 1 | ended at 566 s, 1.1 GiB peak |
| `SOtilde+` | 0 | no route: its character quotient does not build |
