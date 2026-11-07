---
tag: 3IEW
name: Constructed lattice 3IEW
latex: L_{\mathrm{3IEW}}
certifications:
  derive: 5427aad8757a511919038acca51ff1d99a3149cc59b10036773715bf19308640
  form.integer_valued: 2bc681c52e35f1311515b61af1e3a55ee37f9f10d12ceddd4a28fe66728689f2
  integral.elementary_primes: 7a10a3c34ea06a62591d567e959af0ce86af697ab098d655ae97cb8c4944facc
  integral.genus_symbol: 83bed6f17c8a0d94a9cfe797c71e2beae16332df0bfbbab081bcbcf957f8ec58
  integral.genus_class_count: 758ea595b041d020862df83cc53cafe556f7869fd27c2271f675d335496dc4f8
  integral.overlattice_count: 75c52717836812e9876f855422dee72edb64f617259d65be1c15e3c75940a6b7
  integral.spinor_genus_count: 0a08236617c69aabf72bcd23754d8e0c124248ec553725599845184dc668cbdc
  integral.spinor_genera: bcbf34f52daff9e409daf74fca1b383b5f78236f1c69216bd259588dd33078df
  integral.hyperbolic_index: 8370c9ebf021331e622d9e9df4f2e909e61c038678392b070630c1579d5fc819
  automorphisms.automorphism_group_generator_morphisms: 0718f58e2a200cb2eb058886a95d4704521e0f20885d5e926d51234e2023bd9c
  integral.discriminant_form: 49ff291a2418c844257b66376d8bc60998e5093301daf90c3709dbb4e904ce19
  integral.primitive_orbits: 45567e4ec1f68fddc9b7f3fcda0979abfe0eb27a17177781e0c17461ccd59828
  integral.modular_scale: 8b93555fd4d1b6b2cda89459d2e6db70f3e4c6e2cb35e410f8d82fa4d39db28f
  integral.anisotropic_primes: 2276516da7c0d87e82c11a1e4f21bbc732eaa538568b88d798cda060a1b8431d
  integral.local_representations: e713e91b339eb57f8c3de1fb575ceaabe713152ff8cedded4786a8416860e2b1
  integral.local_densities: 3991650430e32ed229ae7dc2a04a97c3f794f17a336b86f88d9ca6750368c3c7
rank: 3
gram_tensor:
- [-2, 0, 0]
- [0, 0, -2]
- [0, -2, 0]
signature: [1, 2]
determinant: 8
definiteness: indefinite
dual_gram_tensor:
- [-1/2, 0, 0]
- [0, 0, -1/2]
- [0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: 4
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{1,2} (2: [2^3]_7)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 1
      z: []
      w: []
    SO:
      constant: 1
      z: []
      w: []
    Otilde:
      constant: 2
      z: []
      w: []
    SOtilde:
      constant: 2
      z: []
      w: []
    O+:
      constant: 1
      z: []
      w: []
    SO+:
      constant: 1
      z: []
      w: []
    Otilde+:
      constant: 2
      z: []
      w: []
    SOtilde+:
      constant: 2
      z: []
      w: []
  discriminant_form:
    orthogonal_group_order: 2
    isotropic_classes: 3
    isotropic_orbits: 2
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 2
    - representative: 7
      least_valuation: 2
    - representative: 2
      least_valuation: 1
    - representative: 6
      least_valuation: 1
    - representative: 10
      least_valuation: 1
    - representative: 14
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [0, 1, 0, 1, 0, 2, 0, 5/2, 0, 1, 0, 1]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IEW
  name: O(L) generator 1
  matrix:
  - [-1, 2, 0]
  - [0, 1, 0]
  - [2, -2, 1]
  scale: 1
- target: 3IEW
  name: O(L) generator 2
  matrix:
  - [-3, 2, -2]
  - [-2, 2, -1]
  - [2, -1, 2]
  scale: 1
- target: 3IEW
  name: O(L) generator 3
  matrix:
  - [1, 0, 2]
  - [-2, 1, -2]
  - [0, 0, 1]
  scale: 1
- target: 3IEW
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICX, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICX, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICX, 3ICZ.
