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

So the group of the T_Co cusps is a setwise stabilizer of a **non-degenerate** sublattice, and the library's exact
index route — the finite character quotient a standard subgroup has, and the one every certified index on this corpus
comes from — does not apply to it: the index is a coset-space question the library declines to answer exactly. That is
a capability fact about the owner's library, not a property of this card, and it is worth naming on its own: an
arithmetic subgroup given by a stabilizer condition has no exact index here, only the enumeration the assertion refuses.

Three inputs would close the item, and each is someone else's to give: a published definition of
$\Gamma_{\mathrm{Co},2} = \mathrm{Stab}_{O(T_{\mathrm{En}})}(T_{\mathrm{Co}})$ to cite, or a decision to key the
card to the group's own draft, or an exact index for the setwise stabilizer of a non-degenerate sublattice from the
owner, plus the owner's class-level equivalence returning at a Coble cusp for the (4.3.9) count.
