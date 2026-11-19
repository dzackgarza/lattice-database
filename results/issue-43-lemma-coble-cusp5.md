# #43, one lemma: the Coble cusp of three classes is two orbits

**Lemma.** At Sterk's `(4.3.9)` the Coble cusp stabilizer acts on the three root classes with exactly two orbits,
$\{\alpha_{12}\}$ and $\{\alpha_{13},\alpha_{14}\}$. The row is stored on card 6JRR under `gamma-co-2` with
`orbit_count: 2`.

**Proof.** Three printed steps and one computation.

1. `(4.3.3)`, p. 18: the acting group is read as $G = W(G) \rtimes S$, "the group $S$ … identified with a subgroup of
   the symmetry group of $\Sigma(G)$" — the reflection subgroup together with the diagram symmetries that are realised
   in $G$. This is the shape of Sterk's whole method in §4.3, and the one he states as $G_v = \{\pm1\}W_v \rtimes
   \mathbb{Z}/2$ at `(4.3.7)`, p. 22.
2. `(4.3.9)`, p. 24: "Symmetries of the graph can be lifted to $\Gamma_v$" — every symmetry of this chamber's diagram
   is realised, so $G_v = W_v \rtimes S$ with $S$ the eight symmetries; `(4.3.10)`–`(4.3.12)`, p. 25, is the
   realisation.
3. *The Coble subgroup is decided on $S$.* Every reflection in a wall of $T_{\mathrm{Co}} = \delta^\perp$ fixes
   $\delta = e - f$ (`results/issue-43-lemma-reflections-fix-delta.md`). So for $g = w s$ with $w \in W_v$,
   $g(\delta) = w(s(\delta))$, and since $w$ fixes $\delta$, $g(\delta) = \pm\delta$ exactly when $s(\delta) =
   \pm\delta$. The $\delta$-preserving part of $G_v$ is therefore $\langle W_v, S_\delta\rangle$ — no product of
   non-preserving symmetries can sneak in, because the $W_v$-part cannot move $\delta$ back.
4. Computed from card 029J's Gram tensor: exactly two of the eight symmetries carry $\delta$ to $\pm\delta$ — the
   identity and the one exchanging $\alpha_{13}$ with $\alpha_{14}$ and fixing $\alpha_{11}$, $\alpha_{12}$
   (`results/issue-43-lemma-coble-image.md`, and pinned in the suite by
   `tests/test_cusp_root_orbits.py::test_only_one_delta_preserving_symmetry_moves_a_coble_class`).

So the Coble image is $\langle W_v,\sigma\rangle$; $W_v$ fixes every class (the root walls have pairwise different
orthogonal neighbour sets), $\sigma$ exchanges $\alpha_{13}$ and $\alpha_{14}$ and fixes $\alpha_{12}$. Two orbits.
$\square$

**What changed from the earlier conditional.** The previous turn recorded this as conditional because $G_v$'s shape is
not printed at `(4.3.9)`. The missing step is supplied by step 3: the condition $\delta \mapsto \pm\delta$ is decided on
the finite symmetry group alone, because the reflection part *cannot* move $\delta$. That converts "the image might be
larger than $\langle W_v,\sigma\rangle$" into "any larger element would need a symmetry outside $S_\delta$, and there is
none".

**What is still not certified.** The count is a *proof from Sterk's algorithm plus a computation*, not a citation of a
printed count and not a run of the owner's group code: `_double_coset_adjustment` does not return at a Coble cusp
(`results/probe-43-coble-cusp5-equivalence.py`, 300 s and 1500 s). The certificate says exactly that, and names every
page it rests on.

**Sources by printed page.** H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*,
Math. Z. 207 (1991), 1–36: `(4.3.3)`, p. 18; `(4.3.7)`, p. 22; `(4.3.9)`, p. 24; `(4.3.10)` and `(4.3.12)`, p. 25.
