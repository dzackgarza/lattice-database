---
tag: 4DEX
name: Constructed lattice 4DEX
latex: L_{\mathrm{4DEX}}
certifications:
  derive: 83e422d4daefead06c8c1e8778c5035dbce7df7836ae9d47102b0d0989fc2cc5
  form.integer_valued: 495be941c4606438a13bb6148619a5ce06dc069e2528c7d991e1f54aac47d18b
  integral.elementary_primes: 40dad9a333c664e0ea1e102ee803076fae59d1629a1d096bc981a6bd573e5f25
  integral.genus_symbol: 8f9e0681e0049c4c5406b5b66274a329690ab8febc1bbe12610e7a9443df1f13
  integral.genus_class_count: f9f394c3b6a16e95ecc1f07aa1598535b5b2d98a13c2b79c600c38f939c5669c
  integral.overlattice_count: e0ce6e2c8e8e18e46e62dc9e092429c2a7ba84d6167ebfa721bdc8ae6ac5091a
  integral.spinor_genus_count: 0c8920c5801dcfba4011ae1e3477379534a39e419ae7e9dac45f06b7d0427ef9
  integral.spinor_genera: 66bef52e87b8fd3aaadd14bf34a7deaad62c74dde814cd6e388ac3e06c2bc278
  integral.hyperbolic_index: 78a549ee92fec2ef73481b2e10968411c840dd808b2dc1a7f849f8c5d7e000c4
  automorphisms.automorphism_group_order: 0ebf178a5707c97eb62d148ee9b37efa19c609c5da2e224c795020ccc20e3dfc
  automorphisms.automorphism_group_generator_morphisms: 131743f9395acd2e491db8f8644f1f1472d56b7afff746f3b3f86ed113ce2673
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
signature: [4, 1]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 0, 0, 0, 1]
- [0, 0, 0, 1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  discriminant_group: [2, 2]
  overlattice_count: 2
  bad_reduction_primes: [2]
  genus_symbol: 'I_{4,1} (2: [1^3 2^2]_3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11]
indefinite:
  isotropic: true
morphisms:
- target: 4DEX
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DEX
  name: O(L) generator 2
  matrix:
  - [-1, -4, 0, 2, -2]
  - [-2, -3, 0, 2, -2]
  - [0, 0, 1, 0, 0]
  - [-2, -4, 0, 3, -2]
  - [2, 4, 0, -2, 3]
  scale: 1
- target: 4DEX
  name: O(L) generator 3
  matrix:
  - [-3, -4, 0, 4, -2]
  - [-2, -1, 0, 2, -1]
  - [0, 0, 1, 0, 0]
  - [-2, -2, 0, 3, -1]
  - [4, 4, 0, -4, 3]
  scale: 1
- target: 4DEX
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 4DEX
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DEX
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, -1]
  - [0, 0, 1, 0, 0]
  - [0, -2, 0, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DEX
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 2, 1, -1]
  - [0, 2, -1, -1, 1]
  - [0, -2, 2, 2, -1]
  - [0, 2, -2, -1, 2]
  scale: 1
- target: 4DEX
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DEX
  name: O(L) generator 9
  matrix:
  - [-1, 0, 0, 0, -2]
  - [0, 0, 1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [-2, 0, 0, 1, -2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DEX
  name: O(L) generator 10
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4DEX
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 0016.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 0002, 0016.
