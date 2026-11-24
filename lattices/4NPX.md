---
tag: 4NPX
name: Constructed lattice 4NPX
latex: L_{\mathrm{4NPX}}
certifications:
  derive: 8810c2f775ff1f786701ef803da6cbc06ddf32e3db5e9d77feefc8b8c22cfb6b
  form.integer_valued: ab117d87b5a68b2891157add727a8ef382ea2da170c1e9263be13f23a411d220
  integral.elementary_primes: a43191ca342f80a5c347d5c841656e53166a7ae74a2ed9c55f692f4613d4b64d
  integral.genus_symbol: 2c289da10e43dffa6821ea29e5c17fb8086060b28867fa8bc59c9aaf984aed2e
  integral.genus_class_count: 12d9e8dc03c96f0436343280e36f537b78dcb7017f07ae107063406e7c44581e
  integral.overlattice_count: 0abee1fa3e4a98c6930e1ff7a2fe4c1903f61b4fa05c7293d2edf4b57d43d4ed
  integral.spinor_genus_count: 2db41193d23e23c05f0338f1871d503a6a5e92246819d0e8d122492ba3cab99d
  integral.spinor_genera: 818fc84c2293ef4e2b3f97b52a9a74e0dac320824cad0b317b37c317b6986ea2
  integral.hyperbolic_index: 09630a894537f46ab73402955fa2b4c63b4024b98cba4f5bd87152f0cd773e79
  automorphisms.automorphism_group_order: fe5da5c1c9dd1321c68bdeaa1bc320120264e703d505140f1fbaf2e4e1dc41c7
  automorphisms.automorphism_group_generator_morphisms: 8746b70958d0413ef12d1c44f1d34fbad43fd0b5be78c19d5fdc0b67c886cd17
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, 0, -2]
- [0, 0, 0, -2, 0]
signature: [3, 2]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, 0, 0, -1/2]
- [0, 0, 0, -1/2, 0]
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
- target: 4NPX
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4NPX
  name: O(L) generator 2
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 2, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, -1, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 2]
  - [0, 0, 1, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 7
  matrix:
  - [1, 0, -2, 0, 0]
  - [-2, 1, 2, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 2]
  - [0, -1, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4NPX
  name: O(L) generator 9
  matrix:
  - [1, -2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-2, 2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 2, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, 0, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, -2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 0, 0, 1, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, -4]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-2, 0, 0, 1, 4]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4NPX
  name: O(L) generator 14
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 2, 1, -2, 2]
  - [0, 1, 0, 0, 1]
  - [0, -1, 0, 1, 0]
  scale: 1
- target: 4NPX
  name: O(L) generator 15
  matrix:
  - [-1, 2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-2, 2, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 16
  matrix:
  - [1, 0, 0, -2, 0]
  - [0, 0, 1, -2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-1, 1, 0, 1, 1]
  scale: 1
- target: 4NPX
  name: O(L) generator 17
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -4, 0]
  - [0, 0, 0, -1, 0]
  - [0, -2, 0, 0, -1]
  scale: 1
- target: 4NPX
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
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY, 3ICZ.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICY, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICY, 3ICZ.
