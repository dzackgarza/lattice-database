# Draft issue: the two kernel plane rows with no record

**Not filed.** This connection cannot create issues on `dzackgarza/lattice-database`; the text below is
the issue to file, and the card `lattices/6JRR.md` and `results/evidence-7-plane-rows.md` name it.

## What is missing

Two rows of `integral.primitive_orbits` on `lattices/6JRR.md` state no plane count: `SOtilde`
($K \cap SO(T_{\mathrm{Co}})$) and `SOtilde+` ($K \cap SO \cap O^{+}$). sage-extensions#286's records do not
supply them — the record's groups are $O$, $\widetilde O$, $\widetilde O^{+}$ and $\Gamma_{\mathrm{Co},2}$
(`results/issue286-acceptance-final.md`, item 1) — and the two sign subgroups `SO` and `SO+`, which are
equally outside that list, are now stored at 1 by the transport lemma
(`results/verify-7-plane-transport.py`), so what is left is the two kernel rows.

| row | subgroup | state |
| --- | --- | --- |
| `SOtilde` | $K \cap SO(T_{\mathrm{Co}})$ | **reachable**: its finite character quotient builds (index 93997183795200, a determinant kernel only), so the parabolic walk is available; it needs machine time, not a repair |
| `SOtilde+` | $K \cap SO \cap O^{+}$ | **no route here**: its character quotient is killed on this host — 594 s alone in a fresh process, 676 s as the fourth quotient of one — and the parabolic route refuses it at `orthogonal_quotients.py:4237` |

