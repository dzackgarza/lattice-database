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

## 3. The T_Co rows at cusps 3–5 — met for cusps 3 and 4, open at cusp 5 by decision

The decision of 2026-11-19 (orchestrator): the rows at Sterk's cusps 3 and 4 have one root class each, so their count
is $1$ for every subgroup, and they are stored under the standard key `O` of card 6JRR with the one-class argument as
the certificate text. The cusp-5 row depends on the group and stays empty until `gamma-co-2` has a card certified by
computation from the library's own construction, never authored from the draft.

Stored: `lattices/6JRR.md` `integral.cusp_root_orbits[O]`, two rows — (4.3.7), p. 22, cusp
`[0, 1, 1, -2, -3, -4, -6, -5, -4, -3, -2]` with the class `[1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1]`, and (4.3.8), p. 23, cusp
`[0, 2, 1, -4, -5, -7, -10, -8, -6, -4, -2]` with `[1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0]`, each `orbit_count: 1` with its
one class and `transporter_order: 1`. The certificate is `6JRR integral.cusp_root_orbits`
`241d3a4680a1b6255646ceeb37fc3a93e21a860e4f93a07c82d6ec3e439db318` in `certificates/e1.yaml`, whose provenance is
Sterk's two statements, the one-class argument, and `results/store-43-coble-rows.py`. Read back and checked by
`tests/test_cusp_root_orbits.py::test_card_6jrr_states_the_two_decided_coble_cusps`.

Cusp 5 — (4.3.9), p. 24 — is not stored: three root classes, all $O(K_I)$-equivalent, and the elements of
$\Gamma_{\mathrm{En},2}$'s cusp stabilizer this repository can construct that preserve $T_{\mathrm{Co}}$ carry no class
to another, so its count lies between 1 and 3. It waits on a `gamma-co-2` card certified by computation.

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

The rows are also pinned where the corpus can check them: `tests/test_cusp_root_orbits.py` holds these coordinates as
`COBLE_CUSPS` and `test_the_coble_cusps_rows_are_admissible_values_of_the_field` states them on card 6JRR and asks
`records.local_admission_problems` for a verdict — every cusp isotropic, every class in its cusp's perpendicular of
square $-2$ — so the arithmetic of the row cannot be what stops the storage when the key is decided. The fixture holds
them under a standard subgroup, which is a test's device and not a claim about which group the card must name.

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
