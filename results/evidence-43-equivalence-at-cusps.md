# #43: what sage-extensions#312's closure does and does not settle at the three cusped rows

The closure is real and it is where the brief says: at sage-extensions `main` (`7753092`) a subgroup
`\Gamma \leq O(L)` cut out by a condition on `A_L` has `isotropic_vector_reduction_image` and, with it,
**exact vector equivalence** — `predicate_subgroups.vectors_are_equivalent`, `vector_equivalence_witness`, whose
`_subgroup_vector_equivalence_witness` (`orthogonal_quotients.py:3396`) walks the finite discriminant quotient, so
`None` is a decision and not a failure to find.

Measured this turn, in the pinned image with that clone bound over `/repos/sage-extensions`:

- the *image object* at a primitive isotropic line is unchanged: `generation_obstruction()` still returns "the
  parabolic at the line … has no constructed generator family" (`isotropic_orbits.py:3785`, and
  `parabolic_generators` still delegates to a family stated for a plane and refusing rank one), and
  `root_class_orbits` at card 029J's fourth cusp still returns **2 components of sizes [1, 1]** (75.7 s).
- the exact equivalence on the *predicate subgroup* is what is new, and it is what the rows need, because a class of
  a root `r` is carried to a class of `r'` by an element of `Stab_\Gamma(v)` exactly when that element carries the
  rank-two degenerate lattice `ZZ v + ZZ r` onto `ZZ v + ZZ r'` — its radical `ZZ v` is characteristic, so
  `r` goes to `r' + t v` for one integer `t`. `results/probe-43-equivalence-at-cusps.py` therefore asks
  `vector_equivalence_witness(r, r' + t v)` for `t` in a window and checks the witness it gets: that it fixes the
  cusp line and carries `r` to the candidate.

**Measured, and the answer is a non-return.** One such call at (4.3.8), for the pair `\alpha_9`, `\alpha_{11}` and
`t = 0`, was killed at its eighteen-minute-twenty-second limit with **no result**; the coset walk of the closed
operation does not reach an answer at a cusp of `T_{En}` in this image inside any budget a card can wait for. So no
verdict is stated here for (4.3.7), (4.3.8) or (4.3.9), and nothing is written to the card.

A second route was attempted and also produced no result: walking the union of the two constructible families -- the
owner's 25 stabilizer generators at (4.3.7), collected in 110 s, and the reflections in all of that chamber's walls --
on `K_J` in its own integer coordinates. It stopped on the reduction object's API (`reduction.coordinates` does not
exist on the reduction this owner returns), so the union was never walked; that is an unfinished probe and not a
negative result, and no conclusion is drawn from it.

What is already proved about those three rows, and does not depend on this call:

- every root class of a row is `O(K_J)`-equivalent to every other (`results/evidence-43-okj-complement.md`), so the
  count lies between 1 and the number of classes;
- the reflections in the chamber's own walls, the only part of the stabilizer the card constructs, put every class in
  an orbit of its own — different orthogonal neighbour sets, pairwise, at every cusped row
  (`results/evidence-43-wv-orbits.md`).

So the three rows are decided by one question, `is [r_i] = [r_j]`, and the owner now has an exact test for it. What
remains is whether that test returns inside a usable time at these cusps.

## Why the call does not return: the route it is on

Asked of the subgroup itself (a 3-second call, no isometry work), $\Gamma_{\mathrm{En},2}$ is
`PreimageSubgroups.parent_class` with

```
contains_character_kernel True
character_data_is_complete True
has_finite_coset_space     True
index                      67456
```

so `_subgroup_vector_equivalence_witness` takes its **second** route (`orthogonal_quotients.py:3403`–`:3423`): "the
witnesses of `left |-> right` inside the supergroup form the coset of the supergroup's stabilizer of `right`, and that
coset is walked through the images in the finite quotient". The supergroup is $O(T_{\mathrm{En}})$ and the stabilizer of
a root in it is infinite, so the coset that gets walked is infinite; the finite quotient bounds the *images*, not the
walk. That is the mechanism behind the eighteen-minute non-return, and it is the thing an orbit computation would have
to replace with a double-coset computation on the finite quotient — what `isotropic_plane_orbits` already does for
planes (`predicate_subgroups.py:645`–`:700`, step 3 there).

So the rows (4.3.7)--(4.3.9) are blocked on that algorithm, not on this card's data: `K_J`, its root classes and the
conflations are all computed and recorded above.

