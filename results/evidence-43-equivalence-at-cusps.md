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
