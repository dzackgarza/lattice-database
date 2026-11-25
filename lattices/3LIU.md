---
tag: 3LIU
name: Constructed lattice 3LIU
latex: L_{\mathrm{3LIU}}
certifications:
  derive: 7fb3b8575c50705efb840186ce2fb4060f23e2f34bb6b0af19178818b6907c10
  form.integer_valued: a1ff4ee9bda53d73d560bca6676525ee655720702b9628a99e4dbb2c5a7b25e0
  integral.elementary_primes: f5c58925173110262b3062986468341b173b78b72480f17c7034c5b665c87a6a
  integral.genus_symbol: 8c2c212821ee508143ed313555be6833890c150481426a297ac5d07fc33257fa
  integral.genus_class_count: effdee99ddbcc66f0c0e3454cd8023e029c9c840e6443cf6060f2326b284c736
  integral.overlattice_count: 64c4dca42f0c9a463bce9ce9d09fad14b64a309e8175e814f7bd2ad3ef593d6b
  integral.spinor_genus_count: 05f091116a8682b89cbc75674bfa55319ca7a0b6fc6abadf7cb3b803b932095e
  integral.spinor_genera: 11bfa2a1e9df6cdcae232f19ee5e85978e44aca718b77613c728eb3d393ca09d
  automorphisms.automorphism_group_order: 3469f82a8f96edf8b67cec2c66d069f0cebce4d9400bcf55b6f9499531064a09
  automorphisms.automorphism_group_generator_morphisms: 234b14770eeed2dd76d92aede0b57213ad3bcf0cd687a884f7d3f4410b7df7be
  integral.primitive_orbits: 8bd49fb25331922bb0f88f49faf391397580ddcc784d085fa4aab9fa2c127c2c
  integral.modular_scale: 2e1fd2c6767980db9c6f6cad9df0413053e49c73e38d5dcb78f7dac3abcd4de0
  integral.anisotropic_primes: 4655c4e99b7535a061636e0e465760350b9e9faf3052739489dc795abc586299
  integral.local_representations: b572989edf533a4c526dcc5509a8b35d3c849de80117e52411597b118923222b
  integral.local_densities: acdefdbf0d69227705852700bebb6be042502856f144d511281a95419a0a9d7c
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 0, 0, -1, 0]
- [0, 0, 0, 0, 2]
signature: [4, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 0, 0, -1, 0]
- [0, 0, 0, 0, 1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2]
  overlattice_count: 1
  bad_reduction_primes: [2]
  genus_symbol: 'I_{4,1} (2: [1^4 2^1]_3)'
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
      constant: 1
      z: []
      w: []
    Otilde+:
      constant: 1
      z: []
      w: []
    SOtilde:
      constant: 1
      z: []
      w: []
    SOtilde+:
      constant: 1
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1, 9/8, 1, 9/8, 1, 15/16, 1, 57/64]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10]
indefinite:
  isotropic: true
morphisms:
- target: 3LIU
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3LIU
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3LIU
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3LIU
  name: O(L) generator 4
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3LIU
  name: O(L) generator 5
  matrix:
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3LIU
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3LIU
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 2]
  - [0, 0, -1, 2, 2]
  - [0, 0, 1, -1, -1]
  scale: 1
- target: 3LIU
  name: O(L) generator 8
  matrix:
  - [-1, 1, 0, 3, 4]
  - [-1, 0, -1, 3, 4]
  - [0, 1, -1, 3, 4]
  - [-1, 1, -1, 6, 8]
  - [0, 0, 0, -2, -3]
  scale: 1
- target: 3LIU
  name: O(L) generator 9
  matrix:
  - [0, 0, 3, 4, 4]
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 4, 5, 4]
  - [0, 0, -2, -2, -1]
  scale: 1
- target: 3LIU
  name: O(L) generator 10
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0001, 3ICW, 0002.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0001, 3ICW, 0002.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0001, 3ICW, 0002.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0001, 3ICW, 0002.
