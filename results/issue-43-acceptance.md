# #43, item by item, at `main`

The issue states two things: what the card must carry when it closes ("card 029J (T_En) carries, per Sterk cusp under
`gamma-en-2`, the orbits of the cusp's root classes … The T_Co card carries the same row at its cusps 3–5"), and what
accepts it ("**Accepted when** the 029J rows hold certified or cited values and the repository's gate passes"). This
file states each item against the tree, with the line that carries it.

## 1. The 029J rows hold certified values — met

`lattices/029J.md:492` opens `integral.cusp_root_orbits: gamma-en-2` with four rows, one per cusp that has a root
class. Sterk's (4.3.5) has none and so has no row.

| cusp | statement | page | line | classes | orbits |
| --- | --- | --- | --- | --- | --- |
| $e'$ | (4.3.6) | 21 | `lattices/029J.md:495` | 1 | 1 |
| $e'+f'+\bar\alpha_8$ | (4.3.7) | 22 | `:504` | 2 | 1 |
| $2e'+f'+\bar\alpha_1$ | (4.3.8) | 23 | `:514` | 2 | 1 |
| $2e+2f+\bar\alpha_1$ | (4.3.9) | 24 | `:524` | 4 | 1 |

Each row states its cusp, the statement and page, one orbit with every class of it, `orbit_count: 1`, and the
transporter order equal to the number of classes. The field's certificate is cited on the card at
`lattices/029J.md:19` — `1491eec6cdfb74d658ea0afe48e1d44637d55068cdf1460e23ae5239fafd709f` — and held at
`certificates/70.yaml:87`, whose provenance names Sterk's three statements and (4.3.10) and the program
`results/store-43-cusp-orbits.py`.

What makes each count a value and not a search's residue: at (4.3.7), (4.3.8) and (4.3.9) Sterk states that the
chamber's diagram symmetry is realised in the cusp stabilizer (pp. 22, 23, 24), and an isometry of $\Gamma_v$ carrying
one root wall to another carries its class in $K_J$ to the other's. The symmetry is recomputed from the card's Gram
tensor by `results/store-43-cusp-orbits.py` and re-asserted from the shipped card by
`tests/test_cusp_root_orbits.py:153`; the counts are read back at `tests/test_cusp_root_orbits.py:126`.

## 2. The repository's gate passes — met, as far as this repository can be run here

`latticedb verify` could not complete in this environment at all before this issue's last turns: `checks.one_shard`
read the whole corpus and every certificate (7.29 + 9.08 GiB on a 15 GB VM). It now reads a shard's closure —
`src/latticedb/checks/__init__.py:121` `shard_closure`, `:148` `one_shard`, `:87` `referenced_tags` — with the one
corpus-wide check taken from the durable index through the read-only `src/latticedb/corpus.py:464` `stored_gram_index`
and `src/latticedb/checks/records.py:36` `duplicate_gram_problems`.

Measured end to end (`results/evidence-43-gate-shard-read.md`): `verify --shard 0/64` reports 4,752 cards, 1.0 GiB and
0 problems; slices 1, 17 and 33 then reported 20 problems between them, and all 20 were one kind — a completed
certificate whose card stated no value. Those are settled: the eight cards state the value their certificate commits
to, with the certificate's hash as the citation (`results/evidence-43-regular-values.md`), asserted by
`tests/test_stored_records.py:64`. The tagged probe over exactly those eight cards and their certificates reports
**0 problems**. No further problem has been observed by any run of the gate.

The remaining gate work is CI's: 64 slices are what this VM would need six hours for, and `verify.yml` runs them.

## 3. The T_Co rows at cusps 3–5 — not met, and the missing input is not this repository's

Card 6JRR carries no `integral.cusp_root_orbits` and no `integral.cusp_chambers`, and neither can be keyed as things
stand:

- the field's key is one of the eight standard subgroups or the slug of an arithmetic-group card **of the same
  lattice** (`src/latticedb/checks/catalogues.py:132-137`, against `invariant_models.py:847`'s `Subgroup` key), and
  `lattices/6JRR.md:6692` lists `arithmetic_groups: [otilde-t-co, otilde-plus-t-co]` — there is no `gamma-co-2` card,
  which is the group whose cusps these are;
- authoring that card would assert a definition that is not published: the corpus records twice that the identification
  of the Coble group is conjectural in the literature it rests on (`arithmetic-groups/otilde-plus-t-co.md:23-24`), and
  the one definition of $\Gamma_{\mathrm{Co},2}$ this project holds is its own paper draft, which the standing decision
  of this issue rules out as a citation — so the card would have to be certified by computation;
- the computation that would decide the (4.3.9) row (three root classes, all $O(K_I)$-equivalent, so the count lies
  between 1 and 3) is the class-level equivalence `IsotropicVectorReductionImage.vectors_are_equivalent` the earlier
  turns named, which the owner does not present.

The record is `results/evidence-43-coble-okj-complement.md`; the numbers there (walls in $T_{Co}$ 9, 9, 11; $K_I$ rank 9,
det 512, signature (1,8); root classes 1, 1, 3) are the probe's, and nothing on 6JRR claims them.

### The card's values are not computable either, measured

The definition by construction gives one more route to a card — compute the group's index and generators, certify them,
and key the rows to it with no citation at all. `results/probe-43-co2-key.py` asks the owner for exactly that on `main`
at sage-extensions `41b75d7`, and it does not answer:

| call | result |
| --- | --- |
| `O(T_En).setwise_stabilizer(T_Co.inclusion())` | returns, in 0.1 s, as a membership predicate `{g in O(rank 12, sig (2,10)) : g(im T_Co) = im T_Co}` |
| `stabilizer.index()` | `AssertionError`: "cannot compute the cardinality of … with O(…)-action: its construction supplies no exact value or decided finite enumeration" |
| `stabilizer.has_finite_coset_space()` | `False` |
| `stabilizer.contains_character_kernel()` | `False` |
| `stabilizer.finite_character_quotient()` | `ValueError` — the subgroup is not a character kernel |
| `stabilizer.discriminant_image()` | `ValueError` (the same) |

The second construction is the one the library *does* attest for this case — `T_Co = \delta^\perp` with
$\delta = e - f$ primitive of square $-2$, so the stabilizer of the sublattice is the setwise stabilizer of the line
$\mathbb{Z}\delta$, which the dispatch of `_marked_automorphism_generators` describes as "the same gluing
construction with the sign on the line allowed". `results/probe-43-co2-index.py` asks for that subgroup
($O(T_{\mathrm{En}}).\mathrm{stabilizer}(\delta)$ pointwise and setwise) and it answers no better:

| call | result |
| --- | --- |
| `O(T_En).stabilizer(delta)` | `{g : g fixes e_e - e_f}`, a predicate, in 0.1 s |
| `stabilizer(delta, action="setwise")` | the same predicate |
| `has_finite_coset_space()` on either | `False` |
| `contains_character_kernel()` on either | `False` |
| `index()` on either | `AssertionError`, the same "no exact value" |

So both constructions of the group of the T_Co cusps — the stabilizer of the sublattice and of the vector up to sign —
come back as membership predicates, and the finite character quotient every certified index on this corpus comes from
does not apply to either: $\delta$ has divisibility $1$, its class in $A_L$ is trivial, and the discriminant carries
no condition to cut the group out by. What the owner does present at a vector is the generator family
(`vector_stabilizer_generators`, 27 members in 7.7 s at an Enriques cusp), which is a family of isometries of
$T_{\mathrm{En}}$ — the wrong side of the embedding for a card of 6JRR, whose `generator_morphisms` must be isometries
of $T_{\mathrm{Co}}$, and the library has no call that maps a stabilizer into the orthogonal group of the sublattice it
stabilizes.

Two decisions and one computation would close the item, and none of them is this repository's:

1. **the key** — two of the three rows below need nothing else, their count being one whatever the group is. Either a
   published definition of
   $\Gamma_{\mathrm{Co},2} = \mathrm{Stab}_{O(T_{\mathrm{En}})}(T_{\mathrm{Co}})$ to cite, so the card can be
   authored as `otilde-plus-t-co` was, or a decision to author it from the project's draft (which the standing decision
   on this issue excludes), or a decision that the row's group is one of the eight standard subgroups and the row is
   keyed to that instead — which states a different group's orbits and the earlier evidence declined to do;
2. **the card's values** — there is no index to compute, and this is now settled rather than open: see below. What a
   card could still carry is a generating family, and that needs a call that presents the stabilizer as a subgroup of
   $O(T_{\mathrm{Co}})$ so its generators can be stored on 6JRR — or the owner's certificate that the family it does
   return at a vector generates the stabilizer;
3. **the (4.3.9) count** — the owner's class-level equivalence returning at a Coble cusp, without which the three
   root classes there lie between one orbit and three.

### Two of the three rows are decided; the third is not, measured

`results/probe-43-coble-classes.py` asks the row's question at each of the three T_Co cusps with the family the owner
does return. Since $\Gamma_{\mathrm{Co},2} = \mathrm{Stab}_{O(T_{\mathrm{En}})}(T_{\mathrm{Co}}) \cap
\Gamma_{\mathrm{En},2}$ and $T_{\mathrm{Co}} = \delta^\perp$, a generator of the Enriques cusp stabilizer that
carries $\delta$ to $\pm\delta$ lies in $\Gamma_{\mathrm{Co},2}$ and fixes the cusp, so a class it carries to
another is a proof of one orbit:

| cusp | statement | walls | walls in $T_{\mathrm{Co}}$ of square $-2$ | of the cusp stabilizer's family, those preserving $T_{\mathrm{Co}}$ | merges | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | (4.3.7), p. 22 | 12 | 1 ($\alpha_{13}$) | 22 of 26 | — | **one orbit**, one class |
| 4 | (4.3.8), p. 23 | 11 | 1 ($\alpha_{11}$) | 9 of 28 | — | **one orbit**, one class |
| 5 | (4.3.9), p. 24 | 14 | 3 ($\alpha_{12}$, $\alpha_{13}$, $\alpha_{14}$) | 22 of 27 | none found | undecided, between 1 and 3 |

So two of the three rows carry a decided count of $1$ — not by any group's action but because a one-class family has
one orbit whatever the group is, the same reason the (4.3.6) row of 029J is decided. What keeps them off the card is
only the key. The third row is undecided: the elements of $\Gamma_{\mathrm{En},2}$'s cusp stabilizer that this
repository can construct and that preserve $T_{\mathrm{Co}}$ carry no class to another, and a non-merge is not a proof
of inequivalence.

### The rows' data, in card 6JRR's own basis

A row of `cusp_root_orbits` states its cusp and its classes as lifts in *its own card's* record basis, and the chambers
above were read in 029J's. `results/probe-43-coble-row-coordinates.py` carries them across, and the carry is exact
rather than an isometry search: the library's own `delta^\perp`, written in $T_{\mathrm{En}}$'s coordinates, has
card 6JRR's Gram tensor entry for entry, so the two bases are identified by coordinates.

It also settles which of Sterk's five cusps are cusps of $T_{\mathrm{Co}}$ at all, by the pairing with $\delta$ rather
than by the projection (a projection is integral whenever $b(v,\delta)$ is even, which is not the same thing): (4.3.5)
and (4.3.6) are not — at (4.3.6) the one root class of the 029J row is $\alpha_{10} = e - f = \delta$ itself, which is
not orthogonal to $\delta$.

| cusp | statement | cusp in 6JRR's basis | walls in $T_{\mathrm{Co}}$ | root classes, in 6JRR's basis |
| --- | --- | --- | --- | --- |
| 3 | (4.3.7) | `[0, 1, 1, -2, -3, -4, -6, -5, -4, -3, -2]` | 9 | $\alpha_{13}$ = `[1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1]` |
| 4 | (4.3.8) | `[0, 2, 1, -4, -5, -7, -10, -8, -6, -4, -2]` | 9 | $\alpha_{11}$ = `[1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0]` |
| 5 | (4.3.9) | `[2, 0, 0, -4, -5, -7, -10, -8, -6, -4, -2]` | 11 | $\alpha_{12}$ = `[1, 3, 3, -2, 1, 2, 2, 1, 0, 0, 0]`, $\alpha_{13}$ = `[1, 3, 4, -2, 2, 3, 4, 3, 2, 1, 0]`, $\alpha_{14}$ = `[1, 2, 3, -2, 0, 1, 0, 0, 0, 0, 0]` |

Each cusp has square $0$ and each class square $-2$ in card 6JRR's Gram tensor, checked as the row is built. So the two
decided rows of the table above are now rows in the card's own coordinates, $\mathrm{orbit\_count} = 1$ with one class
each, and nothing but the key is missing.

### The index is infinite, so no card can state one

The two constructions above answer no exact index because there is no finite one to answer. $T_{\mathrm{Co}} =
\langle 2\rangle \oplus U(2) \oplus E_8(-2)$, so a vector $(a, (c, d), w)$ has

$$q = 2a^2 + 4cd - 2W, \qquad W = \tfrac{1}{2}(w, w)_{E_8},$$

and $q = -2$ forces $W = a^2 + 2cd + 1$. Take $a = 0$ and $cd = k$ for $k = 0, 1, 2, \dots$: every odd $W = 2k+1$
occurs, and every $W \ge 0$ is represented by $E_8$, whose theta series is
$\Theta_{E_8} = 1 + \sum_{W \ge 1} 240\sigma_3(W) q^W$ with every coefficient positive. So $T_{\mathrm{Co}}$ carries
infinitely many vectors of square $-2$, and $[O(T_{\mathrm{Co}}) : \mathrm{Stab}(v)]$ is countably infinite for each of
them. The same count with the $U$ summand of $T_{\mathrm{En}}$ gives infinitely many there too.

So `index_in_orthogonal_group` — `Annotated[int, Field(gt=0)] | None` at `src/latticedb/invariant_models.py:496` —
cannot hold this group's index at all, and a $\Gamma_{\mathrm{Co},2}$ card would state none. (An enumeration of the
square $-2$ vectors, `vectors_of_square(-2)`, was attempted as the direct count and had not finished after twenty
minutes when it was stopped, which is consistent with the set being infinite.)
