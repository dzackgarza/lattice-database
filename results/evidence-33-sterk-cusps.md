# #33: Sterk's chambers at the 0-cusps of Γ_En,2

Source: H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207
(1991), 1–36, §4.3. Read from the text layer of `tmp/sterk-1991-part-i.pdf` and the OCR
`tmp/sterk-1991-part-i.md`; where they differ the text layer wins (the OCR prints ϑ for 9). The wall
lists of (4.3.7) and (4.3.9), which that text layer garbles, are the orchestrator's reading of the
printed pages, pp. 22 and 24.

## What the notation is

The earlier version of this file said that `ᾱ_i` is "the copy of `α_i` in the second summand of M",
and that reading does not survive the paper's own arithmetic. §1.2 defines two bases of E8:

> By α_1 … α_8 ∈ E_8 we denote the basis of E_8 such that (ᾱ_i, α_j) = δ_ij

— the barred vectors are the **dual basis** of the simple roots, not a second copy of them. In
L_- = H ⊕ H(2) ⊕ E8(−2) (the card of 029J in its own basis e_1, …, e_12) this is

    α_1 … α_8            the E8(−2) simple roots, Gram diag(−4) with +2 for adjacent nodes
    ᾱ_1 … ᾱ_8            the dual basis, (ᾱ_i, α_j) = 2 δ_ij, Gram −2 (C⁻¹), C the E8 Cartan matrix

and Sterk states the scaling himself in (4.3.5): "(ᾱ_i, α_i) = 2, because we are working in E8(−2)".
Their squares are −2 (C⁻¹)_ii, that is

    ᾱ_1 −8,  ᾱ_2 −16,  ᾱ_3 −28,  ᾱ_4 −60,  ᾱ_5 −40,  ᾱ_6 −24,  ᾱ_7 −12,  ᾱ_8 −4

Three independent statements of the paper confirm the identification of the lattice:

- (4.2.3), p. 16, lists the five cusps as e, e′, e′+f′+ω (ω² = −4), e′+2f′+γ (γ² = −8) and
  2e+2f+α (α² = −8). With (e′, f′) = 2 and the E8(−2) squares above, each of the three composite
  vectors is isotropic: 4 − 4 = 0, 8 − 8 = 0, 8 − 8 = 0.
- (4.3.7) computes an isotropic vector as α_9 + α_10 = (f′ − e′) + (ᾱ_8 + 2e′) = e′ + f′ + ᾱ_8, whose
  square is 4 − 4 = 0 only with (e′, f′) = 2 and ᾱ_8² = −4.
- (4.3.9) prints a basis ẽ = e + e′ + f′ − α_1, f̃ = f + e′ + f′ − α_1, α̃_1 = e′ − f′, α̃_2 = α_2,
  α̃_3 = f′ + α_3, α̃_4 … α̃_8 of v^⊥/ℤv for v = 2e + 2f + ᾱ_1; with the same conventions ẽ and f̃ are
  isotropic, (ẽ, f̃) = 1, and both are orthogonal to v, and α̃_1 … α̃_8 span E8(−2) (determinant 256).

With the unbarred α_i read as simple roots and the barred ones as the dual basis, (4.3.5)'s printed
check

    (α_10, e′+f′)² / |α_10²| = 4,   (α_11, e′+f′)² / |α_11²| = 16,   (α_12, e′+f′)² / |α_12²| = 64

comes out exactly, and every one of the twelve walls has square −4. With the barred vectors read as
simple roots, α_11 and α_12 have square +8 and +44: they are not walls, and they are the defect the
brief's rule (a positive diagonal entry) was written to catch.

The eight walls of (4.3.5) are the simple roots, although both transcriptions print them with a bar:
they are the E8 diagram of Fig. 4, and the dual vectors would make it no Coxeter diagram at all —
(ᾱ_1, ᾱ_3) = −14 with squares −8 and −28 gives |g₁₃| = 0.935, which is no cos(π/m) of Sterk's table.
So the bar in that list is the paper's own inconsistency, and the four vectors α_9 … α_12 beside it
are the dual ones.

Sterk's numbering of E8 (Fig. 1, p. 3) is Bourbaki's: the chain 1–3–4–5–6–7–8 with α_2 at α_4. Fig. 3,
p. 19, prints the coefficients 4, 7, 10, 8, 6, 4, 2 — the row of C⁻¹ for the chain nodes 1, 3, 4, 5, 6,
7, 8, with 5 (the coefficient of α_2) not recovered from the text layer — that is, up to sign, the
vector ᾱ_1 of square −8 used in (4.3.8) and (4.3.9).

## The rows

