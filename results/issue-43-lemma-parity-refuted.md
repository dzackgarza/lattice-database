# #43, one lemma refuted: no congruence separates the Coble classes at (4.3.9)

**Claim to test.** Since $\Gamma_{\mathrm{En},2}$ is cut out by a congruence condition on the discriminant group, one
might hope that the classes at a cusp are separated by reduction modulo $2$: if $g r \equiv r \pmod{2L}$ for every
$g \in \Gamma_{\mathrm{En},2}$, then two classes whose difference is odd lie in different orbits, and the count at
(4.3.9) is decided.

**Refuted.** The premise fails, and the test proves nothing — it would contradict a row this card already states.

Computed from card 029J's Gram tensor, at `(4.3.9)`:

| difference | coordinates | even? |
| --- | --- | --- |
| $\alpha_{12} - \alpha_{11}$ | $(2,0,3,3,-2,1,2,2,1,0,0,0)$ | no |
| $\alpha_{13} - \alpha_{11}$ | $(2,0,3,4,-2,2,3,4,3,2,1,0)$ | no |
| $\alpha_{14} - \alpha_{11}$ | $(2,0,2,3,-2,0,1,0,0,0,0,0)$ | no |
| $\alpha_{13} - \alpha_{12}$ | $(0,0,0,1,0,1,1,2,2,2,1,0)$ | no |
| $\alpha_{14} - \alpha_{13}$ | $(0,0,-1,-1,0,-2,-2,-4,-3,-2,-1,0)$ | no |

Every difference is odd, including the three among $\alpha_{11},\alpha_{12},\alpha_{13},\alpha_{14}$ — and
`lattices/029J.md:524` states those four are **one** $\Gamma_{\mathrm{En},2}$-orbit. So
$\Gamma_{\mathrm{En},2}$ does not act trivially on $L/2L$, and "odd difference" carries no information. The same test
that would put $\alpha_{12}$ and $\alpha_{13}$ in different Coble orbits would also split the stored $T_{En}$ row, which
the chamber's symmetry forbids.

**What the refutation teaches.** The stored (4.3.9) row of 029J cannot rest on a congruence argument at all: it rests on
Sterk's `(4.3.9)`, p. 24, "Symmetries of the graph can be lifted to $\Gamma_v$", and $\Gamma_v$ there is the stabilizer
in $\Gamma$, not in $\Gamma_{\mathrm{En},2}$. So the row's key is a *statement about a subgroup larger than the key
names*, which is the same weakening the Coble side runs into and cannot use: for $T_{\mathrm{Co}}$ there is no printed
statement at all.

**Where that leaves the 135-orbit $\Gamma_{\mathrm{Co},2}$-cusp.** The count is $1$ or $2$ — $\alpha_{13}$ and $\alpha_{14}$ are joined by the symmetry fixed
in `results/issue-43-lemma-alpha13-alpha14.md`, and the question is whether $\alpha_{12}$ joins them. No congruence
separates them (this file), no diagram symmetry joins $\alpha_{12}$ to the others while fixing $\delta$ (that file), and
the owner's exact equivalence does not return at a $\Gamma_{\mathrm{Co},2}$-cusp
(`results/probe-43-coble-cusp5-equivalence.py`). What is left is a word in the group's generators, which is the walk the
earlier probes ran to depth four without a hit.

**Sources.** H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*, Math. Z. 207 (1991), 1–36,
`(4.3.9)`, p. 24, and `(4.3.10)`, p. 25, for the lattice the walls span; card `lattices/029J.md:524` for the stored row
the refutation is checked against.
