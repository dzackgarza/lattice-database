---
tag: 3IDA
name: Constructed lattice 3IDA
latex: L_{\mathrm{3IDA}}
certifications:
  derive: 1bd9c9f002be5881c16c2fac77d52f97d0793cc279ebc75fcae3537e903e7493
  form.integer_valued: 7b8f16022770201c7730e80227694ea19f9c13e85b98ac099179dd479010e410
  integral.elementary_primes: 79670a2228af378d32dbbbbf4f800121ee07722a84262684215338f6a5c05f61
  integral.genus_symbol: 769fa66ad69b6ff1d8878a4c6591a91a5dfaf1ab75697c403bd7a339537321c7
  integral.genus_class_count: 99916d81cb36c76668c70c8f8af6248ad897be726c4ade0ed06a8b15f594598d
  integral.overlattice_count: 9fd17a3feba53f0ae59a5a2db2ccfdbe6cc690115f28c0656a0a2dc1f1426351
  integral.spinor_genus_count: c9e01ab8b8f2f579f92e618919d028bba9367e88076e72ffb6bbf75f0b7b7bfb
  integral.spinor_genera: e630754bc4ba3d8db030896c39ec7c9be3a47b45c3e3293ceb97e22197a78fcc
  integral.hyperbolic_index: b40d55208e17d60d285e6e9160106d7e355cb1231f4fc523d62d821463553c80
  automorphisms.automorphism_group_generator_morphisms: e1a990a2dd67ed4c37dba83bdaf164fb1e6ae43517db51f6502f6d76691c5e65
  integral.primitive_orbits: 24052bf51f63892f6979afe7283ad2961f17e15bdfc1091ba56ad0e08abbf96e
  integral.modular_scale: 922415750c691e618170a0ff600033084eacecc55c724dfeb47fcc24983866a6
  integral.anisotropic_primes: ceb2a13b769c0881f02e5fbb951e3be022a3409c03d5f933ecb657e915d296a5
  integral.local_representations: f7ed83882c605157b54dd7eeb626e20748677d9584b7602beb2a630ea1f46b3f
  integral.local_densities: 40aadf425105d04f5f6add9e7c00ce87724d13b2cfa844d52eeb753f47ba0138
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 1, 0]
- [0, 0, -1]
signature: [2, 1]
determinant: -1
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, 1, 0]
- [0, 0, -1]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 2
  modular_scale: 1
  discriminant_group: []
  overlattice_count: 1
  bad_reduction_primes: [2]
  genus_symbol: I_{2,1}
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
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
      constant: 1
      z: []
      w: []
    SOtilde:
      constant: 1
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
    densities: [2, 1/2, 1/2, 2, 1, 1/2, 1/2, 5/4, 2, 1/2, 1/2, 5/4]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 3IDA
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, 1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDA
  name: O(L) generator 3
  matrix:
  - [0, 1, 0]
  - [1, 0, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDA
  name: O(L) generator 4
  matrix:
  - [-2, 1, 2]
  - [-1, 2, 2]
  - [-2, 2, 3]
  scale: 1
- target: 3IDA
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICW.
