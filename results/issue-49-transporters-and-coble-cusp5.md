# #49: the transporter orders at Sterk's cusps, and the 135-orbit $\Gamma_{\mathrm{Co},2}$-cusp (chamber of Sterk (4.3.9))

Record: `results/probe-49-cusp-symmetries.py`, run output `results/probe-49-cusp-symmetries.log`, both on card 029J's
stored chambers (`integral.cusp_chambers['gamma-en-2']`). Writer: `results/store-49-transporters-and-coble-cusp5.py`.

## (a) Transporter orders

**Definition** (`RootClassOrbit.transporter_order`). The order of the permutation group that the chamber stabilizer
$S \le G_v$ induces on the orbit's root walls. $S$ embeds in the symmetry group of the Coxeter diagram with wall squares
kept, because the walls span $K_J \otimes \mathbb{Q}$.

**Computation.** For each chamber the Gram-preserving permutations of the walls were enumerated, and each was checked
to be an integral isometry of $K_J = v^\perp/\mathbb{Z}v$ (all are). Sterk states that they are realized in
$\Gamma_v$: (4.3.7), p. 22; (4.3.8), p. 23; (4.3.9), p. 24.

| cusp | symmetries | root walls | induced order |
| --- | --- | --- | --- |
| (4.3.6) | 1 | $\alpha_{10}$ | 1 |
| (4.3.7) | 2 | $\alpha_9, \alpha_{13}$ | 2 |
| (4.3.8) | 2 | $\alpha_9, \alpha_{11}$ | 2 |
| (4.3.9) | 8 | $\alpha_{11}, \ldots, \alpha_{14}$ | 8 |

At (4.3.9) the stored value 4 was wrong. The group is transitive on four walls and contains the symmetry that exchanges
$\alpha_{13}$ and $\alpha_{14}$ and fixes $\alpha_{11}$ and $\alpha_{12}$, so the group is not regular and its order is 8.

## (b) The 135-orbit $\Gamma_{\mathrm{Co},2}$-cusp (chamber of Sterk (4.3.9)): four orbits

$T_{\mathrm{Co}} = \delta^\perp$ with $\delta = e - f = -\alpha_{11}$, which is a wall of the chamber $C$.

1. Every $g \in G_v$ has the form $\pm w s$, with $w \in W_v$ and $s$ a diagram symmetry, because $w^{-1}g$ preserves $C$.
2. If $g(\delta) = \pm\delta$, then $s(\alpha_{11})$ is $W_v$-conjugate to $\pm\alpha_{11}$, so $s_{s(11)}$ is conjugate
   to $s_{11}$. Two simple reflections are conjugate only when an odd-labelled path joins them (Bourbaki, Lie IV §1,
   Ex. 3; Allcock, arXiv:1106.3822v2, the odd diagram of Thm. 4). $\alpha_{11}$ has only the edges of order 4 to
   $\alpha_9$ and $\alpha_{10}$, so $s(\alpha_{11}) = \alpha_{11}$. Of the 8 symmetries, only the identity and
   $\sigma$ ($\alpha_{13} \leftrightarrow \alpha_{14}$) do this.
3. $\mathrm{Stab}_{W_v}(\pm\alpha_{11}) = C_{W_v}(s_{11}) = \langle s_{11}\rangle \times W_\perp$. The free part is
   $\pi_1$ of the odd component of $\alpha_{11}$, which is a single vertex with no edge, so it is trivial (Allcock,
   arXiv:1106.3822v2, Theorem 5 and Corollary 6). $W_\perp$ has as Coxeter system the elements $r_u = (u s_{11})^{\lambda-1}u$
   for $u$ joined to $\alpha_{11}$ by an even edge $2\lambda$. Its simple roots are the 11 walls orthogonal to
   $\alpha_{11}$, together with $\beta_9 = \alpha_9 + \alpha_{11}$ and $\beta_{10} = \alpha_{10} + \alpha_{11}$, both of
   square $-2$.
4. $s_{11}$ is trivial on $\delta^\perp$. Every root of $K_I$ is $W_\perp$-conjugate to a simple root, and two simple
   roots are conjugate only by an odd path. The five root walls $\beta_9, \beta_{10}, \alpha_{12}, \alpha_{13}, \alpha_{14}$
   have no odd edge between them (the log prints the diagram). So there are five $W_\perp$-classes, and $\sigma$ joins
   $\alpha_{13}$ and $\alpha_{14}$.

The count is **4**: $\{\beta_9\}$, $\{\beta_{10}\}$, $\{\alpha_{12}\}$, $\{\alpha_{13}, \alpha_{14}\}$. The lower bound
($\ge 4$; it would be 5 without $\sigma$) uses only steps 1–4. The identification of $\alpha_{13}$ with $\alpha_{14}$
uses Sterk's lifting of $\sigma$, (4.3.9), p. 24.

The earlier framing "three classes, count in $\{1,2,3\}$" omitted $\beta_9$ and $\beta_{10}$. These are roots of
$K_I$ and walls of the chamber of $W_\perp$, which is the face $C \cap \delta^\perp$.

Not checked here: printed page numbers for Allcock. The arXiv v2 statements were read online. Bourbaki's exercise was
not read at its page.
