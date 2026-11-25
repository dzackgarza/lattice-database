---
tag: 4OHO
name: Constructed lattice 4OHO
latex: L_{\mathrm{4OHO}}
certifications:
  derive: e5fe88ade7a08ce5b2f8fff7c7dafc290e855997887a44e5f055cc93bcde54da
  form.integer_valued: bae670f8e5270e54180000cedc7fd5b3b2119fc6ad957a4e9ea635ee22225289
  integral.elementary_primes: 6946b9f4c7d8f3dc8ab36b0945c5ef0cebc6aa1ec1efab0ac61df867bd5e100c
  integral.genus_symbol: ebc42668049c5be9d64a2637fb738a667f33419efc15447e29e4c4eeb963c8f2
  integral.genus_class_count: dd0d845bb5269c575559a3a29d22cbfaafc493932ca20ae1d93eab7d15bd78c9
  integral.overlattice_count: 2596014b1a7d4a6c1c0dc25d2b96ce0f8da441d9fa9b38dcc10af92def55e78a
  integral.spinor_genus_count: cd9552fb16114cce2ff10773b74ed2c8ee9b2c772120b005474075b27d02b9c1
  integral.spinor_genera: 6ea958eaa9f65d46ca237b4af27f1eb94899878867d556dc891d8b236598f809
  automorphisms.automorphism_group_order: 73a3a67d6e641397ae5186060957fffa2f2f3958edd070767c50efdc09ff651a
  automorphisms.automorphism_group_generator_morphisms: 1dcdae9c6a939aefae5befb57ce7b1c18704a42e27e2c1780813b2a766074326
  integral.primitive_orbits: 7a84f379707bc70eabb76b7a4dd3f820bb18a79959854030935183cb5117dc12
  integral.modular_scale: 4cc6477b210172135521954a67ea31c601a8c5c05075b5c66205e1a4ecd22b2b
  integral.anisotropic_primes: 49402569fc72cb9c387170f90667ed4160232750864deeffbd89f53791648fd0
  integral.local_representations: a8d3b0a9e032282481d4ff9cd924e9cb02ee26955dde3dca7b7e6a96ccfc8205
  integral.local_densities: 3ca05003107c3b79425dbbc3aceaad364c72391c63a5cafa014cced4564b1056
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 0, 2, -1]
- [0, 0, 0, -1, 2]
signature: [4, 1]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 0, 2/3, 1/3]
- [0, 0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{4,1} (2: [1^-3]_1 2^2; 3: 1^4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
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
    Otilde:
      constant: 3
      z: []
      w: []
    Otilde+:
      constant: 3
      z: []
      w: []
    SOtilde:
      constant: 3
      z: []
      w: []
    SOtilde+:
      constant: 3
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [3/4, 3/2, 3/2, 15/32, 1/4, 3/2, 3/2, 9/16]
  - prime: 3
    densities: [8/9, 8/9, 32/27, 8/9, 8/9, 34/27, 8/9, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16]
indefinite:
  isotropic: true
morphisms:
- target: 4OHO
  name: O(L) generator 1
  matrix:
  - [-7, 12, -12, -12, 0]
  - [-6, 10, -9, -9, 0]
  - [6, -9, 10, 9, 0]
  - [-8, 12, -12, -11, 0]
  - [-4, 6, -6, -6, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 2
  matrix:
  - [-3, 4, -8, -6, 0]
  - [-4, 5, -8, -6, 0]
  - [2, -2, 5, 3, 0]
  - [-4, 4, -8, -5, 0]
  - [-2, 2, -4, -3, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 3
  matrix:
  - [-17, 24, -24, -24, 12]
  - [-12, 17, -16, -16, 8]
  - [12, -16, 17, 16, -8]
  - [-12, 16, -16, -15, 8]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, -2, 1, 2, -1]
  - [0, 2, 0, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 5
  matrix:
  - [-1, 0, -2, 0, 0]
  - [-1, 1, -1, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 6
  matrix:
  - [-1, 2, -4, -4, 2]
  - [-2, 3, -4, -4, 2]
  - [1, -1, 3, 2, -1]
  - [-2, 2, -4, -3, 2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 7
  matrix:
  - [-3, 8, -4, -6, 0]
  - [-2, 5, -2, -3, 0]
  - [4, -8, 5, 6, 0]
  - [-4, 8, -4, -5, 0]
  - [-2, 4, -2, -3, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4OHO
  name: O(L) generator 9
  matrix:
  - [-1, 4, -6, -6, 0]
  - [-3, 7, -9, -9, 0]
  - [2, -4, 7, 6, 0]
  - [-4, 8, -12, -11, 0]
  - [-2, 4, -6, -6, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 10
  matrix:
  - [-1, 6, -4, -6, 0]
  - [-2, 7, -4, -6, 0]
  - [3, -9, 7, 9, 0]
  - [-4, 12, -8, -11, 0]
  - [-2, 6, -4, -6, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 12
  matrix:
  - [-1, 2, 0, 0, 0]
  - [-1, 1, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OHO
  name: O(L) generator 13
  matrix:
  - [-3, 8, -4, -6, 0]
  - [-4, 8, -5, -6, 0]
  - [4, -9, 6, 8, -1]
  - [-4, 8, -6, -7, 0]
  - [2, -4, 2, 3, -1]
  scale: 1
- target: 4OHO
  name: O(L) generator 14
  matrix:
  - [-1, 0, -2, 0, 0]
  - [-2, 2, -3, -2, 1]
  - [1, -1, 3, 2, -1]
  - [-2, 2, -4, -3, 1]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4OHO
  name: O(L) generator 15
  matrix:
  - [3, -4, 4, 4, -2]
  - [-2, 2, -3, -2, 1]
  - [2, -3, 2, 2, -1]
  - [-2, 2, -2, -1, 1]
  - [-2, 2, -2, -1, 0]
  scale: 1
- target: 4OHO
  name: O(L) generator 16
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0013, 0012.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0001, 0013, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 0013, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0013, 0012.
