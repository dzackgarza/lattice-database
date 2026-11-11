---
title: Orbits of primitive vectors
summary: The series $F_{L,\Gamma}(z, w)$ of $\Gamma$-orbits of primitive vectors of each norm, whose constant term counts $\Gamma$-orbits of primitive isotropic lines, and the series $F_{A_L,\Gamma}(z, w)$ of $\Gamma$-orbits on the discriminant group, for eight subgroups $\Gamma$ of $O(L)$.
order: 10
---

Let $L$ be an [integral](lattices.html#integral) lattice that is [nondegenerate](lattices.html#degenerate), with [discriminant group](discriminant-forms.html#discriminant-group) $A_L$.

## Eight subgroups of the orthogonal group {#groups}

::: {.definition}
$SO(L)$ is the kernel of $\det\colon O(L) \to \{\pm 1\}$.
The *stable orthogonal group* $\widetilde{O}(L)$ is the kernel of $O(L) \to O(A_L)$ ([GHS 2013](https://arxiv.org/abs/1012.4155), (6)). $O^+(L)$ is the kernel of the real spinor norm $\operatorname{sn}_\mathbb{R}\colon O(L \otimes \mathbb{R}) \to \mathbb{R}^*/(\mathbb{R}^*)^2 = \{\pm 1\}$, restricted to $O(L)$.
For a subgroup $\Gamma$ of $O(L)$, $\Gamma^+ = \Gamma \cap O^+(L)$, $S\Gamma = \Gamma \cap SO(L)$ and $\widetilde{\Gamma} = \Gamma \cap \widetilde{O}(L)$; so $\widetilde{O}^+(L) = \widetilde{O}(L) \cap O^+(L)$ ([GHS 2013](https://arxiv.org/abs/1012.4155), (7)).
:::

A record names the eight groups $O$, $SO$, $O^+$, $SO^+$, $\widetilde{O}$, $S\widetilde{O}$, $\widetilde{O}^+$ and $S\widetilde{O}^+$ with the keys `O`, `SO`, `O+`, `SO+`, `Otilde`, `SOtilde`, `Otilde+` and `SOtilde+`.

## Cokernel of the discriminant action {#mm-cokernel}

Let $L$ be a nondegenerate even lattice, and let $\rho_L\colon O(L)\to O(A_L,q_L)$ be its discriminant action.
As a pointed set, define $MM(L):=O(A_L,q_L)/\operatorname{im}\rho_L$, the set of left cosets pointed by the image subgroup.
The sequence $$1\longrightarrow\widetilde O(L)\longrightarrow O(L)\xrightarrow{\rho_L}O(A_L,q_L)\longrightarrow MM(L)\longrightarrow 1$$ is exact as a sequence of pointed sets: the preimage of the distinguished coset is $\operatorname{im}\rho_L$.
A finite computation can specify $MM(L)$ by coset representatives.
*MM-triviality* means that this set has one element, equivalently that $\rho_L$ is surjective.

When $\operatorname{im}\rho_L$ is normal, the coset set is a quotient group.
It is a $\mathbb Z$-module only when this group is abelian.
For an even indefinite $L$ with $\operatorname{rank}L>3$, the [Miranda–Morrison exact sequence](https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2013/63.pdf), stated in Akyol–Degtyarev, Theorem 3.8, is $$O(L)\xrightarrow{\rho_L}O(A_L,q_L)\longrightarrow E(L)\longrightarrow\mathfrak g(L)\longrightarrow 1,$$ where $E(L)$ is the Miranda–Morrison group and $\mathfrak g(L)$ is the genus group.
Under these hypotheses $MM(L)\cong\ker(E(L)\to\mathfrak g(L))$ is an $\mathbb F_2$-vector space.
Its isomorphism class as a torsion $\mathbb Z$-module is determined by $d=\dim_{\mathbb F_2}MM(L)$: it is $(\mathbb Z/2\mathbb Z)^d$.
Theorem 3.12 gives a local formula.
The full group $E(L)$ equals $MM(L)$ only when $\mathfrak g(L)=1$.

The reflection in $w \in L \otimes \mathbb{R}$ with $b(w, w) \neq 0$ is $\sigma_w(x) = x - \frac{2 b(x, w)}{b(w, w)} w$.
Every element of $O(L \otimes \mathbb{R})$ is a product $\sigma_{w_1} \cdots \sigma_{w_m}$ of reflections, and $$\operatorname{sn}_\mathbb{R}(\sigma_{w_1} \cdots \sigma_{w_m}) = \prod_{i=1}^m \left(-\frac{b(w_i, w_i)}{2}\right) \in \mathbb{R}^*/(\mathbb{R}^*)^2$$ ([Dawes 2022](https://arxiv.org/abs/2205.10601), (4)).

::: {.proposition}
On a positive definite lattice, $O^+(L) = SO(L)$.
On a negative definite lattice, $O^+(L) = O(L)$.
:::

::: {.proof}
A product of $m$ reflections has determinant $(-1)^m$.
When $b$ is positive definite, each factor $-b(w_i, w_i)/2$ is negative, so the spinor norm is $(-1)^m$ too.
When $b$ is negative definite, each factor is positive, so the spinor norm is $1$.
:::

So on a definite lattice the eight groups are at most four.
When $A_L = 0$, $\widetilde{O}(L) = O(L)$, and the eight groups are at most four again.

## The series of orbits {#primitive-orbits}

::: {.definition}
For a subgroup $\Gamma$ of $O(L)$ and an integer $n \neq 0$, $c_\Gamma(n)$ is the number of $\Gamma$-orbits on the primitive vectors $v \in L$ with $b(v, v) = n$, when it is finite.
A *primitive isotropic line* is a rank-one isotropic sublattice $\mathbb{Z}v$ with $v$ primitive isotropic, and $c_\Gamma(0)$ is the number of $\Gamma$-orbits of them, when it is finite.
The *series of orbits of primitive vectors* is $$F_{L,\Gamma}(z, w) = c_\Gamma(0) + \sum_{n \geq 1} c_\Gamma(n) z^n + \sum_{n \geq 1} c_\Gamma(-n) w^n \in \mathbb{Z}[[z, w]].$$
:::

The constant term counts primitive isotropic *lines* and not primitive isotropic vectors: every primitive isotropic vector has norm $0$, so it spans one of them, and the primitive vectors of the line $\mathbb{Z}v$ are exactly $v$ and $-v$, since $kv$ is imprimitive for $|k| \geq 2$ — so a line orbit is the union of at most two vector orbits, and the two counts are not the same count.
A $\Gamma$-orbit of lines is the image of the $\Gamma$-orbits of its primitive vectors, and $\Gamma[v] = \Gamma[-v]$, so one line orbit is the union of the orbit of $v$ and the orbit of $-v$.
Those are two orbits, or one when $-v = \gamma v$ for some $\gamma \in \Gamma$; by the [proposition below](#discriminant-orbits) that happens exactly when $v^* + L = -v^* + L$ in $A_L$, that is when $2(v^* + L) = 0$.
So $$c_\Gamma(0) = \tfrac{1}{2}\bigl(c_\Gamma^{\mathrm{vec}}(0) + s_\Gamma\bigr),$$ where $c_\Gamma^{\mathrm{vec}}(0)$ is the number of $\Gamma$-orbits of primitive isotropic vectors and $s_\Gamma$ is the number of those orbits that are their own negative.
The number a record stores in `integral.primitive_orbits[Γ].constant` is $c_\Gamma(0)$, the line count; the two counts agree exactly when every orbit is its own negative, as they do on a definite lattice, where both are $0$.
The line count is the number of $0$-cusps of the Baily–Borel boundary, which is why it is the line count that a card stores.

$c_\Gamma$ counts primitive isotropic *planes* as well, the rank-two totally isotropic sublattices $E = \mathbb{Z}v + \mathbb{Z}w$, and a record stores that number in `planes`: these are the $1$-cusps of the Baily–Borel boundary, as the lines are its $0$-cusps, and for a lattice of signature $(2, n)$ they are the next stratum of the same compactification.
A lattice of signature $(1, n)$ has no isotropic plane, and on a definite lattice the count is $0$.
A row whose key is not one of the eight standard groups names an arithmetic-group card of the same lattice, such as $\Gamma_{\mathrm{En},2}$, and its coefficients are that subgroup's.
Where a source states the sizes of the $\Gamma$-orbits of isotropic planes and not only how many there are, the row states them in `orbit_lengths`, in the order its citation names them: their sum is the number of primitive isotropic planes, which for a source that counts $1$-cusps is the row's `planes`, and their number is the number of orbits, which is `planes` for a source that counts orbits.

So $F_{L,\Gamma}(0, 0) = c_\Gamma(0)$ is the number of $\Gamma$-orbits of primitive isotropic lines, the coefficient of $z^n$ is the number of $\Gamma$-orbits of primitive vectors of norm $n$, and the coefficient of $w^n$ is that of norm $-n$.
A record states the coefficients that are known, through $z^4$ and $w^4$ at first, and a coefficient that is not known is null; a count that the owner states to be countably infinite is `aleph0`, so a stated count is never dropped for being infinite.
An indefinite card states the constant term alone: no positive or negative norm is bounded there.

Each coefficient obeys these relations, which `latticedb check` verifies:

- $c_\Gamma(n) = 0$ exactly when no primitive vector has norm $n$, for every nonzero $n$ and every $\Gamma$; $c_\Gamma(0) = 0$ exactly when $L$ has no primitive isotropic vector.
  That is so for odd $n$ when $L$ is even, and for $n$ of the sign opposite to $b$ when $L$ is definite.

- When $n$ has no square factor $k^2 > 1$, every vector of norm $n$ is primitive, since $b(kv, kv) = k^2 b(v, v)$.
  Then $c_\Gamma(n) = 0$ exactly when the [theta series](definite-lattices.html#theta-series) has no vector of norm $n$.

- For $H \subseteq \Gamma$, each $\Gamma$-orbit is a union of $H$-orbits, so $c_H(n) \geq c_\Gamma(n)$.

- Two keys that name one group, by the proposition above, have the same coefficients.

## Computation {#computation}

::: {.proposition}
Let $\varphi\colon G \to Q$ be a surjective homomorphism with kernel $H$, and let $G$ act on a set $X$.
Then $x \mapsto G \cdot (x, 1)$ induces a bijection from the $H$-orbits on $X$ to the $G$-orbits on $X \times Q$, where $g \cdot (x, q) = (g x, \varphi(g) q)$.
:::

::: {.proof}
$g \cdot (x, 1) = (y, 1)$ exactly when $y = g x$ and $g \in H$.
Every $G$-orbit meets $X \times \{1\}$: for $g$ with $\varphi(g) = q$, $g^{-1} \cdot (x, q) = (g^{-1} x, 1)$.
:::

For a definite lattice, `latticedb certify` computes $c_\Gamma(n)$ for $1 \leq |n| \leq 4$.
The function `qfauto` of PARI/GP gives generators of $O(L)$, and `qfminim` gives the vectors of norm at most 4, of which it keeps the primitive ones.
For $SO$, $\widetilde{O}$ and $S\widetilde{O}$, $Q$ is the image of $O(L)$ under $\det$, under $O(L) \to O(A_L)$, or under both, and the orbits are those of the proposition.
$O^+$ and its subgroups are then given by the [proposition on definite lattices](#groups).

For an indefinite lattice the sets are infinite.
Dawes gives algorithms for the orbits of vectors under subgroups of $O(L)$ ([Dawes 2022](https://arxiv.org/abs/2205.10601), Algorithms 2.1 to 2.3). When $L$ is even and contains two orthogonal hyperbolic planes, the coefficients of $F_{L,\Gamma}$ are given by the discriminant group $A_L$ and its finite quadratic form $q_L\colon A_L \to \mathbb{Q}/2\mathbb{Z}$, through the proposition below.

### The series on the discriminant group {#discriminant-orbits}

Define, for a subgroup $\Gamma$ of $O(L)$, the *series of orbits on the discriminant group* $$F_{A_L,\Gamma}(z, w) = c_\Gamma(0) + \sum_{n \geq 1} c_\Gamma(n) z^n + \sum_{n \geq 1} c_\Gamma(-n) w^n,$$ where $c_\Gamma(n)$ is the number of $\Gamma$-orbits on the classes $\alpha \in A_L$ with $q_L(\alpha) = n / \operatorname{ord}(\alpha)^2$.
This is a function of $(A_L, q_L)$ alone, defined for every nondegenerate $L$; it is the object the proposition below computes, and it equals $F_{L,\Gamma}$ on the stated class.
The two series are different functions in general: $F_{L,\Gamma}$ grades the primitive vectors of $L$, and $F_{A_L,\Gamma}$ grades the classes of $A_L$.

The *divisor* $\operatorname{div}(v)$ of $v \in L$ is the positive generator of the ideal $b(v, L) \subseteq \mathbb{Z}$.
Then $v^* = v / \operatorname{div}(v)$ is in $L^\vee$, and its image in $A_L$ has order $\operatorname{div}(v)$ when $v$ is primitive ([GHS 2009](https://arxiv.org/abs/0810.1614), Section 3.3).

::: {.theorem data-name="Eichler"}
Let $L = U \oplus U_1 \oplus L_0$ be an even lattice, with $U = \mathbb{Z}e \oplus \mathbb{Z}f$ and $U_1$ hyperbolic planes, and let $L_1 = U_1 \oplus L_0$.
If $u, v \in L$ are primitive, $b(u, u) = b(v, v)$ and $u^* \equiv v^* \bmod L$, then $\tau(u) = v$ for some $\tau$ in the group $E_U(L_1)$ generated by the Eichler transvections $t(e, a)$ and $t(f, a)$ with $a \in L_1$ ([GHS 2009](https://arxiv.org/abs/0810.1614), Proposition 3.3(i), with the hypothesis of Section 1 that $L$ is even).
$E_U(L_1)$ is a subgroup of $S\widetilde{O}^+(L)$ ([GHS 2009](https://arxiv.org/abs/0810.1614), (10)).
:::

The theorem needs $L$ even.
In the odd lattice $U^2 \oplus \langle 1 \rangle$ with $b(x, x) = 1$, the vectors $x$ and $e + x$ are primitive of norm 1, and $A_L = 0$.
But $x$ is characteristic, $b(x, y) \equiv b(y, y) \bmod 2$ for every $y$, and $e + x$ is not, since $b(e + x, f) = 1$ and $b(f, f) = 0$.
An isometry keeps this property, so no element of $O(L)$ sends $x$ to $e + x$.

::: {.proposition}
Let $L = U \oplus U_1 \oplus L_0$ be even, and for an integer $n$ let $S_n$ be the set of $\alpha \in A_L$ of some order $d$ with $q_L(\alpha) = n / d^2$ in $\mathbb{Q}/2\mathbb{Z}$.
Then $v \mapsto v^* + L$ is a surjection from the primitive vectors of norm $n$ onto $S_n$, and its fibres are the $\widetilde{\Gamma}$-orbits for each $\widetilde{\Gamma}$ with $E_U(L_1) \subseteq \widetilde{\Gamma} \subseteq \widetilde{O}(L)$.
So $c_\Gamma(n) = |S_n|$ for $\Gamma = \widetilde{O}, S\widetilde{O}, \widetilde{O}^+, S\widetilde{O}^+$.
For $\Gamma = O, SO, O^+, SO^+$, $c_\Gamma(n)$ is the number of $O(q_L)$-orbits on $S_n$.
:::

::: {.proof}
For $v$ primitive of norm $n$ and $d = \operatorname{div}(v)$, $v^* + L$ has order $d$ and $q_L(v^* + L) = n / d^2$, so it is in $S_n$.
Let $\alpha \in S_n$ have order $d$.
Since $A_L = A_{L_0}$, $\alpha = x + L$ for some $x \in L_0^\vee$ with $d x \in L_0$, and $d^2 b(x, x) \equiv n \bmod 2 d^2$.
So $m = (n - d^2 b(x, x)) / 2d^2$ is an integer, and $v = d(e + m f + x)$ is in $L$ with $b(v, v) = n$.
$b(v, f) = d$ and $b(v, L) \subseteq d \mathbb{Z}$, so $\operatorname{div}(v) = d$ and $v^* + L = \alpha$.
If $v = k w$ with $w \in L$, then $\frac{d}{k} x \in L_0$, so $d$ divides $d / k$ and $k = 1$: $v$ is primitive.
Each $\widetilde{\Gamma}$ fixes $v^* + L$, and by the theorem $E_U(L_1)$ is transitive on each fibre; so the fibres are the $\widetilde{\Gamma}$-orbits.

For $SO^+ \subseteq \Gamma$, the map is $\Gamma$-equivariant and each fibre is one $S\widetilde{O}^+$-orbit, so the $\Gamma$-orbits correspond to the orbits on $S_n$ of the image of $\Gamma$ in $O(q_L)$.
The reflections $\sigma_{e+f}$ and $\sigma_{e-f}$ are in $O(L)$, since $b(e \pm f, e \pm f) = \pm 2$, and act trivially on $A_L = A_{U_1 \oplus L_0}$, so they are in $\widetilde{O}(L)$.
Their determinants are $-1$ and $-1$, and their real spinor norms $-b(w, w)/2$ are $-1$ and $1$; so they map onto $O(L) / SO^+(L) \subseteq \{\pm 1\}^2$, and $O(L) = \widetilde{O}(L) \cdot SO^+(L)$.
Thus $O$, $SO$, $O^+$ and $SO^+$ have one image in $O(q_L)$.
$L$ is even and indefinite, and $\operatorname{rank} L = 4 + \operatorname{rank} L_0 \geq l(A_L) + 4$, where $l$ is the minimal number of generators; so $O(L) \to O(q_L)$ is surjective ([Nikulin 1980](https://doi.org/10.1070/IM1980v014n01ABEH001060), Theorem 1.14.2).
:::

`latticedb certify` computes $F_{L,\Gamma}$ through $z^4$ and $w^4$ for a definite lattice, by enumerating its vectors, and $F_{A_L,\Gamma}$ through $z^4$ and $w^4$ and $n = 0$ for an even lattice whose hyperbolic index, stored or bounded from below by stored embeddings $U^k \to L$, is at least 2. The two are stored in `integral.primitive_orbits` and `integral.discriminant_orbits`.
`integral.primitive_orbits` is requested on an indefinite card too, and carries the coefficients that the owner's `primitive_orbit_series` returns for it: the constant term $c_\Gamma(0)$, the number of $\Gamma$-orbits of primitive isotropic **lines** of the [section above](#primitive-orbits), which the [proposition](#discriminant-orbits) counts through the isotropic classes of $A_L$, and no $z$- or $w$-coefficient, since no norm is bounded there.
By that section $c_\Gamma(0)$ is not the number of $\Gamma$-orbits of primitive isotropic vectors unless every one of them is its own negative; the [example below](#discriminant-orbits) is a lattice where the two differ. The class `TorsionQuadraticModule` of SageMath gives $A_L$, $q_L$ and generators of $O(q_L)$, and the orbits on $S_n$ are found by breadth-first search.
By the proposition above, $F_{A_L,\Gamma}$ equals $F_{L,\Gamma}$ on that class; outside it the two differ, and $F_{A_L,\Gamma}$ is what this computation yields.
For an odd lattice the coefficients are stated with a `reference` that proves them.

::: {.example}
Let $L_9 = U \oplus U \oplus \langle -18 \rangle$, with basis $e, f, e_1, f_1, g$ and $b(g, g) = -18$, so that $A_{L_9} = \mathbb{Z}/18$ and the class of $k g / 18$ has $q_L = -k^2/18$ in $\mathbb{Q}/2\mathbb{Z}$.
Then $q_L = 0$ exactly for $k = 0, 6, 12$, so by the proposition $\widetilde{O}(L_9)$ has three orbits of primitive isotropic vectors: $e$, and the vector $v = 3e + 3f + g$ with its negative.
Indeed $v$ is primitive and isotropic, $\operatorname{div}(v) = 3$, and $v^* + L = e + f + g/3$ is the class $6$, while $(-v)^* + L = -e - f - g/3$ is the class $12$.
The classes $6$ and $12$ are negatives of one another, so the orbits of $v$ and of $-v$ are one orbit of lines, and the class $0$ satisfies $2 \cdot 0 = 0$, so its orbit is its own negative and is another.
So $\widetilde{O}(L_9)$ has $3$ orbits of primitive isotropic vectors and $c_{\widetilde{O}}(0) = 2$: two orbits of primitive isotropic lines.
:::

::: {.example}
Let $L = U^2 \oplus L'$ be even and unimodular.
Then $A_L = 0$ and $S_n = \{0\}$ for each even $n$, so $c_\Gamma(n) = 1$ for each of the eight groups: the vector $e + \frac{n}{2} f$ in the first $U$ is primitive of norm $n$.
For the K3 lattice $U^3 \oplus E_8(-1)^2$ this is [GHS 2013](https://arxiv.org/abs/1012.4155), Example 7.6.
:::

GHS 2009: V. Gritsenko, K. Hulek and G. K. Sankaran, *Abelianisation of orthogonal groups and the fundamental group of modular varieties*, arXiv:0810.1614. GHS 2013: V. Gritsenko, K. Hulek and G. K. Sankaran, *Moduli of K3 surfaces and irreducible symplectic manifolds*, arXiv:1012.4155. Dawes 2022: M. Dawes, *Orbits in lattices*, arXiv:2205.10601.

## Counts of polarizations {#polarizations}

A numerical polarization of an Enriques surface $S$ is a primitive class $h \in \operatorname{Num}(S) = M(1/2) = U \oplus E_8(-1)$ with $h^2 = 2d > 0$ ([Dutour Sikirić–Hulek 2024](https://arxiv.org/abs/2302.01679), Section 2, p. 6).
$U \oplus E_8(-1)$ is 2-reflective, and its Weyl group is its isometry group ((8), p. 9), so the $O(U \oplus E_8(-1))$-orbits of primitive vectors of one degree — the polarizations of that degree up to isometry — are counted in the fundamental domain $D$ of that Weyl group (Section 3.1, p. 8).
Dutour Sikirić and Hulek write $\#h$ for that number in degree $2d$, and $\#\Gamma_h$ for the number of conjugacy classes of the groups $\Gamma_h = \pi_N^{-1}(\pi_M(O(M, h))) \subset O(N)$ that those polarizations define ((5) and Question 2.1, p. 7); that number equals the number of conjugacy classes of their images $\bar\Gamma_h = \pi_M(O(M, h)) \subset O^+(\mathbb{F}_2^{10})$, because $\pi_N$ is onto and its kernel lies in every $\Gamma_h$, and they tabulate both counts for $2d = 2, \dots, 72$ in Table 4, p. 17.

A card stores the two counts under `integral.polarization_counts`, keyed by the degree $2d$ written as its decimal text — a stored mapping has string keys — and under the table's own names, each row citing the table and its page.
The table's two cumulative columns are sums of the stored rows and are not values of their own, so they are not stored.

## The chamber at a cusp {#chamber-at-a-cusp}

Let $L$ be an [integral](lattices.html#integral) lattice of signature $(2, n)$ and let $\Gamma \leq O(L)$ be a subgroup.
Its $0$-cusps are its [orbits of primitive isotropic lines](#primitive-orbits).
For a primitive isotropic $v \in L$ the quotient $v^\perp/\mathbb{Z}v$ is an integral lattice of signature $(1, n-1)$, whose positive cone modulo $\mathbb{R}_{>0}$ is a hyperbolic space $\mathcal{H}$; the stabilizer $\Gamma_v$ of $v$ acts on it through its image $G_v \leq O(v^\perp/\mathbb{Z}v)$, and the subgroup $W_v$ generated by the reflections $\sigma_w$ in the vectors $w$ of negative square in $G_v$ is its reflection subgroup.

::: {.definition}
A *chamber at the cusp* $\mathbb{Z}v$ is a fundamental domain of $W_v$ in $\mathcal{H}$: a set $\{x \in \mathcal{H} : b(x, w_i) \geq 0 \text{ for every } i\}$ of finite volume whose boundary hyperplanes $w_i^\perp$ are the *walls*, none of them superfluous.
A wall is a vector of negative square in $v^\perp$, and the walls of a chamber span $v^\perp/\mathbb{Z}v$ over $\mathbb{Q}$.
:::

Sterk's construction of these chambers for $\Gamma_{\mathrm{En},2}$ is Vinberg's algorithm (H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*, Math. Z. 207 (1991), 1–36, (4.3.2)–(4.3.4), pp. 17–19; È. B. Vinberg, *The groups of units of certain quadratic forms*, Mat. Sb. 87 (1972)), which is the owner's operation and not the database's.
A chamber is described by its walls and by their *Coxeter diagram*: the vertices are the walls, and for two walls $w_i, w_j$ one sets
$$g_{ij} = \frac{b(w_i, w_j)}{\sqrt{b(w_i, w_i)\, b(w_j, w_j)}},$$
draws no edge when $g_{ij} = 0$, an edge of order $m$ when $g_{ij} = \cos(\pi/m)$ for $m = 3, 4, 6$, and an edge of order $\infty$ when $|g_{ij}| = 1$ (Sterk, Fig. 2, p. 18).
Because $b(w_i, w_i) < 0$, the sign of $g_{ij}$ is the sign of $b(w_i, w_j)$ and does not change the diagram; and a pair with $b(w_i, w_j) = 0$ is no edge.
Sterk marks a wall of square $-4$ with $\circ$ and one of square $-2$ with $\bullet$, and draws an arrow towards the wall of smaller $|b(w, w)|$ when two adjacent walls have different squares; the arrow is not part of the diagram here, because the Gram matrix the card stores fixes the squares.

A record states the chamber in `integral.cusp_chambers`, keyed by the subgroup and then by cusp: the cusp $v$, the walls with the source's own names and their coordinates in the record basis, the statement, printed page and figure that print them, and the wall count, the Gram matrix $b(w_i, w_j)$ and the diagram.
The walls are the source's transcription; the three invariants of them are what the card's Gram tensor says, computed once by the program the certificate names, and `latticedb certify` never requests the field, because no preamble operation searches for a chamber.
A row whose wall has positive square, or whose walls do not span $v^\perp/\mathbb{Z}v$ over $\mathbb{Q}$, is a transcription defect and not a chamber.
A source that prints a chamber only as a figure does not state it, and a card stores no row for that cusp.
