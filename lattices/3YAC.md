---
tag: 3YAC
name: Constructed lattice 3YAC
latex: L_{\mathrm{3YAC}}
certifications:
  derive: 36a88b925d459af980b8257e5664b7c64397e9204919d8f1f5480f100562ddc5
  form.integer_valued: 92b6b3500b7df331abe326d576684e87c727d87531b93710368947167e8ff801
  integral.elementary_primes: 0c3ee0bfea42f94e7d143897d254200c5e9182afb050b606f1d633dc9a50e55e
  integral.genus_symbol: dde889ee8c3fbb3c4f20200bde07456ead1b5a00cd428a6de1123f43c4386290
  integral.genus_class_count: fcd5549177e5eb5ca6b33fb957a065449bc98385ae532f32c86edc55438f086e
  integral.overlattice_count: d1a768155000020354a17832aa4701955227c8cbb9d65eeb4b3b88c98f73249f
  integral.spinor_genus_count: 59e522fb3e6ee23805db3c5d634d1dd08246f43bc94eba02b0c6e6efc6b517aa
  integral.spinor_genera: 056f333f6d3436a68c390f6c48be159a2daa96ad6200887af48d4240c1b713f5
  integral.hyperbolic_index: 8130a519154a29f1bfbe1d95442a27700052d66173f28fdc05796dd8e55785cd
  automorphisms.automorphism_group_generator_morphisms: 8d6132d21173a102b4b7885068ca48164088c794101d0e8841e1afc302463f6a
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 0, -1]
- [0, 0, -1, 0]
signature: [3, 1]
determinant: -1
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 0, -1]
- [0, 0, -1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 2
  discriminant_group: []
  overlattice_count: 1
  bad_reduction_primes: [2]
  quadratic_character: -4
  genus_symbol: I_{3,1}
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 3YAC
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3YAC
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 3YAC
  name: O(L) generator 3
  matrix:
  - [0, -1, -1, 0]
  - [-1, 0, -1, 0]
  - [0, 0, 1, 0]
  - [1, 1, 1, 1]
  scale: 1
- target: 3YAC
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0]
  - [-1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3YAC
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICY.
