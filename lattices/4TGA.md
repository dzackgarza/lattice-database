---
tag: 4TGA
name: Constructed lattice 4TGA
latex: L_{\mathrm{4TGA}}
certifications:
  derive: ead90536655ae01a25f827ab7b265d2ecebd7bee84d7b745856f0a2c9a07faa2
  form.integer_valued: 25f0e35d4c4878d82b6fc5799aa45df1cfc3b1604a13ecf9d2238a939d5353dc
  integral.elementary_primes: 280b0e3a3e258e49af6c7d401f98963ccfeee1fdb5bd6f8c11e7482ba28ef35e
  integral.genus_symbol: 007793c3a98b7cd8bb989c8c3f89e06398418f6b6474cc043b80a93a7fefb78d
  integral.genus_class_count: f3f5a5b84f351b6c67020bc39d16f87d2713fef45293287ba62bdae6ce597341
  integral.overlattice_count: 96ceebcf0875802a4cf6dc737c47f92330d66e2a8afaf937f39ec554d45733a5
  integral.spinor_genus_count: 10c46f420c44c7d4d5c9b314ec959b9bb346d72d00d40a928465387b6a99f583
  integral.spinor_genera: 0eedfa74c06482524a023ca8a9a446c13f67160ef5a0bacae853d8b6594fe6e7
  automorphisms.automorphism_group_order: 563095275ecee072247b533b9e70afc373df6f1d85d4f181eaf75215118ec49f
  automorphisms.automorphism_group_generator_morphisms: 51862dea4326b817bdc5ef9a416781457bf158d562395affb1d1659d920c5e97
  integral.primitive_orbits: e3804152bad8778371bb1f633d253b0243d2d8dd1b219b2a03a28c2b9f5c9289
  integral.modular_scale: 5eb118f0990fc91dc5f21ff2d692635cbd58964c3ea45c16de0463d6b18dec17
  integral.anisotropic_primes: 41309ca6acc371dadf813e998042335365e5036e537a3960b3e9ffeebc22e755
  integral.local_representations: 19a7b8f4e8988635c6808fb7ae5d7d6376e75d5eae3d4542e557ba75cafdf33f
  integral.local_densities: d5b754f32908d025a84aa2d7b4eaca254c0a0c3a774588309a4802caa2a69ca7
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 2, 0]
- [0, 0, 0, 0, -2]
signature: [1, 4]
determinant: 4
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 1/2, 0]
- [0, 0, 0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2, 2]
  overlattice_count: 2
  bad_reduction_primes: [2]
  genus_symbol: 'I_{1,4} (2: [1^3 2^2]_5)'
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
      constant: 2
      z: []
      w: []
    SOtilde:
      constant: 2
      z: []
      w: []
    SOtilde+:
      constant: 2
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [3/4, 1, 1, 29/32, 5/4, 1, 1, 17/16]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11]
indefinite:
  isotropic: true
morphisms:
- target: 4TGA
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4TGA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4TGA
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4TGA
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4TGA
  name: O(L) generator 5
  matrix:
  - [-8, 0, -3, -12, 0]
  - [0, 1, 0, 0, 0]
  - [-3, 0, 0, -4, 0]
  - [6, 0, 2, 9, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4TGA
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, -2, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [1, 0, 0, 2, 1]
  - [-1, 0, 0, -1, 0]
  scale: 1
- target: 4TGA
  name: O(L) generator 7
  matrix:
  - [-8, 0, 3, -12, 0]
  - [0, 1, 0, 0, 0]
  - [3, 0, 0, 4, 0]
  - [6, 0, -2, 9, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4TGA
  name: O(L) generator 8
  matrix:
  - [-1, 0, 0, -2, 2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [1, 0, 0, 2, -1]
  - [-1, 0, 0, -1, 0]
  scale: 1
- target: 4TGA
  name: O(L) generator 9
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4TGA
  name: O(L) generator 10
  matrix:
  - [-11, 6, 2, -18, 2]
  - [6, -3, -2, 10, -2]
  - [2, -2, -1, 4, 0]
  - [9, -5, -2, 15, -2]
  - [1, -1, 0, 2, -1]
  scale: 1
- target: 4TGA
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 0002, 3ICX.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 0002, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 0002, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 0002, 3ICX.
