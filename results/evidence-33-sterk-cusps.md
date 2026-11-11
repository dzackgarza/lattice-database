# #33: what Sterk's five statements print, and why each chamber row stops

Source: H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207
(1991), read as text (`tmp/sterk-1991-part-i.md`, pages from the PDF text layer). Route 1: a row is a
computation over the vectors the statement prints, certified by the repository's mechanism.

The lattice is $L_- = H \oplus E_8(-2)$; the walls of the chamber at the cusp $v$ are the vectors the
statement prints, in Sterk's basis, with his conventions: in (4.3.6) "$\\circ$: $(-4)$-vector,
$\\bullet$: $(-2)$-vector", and in (4.3.5) "$\\{(\bar\alpha_i,\alpha_i)\} = 2$, because we are working in
$E_8(-2)$".

| statement | printed page | cusp $v$ | figure | what the statement prints |
| --- | --- | --- | --- | --- |
| (4.3.5) | 19 | $e$ | Fig. 4 | $M(2)$ projects onto $e^\perp/\mathbb{Z}e$; the four extra walls $\\alpha_9 = f'-e'$, $\\alpha_{10} = \\bar\\alpha_9 + 2e'$, $\\alpha_{11} = 2e'+2f'+\\bar\\alpha_1+\\bar\\alpha_9$, $\\alpha_{12} = 5e'+3f'+2\\bar\\alpha_2$; the $\\alpha_1,\\dots,\\alpha_8$ of $E_8(-2)$ are named, not reprinted |
| (4.3.6) | 21 | $e'$ | Fig. 6 | $G_{e'} = O(H\oplus E_8(-2))$; extra walls $\\alpha_9 = \\bar\\alpha_9 + 2f$, $\\alpha_{10} = e-f$ |
| (4.3.7) | 21–22 | $e'+f'+\\bar\\alpha_8$ | Fig. 8 | a basis of $v^\\perp/\\mathbb{Z}v$: $e, f, \\alpha_1,\\dots,\\alpha_7, -f'+\\alpha_8$; its extra walls up to $\\alpha_9$ |
| (4.3.8) | 23 | $2e'+f'+\\bar\\alpha_1$ | Fig. 10 | a basis: $e, f, -e'+\\alpha_1, \\alpha_2,\\dots,\\alpha_8$ |
| (4.3.9) | 23 | $2e+2f+\\bar\\alpha_1$ | Fig. 10 area | a basis: $\\tilde e, \\tilde f, \\tilde\\alpha_1,\\dots,\\tilde\\alpha_8$ |

## Why no row lands

A row's wall set must be *complete* for its Gram matrix to be the chamber's and its vertex count to be
the number of walls. Each statement prints the walls that augment the obvious $E_8(-2)$ (or $H$-summand)
basis — it does not print the whole set: the $H$-summand walls of (4.3.5)–(4.3.9) are never given as
vectors, and the $\\alpha_1,\\dots,\\alpha_8$ are named rather than written in the coordinates of $L_-$.
Completeness is visible only in Figs. 4, 6, 8 and 10, which the text layer holds as images.

So each of the five rows **stops**, and for the same reason:

- (4.3.5) $e$, p. 19 — stops: the $H(2)$-summand walls are not printed; $\\alpha_1,\\dots,\\alpha_8$ are named only.
- (4.3.6) $e'$, p. 21 — stops: same, the $H$-summand walls are not printed.
- (4.3.7) $e'+f'+\\bar\\alpha_8$, p. 21–22 — stops: same.
- (4.3.8) $2e'+f'+\\bar\\alpha_1$, p. 23 — stops: same.
- (4.3.9) $2e+2f+\\bar\\alpha_1$, p. 23 — stops: same.

No Vinberg search is run to fill them: sage-extensions#297 is tested against these rows, so a chamber
computed here rather than read from the statement would make that test circular. No `theory/` field is
added, because a field with no certifiable row is not a schema the repository can use; the design is
stated above for when the vectors exist.

What would unblock each row: the wall vectors in the coordinates of $L_-$ for that statement — either
from Sterk's own list (if Part I prints them elsewhere, e.g. in §2 for $E_8(-2)$ and for $H$), or from
the owner's construction of the same chamber, cited as such.
