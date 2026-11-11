# #36: the ideal vertices of 0124's reflection polyhedron, and why 0125 stops

Source: H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*, Math. Z. 207
(1991), 1–36, read from the PDF text layer of
`tmp/sources/sterk-1991-compactifications-of-the-period-space-of-enriques-surfaces-i.pdf` (printed page
numbers agree with the PDF's pages) and its OCR `tmp/sterk-1991-part-i.md`.

## Card 0124 = U ⊕ E8(−2), type (10, 8, 0) — transcribed

| What | Where |
| --- | --- |
| the quotient is this lattice | (4.3.4), p. 19: `v^⊥/Zv ≅ H ⊕ E8(−2)` for every `v ≠ e`, and (4.3.6), p. 21: "(e')^⊥/Ze' can be identified with the sublattice H ⊕ E8(−2)" |
| the reflection group is `O(L)` up to ±1 | (4.3.6), p. 21: "It is evident that `G_e' = O(H ⊕ E8(−2))`", and, "As there are no symmetries we have `O(H ⊕ E8(−2)) = {±1}·W_e'`" |
| the diagram | Fig. 6, p. 21: the nodes `α_1, …, α_8`, `α_9 = ᾱ_8 + 2f`, `α_10 = e − f`, with the legend "∘: (−4)-vector, •: (−2)-vector" |
| the ideal vertices | Fig. 7, p. 21: "In the picture we see the two maximal parabolic subdiagrams" |
| why a maximal parabolic subdiagram is an ideal vertex | (4.3.3), p. 18 (Vinberg 1972, Sterk's [26]): "every isotropic line in N_Q is W(G)-equivalent to some vertex at infinity of P; the vertices at infinity of P correspond to the parabolic subdiagrams of rank n − 1 of Σ(G)" |

Count: **2**. Ten walls and `n = 9`, so a maximal parabolic subdiagram has rank 8; the printed diagram is
connected, so those are the 9-vertex affine subdiagrams, and the paper counts two of them. No symmetry
group acts, so the count of subdiagrams is the count of vertices, not of orbits.

Stored: `lattices/0124.md`, `integral.cusp_chambers.O[0]` — `statement: 4.3.6`, `printed_page: 21`,
`figure: 6`, the ten walls in the card's own basis, their Gram matrix and diagram computed from the
card's Gram tensor, and `ideal_vertices: 2`. Certificate
`b41ae48d2742fcde316c138b37f747020d5545e73fa29ffdeb534c724ff37720`, written to
`certificates/29.yaml` and cited on the card. `results/transcribe-36-sterk-ideal-vertices.py` is the
program; it evaluates the card's stored form on the source's vectors and runs no Vinberg search.

What the script checks about the printed data, without storing a claim it did not read:

* the card is `H ⊕ E8(−2)` in Sterk's decomposition — the first two basis vectors span `H`, the E8
  Dynkin diagram in Sterk's numbering (Fig. 1, p. 3) is the card's `−2·Cartan(E8)` block, and the two
  summands are orthogonal;
* `ᾱ_8` is the dual of `α_8` in `E8(−2)`, `(ᾱ_8, α_j) = 2δ_{8j}`, of square `−4`;
* the ten walls have negative square, `α_10 = e − f` is the only `(−2)`-vector and the other nine are
  `(−4)`-vectors, which is the legend of Fig. 6 — the source's sign convention;
* the walls span `L` over `Q`, so the chamber is full-dimensional in `H^9`;
* the diagram the card stores is the ten walls' own Gram, nine edges, `α_9–α_10` of order 4 and the
  rest of order 3.

## Card 0125 = U(2) ⊕ E8(−2), type (10, 10, 0) — computed

No source prints the chamber of the reflection part of `O(U(2) ⊕ E8(−2))`, so its `O` row is a
computed value: `genus.store_cusp_chambers` writes it and its certificate names the operation and its
revision instead of a citation.

* The mathematics is the preamble's: `HyperbolicLattices(ZZ)(Lattices(ZZ)(the card's gram_tensor))`
  `.fundamental_chamber(max_roots=20, max_decompositions=2000)` ran Vinberg's algorithm at
  sage-extensions `5a9874e22ea18fb223ff53cf2a3e48dd63c022b4` and returned ten walls and ten primitive
  rays, with `is_complete_wall_set()` true at those bounds.
* The rays' squares are `(0, 36, 84, 60, 40, 24, 12, 20, 8, 4)` — exactly sage-extensions#299's
  recorded measurement — so exactly one vertex is on the light cone: **one ideal vertex**, and
  `is_cocompact()` is `False`.
* By Vinberg's criterion that vertex is a maximal parabolic subdiagram of rank `n − 1`: the ideal ray is
  `−f`, of coordinates `(0, −1, 0, …, 0)`, the walls orthogonal to it are nine in one connected
  component, and `9 − 1 = 8 = n − 1` for `n = 9` ((4.3.3), p. 18; Vinberg 1972).
* The row states the ten walls (`w_1, …, w_10`, in the order the operation returns them — no source's
  names), their Gram matrix, their nine-edge Coxeter diagram and `ideal_vertices: 1`, with no statement,
  page or figure. Certificate `12a3571c1d15ae8e99771f894e0bdfbb928fe8aafe34da732287ea6f67917e13` in
  `certificates/97.yaml`. `results/compute-36-0125-chamber.py` is the program.

### Why Sterk's own chamber gets no row

(4.3.5), p. 19, prints "the diagram of the reflection group `W_e ⊂ G_e`", with
`G_e = {g ∈ O(M(2)) : the induced map on M(2)*/M(2) respects the decomposition}` — a finite-index
subgroup that the paper never identifies with `O`, unlike (4.3.6) for 0124. That chamber has twelve
walls (Fig. 4, p. 19), not the ten the lattice's own search returns, and the only count printed for its
ideal vertices is a count of orbits: "The maximal parabolic subdiagrams (**modulo symmetries**) are
indicated below" (p. 19, Fig. 5 on p. 20), and "we do not only find **four equivalence classes** in
`I_1(e^⊥/Ze)`, but that we find four labelled classes" modulo `S_e ≅ Z/2 × Z/2` (p. 20).

`integral.cusp_chambers` keys a non-standard group by the slug of an `arithmetic-groups/` card of the
same lattice (`checks.catalogues`), and card 0125 has no card defining `G_e`. So the key is missing and
the row is not stored; the missing key is written up in `results/issue-36-ge-key.md` for filing.

## What was measured

* `just test`'s selection (`tests/test_model.py`, `tests/test_card_merge.py`), `tests/test_stored_records.py`,
  `tests/test_catalogue_schemas.py`, `tests/test_verification.py` and `tests/test_genus.py` in the pinned
  image at sage-extensions `dbe90c02ae`: see the commit message for the counts.
* The card's front matter is otherwise unchanged: parsed before and after the write, the only additions
  are `integral.cusp_chambers`, its certificate and its reference. The card's text was in a
  nested-block YAML style no other card uses; the writer re-emits the corpus's canonical style, which is
  the rest of the diff.
* No full-corpus build, no `tests/validation/test_build.py`: as in #37, the site and `corpus.load` do
  not fit this VM beside the other projects' work.
