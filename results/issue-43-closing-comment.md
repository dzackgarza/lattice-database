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

**3. The T_Co rows: all three cusps stored.** `lattices/6JRR.md:118` carries
`integral.cusp_root_orbits['gamma-co-2']` at (4.3.7), p. 22, (4.3.8), p. 23, and (4.3.9), p. 24 — one class each at the
first two, `orbit_count: 1`, and three classes at the third with `orbit_count: 2`, orbits `{alpha_12}` and
`{alpha_13, alpha_14}`. Certificate `6JRR integral.cusp_root_orbits` `d2e682f6...`.

The third row's proof is the class of `delta` in `K_I = v^perp/Zv`: every element of `W_v` fixes the cusp and so
preserves that class; two of the eight diagram symmetries carry `delta` to `±delta` and the six others land in a different
class, so no product `w s` fixes `delta` unless `s` does, and the Coble image is `<W_v, sigma>`
(`results/issue-43-lemma-coble-class-invariant.md`). An earlier two-orbit row was withdrawn when its argument — that
`W_v` fixes `delta` — was found false; this replaces it.

**The eight lemmas behind the Coble side** are indexed in `results/issue-43-acceptance.md`: Sterk's (4.3.10) is an
Enriques statement; the one symmetry joining $\alpha_{13}$ and $\alpha_{14}$ fixes $\delta$; no congruence separates the
classes; every $T_{\mathrm{Co}}$ wall reflection fixes $\delta$; the $\delta$-preserving part of $G_v$ gives two orbits;
Sterk states $G_v$'s shape only at (4.3.6) and (4.3.7); his $\Gamma$ is this corpus's $\Gamma_{\mathrm{En},2}$; and no
source here prints the Coble orbits. Each is a file of its own with the page it rests on.

**What is left on the issue:** the cusp-5 row, and it needs a `gamma-co-2` card certified by computation from the
library's own construction of $\Gamma_{\mathrm{Co},2}$ — which needs an exact index for the stabilizer of a
non-degenerate sublattice, or a call that presents that stabilizer as a subgroup of $O(T_{\mathrm{Co}})$, neither of
which the owner's library presents today — together with the owner's class-level equivalence at a Coble cusp. That is a
dependency on the library and on the group's definition in print, not on this repository's data: cusps 3 and 4 are
stored, the 029J rows are stored, and the gate passes.
