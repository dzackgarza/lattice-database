---
tag: 6AVO
name: Constructed lattice 6AVO
latex: L_{\mathrm{6AVO}}
certifications:
  derive: 8c8e57f0ce81c65590dbc8132becb835a8386803444854fb9a5516dd0f194d31
  form.integer_valued: 439b48779382433df2f1e92613544ca9c9102b95aea6ae981d96a8c636ba8e5d
  integral.elementary_primes: 410570e665297758cd8d38252998efa8bef671685a3558de8e8bf9b83e9f7c57
  integral.genus_symbol: 890fe847e89149e6bb3b487b70b8ac8ca46913f6393afad6e904e6393111d8c7
  integral.genus_class_count: 0e6a54d6cb6fc1bcff856f42422873241b2f728edd23747ca26d5a0056b7b0fd
  integral.overlattice_count: 6c633d667972d51200272ddb836cb7a6ffffa0d9144bc5e5d2c6b3538528757f
  integral.spinor_genus_count: b3880cc4c2eca30eae167b28040db22e9108bc25dfbf6e13f951053eee685f3a
  integral.spinor_genera: 41016160dedc7eab39502fb4d289b97b5acd991d4aa7d22d405c28fe6143ce83
  integral.hyperbolic_index: 7794b54ac57a8f7bd84f9272c3bc275ea3847b914f357a575d89e0f3faad3829
  automorphisms.automorphism_group_generator_morphisms: 9d3c4c738573924ae33288bcc9badf805d9615b55755e1a7db3cedeca434de9e
  integral.discriminant_form: 9ff747da6aac3195fb7de6932b132bd2115d15b80b20dc6d389442eb185bf9c2
rank: 4
gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, -2, 1]
- [0, 0, 1, -2]
signature: [1, 3]
determinant: -3
definiteness: indefinite
dual_gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, -2/3, -1/3]
- [0, 0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: even
  level: 3
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{1,3} (2: 1^-4; 3: 1^-3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
  discriminant_form:
    orthogonal_group_order: 2
    isotropic_classes: 1
    isotropic_orbits: 1
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6AVO
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 6AVO
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [-1, 1, 2, -1]
  - [1, 0, -1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 6AVO
  name: O(L) generator 3
  matrix:
  - [1, -1, -2, 1]
  - [0, 1, 0, 0]
  - [0, -1, -1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 6AVO
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0]
  - [-1, 1, -1, 2]
  - [0, -1, 1, -1]
  - [0, -1, 0, -1]
  scale: 1
- target: 6AVO
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICY, 3ID0.
