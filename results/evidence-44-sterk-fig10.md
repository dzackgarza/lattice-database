# #44: Sterk's Fig. 10 roots belong to 2e' + f' + bar_alpha_1, and the card already stores that vector

Read from the PDF text layer of `tmp/sterk-1991-part-i.pdf` (`pdftotext -layout`), whose reading of
Fig. 10 agrees with the OCR in `tmp/sterk-1991-part-i.md`.

## The definitions, with pages

- Sterk works in $L_- = H \oplus H(2) \oplus E_8(-2)$, and (4.2.2)-(4.2.3), **p. 16**, lists the five
  cusps by the primitive isotropic vectors $e$, $e'$, $e' + f' + \omega$, $e' + 2f' + \alpha$,
  $2e + 2f + \alpha$ ($\omega^2 = -4$, $\alpha^2 = -8$).
- His own note in (4.3.5), **p. 19** — " $(\bar\alpha_i, \alpha_i) = 2$, because we are working in
  $E_8(-2)$ " — fixes $\bar\alpha_i$: $(\bar\alpha_i, \alpha_j) = 2\delta_{ij}$, i.e.
  $\bar\alpha_i = -\sum_j (C^{-1})_{ij}\alpha_j$, with squares $-8, -16, -28, -60, -40, -24, -12, -4$.
  The $2\delta$ normalization is forced by his printed check of (4.3.5), $(\alpha_i, e'+f')^2/\lvert(\alpha_i,\alpha_i)\rvert
  = 4, 16, 64$: with $\delta_{ij}$ it would read $16$ for $\alpha_{10}$.
- (4.3.8), **p. 23**, sets $v = 2e' + f' + \bar\alpha_1$ and prints $e$, $f$, $-e' + \alpha_1$,
  $\alpha_2, \ldots, \alpha_8$ as a basis of $v^\perp/\mathbb{Z}v$; Fig. 10 prints the eleven walls
  $\alpha_2, \ldots, \alpha_8$, $\alpha_9 = f - e$, $\alpha_{10} = \bar\alpha_8 + 2e'$,
  $\alpha_{11} = e + f + \alpha_1 - e'$, $\alpha_{12} = 2e - 2e' + \bar\alpha_8 - \bar\alpha_1$, and the
  span $\mathbb{Z}\{e + f, e - f, -e' + \alpha_1, \alpha_2, \ldots, \alpha_8\}$.

In the card's basis ($e = e_1$, $f = e_2$, $e' = e_3$, $f' = e_4$, $\alpha_i = e_{i+4}$) that $v$ is

    2e' + f' + bar_alpha_1 = (0, 0, 2, 1, -4, -5, -7, -10, -8, -6, -4, -2),  v^2 = 0, primitive,

which is the vector the card's (4.3.8) row states.

## The two pairings, from the card's Gram tensor

| printed root | $(r, 2e' + f' + \bar\alpha_1)$ | $(r, e' + 2f' + \bar\alpha_1)$ |
| --- | --- | --- |
| $\alpha_2, \ldots, \alpha_8$ (each, square $-4$) | 0 | 0 |
| $\alpha_9 = f - e$ (square $-2$) | 0 | 0 |
| $\alpha_{10} = \bar\alpha_8 + 2e'$ (square $-4$) | 0 | 4 |
| $\alpha_{11} = e + f + \alpha_1 - e'$ (square $-2$) | 0 | $-2$ |
| $\alpha_{12} = 2e - 2e' + \bar\alpha_8 - \bar\alpha_1$ (square $-4$) | 0 | $-4$ |

$(2e' + f' + \bar\alpha_1, e' + 2f' + \bar\alpha_1) = 2$, so the two are different lines. The eleven
walls have rank 10 and together with $v$ rank 11: they span $v^\perp/\mathbb{Z}v$ and $v$ lies in their
span, as the row's own checks require. The paper's printed basis $e, f, -e' + \alpha_1, \alpha_2,
\ldots, \alpha_8$ pairs with $2e' + f' + \bar\alpha_1$ as all zeros and with $e' + 2f' + \bar\alpha_1$ as
$-2$ on $-e' + \alpha_1$. So Sterk's label, his printed basis and his printed roots agree, and the
statement is internally consistent.

The card's stored row is that transcription exactly: all eleven stored wall vectors equal the printed
formulas vector by vector, the stored `cusp` equals $2e' + f' + \bar\alpha_1$, and every stored wall is
orthogonal to it.

## Why the reading is not a choice

The scan does not resolve the subscript of the $\bar\alpha$ in its printed $\alpha_{10}$ and
$\alpha_{12}$, so every reading was tested: of the eight $\bar\alpha_i + 2e'$ for $\alpha_{10}$, only
$\bar\alpha_8$ keeps all eleven roots orthogonal to $v$ with squares in $\{-2, -4\}$ and their span in
the span the page prints; of the sixteen $\bar\alpha_8 \pm \bar\alpha_j$ for $\alpha_{12}$, six keep
those conditions, and only $\bar\alpha_8 - \bar\alpha_1$ gives the diagram Fig. 10 draws — the $E_7$ on
$\alpha_2, \ldots, \alpha_8$ with $\alpha_{10}$ and $\alpha_{12}$ at $\alpha_8$, $\alpha_{11}$ at
$\alpha_3$ of order 4 and $\alpha_9$ at $\alpha_{12}$ of order 4. The other five readings put
$\alpha_{12}$ on $\alpha_3$ or on $\alpha_4$–$\alpha_7$, which the figure does not.

## Where the issue's numbers come from

`sage-extensions` `Sterk.selected_isotropic_vectors()["Sterk_4"]` is
`c.lift(c(e' + 2f') + 2w1)` — (4.2.3)'s representative $e' + 2f' + \bar\alpha_1$, the *other* line —
and `Sterk.cusp_roots_in_TEn` carries Fig. 10's roots into $T_{\mathrm{En}}$ through an isometric
embedding of the index-two lattice they span, which is the paper's own statement in (4.3.10), p. 23
(the span is $\mathbb{Z}\{e - f, e + f\} \oplus E_8(-2)$). Pairings between roots carried over by that
embedding and the card's vector in the card's basis therefore compare two coordinate systems; they are
not a test of the card, and the nonzero list in #44 (whose first entry, $-6$ for $\alpha_2$, cannot
arise in the card's basis, where $(\alpha_2, \bar\alpha_1) = 0$) is that artifact.

## What changed

The `cusp` field needed no correction: it already holds the vector Fig. 10's eleven roots are
orthogonal to, with `statement: 4.3.8` and `printed_page: 23`. The card's prose now states both
vectors the paper prints, with their pages, the pairing between them, the pairings of the printed
roots against each, the basis check, and the subscript ambiguity above — so a reader can see why the
row holds the one it does. No card value, certificate or test changed.

Measured with `results/transcribe-33-sterk-cusps.py`'s conventions reproduced in a scratch script;
`just test`: 74 passed.
