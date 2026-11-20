---
tag: 4AQJ
name: Constructed lattice 4AQJ
latex: L_{\mathrm{4AQJ}}
certifications:
  derive: 5b25ed4537767f14d2440de1beb5c8a1b80857d8ee7c592c3dedeafb626ee453
  form.integer_valued: e2b26a0314b253adea44a4a9facaf39e185779e76783bea623611296d0cd6343
  integral.elementary_primes: fb1129cd2c52c4ccce2548288f6d9d7ab68d828c7bf14609a9675a6f2cf867ba
  integral.genus_symbol: 9695179324689c715fcbbdb4d6a55a113181196917b6733a1c10ccb361b4dcef
  integral.genus_class_count: 35d69c41db73207ec003e4d1e1945a6d69813f045443c535de45347b1b0908a4
  integral.overlattice_count: 7a5e4fa1c43a50427793c5bbd7559d4e11c0f12649b14c72d8318b5673af92dd
  integral.spinor_genus_count: ef1d2280ec4945ac3924fe2c2dd07df4dccf927a5a7f02025af26c7eba4767d4
  integral.spinor_genera: 028c8fd0de8b5c504a437bc1ca60869f3b37ae7a8c5648e9019a7dd52c891f7b
  automorphisms.automorphism_group_order: 9b46d8cf2a9acb67114f68ef30ddbfd14f1f366a3d18e801e3e8383d0a5a2896
  automorphisms.automorphism_group_generator_morphisms: c98da1eb600e56af7e1b08e52dbf0429fcb110e2f4a11a50bca9a712e3da04f9
  integral.primitive_orbits: 629f8110a70ec825b6885403eae7867c177c8a2b34fe5d167fad2a0ca64839ad
  integral.modular_scale: 0d58cc34d9fe83c321804efcaf76f84fc1627e0bbff3ba0316d8dd8b300b78b9
  integral.anisotropic_primes: 750a4a36e0c681d0997af211b86fa70732c0fc8ea1fd742848d6cc3ee40f44bd
  integral.local_representations: 650a46dd5b6c9f815800ca87b48fa0626a9e701fe5effa1bcc78a2388b6f7607
  integral.local_densities: 55a121da2d51f9b774a48a0b44e4899cba583fdd4cc181136ab3871a8e730fde
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, 2, -1]
- [0, 0, -1, 2]
signature: [3, 1]
determinant: -3
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, 2/3, 1/3]
- [0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'I_{3,1} (2: [1^-4]_0; 3: 1^3 3^-1)'
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
    densities: [1, 3/2, 1, 1/4, 1, 3/2, 1, 7/8, 1, 3/2, 1, 1/4]
  - prime: 3
    densities: [2/3, 4/3, 8/9, 2/3, 4/3, 10/9, 2/3, 4/3, 26/27, 2/3, 4/3, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 4AQJ
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4AQJ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 4AQJ
  name: O(L) generator 3
  matrix:
  - [0, 1, 1, 1]
  - [-1, 2, 1, 1]
  - [1, -1, 0, -1]
  - [1, -1, -1, 0]
  scale: 1
- target: 4AQJ
  name: O(L) generator 4
  matrix:
  - [-2, 3, 3, 0]
  - [-3, 4, 3, 0]
  - [2, -2, -1, 0]
  - [1, -1, -1, 1]
  scale: 1
- target: 4AQJ
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 0012.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICW, 0012.
