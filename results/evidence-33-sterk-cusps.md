# #33: Sterk's chambers at the 0-cusps of Γ_En,2

Source: H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207
(1991), 1–36, §4.3. Read from the text layer of `tmp/sterk-1991-part-i.pdf` and the OCR
`tmp/sterk-1991-part-i.md`; where they differ the text layer wins (the OCR prints ϑ for 9).

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
| (4.3.8) | 23 | 10 | 2e′+f′+ᾱ_1 | α_2 … α_8, α_9 = f−e, α_10 = ᾱ_8+2e′, α_11 = e+f+α_1−e′, α_12 = 2e−2e′+ᾱ_8−ᾱ_1 | 11 |
| (4.3.7) | 21–22 | 8 | e′+f′+ᾱ_8 | only in the figure; the text gives the basis e, f, α_1 … α_7, −f′+ᾱ_8 of v^⊥/ℤv and the span ℤ{α_1 … α_7, α_8−f′, e+f, e−f} | **stops** |
| (4.3.9) | 23–24 | 12 | 2e+2f+ᾱ_1 | the basis prints; the six vectors α_9 … α_14 of the figure do not survive the scan | **stops** |

The counts agree with the consumer's: sage-extensions#297 states that Sterk publishes the diagrams of
the polarized cusps j = 2, …, 5 with 10, 12, 11 and 14 walls, and the four statements print 12, 10, 11
and 14 walls in this order. The 14 is (4.3.9), the row that does not land.

For (4.3.8) the text layer and the OCR disagree twice, and orthogonality to the cusp decides both:
α_9 is f − e (not f′ − e′, which is not orthogonal to 2e′+f′+ᾱ_1), and α_10 is ᾱ_8 + 2e′ (not
ᾱ_3 + 2e′: (ᾱ_3, ᾱ_1) = −14 ≠ −4). The last wall is α_12 = 2e − 2e′ + ᾱ_8 − ᾱ_1, which both readings
degrade ("ᾱ_8 − ᾱ_12" in the OCR, "α_5 − ᾱ_8" in the text layer) and which is the only combination of
those letters that is orthogonal to the cusp with a negative square.

## What is stored and what was computed

`integral.cusp_chambers['gamma-en-2']` on the card of 029J holds the three rows above with the cusp,
the walls (each with the source's name and its coordinates in the card's basis), the statement, page
and figure, and then the wall count, the Gram matrix b(w_i, w_j) and the Coxeter diagram, which
`results/transcribe-33-sterk-cusps.py` computed from the card's Gram tensor. The certificate is

    029J integral.cusp_chambers
    hash f546443699b5c3b377638ac85f9fe41ff4159cf9e1aba0762882909ad1a1db94

with the citation of the statements and the computing program as its provenance. No Vinberg search was
run for any row: the walls are the source's, and the three invariants are the card's form on them.

Checks the script asserts for every row, and that `tests/test_model.py` re-runs from the card alone:
the cusp is primitive isotropic; every wall is orthogonal to the cusp and has negative square; the
walls span v^⊥/ℤv over ℚ (rank 10 of 12); the stored Gram matrix is b on those vectors; and every
non-orthogonal pair has |g_ij| = cos(π/m) for m ∈ {3, 4, 6} or |g_ij| = 1.

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
cusp" and the page of 029J shows the three statements — and its internal-link check passes for both new
links (`../theory/orbits.html#chamber-at-a-cusp` from the card and `../tag/029J.html#cusp-chambers` from
the arithmetic-group card); it fails only on `theory/roots.html`, which links to tags the copy does not
hold.
