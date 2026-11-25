---
tag: 4IGQ
name: Constructed lattice 4IGQ
latex: L_{\mathrm{4IGQ}}
certifications:
  derive: 8e61521978fae07fcd3117edeb255839c74b944a4614348b4cbb54e3e759da4c
  form.integer_valued: fb99695f11af0c3f38aae529c6739b588ace273b5ba18b6c98e7afe0c606ac56
  integral.elementary_primes: 7f0ec1fb8d95d5f909407b2e4b3776df841163c41ad2ced973e70af3a6ce8d67
  integral.genus_symbol: 64637b77e58645856ee95d615f259d3dbfc3141406455b38c7dc4b894b5f0787
  integral.genus_class_count: bf55e1d464304c21a88e1bc408b5cfe31032afec882d988c043406059c9ad715
  integral.overlattice_count: 6f7f5b1e56c156a2a4bd39f2814a08015d5b6f8f6e0a93f57dd8e958dc8310ee
  integral.spinor_genus_count: cfbe71f401acbf3afbd2181d4459f97539c2cc5cacbc62d1f3039f85396dd587
  integral.spinor_genera: b9c9b263d6f727765e4fc7a0bacf089544b7561b47d8301713c8af05fae3732d
  integral.hyperbolic_index: a86c5722f1bdaca58de079c130ceceb00ea58a8eaec323be8fa00302df0de9bd
  automorphisms.automorphism_group_order: 751c8aad7dd8f53be118e7bae2c5c1fd011165b4e8b828103a4fef002f0b1adf
  automorphisms.automorphism_group_generator_morphisms: 07717e7f50c6d5d68474ed183cc9f2d23b389c4ee5628ea63f353d653aa36455
  integral.primitive_orbits: 4a0dba05762650273f8dafcf6d9240ef352f3fc8304c614c40ba3488a2545c82
  integral.modular_scale: a65e8be1a97cecf736351618e4c58784b1faaee13219a03f082bc96766664152
  integral.anisotropic_primes: 15113b467daf6257e92b6c7fa5be6dadb3e76b1e021e9ebbc0c181c6c26a1402
  integral.local_representations: 79f41e4780b7986ccfb043ad39fa67a54f0c1278e905d25302a6e496a4809a37
  integral.local_densities: bb1f0ebedc453a06c7fd50677113a9fe7066dbc8c68b3edf9c24127dbad032f4
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, -2, 0]
- [0, 0, 0, 0, -2]
signature: [1, 4]
determinant: 16
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, -1/2, 0]
- [0, 0, 0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 11
  bad_reduction_primes: [2]
  genus_symbol: 'I_{1,4} (2: [1^1 2^4]_5)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 1
      z: []
      w: []
    O+:
      constant: 1
      z: []
      w: []
    SO:
      constant: 1
      z: []
      w: []
    SO+:
      constant: 1
      z: []
      w: []
    Otilde+:
      constant: 6
      z: []
      w: []
    SOtilde:
      constant: 6
      z: []
      w: []
    SOtilde+:
      constant: 6
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1/2, 1, 1, 13/16, 3/2, 1, 1, 9/8]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13]
indefinite:
  isotropic: true
morphisms:
- target: 4IGQ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4IGQ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4IGQ
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4IGQ
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4IGQ
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  scale: 1
- target: 4IGQ
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4IGQ
  name: O(L) generator 7
  matrix:
  - [3, 4, 0, 0, 0]
  - [-2, -3, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4IGQ
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4IGQ
  name: O(L) generator 9
  matrix:
  - [3, 2, -2, -2, -2]
  - [-1, 0, 1, 1, 1]
  - [1, 1, 0, -1, -1]
  - [1, 1, -1, 0, -1]
  - [1, 1, -1, -1, 0]
  scale: 1
- target: 4IGQ
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4IGQ
  name: O(L) generator 11
  matrix:
  - [3, 4, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [2, 3, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4IGQ
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4IGQ
  name: O(L) generator 13
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ICX, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ICX, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICX, 3ICX, 3ICX, 3ICX.
