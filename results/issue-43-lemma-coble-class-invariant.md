# #43, one lemma: the class of $\delta$ in $K_I$ settles the 135-orbit $\Gamma_{\mathrm{Co},2}$-cusp

**Refuted (#49).** The step "every element of $W_v$ ... preserves the class there of any vector of $v^\perp$" is
false: fixing $v$ preserves $K_I$ as a whole, not each class. On card 029J the wall $\alpha_9$ of `(4.3.9)` has square
$-4$, pairs $0$ with the cusp and $-2$ with $\delta$, so its reflection, an element of $W_v$, sends $\delta$ to
$\delta - \alpha_9$, a different class. The row this lemma supported is withdrawn from card 6JRR.

**Lemma.** At Sterk's `(4.3.9)` the $\Gamma_{\mathrm{Co},2}$-cusp stabilizer acts on the three root classes with exactly two orbits,
$\{\alpha_{12}\}$ and $\{\alpha_{13},\alpha_{14}\}$.

**Proof.** Write $G_v = W_v \rtimes S$ — Sterk `(4.3.3)`, p. 18, for the shape, `(4.3.9)`, p. 24, that the symmetries of
this chamber lift, `(4.3.10)`–`(4.3.12)`, p. 25, for the realisation. Every element of $W_v$ fixes the cusp $v$, so it
acts on $K_I = v^\perp/\mathbb{Z}v$ and preserves the class there of any vector of $v^\perp$. Now $\delta = e - f$ is
orthogonal to $v$, so its class $[\delta] \in K_I$ is defined and nonzero.

Computed from card 029J's Gram tensor, of the eight diagram symmetries exactly two send $\delta$ to $\pm\delta$ — the
identity and the one exchanging $\alpha_{13}$ with $\alpha_{14}$ — and **the six others send it to a different class of
$K_I$**. Since the $W_v$-part preserves classes, no product $ws$ with $w \in W_v$ can carry $\delta$ to $\pm\delta$ unless
$s$ already does. The $\delta$-preserving part of $G_v$ is therefore exactly $\langle W_v, \sigma\rangle$.

On the classes: every reflection in a wall of $T_{\mathrm{Co}}$ fixes the cusp's root classes (the root walls have
pairwise different orthogonal neighbour sets, `results/issue-43-lemma-reflections-fix-delta.md`), and $\sigma$ exchanges
$\alpha_{13}$ with $\alpha_{14}$ while fixing $\alpha_{12}$. Two orbits. $\square$

**What this repairs.** The row was withdrawn because the earlier argument claimed $W_v$ fixes $\delta$, which is false —
only the eleven reflections in walls of $T_{\mathrm{Co}}$ do. The class of $\delta$ in $K_I$ is the invariant that
survives: the $W_v$-part cannot change it, so the six symmetries that move $\delta$ out of its class (up to sign) are
excluded even though they can be multiplied by reflections. The false step is replaced, not patched.

**What is still not claimed.** This is a proof from Sterk's algorithm plus a computation of one invariant, not a printed
count and not a run of the owner's group code, which does not return at a $\Gamma_{\mathrm{Co},2}$-cusp
(`results/probe-43-coble-cusp5-equivalence.py`, 300 s and 1500 s). The certificate says so.

**Sources by printed page.** H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*,
Math. Z. 207 (1991), 1–36: `(4.3.3)`, p. 18; `(4.3.9)`, p. 24; `(4.3.10)` and `(4.3.12)`, p. 25. The walls, the
pairings and the class computation are card 029J's.
