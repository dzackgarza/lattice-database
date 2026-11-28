---
tag: 4NMF
name: Constructed lattice 4NMF
latex: L_{\mathrm{4NMF}}
certifications:
  derive: a72180e87062b13e44c06d9f23d19cd934bb5f6605afdaa38bfb252bf3e53136
  form.integer_valued: 88e09a4ca649de516b36a0b52941796deae3c73b937b0e7e37e5a8f60e9d4a4d
  integral.elementary_primes: 39112fdfa65440fcac777c1a8d3d5a100bf962e69d484747cfb0994c36735927
  integral.genus_symbol: ec1f147dd8e4721b8d08ca5798db1c14fc6fa153acf327f1c299fb7570cf9b4c
  integral.genus_class_count: 9d421f0a8fc84033a34c67ed8deb19b0e1806c82d6e307b88a4c561aec4355b1
  integral.overlattice_count: 7c1640ed3213fa7a8ff4cba7dc94b4048bdfbb8cd2131e4f2406959dabacedae
  integral.spinor_genus_count: 77e2cb009fa85a37d6b54d48757b334121c3a1d348e2028d8b46cf030db4e4d6
  integral.spinor_genera: da79045a0701efbece9aceb9b05fedc8ca26b1fbf2fcedd00c30d9a0bbbee189
  integral.hyperbolic_index: 8565548f2cac706f8d8427784594667cd1da8732ed247e8891d06a1549b45f9b
  automorphisms.automorphism_group_order: 4829d9f6f1bda1a1f1d4bbd13f9a3ac60872930b12cc9e2dd04c1f24c1ddd815
  automorphisms.automorphism_group_generator_morphisms: 186c16dc75bbdca2d55fe514f0091bff25d0e8f5389c4ebaef63f61eb9676889
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, 0, 2]
- [0, 0, 0, 2, 0]
signature: [3, 2]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
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
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18]
indefinite:
  isotropic: true
morphisms:
- target: 4NMF
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4NMF
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 4]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 2]
  - [2, -1, 0, -1, 4]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4NMF
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4NMF
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, -2]
  - [0, 0, 1, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 5
  matrix:
  - [1, 0, -2, 0, 0]
  - [-2, 1, 2, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, -2, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, -1, 0, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 0, 0, -1, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4NMF
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -2, 0]
  - [0, 0, 0, -1, 0]
  - [0, 1, 0, 0, -1]
  scale: 1
- target: 4NMF
  name: O(L) generator 11
  matrix:
  - [1, -2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-2, 2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 12
  matrix:
  - [-1, 0, 2, 0, 0]
  - [-2, 1, 2, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 13
  matrix:
  - [-1, 0, 0, 0, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-1, 0, 0, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 14
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, -2, 0]
  - [0, 1, 0, 2, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, 1, -2, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 15
  matrix:
  - [-1, 0, 0, 2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [1, 0, 0, -1, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 16
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 2]
  - [0, 1, 0, 0, -2]
  - [0, 1, -1, 1, -2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 17
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NMF
  name: O(L) generator 18
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY, 0013.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICY, 0013.
