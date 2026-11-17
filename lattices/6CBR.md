---
tag: 6CBR
name: Constructed lattice 6CBR
latex: L_{\mathrm{6CBR}}
certifications:
  derive: a514676ad424db15f968df3c141b1045e0bcb36ed93521f5efca94cef4bd36fe
  form.integer_valued: 1e4924b5e4b47ac3ecf8ae760545efd4e3b5ea659a89720f9f8aa845d26cd678
  integral.elementary_primes: 96ad1cafbff91f8802de0324e5cbf7089cc754137cd110efa4abcf3125cdc389
  integral.genus_symbol: e995711643bb75c09920d39422ad7aa5639c3422ad7a0e905128bd7e199f827e
  integral.genus_class_count: fd9cc1692e6e3058e4c3daa05e3b270a4b5314c176a33d477e96dc49ecf49862
  integral.overlattice_count: 94b48a2ef4b251c321c53cbd098ac8ea09b310d7dbbd1173dd0bacc47e052b1f
  integral.spinor_genus_count: 1bf583cfa0c96c7ef724127de8e3ea0cc590c5348fb640d863af6bf24c7ce09f
  integral.spinor_genera: 3e06f785144daff83ccf21aae0e937ed4ef9c27eb9f81036c1bbf854513a7cfb
  integral.hyperbolic_index: afe4908c622363ce7f81676ff398cbec45942602360e79670beff75b96c295d7
  automorphisms.automorphism_group_generator_morphisms: bd1f582c2813173c645d86fd03cf813d5a9513b0ab59062e6bc1ea733476a92e
  integral.discriminant_form: 6fc63120f2a0d5ad12beaf9d98d5a867548869edd05e7e04f0d18eef7601c032
rank: 4
gram_tensor:
- [0, 2, 0, 0]
- [2, 0, 0, 0]
- [0, 0, 0, -2]
- [0, 0, -2, 0]
signature: [2, 2]
determinant: 16
definiteness: indefinite
dual_gram_tensor:
- [0, 1/2, 0, 0]
- [1/2, 0, 0, 0]
- [0, 0, 0, -1/2]
- [0, 0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 2
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 31
  delta: 0
  bad_reduction_primes: [2]
  quadratic_character: 1
  genus_symbol: 'II_{2,2} (2: 2^4)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 72
    isotropic_classes: 10
    isotropic_orbits: 2
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12]
indefinite:
  isotropic: true
morphisms:
- target: 6CBR
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6CBR
  name: O(L) generator 2
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 1]
  - [-1, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6CBR
  name: O(L) generator 3
  matrix:
  - [1, 0, -1, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, -1, 0, 1]
  scale: 1
- target: 6CBR
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6CBR
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, -1, 0]
  - [0, 0, 1, 0]
  - [-1, 0, 0, 1]
  scale: 1
- target: 6CBR
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, -2]
  - [0, 1, 0, 0]
  - [0, -2, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6CBR
  name: O(L) generator 7
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6CBR
  name: O(L) generator 8
  matrix:
  - [1, 1, -1, -1]
  - [0, 1, 0, 0]
  - [0, 1, 0, -1]
  - [0, 1, -1, 0]
  scale: 1
- target: 6CBR
  name: O(L) generator 9
  matrix:
  - [0, 1, -1, 0]
  - [1, 0, 1, 0]
  - [0, 0, 1, 0]
  - [-1, 1, -1, 1]
  scale: 1
- target: 6CBR
  name: O(L) generator 10
  matrix:
  - [0, 0, 0, 1]
  - [1, 0, -1, 0]
  - [0, -1, 0, 1]
  - [1, 0, 0, 0]
  scale: 1
- target: 6CBR
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6CBR
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, -1]
  - [0, 0, 0, 1]
  - [-1, 0, 1, 0]
  scale: 1
related:
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0013, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 0013, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 0013, 3ICZ.
