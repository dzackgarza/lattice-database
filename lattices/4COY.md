---
tag: 4COY
name: Constructed lattice 4COY
latex: L_{\mathrm{4COY}}
certifications:
  derive: 9464be60e95b073298f0b0e429aa10a33f324ab9bf070ea11db70d07a29e9685
  form.integer_valued: c3eb3d1d9e24ca3572f5f8445acaa39b36182fc39acaf2bc91726cc88551e873
  integral.elementary_primes: 721b9e0c801b9b3f8eeffe67f2982d3d0f006f4b1205a30a87cb3051d9427ad9
  integral.genus_symbol: e8d95aad498aacde9ff350d1ea1333a0a9390c613aa1e810dd42472e2f029726
  integral.genus_class_count: 83dd94f8897780ebe8d9d97edf2c087f218df678596f8c27c7e04476387e14b3
  integral.overlattice_count: 70cf8437ba89b77dfd010e0f66e8287d1966b52f961fafc94a42ff7d2e1369fd
  integral.spinor_genus_count: 75ba155fcbd1c3a87daabaf60d9b9341b330d4833231254a8a3e2034efbd40e4
  integral.spinor_genera: 76f9fb9dec5bf9fe38e1429cd8b3d37956fb62bc026a26926aff5bb8c9683c4c
  integral.hyperbolic_index: f2f93b6dfe97915f61cced0c31a9cdadb5daf0e20b42c8d912254328061bfeda
  automorphisms.automorphism_group_generator_morphisms: 364b8bedb6c2e48b46641d080d13c9265d46b163d97f74b6d70167be576c8dfd
  automorphisms.automorphism_group_order: 44f06f8ddf8aca6dcc497e5f34bc6a0a77bcc546ee67a1c7b5f114d28ccbbe0c
  integral.modular_scale: b6fbdfd20132a299b91ec19ac8894b7721c5b15cbfd66575cf9f10cc7da67c75
  integral.anisotropic_primes: a6f3996e7d71fc4b401db2e50aa3daca2a599ed48dae03dc714f50df67219629
  integral.local_representations: 2c5cd2ab6e8e972e7ca826ca47e9a90a7b82b6b62c3f9227bf5ffedd6ba78e38
  integral.local_densities: 6f7deafe79f7cbfa40374d5eed12cdd43d4331afa0bfbc09e9762a335200e348
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 2, 0, 0]
- [0, 0, 2, 0]
- [0, 0, 0, -2]
signature: [3, 1]
determinant: -8
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1/2, 0, 0]
- [0, 0, 1/2, 0]
- [0, 0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  bad_reduction_primes: [2]
  quadratic_character: -8
  genus_symbol: 'I_{3,1} (2: [1^1 2^3]_2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [3/2, 5/4, 3/2, 9/8, 1/2, 5/4, 1/2, 17/16, 3/2, 3/4, 3/2, 9/8]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9]
indefinite:
  isotropic: true
morphisms:
- target: 4COY
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4COY
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4COY
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4COY
  name: O(L) generator 4
  matrix:
  - [-17, 0, 0, -24]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [12, 0, 0, 17]
  scale: 1
- target: 4COY
  name: O(L) generator 5
  matrix:
  - [-1, 0, -2, -2]
  - [0, 1, 0, 0]
  - [-1, 0, 0, -1]
  - [1, 0, 1, 2]
  scale: 1
- target: 4COY
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4COY
  name: O(L) generator 7
  matrix:
  - [-7, 0, 2, -10]
  - [5, 0, 0, 7]
  - [0, 1, 0, 0]
  - [7, 0, -1, 10]
  scale: 1
- target: 4COY
  name: O(L) generator 8
  matrix:
  - [-15, 8, 8, -24]
  - [4, -2, -1, 6]
  - [4, -1, -2, 6]
  - [12, -6, -6, 19]
  scale: 1
- target: 4COY
  name: O(L) generator 9
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 3ICX.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0002, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 0002, 3ICX.
