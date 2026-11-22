---
tag: 5ICG
name: Constructed lattice 5ICG
latex: L_{\mathrm{5ICG}}
certifications:
  derive: 85457b8e6ada062c249d926f0178117d6bb479eb6f9e9f80d6000e43abc2a894
  form.integer_valued: 008b5136c8d7502c57ffde86c0cd63f6269e8dc502e73b96c55a9964cbb1b7f1
  integral.elementary_primes: f53950f063c98c9dbb3420289973d71d484042eb6225468e47e49aa0082787bd
  integral.genus_symbol: 03484ff4935c123d158581f6b560a75253e9c759714f679acaf35d71f09f964b
  integral.genus_class_count: 260a757c99d3227e17139d7e941dab7990f672968c7491a3f428a44a0036447d
  integral.overlattice_count: cd664ac3ecdc4532f732ee6cd29668ff9e20380f888c57e78e42d2636ad24442
  integral.spinor_genus_count: d7162acdba5bdd4a7b28f8e875e80c62f494c00a19b2ab57bf0a6da8a5f199d4
  integral.spinor_genera: 98f2db428c20d833471ce4b313958cb637370baead731d678c6a2551449a6873
  integral.hyperbolic_index: fd8f0ee78b71835bcef0107552bf8c1ab30661d0052b8b61afa804ab49ef11e7
  definite.automorphism_group_order: 03c37a83b076f9b0bd879fd3d73f6ec2c34e371f78a781e277f95eceaf5819d6
  definite.automorphism_group_generator_morphisms: 026c3ecf99d00c35f5c9b796fc799d55c7a9f98c32a4c80105f5269b3b3c877b
  integral.discriminant_sequence: b1129f2970d6563990ad25a43a0fa738bba920561a67f8e26d84abe85a405152
  integral.primitive_orbits: b0acdf41d9e0bb80b7dceefa9b352384f0cafe3e92160b0f8aa4253a2b33ddc6
  integral.modular_scale: bb80e8c15629a030f60ee3be531859f7a1c6e24b8428e2f04de3d973bf53381c
  definite.genus_theta_series: 698ea970f4fda059c573175940f18ed651b3b209e442f9d96263362bb460f5ea
  definite.theta_series_cuspidal_component: 19bdf123a988126dc2a31b3593f41ac4dd1fabac8c42e2948b3cee3bf39bea2e
  definite.siegel_eisenstein_coefficients: 5b237fd0d85bd5d7a0d1e11ec76f1d878bfb5f1bdb5c1a1462308a8a5706c500
  integral.anisotropic_primes: dfbb2e8aa5263d033536bd97987b25bc85a65cfd39730c223146b63f3f6bba0b
  integral.local_representations: de9adaff47db8a96fda7d6d68b6ead35619d557280f0428e80a99ad6202fbf51
  integral.local_densities: 7b1e085fb7462bc745154c9682829d195a30694af214f75236a3c3f95fd3f273
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2, 1, 0, 0]
- [0, 1, -2, 1, 1]
- [0, 0, 1, -2, 0]
- [0, 0, 1, 0, -2]
signature: [0, 5]
determinant: -4
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, -1, -1/2, -1/2]
- [0, -1, -2, -1, -1]
- [0, -1/2, -1, -1, -1/2]
- [0, -1/2, -1, -1/2, -1]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 2
  modular_scale: false
  discriminant_group: [2, 2]
  discriminant_sequence:
    discriminant_factors: [2, 2]
    discriminant_basis_lifts:
    - ['0', -1/2, '0', 1/2, '0']
    - ['0', -1/2, '0', '0', 1/2]
    discriminant_quadratic_gram:
    - ['0', 1/2]
    - [1/2, '0']
    discriminant_group_order: 6
    discriminant_generators:
    - - [1, 1]
      - [1, 0]
    - - [1, 1]
      - [0, 1]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [0, 1]
      - [1, 0]
    - - [0, 1]
      - [1, 0]
    - - [1, 1]
      - [0, 1]
    image_order: 6
    kernel_order: 384
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 4
  bad_reduction_primes: [2]
  genus_symbol: 'I_{0,5} (2: [1^3]_3 2^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    SO:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    Otilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 3]
    SOtilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 3]
    O+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    SO+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    Otilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 3]
    SOtilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 3]
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [3/2, 3/2, 3/4, 9/16, 3/2, 3/2, 1/4, 9/16]
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 2304
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 24, 48, 26, 48, 144, 192, 72]
  genus_theta_series: [1, 2, 24, 48, 26, 48, 144, 192, 72]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [2, 24, 48, 26, 48, 144, 192, 72]
  root_system: [D4]
  roots:
  - type: F4
    scale: -1
    simple_roots:
    - [0, 1, 0, -1, 0]
    - [0, 0, 0, 1, -1]
    - [0, 0, 0, 0, 1]
    - [0, 0, 1, 0, 0]
  - type: A1
    scale: -1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-1, -2]
morphisms:
- target: 5ICG
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5ICG
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 1, -1, 1, -1]
  - [0, 1, -1, 1, 0]
  - [0, 1, 0, 0, -1]
  scale: 1
- target: 5ICG
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, 1, -1, -1]
  - [0, 0, 1, 0, -1]
  - [0, 0, 1, -1, 0]
  scale: 1
- target: 5ICG
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, -1, 0]
  - [0, 0, 1, -2, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3IF8.
- tag: 3IF8
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3IF8.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3IF8.
