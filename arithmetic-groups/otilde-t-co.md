---
slug: otilde-t-co
name: Otilde(T_Co)
latex: \widetilde O(T_{\mathrm{Co}})
lattice: 6JRR
ambient_lie_group: o-2-9
standard_name: Otilde
data:
  abstract_structure: the kernel of O(T_Co) -> O(A_T_Co)
  cardinality: aleph0
  index_in_orthogonal_group: 46998591897600
---

The discriminant kernel of $O(T_{\mathrm{Co}})$, the kernel of the reduction $\varphi \colon O(L) \to O(A_L)$ of Dolgachev–Kondo, Section 2, (2.1), p. 510, written $\widetilde O(L) = O(L)^{*}$ there; it is a subgroup of $O(L_{\mathbb{R}}) \cong O(2, 9)$ and is countably infinite, being an infinite subgroup of finite index.

`latticedb certify` asks the preamble for its index in $O(T_{\mathrm{Co}})$, the cardinality of $O(L)/\widetilde O(L)$, which is $|O(A_{T_{\mathrm{Co}}}, q)|$, and for the isometries of $T_{\mathrm{Co}}$ that generate it, at `L.stable_orthogonal_group()`.
The index is stored as `data.index_in_orthogonal_group` and the generators as `data.generator_morphisms`; each generator is one `morphisms` entry of the card of [6JRR](../tag/6JRR.html) with `scale: 1`, stored once, and the two values are certified on that card under `arithmetic-group.otilde-t-co.index_in_orthogonal_group` and `arithmetic-group.otilde-t-co.generator_morphisms`.
The index the computation returned is $46998591897600 = |O(A_{T_{\mathrm{Co}}}, q)|$, the order of the finite orthogonal group of the discriminant form — the finite image of $\varphi$ — read from that finite group rather than from its coset space, whose cardinality is the same number.
No generating set has been returned, so `data.generator_morphisms` is absent and this card claims none; the generation clause of #7 is recorded as **not supplied**, and sage-extensions#597 is where the reason is proved rather than asserted.
The refusal is not a limit of the machine. $\widetilde O(T_{\mathrm{Co}})$ is the principal congruence subgroup of level $2$: $T_{\mathrm{Co}} = 2\cdot(\langle 1 \rangle \oplus II_{1,9})$, so $L = 2L^{*}$ and $x \mapsto x/2$ is an $O(L)$-equivariant bijection $L/2L \to A_L$. Every published generation statement fails a hypothesis here, and the deciding one is $\mathrm{rank}_2(T_{\mathrm{Co}}) = 0$: Kneser's theorem needs $\mathrm{rank}_2 \ge 6$, Gritsenko–Hulek–Sankaran's Proposition 3.4 needs two hyperbolic planes, and Allcock's Bertini-involution family is stated for $\Lambda(2)$ of rank $10$ — card [0125](../tag/0125.html) — which is not this rank-eleven lattice; the owner's `stable_orthogonal_group_generators` therefore refuses with the failing hypothesis and its value named, instead of asserting a card identity.
The only route left is the Schreier family over a transversal of the finite image: $46998591897600$ cosets, since $\varphi$ is onto and $|O(A_{T_{\mathrm{Co}}}, q)| = 46998591897600$. `group_generators()` on this subgroup reaches that transversal and did not return in $600$ s, peaking at $4607$ MiB and still rising, ended by its own timeout (exit $124$); the earlier whole-job attempt spent $4782$ s and $14.4$ GB before its runner killed it. An index is a finite computation and the one above is certified; a generating family of the kernel is not, so none is stored.
