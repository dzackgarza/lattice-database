---
tag: 5EBP
name: Constructed lattice 5EBP
latex: L_{\mathrm{5EBP}}
certifications:
  derive: 815e3ba9e8ac6d286d88deebe42a95fa5c3c480b3172fdaeb248fcf81159560e
  form.integer_valued: 5dff869287b0ce4d5679e2c64b1eecb04ac82b8d22ca4fa001c2c83e6e4d6910
  integral.elementary_primes: bb9959b44ad3a147cd6c55731682d1d3901b9f74c1174ea47343b47e72229ab5
  integral.genus_symbol: 3e8f956c946f63d7d25ba4c48c3497d84b400fcf689d27af6770a68dfde4ab55
  integral.genus_class_count: 06bbc29d729b0925dbbd4749735fe83b0b233623034e561f696b33d2aec14a77
  integral.overlattice_count: b8a4feee123a26f2c0fbca2fe3f6d11bcf54e10991ca53bc932c8df115bece26
  integral.spinor_genus_count: 28e9b3e8df0488d86f853c0f0a56969212ff9935eec119db53e3d7ac031f65f5
  integral.spinor_genera: c6d1029198b9c0c1c3b952af035b43038097c000c1a6d41dfd9dee50b3dc367f
  integral.hyperbolic_index: 3e13fabaf53ddcf86ca467068ff924e091b7842f5085d96b7c23a5eaff5549a2
  automorphisms.automorphism_group_order: 455870e4af968d29963e0e0504716e8cc7bb421413c5b83a99521b1b033efbf5
  automorphisms.automorphism_group_generator_morphisms: e6685f2f289bd4bef436d7d2863768b51a7c9888a1e2478326ac851875da243b
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 0, -2, 3]
- [0, 0, 0, 3, -6]
signature: [1, 4]
determinant: 3
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 0, -2, -1]
- [0, 0, 0, -1, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{1,4} (2: [1^-5]_7; 3: 1^4 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 5EBP
  name: O(L) generator 1
  matrix:
  - [-1, 0, 2, 0, 0]
  - [-2, 1, 2, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EBP
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 1, -1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 2, -1, 0]
  - [0, 0, 1, -1, 1]
  scale: 1
- target: 5EBP
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5EBP
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EBP
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5EBP
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0016, 3ID3.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0016, 3ID3.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0016, 3ID3.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 0016, 3ID3.
