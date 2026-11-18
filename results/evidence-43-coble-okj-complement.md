# #43, the T_Co side: the same invariant collapses cusps 3--5 of $K_I$

The issue's third item asks the T_Co card (6JRR) for the row at its cusps 3--5. This is the probe of the same
$O(K)$-invariant there, on the same footing as `results/evidence-43-okj-complement.md`: separate the cusp's root
classes by an invariant of the largest group that acts, and where the complement's genus has one class, read whether
any separation survives at all.

## What it computes

$T_{Co} = \delta^\perp$ inside $T_{En}$ with $\delta = e - f$ in the card's coordinates, so a wall is in $T_{Co}$
exactly when it is orthogonal to $\delta$; at cusps 3--5 Sterk's cusp vector has equal $e$ and $f$ coefficients, so it
lies in $T_{Co}$ and $K_I = \eta^\perp/\mathbb{Z}\eta$ is built inside it. The card alone supplies everything:
`results/probe-43-coble-okj-invariant.py`, host Sage 10.8, Sage only (no preamble import, no pinned image needed).
Runtime 1.1 s for all three cusps; log `results/evidence-43-coble-okj-complement.log`.

A root of $K_I$ is a wall that lies in $T_{Co}$, is orthogonal to the cusp, and has square $-2$. For each root,
$K_I = \langle r\rangle \perp r^\perp$ orthogonally, so two root classes are $O(K_I)$-equivalent iff their
complements are isometric, exactly as on the $T_{En}$ side, and each complement is an even 2-elementary lattice of
rank 8 whose genus Sage's `representatives()` counts.

## The result

| statement | page | walls in $T_{Co}$ | $K_I$ | root classes | complement | $\delta$ | classes in its genus | $O(K_I)$-orbits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (4.3.7) | 22 | 9 of 12 | rank 9, det 512, sig $(1,8)$ | 1 | $-256$, genus `[2^8]_2` | 1 | 1 | 1 |
| (4.3.8) | 23 | 9 of 11 | rank 9, det 512, sig $(1,8)$ | 1 | $-256$, genus `[2^8]_2` | 1 | 1 | 1 |
| (4.3.9) | 24 | 11 of 14 | rank 9, det 512, sig $(1,8)$ | 3 | $-256$, genus `[2^8]_2` | 1, 1, 1 | 1, 1, 1 | **1** |

Three of the three rungs agree with the sage-extensions report `results/issue370-the-coble-root-orbits.md`
independently of it: the walls in $T_{Co}$ are $9$, $9$ and $11$; $K_I$ is rank 9, determinant 512, signature
$(1,8)$ at all three cusps; and the roots of $K_I$ number $1$, $1$ and $3$. That report's own table gives the same
three counts and the same $\Gamma_{\mathrm{Co},2}$ components, $1$, $1$ and $3$.

## The finding, and the second blocker

At (4.3.9) the three root classes of $K_I$ are all $O(K_I)$-equivalent --- every complement is the one class of its
genus --- so, as on the $T_{En}$ side, no invariant of any group containing the cusp stabilizer separates them, and
the count of stabilizer-orbits lies between 1 and 3 with the index deciding it. At (4.3.7) and (4.3.8) the family
has one class, so those two rows are decided by triviality and carry no information about the group.

The second blocker is the register. `integral.cusp_root_orbits` is keyed by the eight standard subgroups or by the
slug of an arithmetic-group card of the same lattice, and card 6JRR lists `arithmetic_groups: [otilde-t-co,
otilde-plus-t-co]` (`lattices/6JRR.md:2022`) --- there is no card for $\Gamma_{\mathrm{Co},2} = R_{\Gamma_{\mathrm{En},2}}$,
which is the group whose cusps 3--5 these are. A row keyed `O` or `Otilde` would state the orbits of a different
group, so the row cannot be written at all until that card exists; and its own values (an index in $O(T_{Co})$, a
generating family) are exactly what #312 withholds.

So item 3 of #43 is blocked twice: no key for the group, and the same #312 collapse behind it. Nothing on 6JRR is
changed by this probe.

## Why the T_Co row cannot be keyed here, in the corpus's own words

The field's key for a named subgroup is the slug of an arithmetic-group card of the same lattice, so the T_Co row needs
a $\Gamma_{\mathrm{Co},2}$ card on 6JRR. The corpus records, twice, that the group of the Coble period domain is not
identified in the literature it rests on:

- `arithmetic-groups/otilde-plus-t-co.md:23`: "That this subgroup is the group $\Gamma_{\mathrm{Co}}$ acting on the Coble
  period domain is **conjectural**." and `:24`: "Dolgachev–Kondo, Proposition 3.2, p. 513, … does not name the subgroup
  of $O(N)$ that acts; the identification … belongs to the family group of the research project, not to this database,
  and no count on the card of 6JRR rests on it."
- `lattices/6JRR.md:2031` and `:2044` repeat it: $\Gamma_{\mathrm{Co}} = \widetilde O^{+}(T_{\mathrm{Co}})$ is a
  conjecture, and Prop. 3.2 settles no count on that card.

$\Gamma_{\mathrm{Co},2} = R_{\Gamma_{\mathrm{En},2}}$ is a finer group still, and the only support this repository holds
for it is the construction in sage-extensions' own test (`#354`, `#358`, research `prop:gamma-co-images`) — an internal
family object, not a published definition and not a value this corpus certifies. Authoring the card would mint exactly
what the data contract forbids: a group asserted on the strength of an unpublished construction, to key rows whose
counts are in any case blocked on the same non-returning equivalence call that stops (4.3.7)--(4.3.9).

So the T_Co item is blocked twice, and neither blocker is mine: a published definition of $\Gamma_{\mathrm{Co},2}$, and
the owner's exact equivalence returning at a cusp.
