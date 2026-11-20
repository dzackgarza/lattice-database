---
tag: 5DFP
name: Constructed lattice 5DFP
latex: L_{\mathrm{5DFP}}
certifications:
  derive: 0f67343750f533da3aec3b32e5a1e4305730ef28f0f713234f79723c5957b48c
  form.integer_valued: 8c0aad16e3954ccebff385c30723c492e7ffa20abfe8166d161a5c2359d9f123
  integral.elementary_primes: 9d0c4ac7185a63ab26b6fc0fa4c1a1fdd2068ec99589ebb312c6436a12783769
  integral.genus_symbol: 33ab4976efacb25a65e63a45f5cbe5f15a3eebb46f34ec18c3e287e408399235
  integral.genus_class_count: 9810f396d0a0c3659ab112c815e02b07473d121d269300ae736f0e9db7553eda
  integral.overlattice_count: 413c520f0cb5437eb53ed8ccb494a5b7af979901b042baead4b4fbcc03085c56
  integral.spinor_genus_count: 5e345aa2d18d351fcc7fbaab989a52940f8286d0d5de8067c1b98286cff87ab4
  integral.spinor_genera: 9458b2c497eef28c59d80c735c443373514b67bf66b24a6399890ee0a916278e
  integral.hyperbolic_index: f1a5de1ec406d825a2713e9f599d16d936dd037aa4b32ac353ac1f7fa4384b6b
  definite.automorphism_group_order: 3d302413217d4967e9ff20fcfde7d42868a0c5e3f2839c4abde74dcdd893cbe0
  definite.automorphism_group_generator_morphisms: 17eaed778c7d60e46207b5fd90529052708f360833f0ab14bf19e49bccfa1d00
  integral.discriminant_sequence: eeedeeb1508ff659a93c7d27506fa7db595f5ccf9d9ea1b76b9fca2f62f7a18e
rank: 4
gram_tensor:
- [-1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, -4, 6]
- [0, 0, 6, -12]
signature: [0, 4]
determinant: 24
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, -1, -1/2]
- [0, 0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  discriminant_group: [2, 2, 6]
  discriminant_sequence:
    discriminant_factors: [2, 2, 6]
    discriminant_basis_lifts:
    - ['0', 1/2, '0', '0']
    - ['0', '0', 1/2, '0']
    - ['0', '0', '0', 1/6]
    discriminant_quadratic_gram:
    - [1/2, '0', '0']
    - ['0', '0', 1/2]
    - ['0', 1/2, 2/3]
    discriminant_group_order: 12
    discriminant_generators:
    - - [1, 0, 0]
      - [0, 1, 3]
      - [0, 1, 4]
    - - [1, 0, 0]
      - [0, 1, 3]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 3]
      - [0, 0, 5]
    image_generators:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    - - [1, 0, 0]
      - [0, 0, 3]
      - [0, 1, 5]
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 1, 5]
    image_order: 12
    kernel_order: 4
    coset_representatives:
    - - [1, 0, 0]
      - [0, 1, 0]
      - [0, 0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  quadratic_character: 24
  genus_symbol: 'I_{0,4} (2: [1^-1 2^3]_2; 3: 1^3 3^-1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 48
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 2, 4, 8, 12, 16, 24, 14, 6, 24, 4, 22]
  root_system: [A1]
  roots:
  - type: G2
    scale: -2
    simple_roots:
    - [0, 0, 1, 0]
    - [0, 0, 0, 1]
  - type: A1
    scale: -1
    simple_roots:
    - [0, 1, 0, 0]
  - type: A1
    scale: -1/2
    simple_roots:
    - [1, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1]
  norms: [-1, -2, -4]
morphisms:
- target: 5DFP
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5DFP
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5DFP
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -1]
  scale: 1
- target: 5DFP
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -3]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID5.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICX, 3ID5.
