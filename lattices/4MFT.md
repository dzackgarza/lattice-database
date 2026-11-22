---
tag: 4MFT
name: Constructed lattice 4MFT
latex: L_{\mathrm{4MFT}}
certifications:
  derive: 7ba96a2f461a66b15fc7b9610cc675f8f77a561b9bfb184ce54cb5077ffe706d
  form.integer_valued: adfe940161f003fea0539795e36bb8966c18245647798fe53b1fc4a74bc897f7
  integral.elementary_primes: 4f1dad518cf1ef6a395f0dc748ba8718fa9a6706e050b1751c64aae6e4a6dc30
  integral.genus_symbol: 924fdada079681de21579f5d8ad04141740e1199dfb99009f34978b770020b1f
  integral.genus_class_count: a19cf7e1d64d2769692d3eaa3a9cbf931650b5bcfac6c2af5e276eef4dbb09b8
  integral.overlattice_count: 12aa7e0e78a0af0b5ab5e740d40210280c6133bcb894fe464614b8684fc625bd
  integral.spinor_genus_count: 3fdf918bca0b6342b93a8adc4b3371344585f465a1a03ec92f352fd78c489a0a
  integral.spinor_genera: ad5f67f4bd78020ad46557e2a5453f39fcfd8e5f1f667a6abb6f028c926ed4c3
  integral.hyperbolic_index: 90dccb75725cfbd31417828f947652b4234f108f3471031d6b005a9ca253a33b
  automorphisms.automorphism_group_generator_morphisms: 6801a0f059d96d91533f6477d3f4eb61659c694d4e30175d46df12cbe343998d
  automorphisms.automorphism_group_order: 1d332951106ed0c85b5af3e231d64141a912b916da4625364d93d3317625708e
  integral.modular_scale: ee3bc00d36087494ed48037b896a9d69c089370480a156ec7bcf34e0f77e47fd
  integral.anisotropic_primes: 5a6b090ff404865d99bd2ad2d2065e479a6a4dcb5ea1b5156c3167c797a71ec7
  integral.local_representations: fa1018909430a6cd23f08b3f02f2c1703eaf47b6331e9867d8a7df502c43f7f9
  integral.local_densities: 297e79d839553aba28ff71e83cbf08a7044a96b7b644b03c2e8909072e0453e3
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, -4, 6]
- [0, 0, 6, -12]
signature: [1, 3]
determinant: -24
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, -1, -1/2]
- [0, 0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  modular_scale: false
  discriminant_group: [2, 2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: -24
  genus_symbol: 'I_{1,3} (2: [1^-1 2^3]_4; 3: 1^-3 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1/2, 5/4, 3/2, 7/8, 3/2, 3/4, 1/2, 17/16, 1/2, 3/4, 3/2, 9/8]
  - prime: 3
    densities: [4/3, 2/3, 8/9, 4/3, 2/3, 10/9, 4/3, 2/3, 28/27, 4/3, 2/3, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: ['O(L) generator 1 #2', 'O(L) generator 2 #2', 'O(L) generator 3 #2', O(L) generator 4, O(L) generator 5, 'O(L) generator 6 #2', 'O(L) generator 7 #2', O(L) generator 8]
indefinite:
  isotropic: true
morphisms:
- target: 4MFT
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -2]
  scale: 1
- target: 4MFT
  name: O(L) generator 2
  matrix:
  - [9, 8, 12, -12]
  - [-4, -3, -6, 6]
  - [-6, -6, -8, 9]
  - [-2, -2, -3, 4]
  scale: 1
- target: 4MFT
  name: O(L) generator 3
  matrix:
  - [5, 4, 4, 0]
  - [-2, -1, -2, 0]
  - [-4, -4, -3, 0]
  - [-2, -2, -2, 1]
  scale: 1
- target: 4MFT
  name: O(L) generator 4
  matrix:
  - [3, 4, 0, 0]
  - [-2, -3, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4MFT
  name: O(L) generator 5
  matrix:
  - [3, 4, 0, 0]
  - [2, 3, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4MFT
  name: O(L) generator 6
  matrix:
  - [9, 8, 12, -12]
  - [-4, -3, -6, 6]
  - [-6, -6, -7, 6]
  - [-4, -4, -5, 5]
  scale: 1
- target: 4MFT
  name: O(L) generator 7
  matrix:
  - [7, 0, 12, -12]
  - [0, 1, 0, 0]
  - [-6, 0, -11, 12]
  - [-2, 0, -4, 5]
  scale: 1
- target: 4MFT
  name: O(L) generator 8
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 4MFT
  name: 'O(L) generator 1 #2'
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, -1, 1]
  scale: 1
- target: 4MFT
  name: 'O(L) generator 2 #2'
  matrix:
  - [9, 8, 12, -24]
  - [-4, -3, -6, 12]
  - [0, 0, 1, 0]
  - [2, 2, 3, -5]
  scale: 1
- target: 4MFT
  name: 'O(L) generator 3 #2'
  matrix:
  - [5, 4, 4, -12]
  - [-2, -1, -2, 6]
  - [2, 2, 3, -6]
  - [2, 2, 2, -5]
  scale: 1
- target: 4MFT
  name: 'O(L) generator 6 #2'
  matrix:
  - [9, 8, 12, -24]
  - [-4, -3, -6, 12]
  - [6, 6, 8, -15]
  - [4, 4, 5, -10]
  scale: 1
- target: 4MFT
  name: 'O(L) generator 7 #2'
  matrix:
  - [7, 0, 12, -24]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [2, 0, 4, -7]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ID5.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICX, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICX, 3ID5.
