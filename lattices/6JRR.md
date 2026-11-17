---
tag: 6JRR
name: T_Co
latex: T_{\mathrm{Co}}
aliases: [Coble lattice]
certifications:
  integral.discriminant_form: 0be391409303d25f25d126795ee881040661b4883ad7473272b34b60b8c414da
  derive: fc58a2a5c04d528184492c0ed5e2beed56005f6c9f7eff25662da9e6a88a34b0
  form.integer_valued: 96d0bf04d04f3d6eaff79ab1f17cc3d72e23fe8fe95340378fda316b15c68df1
  integral.elementary_primes: 32545f4c763545bb5467152a650f6a22b4183d9aa45fdcd9da20dd7be1c474a7
  integral.genus_symbol: 7ae1183ff01d083ec5990da4a6fdb4f8a14882c2c8d52557470258e6b78493b8
  integral.genus_class_count: 7243bd5404f045797450584d7abd512e3f919fe3fcf446139f92118eae583f5c
rank: 11
gram_tensor:
- [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
- [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [0, 0, 0, -4, 0, 2, 0, 0, 0, 0, 0]
- [0, 0, 0, 0, -4, 0, 2, 0, 0, 0, 0]
- [0, 0, 0, 2, 0, -4, 2, 0, 0, 0, 0]
- [0, 0, 0, 0, 2, 2, -4, 2, 0, 0, 0]
- [0, 0, 0, 0, 0, 0, 2, -4, 2, 0, 0]
- [0, 0, 0, 0, 0, 0, 0, 2, -4, 2, 0]
- [0, 0, 0, 0, 0, 0, 0, 0, 2, -4, 2]
- [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -4]
signature: [2, 9]
determinant: -2048
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [0, 0, 1/2, 0, 0, 0, 0, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [0, 0, 0, -2, -5/2, -7/2, -5, -4, -3, -2, -1]
- [0, 0, 0, -5/2, -4, -5, -15/2, -6, -9/2, -3, -3/2]
- [0, 0, 0, -7/2, -5, -7, -10, -8, -6, -4, -2]
- [0, 0, 0, -5, -15/2, -10, -15, -12, -9, -6, -3]
- [0, 0, 0, -4, -6, -8, -12, -10, -15/2, -5, -5/2]
- [0, 0, 0, -3, -9/2, -6, -9, -15/2, -6, -4, -2]
- [0, 0, 0, -2, -3, -4, -6, -5, -4, -3, -3/2]
- [0, 0, 0, -1, -3/2, -2, -3, -5/2, -2, -3/2, -1]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  discriminant_group: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{2,9} (2: [2^11]_1)'
  genus_class_count: 1
  discriminant_form:
    orthogonal_group_order: 46998591897600
    isotropic_classes: 528
    isotropic_orbits: 2
indefinite:
  isotropic: true
morphisms: []
arithmetic_groups: [otilde-t-co, otilde-plus-t-co]
references:
- citation: 'I. Dolgachev, S. Kondo, "The rationality of the moduli spaces of Coble surfaces and of nodal Enriques surfaces", Izv. Math. 77:3 (2013), 507-524, Section 2, p. 510: the conventions ($\mathbb{E} = E_8 \oplus U$ with $E_8$ the even negative definite lattice of the Cartan matrix, $L(2)$ the form $2b$, $\langle m \rangle$ the rank-one lattice of a vector of norm $m$, $A_L = L^*/L$ with its quadratic form $q_L$), and Section 3, equation (3.6) with Proposition 3.2, p. 513: the Coble lattice is $N = \langle 2 \rangle \oplus \mathbb{E}(2) = \langle 2 \rangle \oplus U(2) \oplus E_8(-2)$, of signature $(2, 9)$, and the moduli space of Coble surfaces is an open subset of $\mathcal{D}(N)/O(N)$.'
---

The Coble lattice $T_{\mathrm{Co}} = \langle 2 \rangle \oplus U(2) \oplus E_8(-2)$, in the basis $e_{0}$ of the first summand, $e_{1}, f_{1}$ of $U(2)$ with $b(e_{1}, f_{1}) = 2$, and the simple roots of $E_{8}(-2)$: rank $11$, signature $(2, 9)$, determinant $-2048$, even.

$T_{\mathrm{Co}}$ is twice the odd unimodular lattice $I_{2,9} = \langle 1 \rangle \oplus U \oplus E_{8}(-1)$, so $T_{\mathrm{Co}} \cong I_{2,9}(2)$; $b(e_{1}, e_{1}) = 0$, so it is isotropic.
Its discriminant group is $A_{T_{\mathrm{Co}}} = (T_{\mathrm{Co}})^{*}/T_{\mathrm{Co}}$, of order $2048$.
The groups studied with it are the discriminant kernel $\widetilde O(T_{\mathrm{Co}})$ and $\Gamma_{\mathrm{Co}} = \widetilde O^{+}(T_{\mathrm{Co}})$, which have their own arithmetic-group cards `otilde-t-co` and `otilde-plus-t-co`.

No invariant of this card is transcribed from a source: `latticedb certify` computes each from the Gram tensor above and certifies it, so a field is absent until its computation runs.
$E_8$ is negative definite, in Dolgachev–Kondo's convention for $\mathbb{E}(2) = (E_8 \oplus U)(2)$ and in the Gram tensor above, whose third summand has $-4$ on its diagonal and $-2$ off it.

`integral.primitive_orbits` states, for each of the eight standard subgroups, the constant term: the number of $\Gamma$-orbits of primitive isotropic *lines*, the $0$-cusps of the Baily–Borel boundary, and not a count of vectors (`theory/orbits.md`).
The preamble returns it for an indefinite lattice as the constant term of `primitive_orbit_series`, which is `isotropic_orbit_representatives(1).cardinality()` of each subgroup; on an indefinite lattice nothing positive or negative is bounded, so the $z$ and $w$ coefficients are empty.
The count is what the operation returned for the stored Gram tensor: no page's count is transcribed, and the observed isotropic classes of $A_{T_{\mathrm{Co}}}$ are not an orbit count.

The arithmetic-group cards attached to this lattice are `otilde-t-co`, the discriminant kernel $\widetilde O(T_{\mathrm{Co}}) = \ker(O(T_{\mathrm{Co}}) \to O(A_{T_{\mathrm{Co}}}))$, and `otilde-plus-t-co`, its intersection with the kernel $O^{+}(T_{\mathrm{Co}})$ of the real spinor norm — not with the determinant-one subgroup, which is $SO$.
Dolgachev–Kondo, Proposition 3.2, p. 513, describes $\mathcal{M}_{\mathrm{Co}}$ as an open subset of $\mathcal{D}(N)/O(N)$; that the group acting on this period domain is the image of $\widetilde O^{+}(T_{\mathrm{Co}})$, which the literature writes $\Gamma_{\mathrm{Co}}$, is a conjecture and not a result proved here or by that proposition, so it settles no count on this card.
