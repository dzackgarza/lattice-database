---
tag: 5TPS
name: Constructed lattice 5TPS
latex: L_{\mathrm{5TPS}}
certifications:
  derive: 846efd739d0be313d7ebbc4669bddd80d113542529337b56c2fe526143855625
  form.integer_valued: 389958ec5122a406bb046a42aa8e9e741a612b2803215c1c8abcbf9eb1db961d
  integral.elementary_primes: cec8685f545532f2705ea8a19fdffb4b23fe9c44f8c0b8becaa01995374bb9f9
  integral.genus_symbol: 647b775c4fbae1585e8f59a0a3d7a114585aef510b8052ede88ec03ba56e39f7
  integral.genus_class_count: e416c7bdcc1683682e3bffc69a6ff22bdcd4dfe509c66738b25f8936c5823da3
  integral.overlattice_count: 93eec18e8b8681ba99bb5185789254f3706dd3d3f1be4caaf2a8a06f85821b50
  integral.spinor_genus_count: 001d0d7dc97d3ae27cfc3aef4e704ebb6d82c319ba2e270ea9d6bd2266b7d291
  integral.spinor_genera: 0768451c6b64d66365a26cb1368b2dd2e51b5ae8a59d0f7d7a72a438b6fc6a69
  integral.hyperbolic_index: f21a59639a3728d876ef7b3ad5dface892f57317f00233b366246cd0d0cbdb12
  automorphisms.automorphism_group_order: ebd5765302127d9c3402a9a9dd835e2001167d3b81773aa2cc1dbbe010e44e9f
  automorphisms.automorphism_group_generator_morphisms: ef1eec27abea331bdce5100b85663743d73247f681ce7d81da637ddcc7206319
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 0, 0, 2]
- [0, 0, 0, 2, 0]
signature: [3, 2]
determinant: 8
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 0, 0, 1/2]
- [0, 0, 0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{3,2} (2: 1^2 [2^3]_1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20, O(L) generator 21, O(L) generator 22, O(L) generator 23, O(L) generator 24, O(L) generator 25]
indefinite:
  isotropic: true
morphisms:
- target: 5TPS
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5TPS
  name: O(L) generator 2
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 2, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, -1, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 2]
  - [0, -1, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 7
  matrix:
  - [1, 1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-2, -1, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 2, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, 0, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 2]
  - [0, 0, -1, 0, 0]
  - [0, 0, -1, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5TPS
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-2, 0, 0, 1, -2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5TPS
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5TPS
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, -2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [-2, 0, 0, 2, -1]
  scale: 1
- target: 5TPS
  name: O(L) generator 14
  matrix:
  - [1, 0, -1, 0, 0]
  - [-2, -1, 1, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5TPS
  name: O(L) generator 15
  matrix:
  - [-1, 0, 0, -2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-2, 0, 0, -2, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 16
  matrix:
  - [1, 0, 1, 0, 0]
  - [2, -1, 1, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5TPS
  name: O(L) generator 17
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 18
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -2, 2, 2]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, 0, -1]
  - [0, 0, 1, -1, 0]
  scale: 1
- target: 5TPS
  name: O(L) generator 19
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 0, 1, 0, -2]
  - [0, -1, 0, -2, 0]
  - [0, 0, -1, 0, 1]
  - [0, -1, 0, -1, 0]
  scale: 1
- target: 5TPS
  name: O(L) generator 20
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 2, 0]
  - [0, -1, 0, 2, 0]
  - [0, 0, 0, 1, 0]
  - [0, 1, 1, -2, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 21
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, -2, 1, -2, -2]
  - [0, -1, 0, 0, -1]
  - [0, -1, 0, -1, 0]
  scale: 1
- target: 5TPS
  name: O(L) generator 22
  matrix:
  - [-1, 0, 0, 2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [2, 0, 0, -2, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 23
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5TPS
  name: O(L) generator 24
  matrix:
  - [-1, 0, -1, 0, 2]
  - [0, 0, 1, 0, -2]
  - [-2, 3, -3, 2, 8]
  - [0, 1, -1, 1, 2]
  - [0, 0, -1, 0, 3]
  scale: 1
- target: 5TPS
  name: O(L) generator 25
  matrix:
  - [-3, 2, 1, -4, 2]
  - [0, 0, -1, 2, 0]
  - [-6, 3, 1, -6, 4]
  - [2, -1, 0, 2, -1]
  - [-2, 2, 0, -1, 2]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0016, 0013.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0002, 0016, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0002, 0016, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0016, 0013.
