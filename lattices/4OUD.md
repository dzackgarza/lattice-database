---
tag: 4OUD
name: Constructed lattice 4OUD
latex: L_{\mathrm{4OUD}}
certifications:
  derive: 39dd5a6d47e170c81db476a3ce2b67ff5d180b928ff97639d3f727a6d87d745c
  form.integer_valued: cf8432a908b83a7b344fc41221c1d2bc5aba76167369fbb04d6217650ea0be79
  integral.elementary_primes: 4c1817d1d889e4ce4588ca8b2fb3109c7759678e7be46d64423cd3b4a74a723a
  integral.genus_symbol: 4a2268e7122b88b462529f283f135b2682487d34048c3c9940ec06e073aaea00
  integral.genus_class_count: 2a18d3c4599f76056a641881a0bfc216428b906e472cfc0031430d886264ff6a
  integral.overlattice_count: af93171a7575a25490665a3fa5ed961faeba83d3cada9a9b8d873d97082def91
  integral.spinor_genus_count: a1fec851b4aa90db84ed089f7a166d672dbd0621e8b79bccb69e8ecc1f3de6a6
  integral.spinor_genera: 55b2e64205158cdd1a78588c56582851d87525a572eb83ad5d801cfaf78ad989
  integral.hyperbolic_index: a23333f9bf01df2979a6c4c4a1063a76a68b999d5f8165cc11281c9913cd12d7
  automorphisms.automorphism_group_order: 447e708772dfad7026f4be95a15b0b8c8d30d5d514f5dc9d9232772f41fdcd10
  automorphisms.automorphism_group_generator_morphisms: c56dfe95eb18d717ac33d3249452ecf9420235e4fa17d13ed30b5a7934998c0c
  integral.primitive_orbits: 5408cded5ada89c18fef5f88b2d038cf69f111a0b07b2e87fe0dcbc24d9e0a6a
  integral.modular_scale: 17a39b07780841cb99af57b7358727ef79dff730b0cd5a0cada11cc76e449f5d
  integral.anisotropic_primes: 3162c8338726be45556104c7c6d3b2782317eed59dcc7ac87ad99725e5d61105
  integral.local_representations: b3afc49425bdafab704442f6bc3f23e454ad04947bcf30ce27c4fcad8c280597
  integral.local_densities: 1dff36059221d6b08cb4ef570dced6edbe4ddc8424c89cfaa443f3f7c7bc9108
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, 0, 0, -2]
- [0, 0, 0, -2, 0]
signature: [3, 2]
determinant: 16
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, 0, 0, -1/2]
- [0, 0, 0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 2
  modular_scale: false
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 31
  bad_reduction_primes: [2]
  genus_symbol: 'I_{3,2} (2: [1^1]_1 2^4)'
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
    Otilde:
      constant: 15
      z: []
      w: []
    Otilde+:
      constant: 15
      z: []
      w: []
    SOtilde:
      constant: 15
      z: []
      w: []
    SOtilde+:
      constant: 15
      z: []
      w: []
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 2
    - representative: 2
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [5/2, 0, 0, 35/16, 3/2, 0, 0, 15/8]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20]
indefinite:
  isotropic: true
morphisms:
- target: 4OUD
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4OUD
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 3
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  scale: 1
- target: 4OUD
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [0, -1, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 1]
  - [0, -1, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 1]
  - [0, 0, 1, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-1, 0, 0, 1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 2, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, -2, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, -4, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [-2, 0, 0, 4, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 11
  matrix:
  - [1, -2, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [-1, 1, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 12
  matrix:
  - [1, 0, -4, 0, 0]
  - [-2, 1, 4, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  scale: 1
- target: 4OUD
  name: O(L) generator 14
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4OUD
  name: O(L) generator 15
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 16
  matrix:
  - [1, 0, 2, 0, 0]
  - [-1, -1, -1, 0, 1]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 1, 1, 0]
  scale: 1
- target: 4OUD
  name: O(L) generator 17
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 1, -1, 1]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, 0, 1]
  - [0, 0, -1, 1, 0]
  scale: 1
- target: 4OUD
  name: O(L) generator 18
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, 1, -1, 1]
  - [0, 1, 0, 0, 1]
  - [0, -1, 0, 1, 0]
  scale: 1
- target: 4OUD
  name: O(L) generator 19
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OUD
  name: O(L) generator 20
  matrix:
  - [-1, 0, -2, 0, 2]
  - [-1, 0, -1, 1, 1]
  - [0, 0, 0, 0, 1]
  - [0, 0, 1, 0, 0]
  - [1, 1, 1, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICZ, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICZ, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICZ, 3ICZ.
