# #40: lifts of Sterk's discriminant stabilizer as self-isometries of card 0125

Source of the group: H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*,
Math. Z. 207 (1991), 1–36, (4.3.5), p. 19: `G_e = {g in O(M(2)) : the induced map on M(2)*/M(2)
respects the decomposition}`, with `M(2) = U(2) + E8(-2)` the card of `0125`. In the owner's terms
`sage-extensions`#354 gives `G_e = rho_L^{-1}(P)`, `P = Stab_{O(A_L)}(A_U(2))`.

## The greedy subfamily call does not return here: four runs

`L.Aut().discriminant_point_stabilizer_image_generators(A_U(2))` is the call that returns the
nine members named in the issue. On the stored Gram tensor of `0125`, at sage-extensions
`2fb37d5a717fac890e9cbf239f63d3a97f487040` (origin/main, 2026-11-17), it was run four times:

| run | reached `rho_L^-1(P)` at | ended at | peak RSS | result |
| --- | --- | --- | --- | --- |
| A | 256.5 s | 1075 s | 2.37 GiB | exit 0, no value, no traceback |
| B | 100.9 s | 845 s | 2.35 GiB | exit 0, no value, no traceback |
| C | 508.6 s | 2600 s | 2.55 GiB | exit 0, no value, no traceback |
| probe | — | still running at the 900 s cap | 2.37 GiB | killed by the run's own limit |

Each ended inside the selection loop over the Schreier family, which has `15 * 67456 - 67455 =
944385` members. Nothing was written to the card by any of them; the `Morphisms` block and the
ledger are unchanged by these runs. The host was shared and oversubscribed throughout (load
average 11–27 on 4 cores, `/proc/vmstat` `oom_kill` 30 since boot), which is what the wall times
show; the owner measured this call at 44.8 s natively.

So the card does not hold the nine members. It holds the owner's other route to the same
mathematical content, in three members.

## The route stored: lifts of `P`'s own generators along `rho_L`

`rho_L` is onto `O(A_L)` — `|rho_L(O(L))| = |O(A_L)| = 46998591897600` — so every element of `P` has
a lift in `O(L)`, and `L.Aut().discriminant_lift(h)` returns one: it factors `h` as a word in the
images of `O(L)`'s own selected generators and evaluates that word in `O(L)`, then checks the lift
against `rho_L` and raises rather than return a wrong element.

Measured by `results/generators-40-ge.py` (peak RSS 971 MiB):

| What | Value | Cost |
| --- | --- | --- |
| `|O(A_L)|` | 46998591897600 | — |
| `|P|` = `O(A_L).stabilizer_of_classes(A_U(2)).cardinality()` | 696729600 | 322 s |
| generators of `P` | 3 | in that call |
| lifts `L.Aut().discriminant_lift(h)` | 3 | 40 s |
| `|orbit(A_U(2))|` = `[O(A_L) : P]` | 67456 | — |
| `|O(A_L)| / 67456` | 696729600 | agrees |
| `|O(A_U(2))| * |O(A_E8(-2))|` = `2 * 348364800` | 696729600 | agrees |
| `|`images of the three`|` in `O(A_L)` | 696729600 | subgroup order |

The checks the program makes before it writes: each matrix is integral, unimodular and satisfies
`M^t G M = G` for the card's stored Gram; each image preserves the set of four classes of
`A_U(2)`; the images' subgroup has `P`'s order; and that order equals the index–stabilizer quotient
and the two summands' product, read from the two diagonal blocks of the card's own Gram.

One of the three lifts is the isometry `O(L)` already stores as `O(L) generator 8`, so it is stored
once and named there; the other two are new entries `H_e generator 1` and `H_e generator 2`.

## What is stored where

| What | Where |
| --- | --- |
| the three self-isometries | `lattices/0125.md`, `morphisms` entries with `target: '0125'`, `scale: 1` |
| the subgroup they generate | `arithmetic-groups/h-e.md`: `name: H_e`, `parent_group: g-e`, `data.generator_morphisms` = the three names, prose stating `rho_L(H_e) = P` and that they are not generators of `G_e` |
| the card's own statement of it | `lattices/0125.md` prose, and `arithmetic_groups: [o-u2-e8, g-e, h-e]` |
| the group `G_e`'s naming of them | `arithmetic-groups/g-e.md` prose |
| the certificate | `certificates/97.yaml`, `0125 arithmetic-group.h-e.generator_morphisms`, hash `109baa7b52f6a78ce3c30bb0f36c91c17ded27c8317c6bdf0d3fb466a2cbbc4a`, whose `by` names the owner revision `2fb37d5a717` and the program; and the same hash cited in `lattices/0125.md` `certifications` |

The hash commits to the computation name, the card's Gram tensor and the three matrices sorted
entrywise, as `genus.certified_value` and `genus._matrix_order` define it — not to the chosen names.

## Not stored, and why

* A generating set of `G_e`. `G_e = Otilde(L) . H_e` and no generating set of the discriminant
  kernel exists (sage-extensions#597); the family that does generate `G_e` has 944385 members.
* `data.index_in_orthogonal_group` for `H_e`. `[O(L) : H_e] = [O(L) : G_e] * [G_e : H_e] =
  67456 * [G_e : H_e]`, and the second factor is the part the missing kernel generators decide.
  The `h-e` card states none, so `latticedb certify` asks it for nothing: `genus.arithmetic_requests`
  skips a card with no `standard_name`.

## Verification of what is stored

`results/check-40-stored-generators.py` reads the card and the `h-e` card alone, builds each stored
matrix as a self-isometry and asks the owner for its discriminant action:

```
3 stored generators, each preserving the four classes of A_U(2)
|their image subgroup| = 696729600
|P| = 696729600
|O(A_L)| = 46998591897600
```

The repository's gate, in the shared Sage image (`/sage/.venv/bin/python`, `PYTHONPATH` = the
preamble's `src` and this repository's `src`):

* `pytest tests/test_model.py tests/test_card_merge.py -q` — `78 passed in 8.55s`.
* the checks of the four cards the change touches, run on the scoped corpus `corpus.cards(root,
  ["0125", "0153", "029J", "029L"])` with the `lie-groups` catalogue added, since `checks.one_shard`
  reads all 302,504 cards (about 7.5 GiB, more than this VM has free):
  `records.problems(loaded, held, {"0125"})` and `relations.morphism_problems(loaded, {"0125"})`
  report `[]`, and `catalogues.problems(loaded)` reports `[]`. The 17 self-morphisms of `0125` are
  checked by the preamble's form-preservation; the `h-e` card's generator names resolve to exactly
  one `scale: 1` self-morphism each; and the cited hash `109baa7b…c4a` matches the one this card's
  value recomputes, which is what `checks.records.arithmetic_problems` requires.
