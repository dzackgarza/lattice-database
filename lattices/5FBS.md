---
tag: 5FBS
name: Constructed lattice 5FBS
latex: L_{\mathrm{5FBS}}
certifications:
  derive: ccf7c83ddcc1cd60d5c4a0bce7bd19b67624eaf53cce772cd6d7cb9840997f2b
  form.integer_valued: 49657fdb8859a1cfc600c187edc78469c51e764ee6982d844c80e13f9caaa597
  integral.elementary_primes: 12fe2578ea3993013132e3b81b93ea26efb5525e1bcb06f14d130201c686b2af
  integral.genus_symbol: 442600cb762629996d5dea013ab3916a95be1054dd7b622c021fd848b8996817
  integral.genus_class_count: 71a1eea03bc74610889444bf4af1e585d9104e4d7c8627ba6f36556d1ec34aac
  integral.overlattice_count: 6c508c38c706d519ce137aed6cecbc7858e85cc8e74bd8eca03e9099741960b8
  integral.spinor_genus_count: 1d518833c0e968ccb85ecc04cc8738b132eb6a017875d949ce13321b409904f3
  integral.spinor_genera: a7a41f6fb809734d9b7c17fc73e283d8af6833b3c6f575d87be0854144198ab1
  integral.hyperbolic_index: 93895e958a5423d30dcd431368bc6b67748d357a23ab8692913633b6d4e27fa3
  automorphisms.automorphism_group_order: f9880c7742c5f45044ee58550f00b40d1a055d522e073a8b94dea329ce08e180
  automorphisms.automorphism_group_generator_morphisms: d94619fcc3fe107fb98022de726ad39208b4de342f3a82f36386b5bcbb73cbac
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 0, 0, -2]
- [0, 0, 0, -2, 0]
signature: [2, 3]
determinant: -16
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 0, 0, -1/2]
- [0, 0, 0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 2
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 31
  bad_reduction_primes: [2]
  genus_symbol: 'I_{2,3} (2: [1^1]_7 2^4)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18]
indefinite:
  isotropic: true
morphisms:
- target: 5FBS
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5FBS
  name: O(L) generator 2
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, -1]
  - [0, 1, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5FBS
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, 1]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  scale: 1
- target: 5FBS
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -1, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, 0, 0, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, -1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, -1, 0, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5FBS
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 0, 0, -1, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, -2]
  - [0, 0, 1, 0, 0]
  - [0, 0, -2, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 10
  matrix:
  - [1, 0, -4, 0, 0]
  - [-2, 1, 4, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 1, -1, -1]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, 0, -1]
  - [0, 0, 1, -1, 0]
  scale: 1
- target: 5FBS
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 1, 0]
  - [0, 1, 0, -1, 0]
  - [0, 0, 0, 1, 0]
  - [0, 1, -1, -1, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 13
  matrix:
  - [-1, 0, 0, 0, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-1, 0, 0, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 14
  matrix:
  - [-1, 0, 0, 2, 0]
  - [0, 0, -1, 1, 0]
  - [0, -1, 0, 1, 0]
  - [0, 0, 0, 1, 0]
  - [1, -1, -1, 0, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 15
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 5FBS
  name: O(L) generator 16
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, -1]
  - [0, 1, 0, 0, 1]
  - [0, -1, 1, 1, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 17
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FBS
  name: O(L) generator 18
  matrix:
  - [-1, -2, 2, 2, -2]
  - [0, -1, -1, 1, 1]
  - [1, 1, -1, -2, 1]
  - [0, -1, 0, 1, 0]
  - [2, 2, -1, -3, 2]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0013, 3ICZ.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0013, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0013, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 0013, 3ICZ.
