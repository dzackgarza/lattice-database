---
tag: 4WTT
name: Constructed lattice 4WTT
latex: L_{\mathrm{4WTT}}
certifications:
  derive: 79fdd6a64386a3ac97c3c3301a12a369de561691a41d90d974c3dd390b2d85d6
  form.integer_valued: fe689ffbdb68d769d7e13d65c588b14b49f9d35781950632e0a3e03624c2b926
  integral.elementary_primes: 0296c6bd0ff15457d431794fac2fada5562807d108c8bc7b8120e8c3da5fd319
  integral.genus_symbol: 8016e36c9a236310baa2f236d02f511878b88f6c2a6a64244626e9167d7fa474
  integral.genus_class_count: b6699702cd8e46a4f7c5ffd62250f64b785be7ecde4e6f24212f573cdfc6f15a
  integral.overlattice_count: baa5e1fb19cd7921dbec758202598d3e710330d0dbfb752d0a11edb10bdea771
  integral.spinor_genus_count: 8181ca9b73671763acb32566a6a2b96f79374d657d18eec7e03b64f086c7a5a1
  integral.spinor_genera: b826c777e7439c3e0aff69e1d39b897e89ba6ab44ba58cb9163b678ac661c669
  automorphisms.automorphism_group_order: 122fb84262b6119b11d6d936e1d8b85f51d72ed21755931f0189d81a1edf37ad
  automorphisms.automorphism_group_generator_morphisms: 14935ad2277267dd0f236631561951fda3786fcf5af6cde28a3ff5bddf4fa2ae
  integral.primitive_orbits: d74973fdbd893a290c38e5fa6a59e204e5d99aadaeb85eb9a575a2c088a9a92c
  integral.modular_scale: afa63603f482107f80e40fbaae9d1d972c48e2d806518f1214ee5a81c3565ec3
  integral.anisotropic_primes: f7eb2699aadd1af860f5add564f74f5ece14a0fa988a7efb1bd111ac6ec2a240
  integral.local_representations: 652d6a75f9e8d6aa354dc99dce28d5606510d1a70d0b5a48aa014648b6e1ffd9
  integral.local_densities: 656977f359a9b0b2d49ab1d16df3252d0ea51be3409645d5736e1a0911fdcc52
rank: 4
gram_tensor:
- [-1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, 2, 0]
- [0, 0, 0, -2]
signature: [1, 3]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, 1/2, 0]
- [0, 0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: 2
  discriminant_group: [2, 2]
  overlattice_count: 2
  bad_reduction_primes: [2]
  quadratic_character: -4
  genus_symbol: 'I_{1,3} (2: [1^2 2^2]_6)'
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
    densities: [1, 1/2, 1, 3/4, 1, 3/2, 1, 7/8, 1, 1/2, 1, 5/4]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 4WTT
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4WTT
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 4WTT
  name: O(L) generator 3
  matrix:
  - [-8, -3, -12, 0]
  - [-3, 0, -4, 0]
  - [6, 2, 9, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4WTT
  name: O(L) generator 4
  matrix:
  - [-1, 0, -2, 2]
  - [0, 1, 0, 0]
  - [1, 0, 2, -1]
  - [-1, 0, -1, 0]
  scale: 1
- target: 4WTT
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 0002, 3ICX.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 0002, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 0002, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICW, 0002, 3ICX.
