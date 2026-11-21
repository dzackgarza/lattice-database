---
tag: 6DHD
name: Constructed lattice 6DHD
latex: L_{\mathrm{6DHD}}
certifications:
  derive: eccd2f61b70f2a744fb1592f3d669031bb18a51b500fa493393b3ceb8c4c4f63
  form.integer_valued: b0b16fbf485830672928db9ab67f991cc3881e0bb6487108e69f395fb0e1ac3f
  integral.elementary_primes: 298e7f41ffa27033db7863b3d9fe9f5022e2fa914dddacb600982cbcd0a58a9f
  integral.genus_symbol: 5335ca3279ce24443449f5c10056f5ed36b2c37ee915a4689aa7f45091c490c2
  integral.genus_class_count: 9c7aa4a9e6837e10b8795c7e7133dadd393ff7c76a794bce1bef302e9139f52f
  integral.overlattice_count: f6c6558d037cad1f0cccbfa0e36c851398cde8939b7041eac3cd90d66cff7485
  integral.spinor_genus_count: 5d2e99ea9d0600e6f11fda6e8ca09e9f43653e0cf57e4c7eacf1c88be3c4246f
  integral.spinor_genera: a354ac0bc90bda8c66f9567d12e115a693658eee0990cec783511c47b2a8de9c
  integral.hyperbolic_index: 74ab93ae5f042ea59d0ea919a39e4455ef63d440b9e79681a3715084e12fe444
  automorphisms.automorphism_group_generator_morphisms: 74deeee2e583ded808d4acbcde584b5a104282c9384caad8467049245bfce7ab
  integral.discriminant_form: d7eb76a76056fadd6d42d2a05e406e2f0317a009ab5756582382f2c1f7e4f86e
  automorphisms.automorphism_group_order: 8e689943d833538d629c28bf64ad64cef35b2682212b2b0e35e623c7f444ad60
  integral.discriminant_orbits: 087a17137d45c029036beb38a9367f4f221f69c9484611031718eebac7f87cf7
  integral.modular_scale: f16d55cd3bbdfa48f344c18ea6363e735757b910e6d2ef50c454513ee33cd678
  integral.anisotropic_primes: f1305403f29f6738452a4846031855ba408746e3e9b8dad3db96c0f42042db63
  integral.local_representations: a9896b748bbbd35db0d08a5667e08759760b4928f8ec917eec160faef7434c08
  integral.local_densities: 91ab6838f91e08a9d2be901b70995821e5d979e9e4bacf23e06d2f12006f243c
rank: 4
gram_tensor:
- [0, 2, 0, 0]
- [2, 0, 0, 0]
- [0, 0, -4, 6]
- [0, 0, 6, -12]
signature: [1, 3]
determinant: -48
definiteness: indefinite
dual_gram_tensor:
- [0, 1/2, 0, 0]
- [1/2, 0, 0, 0]
- [0, 0, -1, -1/2]
- [0, 0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 6
  modular_scale: false
  discriminant_group: [2, 2, 2, 6]
  overlattice_count: 31
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{1,3} (2: 2^-4; 3: 1^3 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 240
    isotropic_classes: 6
    isotropic_orbits: 2
  discriminant_orbits:
    Otilde:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    SOtilde:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    Otilde+:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    SOtilde+:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    O:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    O+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
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
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [0, 0, 0, 5, 0, 0, 0, 5/2, 0, 0, 0, 5]
  - prime: 3
    densities: [2/3, 4/3, 8/9, 2/3, 4/3, 10/9, 2/3, 4/3, 26/27, 2/3, 4/3, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: ['O(L) generator 1 #2', O(L) generator 2, 'O(L) generator 3 #2', 'O(L) generator 4 #2', O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6DHD
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -2]
  scale: 1
- target: 6DHD
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DHD
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [1, 1, -1, 0]
  - [2, 0, -1, 0]
  - [1, 0, -1, 1]
  scale: 1
- target: 6DHD
  name: O(L) generator 4
  matrix:
  - [1, 1, -1, 0]
  - [1, 1, -2, 3]
  - [1, 2, -3, 3]
  - [1, 1, -2, 2]
  scale: 1
- target: 6DHD
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6DHD
  name: 'O(L) generator 1 #2'
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, -1, 1]
  scale: 1
- target: 6DHD
  name: 'O(L) generator 3 #2'
  matrix:
  - [1, 0, 0, 0]
  - [1, 1, 1, -3]
  - [1, 0, 2, -3]
  - [1, 0, 1, -2]
  scale: 1
- target: 6DHD
  name: 'O(L) generator 4 #2'
  matrix:
  - [1, 1, 1, -3]
  - [1, 1, 2, -3]
  - [2, 1, 3, -6]
  - [1, 1, 2, -4]
  scale: 1
related:
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 0013, 3ID5.
