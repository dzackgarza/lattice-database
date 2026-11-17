---
tag: 4IGP
name: Constructed lattice 4IGP
latex: L_{\mathrm{4IGP}}
certifications:
  derive: 556bbc2d740bf45c6b3ba611ac559432f1a60ea6f129fb6d1e70215735e17710
  form.integer_valued: cb8a890904353d0f113b7e90541936aca4cdd3f611f6732e9dc38659c99211f3
  integral.elementary_primes: 699380e7259d845ff54907c87ce684e7d6c662de11750157d4487dd60eff1d94
  integral.genus_symbol: 41883fd00f95895758e91a48215aa8300f1c21818a86dc1a9b2f3a9cc7afe0ee
  integral.genus_class_count: 3935bb47695d754ee7a1d0703b6d9bd9d325286801a70ea5df52e310dc9f55ca
  integral.overlattice_count: d17a9f07b61eab956da7331f652bcc6d26ffd27773b7c2854ded9da8c6d38dea
  integral.spinor_genus_count: a481cc02871660518aae72f43ffbfc045ba9065a49fd79289b7cdcf783873e02
  integral.spinor_genera: ecae65e892985c9a0b7cabe72a7e86847ba24bc3c5e48b7d51636faccdd1094f
  integral.hyperbolic_index: 6ec807d2ba60500f13e829da265025ab59a7e380888b56a99c82a2c6baf69a92
  automorphisms.automorphism_group_generator_morphisms: 105648960de1cb620875ccfd7b801e0ed4417d4ade9197d0516944ca0b3df70c
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, -2, 0]
- [0, 0, 0, -2]
signature: [1, 3]
determinant: -8
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, -1/2, 0]
- [0, 0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  bad_reduction_primes: [2]
  quadratic_character: -8
  genus_symbol: 'I_{1,3} (2: [1^1 2^3]_6)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9]
indefinite:
  isotropic: true
morphisms:
- target: 4IGP
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4IGP
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 4IGP
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 4IGP
  name: O(L) generator 4
  matrix:
  - [3, 4, 0, 0]
  - [-2, -3, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4IGP
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0]
  - [0, 0, -1, 0]
  - [0, -1, 0, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4IGP
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4IGP
  name: O(L) generator 7
  matrix:
  - [3, 4, 0, 0]
  - [0, 0, 1, 0]
  - [2, 3, 0, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4IGP
  name: O(L) generator 8
  matrix:
  - [5, 4, -4, -4]
  - [-2, -2, 1, 2]
  - [2, 2, -2, -1]
  - [2, 1, -2, -2]
  scale: 1
- target: 4IGP
  name: O(L) generator 9
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ICX.
