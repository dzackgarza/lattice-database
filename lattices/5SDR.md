---
tag: 5SDR
name: Constructed lattice 5SDR
latex: L_{\mathrm{5SDR}}
certifications:
  derive: 4175abd77a297b01d34688a09456d3a0efeaf5a6688470703504706ed59fdaa8
  form.integer_valued: 75ce61b28a64652212362fb6c4c0f8ba5697e071bac4ff9ad075602e9dd05eb0
  integral.elementary_primes: 7c79efb13fb34d50afa51fff0c1d1f3dae6b16cd6aa872b266a53fb62d87c3d3
  integral.genus_symbol: 2f6e6e8577845cc4074ed4376c8f428e61a1da49bd6ac9cf8d3416b3b0f3fcb4
  integral.genus_class_count: 3dc75abe246a795c18db080c52acf370df5336d52b940606f43b962b07236318
  integral.overlattice_count: 383d22f4944080aa8bf15ef7fa7a26377b10d7cdafeea9699e9215f05d463db3
  integral.spinor_genus_count: 089b948c59834f9e9c93f2f9b05a36bd18d72b239a2c1ec9ad4fcc6611a8f5cc
  integral.spinor_genera: 8100490dbbae7231e1d488682d9e156a423db0872a5fb154f88c740a3ba6c3dd
  integral.hyperbolic_index: 6ac87915b108d99cb5dae7e75eb25a3ec1e3d1102b0d5bb9ab4a2c89333f545f
  automorphisms.automorphism_group_generator_morphisms: eb9043add816a89197c544665cf08a221096a8ee06a52a1cb4bcdeaebd30e3b7
  integral.discriminant_form: 8b6eefae6068fe6f5ce67d759cb7ab9fd36555632a0de775a92b07ccca4335fc
  automorphisms.automorphism_group_order: fbed43bb44a271deb591cd78e348d16bb227f68457ae88892e5d8a28427eef51
  integral.discriminant_orbits: f42a1ff3c6a20452347419a39f83522277943f97efe92b4b917d468bc67b8048
  integral.modular_scale: a9b211a6e27a4c9df956238353489ae1c5fcb715e9f29377eec76548023e11fc
  integral.anisotropic_primes: 2837ac8b6fb62529d25446761cf1f196ad849635e99a493e56a70cd2b905e058
  integral.local_representations: 13c68999a803dafc1c424ae6e53180165b8d1eb8952c88d00925122f9e8932c1
  integral.local_densities: d4426df1c989d2d66f109a6bf39ae9c970dd578c165aa3a309d664ec2f21330c
rank: 4
gram_tensor:
- [2, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, -2, 1]
- [0, 0, 1, -2]
signature: [1, 3]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, -2/3, -1/3]
- [0, 0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  modular_scale: false
  discriminant_group: [2, 6]
  overlattice_count: 2
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{1,3} (2: 1^-2 [2^2]_0; 3: 1^-3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
  discriminant_form:
    orthogonal_group_order: 2
    isotropic_classes: 2
    isotropic_orbits: 2
  discriminant_orbits:
    Otilde:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    SOtilde:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    Otilde+:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    SOtilde+:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    O:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    SO:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    O+:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
    SO+:
      constant: 2
      z: [0, 2, 0, 1]
      w: [0, 2, 0, 1]
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
    densities: [0, 2, 0, 3/2, 0, 2, 0, 11/4, 0, 2, 0, 3/2]
  - prime: 3
    densities: [4/3, 2/3, 10/9, 4/3, 2/3, 8/9, 4/3, 2/3, 28/27, 4/3, 2/3, 10/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9]
indefinite:
  isotropic: true
morphisms:
- target: 5SDR
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5SDR
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 5SDR
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 5SDR
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 5SDR
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 5SDR
  name: O(L) generator 6
  matrix:
  - [3, -2, -2, 1]
  - [2, -1, -2, 1]
  - [2, -2, -1, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 5SDR
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5SDR
  name: O(L) generator 8
  matrix:
  - [7, 0, -6, 0]
  - [0, 1, 0, 0]
  - [8, 0, -7, 0]
  - [4, 0, -4, 1]
  scale: 1
- target: 5SDR
  name: O(L) generator 9
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ID0.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICX, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICX, 3ID0.
