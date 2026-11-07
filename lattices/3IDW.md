---
tag: 3IDW
name: Constructed lattice 3IDW
latex: L_{\mathrm{3IDW}}
certifications:
  derive: ff84817c99dc17e5c70670441d3a74e788c2194d9e579714b6adc4fafca89793
  form.integer_valued: d05410e513be0e482e96cc09f7d449efa70e39a567768d1195a5cf5a16139d6e
  integral.elementary_primes: ec14c568fc3bf1219acf1ee6a412c4095656ff97bc4b6bb51a26e47f8747e1fb
  integral.genus_symbol: 341905e17cf6c19cf039779957809748f01ab067cd07fc8c4827443a2aac7bab
  integral.genus_class_count: 688f614af3d7799ede466851a2bf2b69b31b7c53ffc43093b9fff03039721802
  integral.overlattice_count: 68764f158e582d4da42daaf30f7dbfd421a5c7a48eb52c6e1bb9ec86f17157af
  integral.hyperbolic_index: 57e7b790192bffad21a28e9801c6e57101bf9ddf332dbcef9f8e347b9c97801b
  automorphisms.automorphism_group_generator_morphisms: ba9a66b9167b99ac47e20f89e672962995c92c8b1ea7db69aeae5b0718545ff0
  integral.primitive_orbits: 8ab1b0326bb90cb06add2fa5eb537c8dc90bc4437a9e0756868caa93aba5dfdc
  integral.modular_scale: 3022265b1f3d5fb99bc04501b28a541293553314de8122f1861887d1e9b232a2
  integral.anisotropic_primes: 835d3ac3bc3fba7f5fba7bc6ac0e6ffebb0cfaea0e3d9f5c1f24c6ef1d6993f7
  integral.local_representations: d4095f5f3ea8bb7be8b06ce30ffbf73be5532c4b57e2f21af86098e99486c9e8
  integral.local_densities: 62b67ca7e60341b85908dc00ba67be13f1203b7ef379218e258b022ae1b0e9b5
rank: 2
gram_tensor:
- [-1, 0]
- [0, 2]
signature: [1, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [-1, 0]
- [0, 1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: 2
  discriminant_group: [2]
  overlattice_count: 1
  bad_reduction_primes: [2]
  quadratic_character: 8
  genus_symbol: 'I_{1,1} (2: [1^1 2^1]_0)'
  genus_class_count: 1
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: []
      w: []
    SO:
      constant: 0
      z: []
      w: []
    Otilde:
      constant: 0
      z: []
      w: []
    SOtilde:
      constant: 0
      z: []
      w: []
    O+:
      constant: 0
      z: []
      w: []
    SO+:
      constant: 0
      z: []
      w: []
    Otilde+:
      constant: 0
      z: []
      w: []
    SOtilde+:
      constant: 0
      z: []
      w: []
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 7
      least_valuation: 0
    - representative: 2
      least_valuation: 1
    - representative: 14
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [2, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
indefinite:
  isotropic: false
morphisms:
- target: 3IDW
  name: O(L) generator 1
  matrix:
  - [-17, -24]
  - [12, 17]
  scale: 1
- target: 3IDW
  name: O(L) generator 2
  matrix:
  - [-3, -4]
  - [2, 3]
  scale: 1
- target: 3IDW
  name: O(L) generator 3
  matrix:
  - [-1, 0]
  - [0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0002.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 0002.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 0002.
