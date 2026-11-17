# #7: the two arithmetic-group indices, and what a generating set would cost

## The index is the order of the finite orthogonal group of the discriminant form

$A_{T_{\mathrm{Co}}} = T_{\mathrm{Co}}^*/T_{\mathrm{Co}}$ is $(\mathbb{Z}/2)^{11}$, order $2048$, and
$\varphi\colon O(T_{\mathrm{Co}})\to O(A_{T_{\mathrm{Co}}},q)$ is onto (`discriminant_representation_is_surjective`
answers `True` in 26.0 s). So the kernel's index is the image's order, computed by the owner from the
finite group and not from the coset space:

    L.discriminant_group().orthogonal_group().cardinality()   46998591897600   1.3 s   392 MiB
    L.stable_orthogonal_group().finite_character_quotient().index()
                                                              46998591897600   0.1 s

Two independent owner computations agree, so the value on the card is not a transcription of one call.

## The spinor kernel's index is twice that

For $\widetilde O^{+}(T_{\mathrm{Co}}) = \ker(\varphi,\mathrm{sn}_{\mathbb R})$ the character image has order
$2|O(A_{T_{\mathrm{Co}}},q)|$: the sign is realized on the discriminant kernel, so
$[\widetilde O:\widetilde O^{+}] = 2$ and $[O:\widetilde O^{+}] = 93997183795200$.

    intersection.finite_character_quotient().image_order()      93997183795200   4.1 s
    intersection.finite_character_quotient().subgroup_image_order()             1   10.6 s
    intersection.finite_character_quotient().index()            93997183795200   0.9 s

## What ran

`latticedb certify --tag 6JRR --minutes 15 --workers 1 --phase fields` for the two computations, in the
pinned image with sage-extensions `ba51bdf9` (origin/main) and this repository's `src` on `PYTHONPATH`:

    6JRR {'arithmetic-group.otilde-t-co.index_in_orthogonal_group': 46998591897600}
    6JRR {'arithmetic-group.otilde-plus-t-co.index_in_orthogonal_group': 93997183795200}
    65 s wall, 0.6 GiB

The previous routes for the same two computations, from `exceeded.yaml`, are the evidence that the fix is
the route and not the machine: the index of $\widetilde O$ ran 5609 s and was killed at
14,061,043,712 bytes, and the index of $\widetilde O^{+}$ ran 7286 s, then 10,921 s and 12,723 s on later
scheduled runs, each time with its worker lost.

`checks.records.problems(corpus.cards(root, ("6JRR",)), certificates.load(root, ("6JRR",)), {"6JRR"})`
reports 0 problems on the two cards and their two citations.

## The generating sets: none, and why

Both cards state no `data.generator_morphisms`, and neither computation has a completed certificate.

* `L.stable_orthogonal_group_generators()` raises for this lattice. Its statement is Allcock's
  Bertini-involution generation of $W_{237}(2)$ for $\Lambda(2) = E_{10}(2)$ — rank 10, signature $(1,9)$,
  $|A_L| = 1024$, card `0125` — and the call asserts that hypothesis:

      AssertionError: the Bertini-involution generation statement covers only L = Lambda(2) ... but
      Integral lattice of rank 11 and signature (2, 9) has rank 11, ... and |A_L| = 2048

* The generic route, `L.stable_orthogonal_group().group_generators()`, is the Schreier family of a
  transversal of the finite image: one isometry of $T_{\mathrm{Co}}$ per coset of $O(A_L,q)$, of which
  there are 46,998,591,897,600, times the 126 generators of $O(T_{\mathrm{Co}})$ the card certifies. The
  2026-11-17 run spent 4782 s and reached 14,382,555,136 bytes before the run killed it for memory
  (`exceeded.yaml`, `6JRR arithmetic-group.otilde-t-co.generator_morphisms`). A fresh probe on today's
  source (`ba51bdf9`, origin/main) under a 6 GiB address-space cap ran the same call for 1800 s without
  returning and was ended by its own timeout (exit 124), so a stale image is not what produced the cost.

A generating set of $\widetilde O(T_{\mathrm{Co}})$ therefore needs either a published finite one — the
Bertini-involution statement is the nearest, and it covers $\Lambda(2)$ only — or an owner operation that
avoids the transversal (a presentation of $O(T_{\mathrm{Co}})$ and lifts of its relators, or a kernel
generating family as in sage-extensions#591). The database records the absence and claims nothing.

## What the two certificates state

`certificates/e1.yaml` holds, and the card of `6JRR` cites,

    6JRR arithmetic-group.otilde-t-co.index_in_orthogonal_group        682c595c52447cd1add71138601fe9259fd3e5e868e05a646a95e0b27c3225f1
    6JRR arithmetic-group.otilde-plus-t-co.index_in_orthogonal_group   326145ccf46247778eb506416cb6c6985eedf61029060ff4497597e2c3f8a3b0
    by: research preamble

Each hash commits to the computation name, the Gram tensor of `6JRR` and the stored integer. Nothing in
either certificate states that a set of isometries generates a group, because no such set is stored.

## Remaining gap, not this item

A card whose `standard_name` is `O` — `co-0`, `o-t-en`, `o-u2-e8` — still has no computable index:
`_standard_subgroup` returns `L.Aut()`, the isometry Mor, which presents no `index`, and the fallback
raises `AttributeError`. That is unchanged by this commit and is not one of the two fields #7 asks for.