| statement | page | figure | cusp v | walls | count |
| --- | --- | --- | --- | --- | --- |
| (4.3.5) | 19 | 4 | e | α_1 … α_8, α_9 = f′−e′, α_10 = ᾱ_8+2e′, α_11 = 2e′+2f′+ᾱ_1+ᾱ_8, α_12 = 5e′+3f′+2ᾱ_2 | 12 |
| (4.3.6) | 21 | 6 | e′ | α_1 … α_8, α_9 = ᾱ_8+2f, α_10 = e−f | 10 |
| (4.3.7) | 22 | 8 | e′+f′+ᾱ_8 | α_1 … α_7, α_9 = f−e, α_10 = 2f′+ᾱ_8, α_11 = 2e−2f′−ᾱ_8 = (e+f)−α_9−α_10, α_12 = 2e+(ᾱ_1−ᾱ_8), α_13 = (e+f)+(α_8−f′) | 12 |
| (4.3.8) | 23 | 10 | 2e′+f′+ᾱ_1 | α_2 … α_8, α_9 = f−e, α_10 = ᾱ_8+2e′, α_11 = e+f+α_1−e′, α_12 = 2e−2e′+ᾱ_8−ᾱ_1 | 11 |
| (4.3.9) | 24 | 12 | 2e+2f+ᾱ_1 | α̃_1, α_2, α_4 … α_7, the dual of α̃_8, α_9 = 2ẽ−α̃_1, α_10 = 2ẽ+(ᾱ̃_2−ᾱ̃_3), α_11 = f̃−ẽ, α_12 = ẽ+f̃+(ᾱ̃_6−ᾱ̃_3), α_13 = ẽ+f̃+(ᾱ̃_1+ᾱ̃_8−ᾱ̃_3), α_14 = ẽ+f̃+α̃_3 | 13 |

All five rows are stored. (4.3.7) and (4.3.9) print their walls in the text beside their figures; the
earlier version of this file took those two blocks to be unreadable, because its text layer renders
several of their vectors with the wrong letters. The two readings above are the orchestrator's, from
the printed pages.

Each row is checked against the page's own cross-references rather than against my arithmetic alone:

- (4.3.7) prints the span of its roots, ℤ{α_1, …, α_7, α_8−f′, e+f, e−f}, and all twelve walls lie in it.
  (4.3.16), p. 27, then reads the primitive isotropic plane ℤv + ℤω off this diagram with
  ω = α_9 + α_12 + α_1 + α_3 + α_4 + α_5 + α_6 + α_7 + α_13, "ω of type 4", i.e. ω ~ 2e′+f′+ᾱ_1. With
  the twelve walls as transcribed, ω is isotropic and primitive, (ω, v) = 0, and it is orthogonal to
  exactly those nine walls and to no other wall, so the parabolic subdiagram of Fig. 9 is the one the
  paper names. That pins α_9, α_11, α_12 and α_13, the four vectors of this statement that the two
  transcriptions do not render cleanly.
- (4.3.9) prints the span ℤ{ẽ+f̃, ẽ−f̃, α̃_1, …, α̃_8}, and all thirteen walls lie in it; ẽ and f̃ span an
  H-summand (both isotropic, (ẽ, f̃) = 1) orthogonal to the E8(−2)-summand α̃_1 … α̃_8, as the statement
  says, and the Gram of α̃_1 … α̃_8 is −2 times the E8 Cartan matrix in Sterk's numbering. The duals
  ᾱ̃_i in α_10, α_12, α_13 are taken in that summand — (ᾱ̃_i, α̃_j) = 2δ_ij — computed from the card's
  own Gram tensor, not transcribed; they are integral combinations of the α̃_j, with squares
  −8, −16, −28, −60, −40, −24, −12, −4.
- The nodes of Fig. 12 inside that summand are α̃_1, α_2, α_4, …, α_7 and the dual of α̃_8. **α̃_3 = f′+α_3
  is not a node**, and that is not a preference: with it, (α̃_3, α_14) = (α̃_3, ẽ+f̃+α̃_3) = −4 against
  squares −4 and −2, so |g| = √2, which is no cos(π/m) — the pair would not be an edge of any Coxeter
  diagram. Of the two readings of the seventh node, that one is refuted by the diagram itself.

The counts are 12, 10, 12, 11 and 13. This does **not** match the consumer's expectation:
sage-extensions#297 states that Sterk publishes the diagrams of the polarized cusps j = 2, …, 5 with
10, 12, 11 and 14 walls, i.e. 12, 10, 11 and 14 in the order of the statements. The earlier version of
this file inferred the 14 for (4.3.9) from that expectation; it is not what the page prints. The figure
as read has the thirteen nodes listed above. A fourteenth node would be α_8 = α̃_8, which the read node
list does not contain, and with it the walls still satisfy every check here (rank 10, wall Gram of
signature (1, 9), all edges of order 3, 4, 6 or ∞, all walls in the printed span) — so the count is a
reading of the figure and not a consequence of the arithmetic, and it is the reading that is stored.
If #297's 14 is a count of this same figure, the node it counts is α_8 and the row should gain it; that
is a question for the page image, which this transcription did not read.

For (4.3.8) the text layer and the OCR disagree twice, and orthogonality to the cusp decides both:
α_9 is f − e (not f′ − e′, which is not orthogonal to 2e′+f′+ᾱ_1), and α_10 is ᾱ_8 + 2e′ (not
ᾱ_3 + 2e′: (ᾱ_3, ᾱ_1) = −14 ≠ −4). The last wall is α_12 = 2e − 2e′ + ᾱ_8 − ᾱ_1, which both readings
degrade ("ᾱ_8 − ᾱ_12" in the OCR, "α_5 − ᾱ_8" in the text layer) and which is the only combination of
those letters that is orthogonal to the cusp with a negative square.

