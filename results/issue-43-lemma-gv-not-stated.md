# #43, one lemma: Sterk states $G_v$'s shape at two cusps, not at four — and the direction matters

**Lemma.** The only statements in Sterk's §4 of the *shape* of the cusp image $G_v$ are at `(4.3.6)` and `(4.3.7)`.
At `(4.3.8)` and `(4.3.9)` he states only that the diagram's symmetries are realised in $\Gamma_v$ — a subgroup statement.
Consequently a count of **one** orbit can be cited from him at those cusps (a transitive subgroup already gives one
orbit), and a count of **two** cannot (that needs the whole image).

**The printed sentences.** Read from the text layer of pp. 20–24 and, for pp. 22 and 24, from the page images:

| cusp | page | what he says about $G_v$ |
| --- | --- | --- |
| (4.3.6) | 20 | "$O(H \oplus E_8(-2)) = \{\pm 1\}\cdot W_{e'}$", after "As there are no symmetries" |
| (4.3.7) | 22 | "We find $G_v = \{\pm1\}W_v \rtimes \mathbb{Z}/2$" |
| (4.3.8) | 23 | "the symmetry is induced by an element of $\Gamma_v$ (see (4.3.10))" — no equality |
| (4.3.9) | 24 | "Symmetries of the graph can be lifted to $\Gamma_v$ (see (4.3.10))" — no equality |

**Why the direction of the argument matters.** At `(4.3.9)` the eight diagram symmetries act transitively on
$\alpha_{11},\alpha_{12},\alpha_{13},\alpha_{14}$, and Sterk says they are realised in $\Gamma_v$. A group that
*contains* a transitive family has one orbit, whatever else it contains — so the stored $T_{En}$ row
(`lattices/029J.md:524`, one orbit) is safe: it needs only the subgroup. The Coble count of $2$ is the opposite kind of
claim: it says the image has **no** element identifying $\alpha_{12}$ with the other two, which needs the image to be
*exactly* what the reflections and the $\delta$-preserving symmetry generate. Sterk gives no such equality at
`(4.3.9)`, and this repository has no other printed source for it.

**Consequence.** The count-of-2 lemma (`results/issue-43-lemma-coble-image.md`) is a conditional whose hypothesis is not
in print, and the cusp-5 row stays empty. What the lemma above does settle is the *asymmetry* of the two sides: the
$T_{En}$ rows are cited correctly because a subgroup suffices for one orbit, and no amount of further reading of Sterk's
§4 will certify two.

**Sources by printed page.** H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*,
Math. Z. 207 (1991), 1–36: `(4.3.6)`, p. 20; `(4.3.7)`, p. 22; `(4.3.8)`, p. 23; `(4.3.9)`, p. 24; `(4.3.10)`, p. 25.
