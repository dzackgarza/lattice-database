---
tag: 4MWI
name: Constructed lattice 4MWI
latex: L_{\mathrm{4MWI}}
certifications:
  derive: c1eb5b72e795d8677c27c859edd8fdbb0b812d3cb2ca016329b9f6e0e1de4e8c
  form.integer_valued: 8edbcca7a77a54af7011a2dbdda9c848cf304745ec0bb52cde1ee0d6e7922a6e
  integral.elementary_primes: 082fe8c885c50580488a15646a4a6dbf1d67b19896a1a116c39200898601166a
  integral.genus_symbol: 52efcb4ba30e47d3e05fb11c466d942894d5737470504444cf12a2ae6bf8eb82
  integral.genus_class_count: 9c17c76a3d6237b2be7c62ab7b1b8b45d1f0e7e94de0a3f1b6251cee0c744652
  integral.overlattice_count: 9169f293010636f972038a5a2ebd4eeed85bf755367390b2514861e8343e29ea
  integral.spinor_genus_count: dc062160434b15b507fe97eb2e5c7bfe4080d5673b56e45881d8df10877116a9
  integral.spinor_genera: 9aec511b48f991576edbaffe86faf30fb51d10a01a4f8d2cb83a3f01be8e7509
  integral.hyperbolic_index: 8d4caf54af57e32d28865b4b9dcc893fd1cbaa02ca6f908ae32720ee3f9e5316
  automorphisms.automorphism_group_order: e9b021ba58404ce400533a970ac96e3f98574bbb05011249faa4d715ae1299ed
  automorphisms.automorphism_group_generator_morphisms: 40a1c13338567c3b38bf591f85982b3b76a4d26b9973f6f7ccc798855990cbcc
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 0, 0, 2]
- [0, 0, 0, 2, 0]
signature: [3, 2]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 0, 0, 1/2]
- [0, 0, 0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 2
  discriminant_group: [2, 2]
  overlattice_count: 4
  bad_reduction_primes: [2]
  genus_symbol: 'I_{3,2} (2: [1^3]_1 2^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20, O(L) generator 21]
indefinite:
  isotropic: true
morphisms:
- target: 4MWI
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4MWI
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, -4, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -2, 0]
  - [0, 0, 0, -1, 0]
  - [-2, -1, 0, 4, -1]
  scale: 1
- target: 4MWI
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4MWI
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 2, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, -1, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 5
  matrix:
  - [1, 0, -2, 0, 0]
  - [-2, -1, 2, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 2]
  - [0, 0, -1, 0, 0]
  - [0, 0, 1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-1, 0, 0, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 2]
  - [0, 1, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4MWI
  name: O(L) generator 10
  matrix:
  - [1, 0, 2, 0, 0]
  - [2, -1, 2, 0, 0]
  - [0, 0, -1, -2, 0]
  - [0, 0, 0, -1, 0]
  - [-2, 1, -2, 0, -1]
  scale: 1
- target: 4MWI
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4MWI
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, -2]
  - [0, 0, -1, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 14
  matrix:
  - [1, 2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-2, -2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 15
  matrix:
  - [-1, 0, 2, 0, 0]
  - [2, 1, -2, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 16
  matrix:
  - [-1, 0, 0, 0, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-1, 0, 0, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 17
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 2, 0]
  - [0, -1, 0, 2, 0]
  - [0, 0, 0, 1, 0]
  - [0, 1, 1, -2, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 18
  matrix:
  - [1, -2, 0, 2, 0]
  - [0, 1, 0, 0, 0]
  - [2, -2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 2, 0, -1, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 19
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, -2]
  - [0, -1, 0, 0, -2]
  - [0, -1, -1, 1, -2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 20
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4MWI
  name: O(L) generator 21
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0016, 0013.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0001, 0016, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0001, 0016, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0016, 0013.
