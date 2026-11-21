---
tag: 5MHS
name: Constructed lattice 5MHS
latex: L_{\mathrm{5MHS}}
certifications:
  derive: 45f638f95060ff225f6390a87c7321b93a5f186302da1c1e099da6cceb8f6559
  form.integer_valued: 2ea1a6d76c334a3646f8cfe1b91d9ff1a039c610aac48eb3d61b95779a29eab6
  integral.elementary_primes: d17dffe774960b995de785c53c7d914de4f968c564477130f36104a5d43401fd
  integral.genus_symbol: cdf76994a012b856f070b59225bc70204303b878b980a39c6aa96dbd4b576ce0
  integral.genus_class_count: a1b44b6993ab13ca12f00d2dcb76935888c135d80b909493d56745360cd6e2a9
  integral.overlattice_count: 24e55efc1869c91d8b58fb4e65cb6bad9f1366d4f185646255e5181f8958c6a4
  integral.spinor_genus_count: 7b388a021159d4f21f3b1e44e9b90ae154adab3bc86c72abd5d51ac077ae499e
  integral.spinor_genera: 846985ca14990514890912611b4237159d522f52d2b0e735770843732fb3951e
  integral.hyperbolic_index: 714d6b1a55e8746054ff9f20e0f2d9f3e35e75def9ab8974b4854e343c3cdd59
  automorphisms.automorphism_group_order: 57a2fab4b895f8717dd29bff4efdc37b0177de4292351990e74cef7a4f0b7d50
  automorphisms.automorphism_group_generator_morphisms: 1ff035f64e77061f6c426d668759a9c4d95719ece3d913e6898d9234f1ad8730
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, 2, -3]
- [0, 0, 0, -3, 6]
signature: [4, 1]
determinant: -24
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
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
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16]
indefinite:
  isotropic: true
morphisms:
- target: 5MHS
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5MHS
  name: O(L) generator 6
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -2]
  scale: 1
- target: 5MHS
  name: O(L) generator 8
  matrix:
  - [0, -1, 2, 2, -3]
  - [-1, 0, 2, 2, -3]
  - [-2, -2, 5, 4, -6]
  - [2, 2, -4, -3, 6]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 9
  matrix:
  - [-1, 0, 2, 2, -3]
  - [0, 1, 0, 0, 0]
  - [-2, 0, 3, 2, -3]
  - [2, 0, -2, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 10
  matrix:
  - [-1, -2, 2, 0, 0]
  - [-2, -1, 2, 0, 0]
  - [-2, -2, 3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 12
  matrix:
  - [4, -3, 6, 3, -3]
  - [3, -4, 6, 3, -3]
  - [6, -6, 11, 6, -6]
  - [-6, 6, -12, -8, 9]
  - [-2, 2, -4, -3, 4]
  scale: 1
- target: 5MHS
  name: O(L) generator 13
  matrix:
  - [-10, -3, 20, 10, -3]
  - [-9, -4, 18, 9, -3]
  - [-16, -6, 33, 17, -6]
  - [14, 6, -32, -17, 6]
  - [4, 2, -10, -5, 1]
  scale: 1
- target: 5MHS
  name: O(L) generator 14
  matrix:
  - [-24, -25, 38, 14, -15]
  - [-23, -24, 36, 12, -12]
  - [-36, -38, 57, 20, -21]
  - [24, 28, -40, -14, 15]
  - [8, 10, -14, -5, 5]
  scale: 1
- target: 5MHS
  name: O(L) generator 15
  matrix:
  - [-1, -2, 4, 0, 3]
  - [-2, -1, 4, 0, 3]
  - [-4, -4, 9, 0, 6]
  - [6, 6, -12, -1, -6]
  - [2, 2, -4, -1, -1]
  scale: 1
- target: 5MHS
  name: O(L) generator 16
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 3ID4.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0002, 3ICX, 3ID4.
