# #43, one lemma: the group Sterk calls $\Gamma$ is the corpus's $\Gamma_{\mathrm{En},2}$

**Why this needed settling.** The rows of `integral.cusp_root_orbits` on card 029J are keyed to `gamma-en-2` and cite
Sterk's "$\Gamma_v$" — the stabilizer of the cusp in *his* group $\Gamma$. If his $\Gamma$ were larger than the corpus's
$\Gamma_{\mathrm{En},2}$, those citations would establish an orbit count for a group larger than the key names, and the
three rows at `(4.3.7)`–`(4.3.9)` would rest on a weaker statement than their key. They do not: the two groups are the
same, and the identity is printed.

**Lemma.** Sterk's $\Gamma$ in §2 is the group the corpus records as $\Gamma_{\mathrm{En},2}$ — the image of
$\{g \in O(L) : g\circ I = I\circ g,\ g(e+f, e+f, 0) = (e+f, e+f, 0)\}$ in $O(L_-)$ — and his $[O(L_-):\Gamma]$ is the
index $67456$ that card `gamma-en-2` states.

**Proof from the printed page.** §2, p. 7, defines the group: "divide out by the group $F$, where $F$ is the image of
$\{g \in O(L) : g \circ I = I \circ g,\ g(e+f, e+f, 0) = (e+f, e+f, 0)\}$ in $O(L_-)$", and `(2.7)`, pp. 6–7, identifies
it with the isometries of $L_-$ whose induced map on $L_-^*/L_-$ respects the two-summand decomposition. `Remark 2.12`,
p. 8, then computes its index:

$$[O(L_-):F] = \frac{2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31}{2\cdot2^{13}\cdot3^5\cdot5^2\cdot7} = 2^7\cdot17\cdot31 = 67456 .$$

Card `arithmetic-groups/gamma-en-2.md:13` states `data.index_in_orthogonal_group: 67456` and cites exactly that remark
for it, and `:4` gives the symbol $\Gamma_{\mathrm{En},2}$; its `abstract_structure` is "the image in $O(T_{En})$ of the
isometries of the K3 lattice that commute with $I_{En}$ and fix $h$" — Sterk's $F$, word for word. Two groups with the
same generators, the same lattice and the same index in $O(T_{\mathrm{En}})$ are the same group.

**Consequence for the stored rows.** Sterk's "the symmetry of the diagram comes from an element in $\Gamma_v$"
`(4.3.7)`, p. 22, "the symmetry is induced by an element of $\Gamma_v$" `(4.3.8)`, p. 23, and "Symmetries of the graph
can be lifted to $\Gamma_v$" `(4.3.9)`, p. 24, are statements about the corpus's `gamma-en-2` cusp stabilizer. The three
rows at `lattices/029J.md:504`, `:514`, `:524` are therefore cited for the group they are keyed to, and the certificate
`029J integral.cusp_root_orbits` (`certificates/70.yaml:87`) says so correctly.

**What it does not rescue.** The same identity is why the Coble side cannot borrow the argument: $T_{\mathrm{Co}}$ is a
different lattice, its cusps are stabilized by $R_{\Gamma_{\mathrm{En},2}}$, and no printed sentence of Sterk's §4 is
about that restriction — which is what `results/issue-43-lemma-gv-not-stated.md` records from the other side.

**Sources by printed page.** H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*,
Math. Z. 207 (1991), 1–36: §2, p. 7, for the definition of $F$; `(2.7)`, pp. 6–7, for the discriminant description;
`Remark 2.12`, p. 8, for the index $67456$; `(4.3.7)`, p. 22, `(4.3.8)`, p. 23, `(4.3.9)`, p. 24 for the cusp
stabilizers. V. Alexeev, P. Engel, D. Z. Garza, L. Schaffler, *Compact moduli of Enriques surfaces of degree 2*,
Nagoya Math. J. 259 (2025), Definitions 2.6 and 2.7, for the same group on the moduli side.
