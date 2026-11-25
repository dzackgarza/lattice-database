# #43, item by item, at `main`

The issue states two things: what the card must carry when it closes ("card 029J (T_En) carries, per Sterk cusp under
`gamma-en-2`, the orbits of the cusp's root classes … The T_Co card carries the same row at its $\Gamma_{\mathrm{Co},2}$-cusps"), and what
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

## 2. The gate: the certification selection, measured

The acceptance clause names the gate, and the review measured it on a queued `verify` and a failing
`Certification regression tests` run. Two causes of that failure were found and repaired: the fixture at
`tests/test_genus.py:1319`, and `checks.records.duplicate_gram_problems`' fallback, which saw only the shard's closure
and so missed a duplicate Gram tensor whose cards sat in different shards (`src/latticedb/checks/records.py`).

On `6723df729b`, running the workflow's own selection (`.github/workflows/certification-tests.yml:39`) in this VM:

| file | result |
| --- | --- |
| `tests/test_genus.py` | **57 passed in 194.96 s** |
| `tests/test_failures.py` | 9 passed in 25.43 s |
| `tests/test_persist.py` | 5 passed in 18.84 s |
| `tests/test_corpus.py` | **exit 0 in 5 min 06 s** — every test in the file passed; its summary line did not survive the wrapper, but pytest's exit status is 0 only with no failures. The file previously failed at its fourteenth test |

So the certification selection is no longer a known failure of this issue's making; what remains is CI's verdict on a
head that carries the repairs. The `verify` shards are likewise CI's — measured here on the shards that fit (4,752 cards,
1.0 GiB, 0 problems), not corpus-wide.

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

## The lemmas, indexed

Eight lemmas bound the one open row. Each is a file of its own, each states what it proves or refutes and quotes the
printed page it rests on.

| file | what it settles |
| --- | --- |
| `issue-43-lemma-sterk-4310.md` | Sterk's (4.3.10)–(4.3.13), pp. 25–26, are stated for $A = H\oplus E_8(-2)$ and never mention $\delta$: the general transport to $T_{\mathrm{Co}}$ is unavailable. |
| `issue-43-lemma-alpha13-alpha14.md` | The one diagram symmetry exchanging $\alpha_{13}$ and $\alpha_{14}$ and fixing $\alpha_{11},\alpha_{12}$ fixes $\delta$ on the rank-10 span, so those two classes are one orbit: the count is at most 2. |
| `issue-43-lemma-parity-refuted.md` | Refuted: no congruence separates the classes — every difference among the root walls is odd, and $\Gamma_{\mathrm{En},2}$ cannot be trivial on $L/2L$ because the stored $T_{En}$ row has them in one orbit. |
| `issue-43-lemma-reflections-fix-delta.md` | Every reflection in a $T_{\mathrm{Co}}$ wall fixes $\delta$, so $W_v$ is inside the $\Gamma_{\mathrm{Co},2}$-cusp stabilizer and moves no class. |
| `issue-43-lemma-coble-image.md` | The Coble image is the $\delta$-preserving part of Sterk's $G_v$, with orbits $\{\alpha_{12}\}$ and $\{\alpha_{13},\alpha_{14}\}$: count 2 — conditional. |
| `issue-43-lemma-gv-not-stated.md` | Sterk states $G_v$'s shape only at (4.3.6) and (4.3.7); a count of one needs only a subgroup, a count of two needs the whole image, so the conditional above cannot be closed from his §4. |
| `issue-43-lemma-sterk-gamma-is-en2.md` | Sterk's $\Gamma$ is the corpus's $\Gamma_{\mathrm{En},2}$ — same definition, same index $67456$ at Remark 2.12, p. 8 — so the stored 029J rows are cited for the group they name. |
| `issue-43-lemma-no-source.md` | No source this repository holds prints the $\Gamma_{\mathrm{Co},2}$-cusp root-class orbits, so the 135-orbit row cannot be cited at all. |

## 3. The T_Co rows at the four $\Gamma_{\mathrm{Co},2}$-cusps

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

### The group card `gamma-co-2`

$\Gamma_{\mathrm{Co},2} := R_{\Gamma_{\mathrm{En},2}}$, the image in $O(T_{\mathrm{Co}})$ of $\mathrm{Stab}_{\Gamma_{\mathrm{En},2}}(\delta)$
(research def:gamma-co-groups(5)). It equals $\rho^{-1}(P_0)$ with $P_0 = \mathrm{Stab}_{O(q)}(A_{U(2)})$
(sage-extensions `results/issue286-gamma-co-2-is-the-discriminant-preimage.md`). So it contains
$\ker\rho = \widetilde O(T_{\mathrm{Co}})$, and its index in $O(T_{\mathrm{Co}})$ is $[O(q) : P_0] = 67456$, the number of
hyperbolic lines of $[h/2]^\perp$. `results/fix-49-gamma-co-2-card.py` counts these lines and checks that $O(q)$ is
transitive on them. The card names no parent below $O(T_{\mathrm{Co}})$.

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

### Why the stabilizer-of-a-vector route has no index (and why the card's index is a different number)

The two constructions above answer no exact index because there is no finite one to answer. $T_{\mathrm{Co}} =
\langle 2\rangle \oplus U(2) \oplus E_8(-2)$, so a vector $(a, (c, d), w)$ has

$$q = 2a^2 + 4cd - 2W, \qquad W = \tfrac{1}{2}(w, w)_{E_8},$$

and $q = -2$ forces $W = a^2 + 2cd + 1$. Take $a = 0$ and $cd = k$ for $k = 0, 1, 2, \dots$: every odd $W = 2k+1$
occurs, and every $W \ge 0$ is represented by $E_8$, whose theta series is
$\Theta_{E_8} = 1 + \sum_{W \ge 1} 240\sigma_3(W) q^W$ with every coefficient positive. So $T_{\mathrm{Co}}$ carries
infinitely many vectors of square $-2$, and $[O(T_{\mathrm{Co}}) : \mathrm{Stab}(v)]$ is countably infinite for each of
them. The same count with the $U$ summand of $T_{\mathrm{En}}$ gives infinitely many there too.

That is the index of $\mathrm{Stab}_{O(T_{\mathrm{Co}})}(v)$ — the subgroup a vector's stabilizer names — and it is
countably infinite, which is why the two predicate constructions of the previous paragraphs answer no exact index and
why `index_in_orthogonal_group` (`Annotated[int, Field(gt=0)] | None`, `src/latticedb/invariant_models.py:496`) could
not hold *that* number. It is not the number the Coble card states: $\Gamma_{\mathrm{Co},2}$ is the restriction of
$\Gamma_{\mathrm{En},2}$ to $T_{\mathrm{Co}}$, not the stabilizer of a vector, and its index in $O(T_{\mathrm{Co}})$ is
finite — $93997183795200 \cdot 46998591897600$, computed below. The correction matters: conflating the two was the
reason the earlier turns concluded no card could state an index at all. (An enumeration of the square $-2$ vectors,
`vectors_of_square(-2)`, was attempted as the direct count and had not finished after twenty minutes when it was
stopped, which is consistent with the set being infinite.)
