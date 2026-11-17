---
tag: 6EKM
name: Constructed lattice 6EKM
latex: L_{\mathrm{6EKM}}
certifications:
  derive: af4a1b5ce1947cb894c070bdf1e1634ee6525465dbcfeab1d4111b7979cfd169
  form.integer_valued: ee216431f0041ac1a815f7ef1d85bc9915ceef93ea5b8ac768a33efa4cfea071
  integral.elementary_primes: 56b57dcc51e1c85801194c4d085dc44efc45056bf2c41ba129cfd27b75337f3f
  integral.genus_symbol: 001aac44cba49510026f1f3b3cbfa9919e722293a34d3bc333390d39c4f8762b
  integral.genus_class_count: 20a620148e7cce57a4af9f60df686a0819bfcc3777e63133710aca6d74b34629
  integral.overlattice_count: 49deb5ae0f63008caf834ee375c62733d9db2222c1cc031ce56288caabeb5725
  integral.spinor_genus_count: 9c8db48c8c39f2cc84c2c952a7cf1d43fb7c9640c3340fe3d1292a4c2652ff55
  integral.spinor_genera: 864a5f3aae05c0b9f021678cefa3d33f12be7c1a3b419a6dc0d9a955439dad52
  integral.hyperbolic_index: 9905aab9bbfc62e9fd3477d04078d5c075e29785f2708c5345fc9adeb69b9de3
  automorphisms.automorphism_group_generator_morphisms: e360a25e5abbb638cd6a8fd6025ca58e0fc115674471c95561e88bf09d5a898d
  integral.discriminant_form: 0dd404f46495fc29f02e790157b91667dac45ce6797922c2f3ed478e30f1ad20
rank: 4
gram_tensor:
- [0, -2, 0, 0]
- [-2, 0, 0, 0]
- [0, 0, 4, -2]
- [0, 0, -2, 4]
signature: [3, 1]
determinant: -48
definiteness: indefinite
dual_gram_tensor:
- [0, -1/2, 0, 0]
- [-1/2, 0, 0, 0]
- [0, 0, 1/3, 1/6]
- [0, 0, 1/6, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 6
  discriminant_group: [2, 2, 2, 6]
  overlattice_count: 31
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{3,1} (2: 2^-4; 3: 1^-3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 240
    isotropic_classes: 6
    isotropic_orbits: 2
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6EKM
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 6EKM
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6EKM
  name: O(L) generator 3
  matrix:
  - [1, 1, 2, -1]
  - [0, 1, 0, 0]
  - [0, -1, -1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 6EKM
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 6EKM
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ID2.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 3ICZ, 3ID2.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICZ, 3ID2.
