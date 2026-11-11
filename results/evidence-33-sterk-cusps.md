# #33: correction — four of the five statements do print their walls

**This file's earlier version was wrong.** It claimed that no statement prints its walls in the
coordinates of $L_-$. It is false for (4.3.5), (4.3.6), (4.3.8) and (4.3.9):

- $\alpha_1,\dots,\alpha_8$ are the simple roots of the $E_8$ diagram Sterk draws in §1–2 (his node
  numbering), in the summands of $M$; $\bar\alpha_i$ is the copy in the second summand. A wall written
  in $\alpha_i, \bar\alpha_i, e, f, e', f'$ is in the coordinates of $L_-$.

| statement | printed page | cusp $v$ | walls printed | figure | row |
| --- | --- | --- | --- | --- | --- |
| (4.3.5) | 19 | $e$ | $\bar\alpha_1,\dots,\bar\alpha_8$ (orthogonal to $x = e'+f'$), $\alpha_9$, then $\alpha_{10}, \alpha_{11}, \alpha_{12}$, checked by $(\alpha_i, e'+f')^2/\lvert\alpha_i^2\rvert = 4, 16, 64$ | Fig. 4 | to be entered |
| (4.3.6) | 21 | $e'$ | $\alpha_1,\dots,\alpha_8$ of the $E_8(-2)$ summand, $\alpha_9 = \bar\alpha_9 + 2f$, $\alpha_{10} = e-f$ | Fig. 6 | to be entered |
| (4.3.7) | 21–22 | $e'+f'+\bar\alpha_8$ | only Fig. 8 and the span of its roots | Fig. 8 | **stops** |
| (4.3.8) | 23 | $2e'+f'+\bar\alpha_1$ | $\alpha_9 = f-e$, $\alpha_{10} = \bar\alpha_3 + 2e'$, $\alpha_{11}, \alpha_{12}$ beside Fig. 10 | Fig. 10 | to be entered |
| (4.3.9) | 23–24 | $2e+2f+\bar\alpha_1$ | $\tilde e, \tilde f, \tilde\alpha_1,\dots,\tilde\alpha_8$, and $\alpha_9$–$\alpha_{14}$ beside Fig. 12 | Fig. 12 | to be entered |

Transcription rule: read the PDF text layer, not the OCR, where they differ (the OCR prints $\vartheta$
for 9 in several places).

A row's Gram matrix, Coxeter diagram and wall count are computed from the lattice's own form and
certified by the repository's mechanism; a row whose Gram matrix has a positive diagonal entry, or whose
walls do not span $v^\perp/\mathbb{Z}v$ over $\mathbb{Q}$, is a transcription defect to fix from the PDF.
