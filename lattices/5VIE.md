---
tag: 5VIE
name: Constructed lattice 5VIE
latex: L_{\mathrm{5VIE}}
certifications:
  derive: 9eb0b7842d5a2d6a78c1ec19ab6dc5c3a097fcfb91b593b31d3d522691335847
  form.integer_valued: f7316535b203950facb37ec43718c33e6cb44469aabce41e3c7a4459dc0ebaca
  integral.elementary_primes: 8fe488c91cacec40eef3c08d7853f607c432cd41f3f20e990b68f53fa14344d2
  integral.genus_symbol: 018d33ce06bcab00817bba84d853ffd76395be8abd4e1daf0311f8acca991222
  integral.genus_class_count: 4924cd9fc0cd87db5e0a40a397ad59f47c4e6a83df50dbe4dbf539390761579c
  integral.overlattice_count: 6b311eaf4dac1443b27291b9f3784d7605834e1e43dc515161ffa405b2e8b0e9
  integral.spinor_genus_count: 59dac47532306cd178e38d256b43ac22a601ef01d9c2eec2827c71d958bb9368
  integral.spinor_genera: ce6933dee2cf857f62aa522db9cea9f8c9ea7d4acde4d61388a4b6e85aeb6b21
  integral.hyperbolic_index: 398a47612808336e6e23bf484a9d0dd8d1b9bac2facecbd693ee8b5c5eb857dc
  automorphisms.automorphism_group_order: a96f609852488fb6ed6c088102aaf56011e6f97bea61c15856252143cde27b7d
  automorphisms.automorphism_group_generator_morphisms: dbf71c01bcadb6bf22ebfa792d71f7df91969465fa143a2dc67db22404778154
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 0, 2, -3]
- [0, 0, 0, -3, 6]
signature: [4, 1]
determinant: -24
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 0, 2, 1]
- [0, 0, 0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  discriminant_group: [2, 2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{4,1} (2: 1^-2 [2^3]_1; 3: 1^-4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15]
indefinite:
  isotropic: true
morphisms:
- target: 5VIE
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -2]
  scale: 1
- target: 5VIE
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 5VIE
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5VIE
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5VIE
  name: O(L) generator 5
  matrix:
  - [-1, 2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [2, -2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5VIE
  name: O(L) generator 6
  matrix:
  - [-3, 2, -2, 0, 0]
  - [-2, 2, -1, 0, 0]
  - [2, -1, 2, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5VIE
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5VIE
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 2, -1, -1, 3]
  - [0, -1, 2, 1, -3]
  - [0, -2, 2, 3, -6]
  - [0, -2, 2, 2, -5]
  scale: 1
- target: 5VIE
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -2, 1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 4, -1, 0]
  - [0, 0, 2, -1, 1]
  scale: 1
- target: 5VIE
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5VIE
  name: O(L) generator 11
  matrix:
  - [1, 0, 2, 0, 0]
  - [-2, 1, -4, -1, 0]
  - [4, -2, 7, 0, 3]
  - [4, -2, 10, 1, 3]
  - [4, -2, 8, 1, 2]
  scale: 1
- target: 5VIE
  name: O(L) generator 12
  matrix:
  - [-1, -4, 2, -2, 0]
  - [4, 10, -5, 3, 3]
  - [-6, -13, 8, -5, -3]
  - [-12, -28, 16, -9, -9]
  - [-8, -18, 10, -6, -5]
  scale: 1
- target: 5VIE
  name: O(L) generator 13
  matrix:
  - [-5, -6, 6, 0, -6]
  - [6, 6, -7, 0, 6]
  - [-6, -7, 8, 1, -9]
  - [-12, -12, 16, 1, -15]
  - [-8, -8, 10, 1, -10]
  scale: 1
- target: 5VIE
  name: O(L) generator 14
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -2, -1, 3]
  - [0, -6, 7, 3, -12]
  - [0, -6, 8, 5, -15]
  - [0, -4, 6, 3, -10]
  scale: 1
- target: 5VIE
  name: O(L) generator 15
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0013, 3ID4.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0002, 0013, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 0002, 0013, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0013, 3ID4.
