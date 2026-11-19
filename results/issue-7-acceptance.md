# `#7` acceptance, item by item, with the line that carries each

Read from `main` at the commit this file lands in, by `.scratch/acceptance-probe.py` (the scoped
`corpus.cards(root, ("6JRR",))` read, `certificates.load`, `checks.records.problems`,
`checks.relations.problems`): line constants, plane counts, certifications, the three group cards,
and 0 records / 0 relations on the affected cards.

## 1. The eight certified line constants on `lattices/6JRR.md`

`integral.primitive_orbits` field certificate `da28cc04…` (`lattices/6JRR.md:21`,
`certificates/e1.yaml`), over the rows at `:75`–`:114`:

| row | `constant` | line |
| --- | ---: | --- |
| `O`, `SO`, `O+`, `SO+` | 1 | `:75`, `:95`, `:80`, `:100` |
| `Otilde`, `SOtilde`, `Otilde+`, `SOtilde+` | 527 | `:85`, `:105`, `:90`, `:110` |

The constant counts primitive isotropic **lines**, not signed vectors: the row's own paragraph says
so and cites `theory/orbits.md`. The first seven arrived by computation; `SOtilde+` arrived after
sage-extensions#596 and is recorded in `failures/e1.yaml` as resolved.

## 2. The plane counts, all eight rows

Every row states `planes` as well, and each is either a computation of this card or carried from a
record with a proof:

| row | `planes` | provenance |
| --- | ---: | --- |
| `O` | 1 | computed here, 208.4 s at 546 MiB |
| `O+` | 1 | computed here, the owner's odd-stabilizer route |
| `Otilde+` | 189720 | computed here, 2000 s at 3.3 GiB |
| `SO`, `SO+` | 1 | record's `O` row (`results/issue286-the-stage-1-call.md:99`) + `results/verify-7-plane-transport.py` |
| `Otilde`, `SOtilde`, `SOtilde+` | 189720 | record (`:275`, `:285`, `:372`, `:373`) + `results/verify-7-kernel-plane-transport.py` |

The record is sage-extensions `main` `47865446a7c37c85d873f91ac9d74cea472e208c`. What this card still
cannot do is compute a kernel plane row here — the walk is 1813–2171 s at 3.3–3.5 GiB and every
attempt ended at the run's reserve floor — which is `results/issue-draft-7-kernel-rows-without-record.md`,
a route and not a value.

## 3. Both arithmetic-group cards, with parent, index and generators

| card | parent | index | generators | line |
| --- | --- | ---: | ---: | --- |
| `arithmetic-groups/otilde-t-co.md` | — | 46998591897600 | 56 | `:7`, `:11`, `:12` |
| `arithmetic-groups/otilde-plus-t-co.md` | `otilde-t-co` | 93997183795200 | 95 | `:7`, `:8`, `:12`, `:13` |

Each index is the order of the subgroup's finite character image, read from the finite orthogonal
group of the discriminant form, not from an enumeration of its cosets; the generators are stored once
each, as scale-1 self-isometries among this card's `morphisms`, and the two fields are certified on the
lattice card as `arithmetic-group.<slug>.index_in_orthogonal_group` (`682c595c…`, `326145cc…`) and
`arithmetic-group.<slug>.generator_morphisms` (`3b6b6031…`, `648cd8af…`).

## 4. The incidence field

`flag_orbits` on the three group cards — `569160` on each standard kernel card, carried from the
record's incidence rows (`:372`, `:373`), and `13` on `gamma-co-2`, proved at
`results/issue607-gamma-co-2-rows-by-the-polar-space.md` at the same commit. The relation itself is
`(1080,3)`-biregular, which `results/probe-7-line-degree.py` and `results/probe-7-star-count.py`
close against the card's own 527 and 189720, and whose edge-to-flag-orbit step
`results/probe-7-injectivity-specimen.py` tests on `T_En` under `O(T_En)` (3 edges, 3 flag orbits).

## 5. The unconditional `Γ_Co = Õ⁺(T_Co)` identification

Corrected. `lattices/6JRR.md:6750` now reads that `Γ_Co` is **not** stated here to be
`Õ⁺(T_Co)`, that the identification is a conjecture with research#753 owning the family group, and
that the proved discriminant preimage is `Γ_Co,2 = R_{Γ_En,2}` with its own card `gamma-co-2`; the
same is stated from the other side at `arithmetic-groups/otilde-plus-t-co.md:28`. The card's earlier
paragraph (`:6774`) already said the identification is a conjecture and settles no count.

## 6. `latticedb verify` on the affected cards

`latticedb verify --shard 1/16`, the shard `6JRR` falls in (`certificates.tag_hash("6JRR") % 16 == 1`),
at sage-extensions `0bbf022b6b`: `memory: 3.6 GiB peak for 18910 cards in shard 1/16`, no problem on
`6JRR` or on either arithmetic-group card. The shard's twelve problems are `definite.regular` /
`definite.spinor_regular` contradictions on seven other definite cards (`02XN`, `03EP`, `05VD`,
`06NV`, `06O4`, `3ICJ`, `3ICR`), which are theirs. Recorded in `results/evidence-7-plane-rows.md`.

## What is not an acceptance item and is not claimed

- A computation route for a kernel plane row on this host: see the draft issue named in item 2.
- `Γ_Co`'s own orbit counts: they are conditional on the conjecture of item 5 and no card states them.
- The `SOtilde+` character quotient, which does not build here (594 s, killed).
