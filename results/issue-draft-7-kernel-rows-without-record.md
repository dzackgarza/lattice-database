# Draft issue: the four plane rows with no record

**Not filed.** This connection cannot create issues on `dzackgarza/lattice-database`; the text below is
the issue to file, and the card `lattices/6JRR.md` and `results/evidence-7-plane-rows.md` name it.

## What is missing

Four rows of `integral.primitive_orbits` on `lattices/6JRR.md` state no plane count, and
sage-extensions#286's records do not supply them: the record's groups are $O$, $\widetilde O$,
$\widetilde O^{+}$ and $\Gamma_{\mathrm{Co},2}$ (`results/issue286-acceptance-final.md`, item 1), so
the two sign subgroups and the two determinant-cutting kernel subgroups are outside it.

| row | subgroup | state |
| --- | --- | --- |
| `SO` | $\ker \det$ | **refused by the owner**: the parabolic route raises at `orthogonal_quotients.py:4237` because the subgroup cuts no discriminant condition, and the odd-stabilizer route that answers $O^{+}$ is guarded to the spinor kernel alone (`:4157`) |
| `SO+` | $\ker\det \cap \ker \mathrm{sn}_{\mathbb{R}}$ | **refused by the owner**, same guard, and it cuts both sign kernels |
| `SOtilde` | $K \cap SO(T_{\mathrm{Co}})$ | **reachable**: its finite character quotient builds (index 93997183795200, a determinant kernel only), so the parabolic walk is available; it needs machine time, not a repair |
| `SOtilde+` | $K \cap SO \cap O^{+}$ | **no route here**: its finite character quotient is killed on this host — 594 s alone in a fresh process, 676 s as the fourth quotient of one — and the parabolic route refuses it at `:4237` |

The value is not in doubt. `results/verify-7-plane-sign-witnesses.py` on the card's stored Gram
exhibits the three diagonal sign isometries that lie in $K$ and fix the standard plane, whose
$(\det, \mathrm{sn}_{\mathbb{R}})$ pairs generate $\{\pm 1\}^2$; with $O(T_{\mathrm{Co}})$ transitive
on the planes (this card's own `O` row is 1), the four kernel subgroups share one plane count, and it
is $189720$ — the count `results/issue286-the-stage-1-call.md:275` and `:285` and the theorem
`thm:coble-plane-orbit-counts` both give.

## What would close each

- `SOtilde`: one run of `certify --tag 6JRR --field 'primitive_orbits[SOtilde].planes' --phase fields`
  on a host with about 4 GiB free for ~40 minutes (the returning $O^{+}$ walk took 2000 s at a 3.3 GiB
  footprint). Every attempt on this VM has been ended at the run's 1676462899 B reserve floor with
  other projects holding the machine: 566 s at a 1.09 GiB worker peak.
- `SO` and `SO+`: the owner's one-guard repair — admit a single sign kernel to the odd-stabilizer route
  and take its witness from the determinant image, leaving `SO+` refused until the two-flip machinery
  exists. Filed in sage-extensions as `lattice-database results/issue-286-so-plane-row-refusal.md`.
- `SOtilde+`: a record of the row, or the same owner repair extended to two sign kernels.

## Why it is long tail and not an acceptance

The plane row of a kernel subgroup walks 189720 plane cusps: 1813–2171 s for the cusps, 6132–7973 s
for the incidence, at 3.3–3.5 GiB. A full-scale row is long tail and never an acceptance (AGENTS.md,
2026-11-19). #7's acceptance is satisfied for every row that a source or a computation has supplied,
and these two are the ones it has not.
