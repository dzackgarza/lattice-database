---
tag: 3XPE
name: Constructed lattice 3XPE
latex: L_{\mathrm{3XPE}}
certifications:
  derive: cc73febaa09f6a708ca55ed3512f5cdbfb23fa6c72f2cc8896ee98a949beba24
  form.integer_valued: c197d39e1d93d5f44c822743ef2ec4efd41c5b05998335d9370489bdda262de4
  integral.elementary_primes: 5e21ee0b41c381a1722b691dc82c3320407630ef46685ad0530b851c1a249221
  integral.genus_symbol: 5fabd9e8177385316d2775b3055130168c5bfb1b03006d977ebdcc9e5772c325
  integral.genus_class_count: de2b681c045063c380f583f56f19c7fe090304833e9d98c4485c22fb4a7a0f8c
  integral.overlattice_count: 8742e0d3188af0e7553140e8c90d7ac2787077b3007b1eab73597c0d0b0fbb89
  integral.spinor_genus_count: cb41aa6e59c9ef240c6b835af49e6b7f026c292552e8891714b40a844a9de625
  integral.spinor_genera: c6043b438d82e3d33e4460102d74a2a7600e68772ce1f0605f500c61249266f9
  automorphisms.automorphism_group_order: cba9580a607144c0627222d0c062861741559b4a6dd8d0a19625401f7a3318c9
  automorphisms.automorphism_group_generator_morphisms: d60e1d906504e1c8a62f2e09593eb6d5e507b954e04ba8bc76392a0a5a741e04
  integral.primitive_orbits: 2b36458d1820a8de5252d650ca8868a27ab224936adacb33473df3588d204ffd
  integral.modular_scale: 67d1a103d53a97ae6017b3af3261d4fe0e4d602250c3bf8a1ec9b527cba5637e
  integral.anisotropic_primes: 3f31f08b81db07394881e97fcd0c10d7d53666cf291fa6edc725a6768ea094d0
  integral.local_representations: b8e2b975fc46264c563457dbc85fca871806fc19f06563ac0609d14ba5c0811a
  integral.local_densities: 09ba75cfb696c905c84f4564e860473f5b45237600282de85dba21d2d6660933
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, 4, -6]
- [0, 0, 0, -6, 12]
signature: [4, 1]
determinant: -24
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, 1, 1/2]
- [0, 0, 0, 1/2, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  modular_scale: false
  discriminant_group: [2, 2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{4,1} (2: [1^-2 2^3]_5; 3: 1^4 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  primitive_orbits:
    O:
      constant: 2
      z: []
      w: []
    O+:
      constant: 2
      z: []
      w: []
    SO:
      constant: 2
      z: []
      w: []
    SO+:
      constant: 2
      z: []
      w: []
    Otilde+:
      constant: 4
      z: []
      w: []
    SOtilde:
      constant: 4
      z: []
      w: []
    SOtilde+:
      constant: 4
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1, 7/8, 1, 5/4, 1, 5/4, 1, 47/64]
  - prime: 3
    densities: [8/9, 8/9, 34/27, 8/9, 8/9, 32/27, 8/9, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14]
indefinite:
  isotropic: true
morphisms:
- target: 3XPE
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3XPE
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3XPE
  name: O(L) generator 3
  matrix:
  - [-31, 0, -48, 0, 24]
  - [0, 1, 0, 0, 0]
  - [24, 0, 37, 0, -18]
  - [12, 0, 18, 1, -9]
  - [8, 0, 12, 0, -5]
  scale: 1
- target: 3XPE
  name: O(L) generator 4
  matrix:
  - [-15, 0, -24, -8, 24]
  - [0, 1, 0, 0, 0]
  - [12, 0, 19, 6, -18]
  - [4, 0, 6, 3, -6]
  - [4, 0, 6, 2, -5]
  scale: 1
- target: 3XPE
  name: O(L) generator 5
  matrix:
  - [-8, -3, -12, 0, 0]
  - [-3, 0, -4, 0, 0]
  - [6, 2, 9, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3XPE
  name: O(L) generator 6
  matrix:
  - [-1, 2, -4, 2, 0]
  - [2, -1, 4, -2, 0]
  - [2, -2, 5, -2, 0]
  - [2, -2, 4, -1, 0]
  - [1, -1, 2, -1, 1]
  scale: 1
- target: 3XPE
  name: O(L) generator 7
  matrix:
  - [0, 1, 0, 0, 0]
  - [-3, 0, -4, 0, 0]
  - [2, 0, 3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3XPE
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3XPE
  name: O(L) generator 9
  matrix:
  - [-31, 0, -48, 0, 24]
  - [0, 1, 0, 0, 0]
  - [24, 0, 37, 0, -18]
  - [0, 0, 0, 2, -3]
  - [4, 0, 6, 1, -4]
  scale: 1
- target: 3XPE
  name: O(L) generator 10
  matrix:
  - [-47, -2, -68, -10, 30]
  - [14, 1, 20, 2, -6]
  - [38, 2, 55, 8, -24]
  - [11, 1, 16, 4, -9]
  - [11, 1, 16, 3, -8]
  scale: 1
- target: 3XPE
  name: O(L) generator 11
  matrix:
  - [-21, 0, -36, 8, 12]
  - [0, 1, 0, 0, 0]
  - [18, 0, 31, -6, -12]
  - [10, 0, 18, -3, -9]
  - [8, 0, 14, -2, -7]
  scale: 1
- target: 3XPE
  name: O(L) generator 12
  matrix:
  - [-5, 2, -8, 2, 0]
  - [2, -1, 4, -2, 0]
  - [4, -2, 7, -2, 0]
  - [1, -1, 2, -2, 3]
  - [1, -1, 2, -1, 1]
  scale: 1
- target: 3XPE
  name: O(L) generator 13
  matrix:
  - [-5, 0, -12, 0, 12]
  - [0, 1, 0, 0, 0]
  - [6, 0, 13, 0, -12]
  - [6, 0, 12, -1, -9]
  - [4, 0, 8, 0, -7]
  scale: 1
- target: 3XPE
  name: O(L) generator 14
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICX, 3ID6.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICX, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICX, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICX, 3ID6.