## The call that does not exist, with the expressions it fails at

The closed operation supplies two cheap parts, both measured this turn
(`results/probe-43-transporter-supergroup.py`, pinned image, owner `main` `7753092`):

- `supergroup.vector_equivalence_witness(r, r')` — the ambient witness — returned in **under 15 s**;
- `supergroup.vector_equivalence_witness(w(v), v)` — a witness carrying the image cusp back — in **2.5 s**, and the
  composite fixes the cusp exactly (`candidate(cusp) == cusp` is `True`).

What does not exist is the class-level step. The three expressions that would carry it, and what each does:

1. `image.contains(candidate)` raises
   `ValueError: cannot decide membership of Morphism from Integral lattice of rank 12 … in the image of the stabilizer
   at 2*e_2 + e_3 - 4*e_4 - … : it is not an isometry of the reduction Integral lattice of rank 10 and signature (1, 9)`
   at `sage_extensions/categories/isotropic_orbits.py:3111`: membership needs the *reduced* isometry, and nothing
   returns that reduction for a transporter built outside the image.
2. `image.root_class_orbits(roots, stabilizer_generators=stabilizer)` returns **2 components of sizes [1, 1]** at
   (4.3.8), because `image.generators()` is empty at a line — `generation_obstruction()` at
   `isotropic_orbits.py:3785`, whose `parabolic_generators` still delegates to a family "stated for a primitive
   isotropic plane and refuses rank one".
3. `gamma.vector_equivalence_witness(r, r' + t v)` — the ambient predicate route — does not return (killed at
   18 min 20 s), because with complete character data it walks the coset of an infinite stabilizer
   (`orthogonal_quotients.py:3403`-`:3423`).

**The missing call, named:** `IsotropicVectorReductionImage.vectors_are_equivalent(left, right)` — an exact decision for
two *classes* of `K_J = v^\perp/\mathbb{Z}v`, returning a witness in `G_v` or a proof that none exists. The owner has the
exact membership test and the exact ambient equivalence; nothing joins them at the quotient. With it the three rows
would be one call each; without it the counts stay between 1 and the number of classes, as the two proved bounds above
say.

## The seeded walk, with membership used correctly

`image.contains(image.reduction_image(g), lift=g)` — membership on the reduced isometry with its lift — is the call
that works, and it is what the earlier refusals at `isotropic_orbits.py:3111` were missing. With it,
`results/probe-43-seeded-transporter.py` at (4.3.8) kept **14 maps**: one seed from the supergroup (a witness
`r -> r'` composed with one carrying the image cusp back, both found in under 40 s) and 13 of the stabilizer's own
generators.

Walking the images of the first root class through those maps, breadth first on classes:

| depth | ball | transporter to the second class |
| --- | --- | --- |
| 1 | 8 | none |
| 2 | 64 | none |
| 3 | 545 | none |
| 4 | 4956 | none |

So the seeded family does not carry one class to the other either; and since the exact equivalence does not return,
neither the constructive nor the decision route closes the row. What would: a call that decides two *classes* of
$K_J$ — `IsotropicVectorReductionImage.vectors_are_equivalent`, named above — or, equivalently, the double-coset orbit
computation at the finite quotient that `isotropic_plane_orbits` already performs for planes.

## The owner's record of it: sage-extensions#72, open

The search for an open issue naming this operation returns one, open and unassigned:
**dzackgarza/sage-extensions#72**, "Preamble lattice capabilities: explicit defects, disabled computations, and domain
restrictions". Its inventory contains the line that is this file's subject:

> **Indefinite vector-equivalence entry point disabled** | Distinct vectors of equal norm in an indefinite lattice |
> `vector_equivalence_witness` and therefore `vectors_are_equivalent` call the disabled marked-isometry entry point.

with its source evidence given there as `src/dzack_research/preamble/categories/lattice_morphisms.py:2980`
(the vector-equivalence dispatch), the disabled port entry points in
`sage-indefinite-port/src/sage_indefinite_port/indefinite/marked_lattices.py:64`, and the decorator that rejects them
in `readiness.py:22`.

So the 18 min 20 s non-return is not a slow computation: the entry point the ambient route reaches is **disabled**
upstream, and that is why (4.3.7), (4.3.8) and (4.3.9) cannot be decided here. The row's own acceptance says such an
obligation "remain[s] open until their owning implementation supplies the stated result" — which is sage-extensions#72,
not this card.
