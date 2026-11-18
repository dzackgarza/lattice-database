# #43: the $O(K_J)$-invariant, and why it cannot decide these rows

The route this file reports on was the one the field's emptiness pointed at: instead of waiting for a generating
family of the cusp stabilizer $\Gamma_v$ (sage-extensions#312), separate the cusp's root classes by an invariant of
the **coarsest** group that acts on them, $O(K_J)$. Since $\Gamma_v \subseteq O(K_J)$, two classes that
$O(K_J)$ separates are $\Gamma_v$-inequivalent, and the orbit count of that row is decided with no knowledge of
$\Gamma_v$ at all.

## The invariant is exactly the complement

Let $r \in K_J$ be a primitive root, $(r, r) = -2$. Then $\langle r\rangle$ is a primitive sublattice and
$K_J = \langle r\rangle \perp r^\perp$ orthogonally, so an isometry $r_1^\perp \to r_2^\perp$ extends by
$r_1 \mapsto r_2$ to an isometry of $K_J$ --- $b(r_i, \cdot)$ kills the other summand, and $(r_1,r_1) = (r_2,r_2)$.
Conversely an isometry of $K_J$ carrying $r_1$ to $r_2$ restricts to $r_1^\perp \to r_2^\perp$. So

> $r_1$ and $r_2$ are $O(K_J)$-equivalent **iff** $r_1^\perp$ and $r_2^\perp$ are isometric,

and the complete $O(K_J)$-invariant is the isometry class of $r^\perp$, not a derived number. Every $r^\perp$ here
is an even 2-elementary lattice of rank 9 and determinant $\pm 2^9$, so its genus is one symbol (rank, signature,
$a = 9$, $\delta = 1$) and Sage's `GenusSymbol_global_ring.representatives()` counts the classes in it.

## The probe

`results/probe-43-okj-complement-invariant.py`, run on host Sage 10.8 (Sage only: it imports no preamble, so it does
not need the pinned image). It builds $K_J$ from the card alone --- $\Lambda = \eta^\perp$ is the kernel of
$x \mapsto b(x,\eta)$, $\eta$'s image in $\Lambda$ is a primitive row $c$, and the rows after a unimodular matrix's
first row $c$ give a $\mathbb{Z}$-basis of $\Lambda/\mathbb{Z}\eta$ --- reads the chamber's walls, keeps those
orthogonal to the cusp of square $-2$, and for each root takes the rank-9 kernel of $x \mapsto b(x, r)$.

Full log: `results/evidence-43-okj-complement.log`. Runtime 13.7 s for all five rows.

| statement | page | $\det K_J$ | root classes | complement | $\delta$ | classes in its genus | $O(K_J)$-orbits on the row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (4.3.5) | 19 | $-1024$ | 0 | --- | --- | --- | no row |
| (4.3.6) | 21 | $-256$ | 1 | 512 | 1 | 1 | 1 |
| (4.3.7) | 22 | $-256$ | 2 | 512 | 1, 1 | 1, 1 | **1** |
| (4.3.8) | 23 | $-256$ | 2 | 512 | 1, 1 | 1, 1 | **1** |
| (4.3.9) | 24 | $-256$ | 4 | 512 | 1, 1, 1, 1 | 1, 1, 1, 1 | **1** |

## The finding

The invariant does not fail to separate these rows because it is coarse: **it has nothing to separate.** At
(4.3.7), (4.3.8) and (4.3.9) the root classes of one cusp are all $O(K_J)$-equivalent --- every complement is the
same lattice, `[2^9]_1`, and each genus has one class, so the complements are isometric (Sage:
`representatives()` returns one class; genus equality on the objects, not on their printed representative matrices,
which differ in a basis). The whole of $O(K_J)$, the largest group that acts, carries each row's root family in one
orbit.

So the count of $\Gamma_v$-orbits on a row lies between $1$ and the number of root classes, and what decides it is
the **index** of $\Gamma_v$'s image in $O(K_J)$ --- precisely the missing generating family of $\Gamma_v$ that
`generation_obstruction()` names at a primitive isotropic line. For (4.3.8) the sage-extensions report's own run
gives two components of one class each, so the true count there is 1 or 2 and nothing computed here can say which.

This is the finding that turns #312 from a nuisance into the blocker: with the coarse group collapsing every row
to one orbit, no invariant of $O(K_J)$ --- or of any group containing $\Gamma_v$ --- can distinguish two root
classes at these cusps, so the values on `029J`'s four cusped rows cannot be certified by any computation that does
not generate $\Gamma_v$. The row at (4.3.6) is the exception and is decided by triviality: a family of one class
has one orbit whatever the group does. It is not stored, because the issue asks for the five rows and one row alone
would state 029J's cusp orbits as complete when four are missing; it can be landed on its own at any time.

The T_Co card's rows at cusps 3--5 have not been touched: they are the same question in $K_I$ under
$\Gamma_{\mathrm{Co},2}$, and this finding is about the $T_{En}$ side.

## Second opinion, in the pinned runtime

The genus in the table above is Sage's own (`IntegralLattice(gram).genus()`), computed on host Sage 10.8. The
repository's own operation for this number is `integral.genus_class_count`, whose owner is
`Lattices(ZZ)(gram).genus_class_number()` in `sage_extensions.categories.lattices`. That operation, in the pinned
image (Sage 11.0.beta5, sage-extensions `main` bound over `/repos/sage-extensions`), on the two complements at
(4.3.8):

```
class number 1 det 512
class number 1 det 512
```

Two implementations agree, so "one class in the genus" is not one library's opinion: each complement at that cusp is
the unique class of its genus, and the two are then isometric.
