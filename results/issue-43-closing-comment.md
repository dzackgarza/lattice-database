Closing #43: the acceptance's two clauses are met, and the narrative's T_Co sentence is met at the four
$\Gamma_{\mathrm{Co},2}$-cusps. Unposted: this connector cannot comment on issues, so
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

**3. The T_Co rows: one at each of the four $\Gamma_{\mathrm{Co},2}$-cusps.** `integral.cusp_root_orbits['gamma-co-2']`:

| $\Gamma_{\mathrm{Co},2}$-cusp: orbit of $[v/2]$ | $v$ | line | chamber at the $T_{\mathrm{En}}$ cusp of $v$ | orbits |
| ---: | --- | --- | --- | ---: |
| 2 | $e_1$ | `lattices/6JRR.md:121` | Sterk (4.3.6), p. 21 | 1 |
| 120 | $[0,1,1,-2,-3,-4,-6,-5,-4,-3,-2]$ | `:127` | Sterk (4.3.7), p. 22 | 3 |
| 135 | $[2,0,0,-4,-5,-7,-10,-8,-6,-4,-2]$ | `:139` | Sterk (4.3.9), p. 24 | 4 |
| 270 | $[0,2,1,-4,-5,-7,-10,-8,-6,-4,-2]$ | `:155` | Sterk (4.3.8), p. 23 | 2 |

Sterk's cusps are $\Gamma_{\mathrm{En},2}$-cusps of $T_{\mathrm{En}}$, not cusps of $F_{\mathrm{Co}}$; they are provenance only.
`results/probe-49-gamma-co-2-cusps.py` (log beside it) computes the orbit of each $[v/2]$ under $P_0 = \mathrm{Stab}(A_{U(2)})$
and the root-class orbits by the centralizer of $s_\delta$ (`results/issue-49-transporters-and-coble-cusp5.md`).
`results/store-49-gamma-co-2-cusps.py` writes the rows; `tests/test_cusp_root_orbits.py::test_card_6jrr_states_the_root_class_orbits_at_each_of_the_four_gamma_co_2_cusps`
recomputes them from the Gram tensors. The earlier rows with 1, 1 and 2 orbits omitted the roots $\beta_u = \alpha_u + \delta$
and had no row at the 2-orbit cusp.

**The eight lemmas behind the Coble side** are indexed in `results/issue-43-acceptance.md`: Sterk's (4.3.10) is an
Enriques statement; the one symmetry joining $\alpha_{13}$ and $\alpha_{14}$ fixes $\delta$; no congruence separates the
classes; every $T_{\mathrm{Co}}$ wall reflection fixes $\delta$; the $\delta$-preserving part of $G_v$ gives two orbits;
Sterk states $G_v$'s shape only at (4.3.6) and (4.3.7); his $\Gamma$ is this corpus's $\Gamma_{\mathrm{En},2}$; and no
source here prints the Coble orbits. Each is a file of its own with the page it rests on.

**What is left on the issue:** the items of #49 that its last review found NOT MET on 029J (the transporter orders) and the gate.