## What is stored and what was computed

`integral.cusp_chambers['gamma-en-2']` on the card of 029J holds the five rows above with the cusp,
the walls (each with the source's name and its coordinates in the card's basis), the statement, page
and figure, and then the wall count, the Gram matrix b(w_i, w_j) and the Coxeter diagram, which
`results/transcribe-33-sterk-cusps.py` computed from the card's Gram tensor. The certificate is

    029J integral.cusp_chambers
    hash 3d07d82fc2fb4bc5f2171e4d73ef7c6e534354d0d9e7ad2e55910f0a7ce25022

with the citation of the five statements and the computing program as its provenance. It supersedes
`f546443699b5c3b377638ac85f9fe41ff4159cf9e1aba0762882909ad1a1db94`, which covered the three rows of
`1224b1b184`. `genus.cite_cusp_chambers` no longer requires the rows on the card to be *equal* to the
rows a source proves: it requires each stored row to be among them, so a statement of the same source
adds its cusp's row and the writer still stops where a stored row is contradicted or silently dropped.
No Vinberg search was run for any row: the walls are the source's, and the three invariants are the
card's form on them.

Checks the script asserts for every row, and that `tests/test_model.py` re-runs from the card alone:
the cusp is primitive isotropic; every wall is orthogonal to the cusp and has negative square; the
walls span v^⊥/ℤv over ℚ (rank 10 of 12, the cusp not in their span); every wall of (4.3.7) and
(4.3.9) lies in the span of the roots that statement prints; the stored Gram matrix is b on those
vectors; and every non-orthogonal pair has |g_ij| = cos(π/m) for m ∈ {3, 4, 6} or |g_ij| = 1.
For (4.3.7) the script additionally recomputes the paper's own ω of (4.3.16) from the stored walls,
and for (4.3.9) the duals ᾱ̃_i from the stored α̃_j.

## Gate

`just test` — the repository's gate, `tests/test_model.py` and `tests/test_card_merge.py` — in the
research image (`/sage/.venv/bin/python`, Python 3.14.10, the interpreter `.github/actions/sage` pins):
**71 passed**, the two tests added here included. The host's own `/opt/math/bin/python3` is 3.12 and
cannot run `tests/test_model.py`, which parses every module of `src/latticedb`: `src/latticedb/seed.py`
uses the PEP 758 `except A, B:` form that 3.12 refuses.

The wider suites were not green here, and not because of this change:

- `tests/test_catalogue_schemas.py`: 17 passed, 2 failed, and the two failures reproduce with the
  pre-change source on `PYTHONPATH` (`git archive HEAD src`, so `latticedb` at HEAD and the current
  cards): `6JRR` states a `certifications` block that its test forbids, and `0012`'s
  `definite.automorphism_group_generator_morphisms` contradicts a stored certificate. Both are data
  drift in the cards, not in this row.
- `tests/test_corpus.py` and `tests/test_genus.py` were not run to completion: `test_corpus` loads the
  whole corpus and reached 5.3 GiB of this 15 GiB VM with no memory left, so the run was stopped. The
  same task in `latticedb verify` is CI-scale (302,504 cards).


`latticedb verify` over the whole corpus is CI-scale (302,504 cards). It was run on `.scratch/mini`, a
copy of the repository holding 029J and the cards its morphisms and arithmetic groups name: nine cards
verified, five problems, and every problem is a card that is not in the copy —

    9 cards verified; 5 problems
      lattices/029L.md: the related tag 0094 is not in the corpus
      geometric-objects/kummer-2.md: cohomology lattice tag 0283 is not in the corpus
      arithmetic-groups/co-0.md: lattice 028S is not in the corpus
      arithmetic-groups/otilde-plus-t-co.md: lattice 6JRR is not in the corpus
      arithmetic-groups/otilde-t-co.md: lattice 6JRR is not in the corpus

— and none of them is 029J: the new reference check finds `gamma-en-2` to be an arithmetic-group card of
029J, and `integral.cusp_chambers` agrees with its completed certificate.

The same check on a copy of that copy whose stored `b(α_1, α_3)` is changed from 2 to 0 on both sides of
the Gram matrix reports exactly the row it falsified:

    lattices/029J.md: integral.cusp_chambers contradicts its completed computation certificate

so the certificate binds the value. (A one-sided edit is refused earlier, by the schema: "the Gram matrix
of a chamber is symmetric".)

`latticedb build` on the same nine-card copy renders the new field — `fields.html` lists "Chamber at a
cusp" and the page of 029J shows the five statements — and its internal-link check passes for both new
links (`../theory/orbits.html#chamber-at-a-cusp` from the card and `../tag/029J.html#cusp-chambers` from
the arithmetic-group card); it fails only on `theory/roots.html`, which links to tags the copy does not
hold.
