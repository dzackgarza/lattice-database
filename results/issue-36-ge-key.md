# `integral.cusp_chambers` has no key for Sterk's `G_e` on card 0125

Filed against `dzackgarza/lattice-database` from #36. This connection's GitHub App has no write access
to issues, so the text is here and was not posted; open it with this body.

## What is missing

Card `0125` = `U(2) + E8(-2)` needs a row for a second chamber, and the field it belongs to has no key
for its group.

* Sterk, *Compactifications of the period space of Enriques surfaces, Part I*, Math. Z. 207 (1991),
  (4.3.5), p. 19, prints "the diagram of the reflection group `W_e ⊂ G_e`", where
  `G_e = {g ∈ O(M(2)) : the induced map on M(2)*/M(2) respects the decomposition}` is the image of the
  stabilizer `Γ_e` of the isotropic vector `e` in `O(M(2)) = O(U(2) + E8(-2))`. It is a proper
  finite-index subgroup of `O`, and the paper does not identify it with `O` as (4.3.6) does for the
  other card of the type.
* The chamber of `W_e` has twelve walls (Fig. 4, p. 19), and the paper prints its maximal parabolic
  subdiagrams only *modulo* the symmetries `S_e ≅ Z/2 × Z/2` (Fig. 5, p. 20): "we do not only find four
  equivalence classes in `I_1(e^⊥/Ze)`, but that we find four labelled classes". So the sourced object
  is "four orbits modulo `S_e`", which is neither the number of ideal vertices of that chamber nor a row
  of the card's `O` key, whose chamber is the ten-walled one of the whole reflection group.

## Why it cannot be stored today

`integral.cusp_chambers` is keyed by `Subgroup = OrbitGroup | Slug`. A key that is not one of the eight
standard groups must be the slug of an `arithmetic-groups/` card of the same lattice:
`checks.catalogues` reports "cusp_chambers names X, which is not an arithmetic-group card of TAG"
otherwise, and `theory/orbits.md#chamber-at-a-cusp` states the same rule. Card `0125` has no such card
for `G_e`, and nothing in the corpus defines `G_e` or `S_e` — the discriminant-decomposition condition
is printed only in Sterk (4.3.5).

So the key the row needs is missing, and #36's batch says to file it and store nothing for `G_e` rather
than to invent the key.

## What would close it

Either an `arithmetic-groups/<slug>.md` card on `0125` defining `G_e` — its ambient Lie group, its
parent `O` card, its index, and its citation to Sterk (4.3.5), p. 19 — after which the row is keyed by
that slug and states the twelve walls with "four orbits modulo `S_e`"; or a schema decision that such a
row is keyed some other way. The `O` row already on the card is not affected: it is the computed
chamber of the whole reflection group, with one ideal vertex, certificate
`12a3571c1d15ae8e99771f894e0bdfbb928fe8aafe34da732287ea6f67917e13`.
