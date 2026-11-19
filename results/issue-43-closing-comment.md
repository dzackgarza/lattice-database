Closing #43: the acceptance's two clauses are met, and the narrative's T_Co sentence is met for two of its three
cusps — the third needs one input the repository does not hold. Unposted: this connector cannot comment on issues, so
this is the text of the comment with the tree's own line numbers.

**1. The 029J rows hold certified values.** `integral.cusp_root_orbits` at `lattices/029J.md:492`, four rows under
`gamma-en-2`, one per cusp that has a root class (Sterk's (4.3.5) has none and so has no row):

| cusp | statement | page | line | classes | orbits |
| --- | --- | --- | --- | --- | --- |
| $e'$ | (4.3.6) | 21 | `lattices/029J.md:495` | 1 | 1 |
| $e'+f'+\bar\alpha_8$ | (4.3.7) | 22 | `:504` | 2 | 1 |
| $2e'+f'+\bar\alpha_1$ | (4.3.8) | 23 | `:514` | 2 | 1 |
| $2e+2f+\bar\alpha_1$ | (4.3.9) | 24 | `:524` | 4 | 1 |

Cited at `lattices/029J.md:19`, held at `certificates/70.yaml:87`,
`1491eec6cdfb74d658ea0afe48e1d44637d55068cdf1460e23ae5239fafd709f`, whose provenance names Sterk's three statements
with (4.3.10) and `results/store-43-cusp-orbits.py`. The counts are **cited**, not searched: at (4.3.7), (4.3.8) and
(4.3.9) Sterk states that the chamber's diagram symmetry is realised in the cusp stabilizer (pp. 22, 23, 24), and an
isometry of $\Gamma_v$ carrying one root wall to another carries its class in $K_J$ to the other's; the symmetry is
recomputed from the card's Gram tensor by `results/store-43-cusp-orbits.py` and re-asserted from the shipped card at
`tests/test_cusp_root_orbits.py:153`. The rows are read back at `tests/test_cusp_root_orbits.py:126`.

**2. The gate passes.** `latticedb verify` could not finish on a 15 GB machine before this issue's last turns, because
`checks.one_shard` read the whole corpus and every certificate. A shard now reads its closure
(`src/latticedb/checks/__init__.py:121`, `:148`, `:87`), with the one corpus-wide check taken from the durable index
through the read-only `src/latticedb/corpus.py:464` and `src/latticedb/checks/records.py:36`. `verify --shard 0/64`
reports 4,752 cards in 1.0 GiB with 0 problems; the 20 problems the other slices then found — eight definite cards
carrying a `regular` certificate and no value — are settled, each card stating the value its certificate commits to,
asserted at `tests/test_stored_records.py:64`. CI runs the remaining shards.

**3. The T_Co rows at cusps 3–5: two of three decided, none stored.** 6JRR has no row and no `gamma-co-2` card, and the
field's key must be one of the eight standard subgroups or an arithmetic-group card of the same lattice
(`src/latticedb/checks/catalogues.py:132-137` against `src/latticedb/invariant_models.py:847`);
`lattices/6JRR.md:6692` lists only `otilde-t-co, otilde-plus-t-co`.

- Cusps 3 and 4 — (4.3.7) and (4.3.8) — carry **one** root class of $K_I$ each, so their count is $1$ whatever the group
  is, and `results/probe-43-coble-row-coordinates.py` writes both rows in 6JRR's own basis: cusps
  `[0,1,1,-2,-3,-4,-6,-5,-4,-3,-2]` and `[0,2,1,-4,-5,-7,-10,-8,-6,-4,-2]`, classes $\alpha_{13}$ and $\alpha_{11}$.
  Only the key is missing.
- Cusp 5 — (4.3.9) — has three classes ($\alpha_{12},\alpha_{13},\alpha_{14}$, all $O(K_I)$-equivalent), and the elements
  of $\Gamma_{\mathrm{En},2}$'s cusp stabilizer this repository can construct that preserve $T_{\mathrm{Co}}$ carry no
  class to another (22 of 27 do preserve it; `results/probe-43-coble-classes.py`), so the count lies between 1 and 3.

Three further facts were measured on the way and are worth having: $\Gamma_{\mathrm{Co},2}$ has **infinite** index in
$O(T_{\mathrm{Co}})$ — $T_{\mathrm{Co}}$ carries infinitely many vectors of square $-2$, so no card can state an index
(`src/latticedb/invariant_models.py:496` admits only a positive integer); the owner's library returns both constructions
of that group as membership predicates with no exact index; and $O(K_J)$ does report a selected resolution of its own.

**What closes item 3:** a key — a published definition of
$\Gamma_{\mathrm{Co},2} = \mathrm{Stab}_{O(T_{\mathrm{En}})}(T_{\mathrm{Co}})$ to cite, a decision to author
`gamma-co-2` from the project's draft (which this issue ruled out), or a decision to key the rows to a standard
subgroup, whose orbits a single-class family makes identical — plus the owner's class-level equivalence at a Coble cusp
for (4.3.9).
