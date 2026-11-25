# #39: Sterk's G_e as an arithmetic-group card, and the W_e chamber under its slug

Source: H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*, Math. Z. 207
(1991), 1–36, (4.3.5), p. 19, with Fig. 4, and Fig. 5, p. 20, read from the PDF text layer of
`tmp/sources/sterk-1991-compactifications-of-the-period-space-of-enriques-surfaces-i.pdf`.

## The group card

`arithmetic-groups/g-e.md`: `G_e`, on lattice `0125`, ambient `o-1-9`, `parent_group: o-u2-e8`,
`cardinality: aleph0`, `abstract_structure` = the stabilizer in `O(U(2) + E8(−2))` of the decomposition
of the discriminant group, and a reference quoting (4.3.5), p. 19 verbatim:
"It is easy to see that `G_e = {g ∈ O(M(2)) : the induced map on M(2)*/M(2) respects the decomposition}`".

`arithmetic-groups/o-u2-e8.md` is the parent: `O(U(2) + E8(-2))`, `standard_name: O`, ambient `o-1-9`.
Card `0125` had no arithmetic-group card at all, so it gains both and names them:
`orthogonal_group: o-u2-e8`, `arithmetic_groups: [o-u2-e8, g-e]`.

## The generators: the call that was tried and where it stops

No public `sage-extensions` call returns `G_e`'s generators, so the card stores none.

The call tried, in the owner's own vocabulary (`Aut()`, `discriminant_preimage`, `predicate_subgroup`,
`schreier_generators`):

```python
L = Lattices(ZZ)(<0125's gram_tensor>)
A = L.discriminant_group()                     # (Z/2)^10, orthogonal_group().cardinality() = 46998591897600
OA = A.orthogonal_group()
gens = tuple(A.module_generators())            # the ten classes

def preserves(element):                        # rho(g) respects A_L = A_U(2) + A_E8(-2)
    for index in range(2):
        image = coordinates(element(gens[index]))       # <-- stops here
        if any(image[2:]): return False
    for index in range(2, 10):
        image = coordinates(element(gens[index]))
        if any(image[:2]): return False
    return True

H = OA.predicate_subgroup(preserves, "rho(g) respects A_L = A_U(2) + A_E8(-2)")
G = L.Aut().discriminant_preimage(H)           # the preimage of a subgroup of the finite O(A_L)
G.schreier_generators(generators=<O(L)'s generators>)
```

Where it stops: the predicate cannot be evaluated at all. `element(gens[index])` for an element of
`O(A_L)` returns an `OwnedJoinCategory.element_class[_GeneralPresentedElement]`, and that element has no
coordinate accessor — `to_vector()` raises `AttributeError: 'OwnedJoinCategory.element_class
[_GeneralPresentedElement]' object has no attribute 'to_vector'` — so the subgroup of `O(A_L)` cannot be
described as a predicate and there is no `H` to take a preimage of. `OA.an_element().image(...)` raises
`AttributeError: 'Objects_with_category' object has no attribute 'Subobjects'` on the same path.

What is public and does work, and is used by the row's program: `A.module_generators()`, applying an
`O(A)` element (`element(x)`), `A.orthogonal_group()`, and `L.discriminant_preimage(H)` and
`PredicateSubgroups.schreier_generators(generators=...)` — the last two are the pieces that would
finish the job once a subgroup element can be read. Enumerating `O(A_L)` instead is not possible: its
cardinality is 46 998 591 897 600. Recorded at sage-extensions
`5a9874e22ea18fb223ff53cf2a3e48dd63c022b4`.

Consequence, stated on the card: `data.generator_morphisms` is absent, so no morphism was written to
`0125` and nothing is claimed about `G_e`'s generating set or its index.

## The row under `g-e`

`integral.cusp_chambers['g-e']` on card `0125`, from `results/transcribe-39-sterk-we-chamber.py`:

