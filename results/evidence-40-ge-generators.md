# #40: the nine members that generate H <= G_e, and the call that returns them

Source of the group: H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*,
Math. Z. 207 (1991), 1–36, (4.3.5), p. 19: `G_e = {g in O(M(2)) : the induced map on M(2)*/M(2)
respects the decomposition}`, with `M(2) = U(2) + E8(-2)` the card of `0125`. In the owner's terms
`sage-extensions`#354 gives `G_e = rho_L^{-1}(P)`, `P = Stab_{O(A_L)}(A_U(2))`, and the call the issue
names is `L.Aut().discriminant_point_stabilizer_image_generators(A_U(2))`.

## The call returns: nine members, 93 s (sage-extensions#459)

At sage-extensions `b501886b` — `origin/main` after #459 closed — the call returns on the stored Gram
tensor of `0125`:

| What | Value |
| --- | --- |
| members returned | **9** |
| time to the members | 93 s |
| peak resident, whole run | 1 175 MiB (1 009 MiB at the members) |
| `|O(A_L)|` | 46998591897600 |
| `|orbit(A_U(2))|` = `[O(A_L) : P]` | 67456 |
| `|P|` = `|O(A_L)|/|orbit|` = engine stabilizer order = `2 * 348364800` | 696729600 |
| `|`images of the nine`|` | 696729600 |

Each member was checked to lie in `rho_L^-1(P)` and to preserve the four classes of `A_U(2)` under the
preimage's own morphism; each matrix is integral, unimodular and satisfies `M^t G M = G`.

`T_Co`'s call was measured by the owner at 11 members in 231.2 s with the same image order, which is
the scale this agrees with.

## Why it needed #459: seven runs at `2fb37d5a717`

At the previous revision the same call never returned, and `discriminant_point_stabilizer` did:
the table records what each run reached and how it ended.

| run | reached the preimage | ended at | peak RSS | result |
| --- | --- | --- | --- | --- |
| A | 256.5 s | 1075 s | 2.37 GiB | exit 0, no value, no traceback |
| B | 100.9 s | 845 s | 2.35 GiB | exit 0, no value, no traceback |
| C | 508.6 s | 2600 s | 2.55 GiB | exit 0, no value, no traceback |
| D | 100.9 s | 1404 s | 2.29 GiB | exit 0, no value, no traceback |
| probe | — | still running at a 900 s cap | 2.37 GiB | killed by the run's own limit |
| E (the loop copied out with progress lines) | — | stopped at 2662 s | 2.51 GiB | no value; the line after `preimage.group_generators()` never printed |
| F | — | ended at a 5400 s cap | 3.26 GiB | no value; `MemAvailable` between 1080 and 6960 MiB, so not a kill |

In the pinned revision the loop was `src/sage_extensions/categories/lattice_morphisms.py:4047-4056`,
over the family built at `:4041` from the preimage at `:4040`. Run E showed which of the two stages
carried the cost: the first line after `preimage.group_generators()` (`:4041`) never printed, so the
Schreier family's construction over the 67 456-point orbit — `15 * 67456 - 67455 = 944385` members —
was the part that did not return. Run F ruled out a kill: with 4–7 GiB of the host free it kept
working to the cap.

#459's repair, at `b501886b`, is the lazy family: `_discriminant_point_orbit_and_section` records the
orbit and its transversal words and no transition table (the table is one entry per point-letter
pair, `2.3e7` of them on `T_Co`), and `_discriminant_point_stabilizer_members` evaluates a member's
letter image when the member asks for it. The family is then as cheap to read a prefix of as the
selection needs.

## What is stored where

| What | Where |
| --- | --- |
| the nine self-isometries | `lattices/0125.md`, `morphisms` entries with `target: '0125'`, `scale: 1` |
| the subgroup they generate | `arithmetic-groups/h-e.md`: `name: H_e`, `parent_group: g-e`, `data.generator_morphisms` = the nine names, prose stating `rho_L(H_e) = P` and that they are not generators of `G_e` |
| the card's own statement of it | `lattices/0125.md` prose, and `arithmetic_groups: [o-u2-e8, g-e, h-e]` |
| the group `G_e`'s naming of them | `arithmetic-groups/g-e.md` prose |
| the certificate | `certificates/97.yaml`, `0125 arithmetic-group.h-e.generator_morphisms`, whose `by` names the owner revision `b501886b` and the program; and the hash cited in `lattices/0125.md` `certifications` |

All nine members turn out to be isometries the card already stored: the family's selected members are
`O(L) generator 1` … `O(L) generator 8` and `O(L) generator 10`, so each is stored once and the `h-e`
card names those entries.

The hash commits to the computation name, the card's Gram tensor and the nine matrices sorted
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
matrix as a self-isometry and asks the owner for its discriminant action; the repository's own checks
(`results/verify-40-scoped-cards.py`) report no problem for `records`, `morphisms` or `catalogues`;
and `tests/test_ge_generators.py` pins the same state in the gate.

## The acceptance, item by item

| Item of the issue | Where it is decided | Verdict |
| --- | --- | --- |
| the card stores a generating set of $G_e$ as self-isometries, or — until generators of $\\widetilde O(L)$ exist — the nine members in a row that names $H$, stating $\\rho_L(H) = P$ | `lattices/0125.md` `morphisms`; `arithmetic-groups/h-e.md` | met: the nine members of the delivered call |
| the `arithmetic-groups/` card of $G_e$ names them | `arithmetic-groups/g-e.md` | met |
| it does not name them as generators of $G_e$ | `arithmetic-groups/g-e.md`, `arithmetic-groups/h-e.md` | met: `parent_group: g-e`, the relation, and no `data.generator_morphisms` on `g-e` |
| the card certifies the computation, the Gram tensor and the result, with the program revision in `certificates/` | `certificates/97.yaml`, `lattices/0125.md` `certifications` | met |
| the repository's gate passes | `tests/`, `justfile` | met |