| What | Value |
| --- | --- |
| statement, page, figure | (4.3.5), p. 19, Fig. 4 |
| walls | 12: `α_1, …, α_8`, `α_9 = f' − e'`, `α_10 = ᾱ_8 + 2e'`, `α_11 = 2e' + 2f' + ᾱ_1 + ᾱ_8`, `α_12 = 5e' + 3f' + 2ᾱ_2`, in card `0125`'s basis (`e' = e_1`, `f' = e_2`, `α_i = e_{i+2}`) |
| wall squares | all `−4`, as Fig. 4 circles every node |
| Gram, diagram | from the card's Gram tensor: 13 edges, orders 3 with one of order `∞` at `α_2–α_12`, `α_9–α_10`, `α_9–α_12` |
| `parabolic_orbits` | four orbits of sizes **1, 2, 2, 4** |
| `ideal_vertices` | absent: the source prints classes, not a count |

Checks the program makes before writing:

* the card is `H(2) ⊕ E8(−2)` in Sterk's decomposition and numbering — the first block is `U(2)`, the E8
  tree in Sterk's numbering (Fig. 1, p. 3) is the card's `−2·Cartan(E8)` block, and the summands are
  orthogonal;
* `ᾱ_i` is the dual basis, `(ᾱ_i, α_j) = 2δ_ij`;
* all twelve walls have square `−4`, and (4.3.5)'s own printed check holds on the card:
  `(α_k, e' + f')²/|(α_k, α_k)| = 4, 16, 64` for `k = 10, 11, 12`;
* **the walls span `L` over ℚ** (rank 10 of 10);
* **the Gram matrix gives Fig. 4's edges**: the 13-edge set is the one card `029J` stores for the same
  statement and figure (`integral.cusp_chambers['gamma-en-2']`, statement `4.3.5`), transcribed there
  earlier from the same print — and it is also exactly the edge set the owner's
  `CoxeterDiagrams().from_roots` builds from the same twelve vectors;
* the owner's `Aut()` of that diagram has order **4**, which is Sterk's `S_e ≅ Z/2 × Z/2`, so the
  classes are the orbits of that group;
* the chamber's primitive rays: 23, of which **9** have square zero — the ideal vertices — and the walls
  orthogonal to each have rank `#vertices − #components = 8 = n − 1`, Vinberg's criterion ((4.3.3), p. 18);
* the 9 ideal vertices fall in **4 orbits** of sizes 1, 2, 2, 4 under `Aut`, matching Sterk's "four
  equivalence classes … four labelled classes" (p. 20), and the orbits partition them.

One correction to a reading worth recording: the owner's `maximal_parabolic_subdiagrams()` returns 36
subdiagrams for this diagram, and `maximal_elliptic_subdiagrams()` 44; "maximal for inclusion" is not
Vinberg's rank-`n − 1` condition (on the 4.3.6 diagram it returns 2 parabolic and 9 elliptic, against
10 rays). The count of ideal vertices is the rank-`n − 1` one, and the program takes it from the
chamber's rays and checks the rank of each subdiagram.

Certificate `0430d4dde789760ff670bab6269cf5bf69ae312faa1ff13d935c83c5f5a4fce7`, in
`certificates/<group of 0125>.yaml`, whose `by` names the citation, the Coxeter-diagram owner and its
revision.

## Not done

* No generator list for `G_e` (above), so no `index_in_orthogonal_group`, no relators, no orbit
  representatives for it.
* The four classes are not labelled with Sterk's types (`Ẽ_8`, `D̃_8`, `Ã_7 ⊕ Ã_1`, `Ẽ_7 ⊕ Ã_1` come
  from §4.3.16, pp. 27–28, and p. 20 says the labelling is "given by the root systems"): Fig. 5 is a
  raster image, so which class carries which label is printed only in the picture and in the types of
  the components, which would need the owner's type recognition on each subdiagram.
* The full-corpus build and `tests/validation/test_build.py` were not run (they do not fit this VM).
