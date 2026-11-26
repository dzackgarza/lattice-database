---
tag: 5ALI
name: Constructed lattice 5ALI
latex: L_{\mathrm{5ALI}}
certifications:
  derive: 02fae691d6494530d426e5c80dbb411b0f80ae3cb8b18972ccf41d51a5e9cceb
  form.integer_valued: c9d450ee6184d320241bad065f9db5e6de752f86e55cb9ce6aa90221943ce973
  integral.elementary_primes: efb5ca5825a92338ae6778b9b3bcf52f016336d23d7a617d0412bd2b70a0b93c
  integral.genus_symbol: e2625bb3033fe15c79a70d73080cd353c78db20fe24f62075add92a404d1dca4
  integral.genus_class_count: 2d577950bc00ef871f3b453b32f0b81b45c33243af34d98f3901c7d60393d938
  integral.overlattice_count: 74b63135e4c4da68cd4c739b9d8cfd9cdb2bd31a41461a6a7c92e44113926750
  integral.spinor_genus_count: ef9669bd553c7e0f1790eb1e4fe91b93f93b6561644fbf410fde48e8c07796b7
  integral.spinor_genera: 4528350d73fc5beceb6ec751ed59c1c49ff4e6749012e1754ef3281f121fb3c2
  integral.hyperbolic_index: d8f4c0ea94088d29b7ef9fe73d2e7f2ac04c1de1251da2c87cb969ea45473379
  definite.automorphism_group_order: 6d225c29f9cbbaf6c1333b4d2c2b0499dd33625d4c95e9fbcbffaf2e3d37ffab
  definite.automorphism_group_generator_morphisms: f5c37574f010a803dd9d7bf0d741985e429fd5ff75218230fc664b69a527700b
  integral.discriminant_sequence: 35dead91494557b3008cc34a4a1c93e20634c93e696ebe33b6067b7a89a97603
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, -2, 1]
- [0, 0, 0, 1, -2]
signature: [0, 5]
determinant: -12
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, -2/3, -1/3]
- [0, 0, 0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  discriminant_group: [2, 6]
  discriminant_sequence:
    discriminant_factors: [2, 6]
    discriminant_basis_lifts:
    - ['0', '-1', 3/2, '1', '-1']
    - ['0', -1/2, 1/2, 1/3, -1/3]
    discriminant_quadratic_gram:
    - [1/2, 1/2]
    - [1/2, 1/3]
    discriminant_group_order: 4
    discriminant_generators:
    - - [1, 3]
      - [0, 1]
    - - [1, 3]
      - [0, 5]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 5]
    - - [1, 0]
      - [0, 5]
    - - [1, 0]
      - [0, 1]
    - - [1, 3]
      - [0, 1]
    image_order: 4
    kernel_order: 48
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 2
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{0,5} (2: [1^-3 2^2]_5; 3: 1^-4 3^1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 192
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 10, 20, 30, 56, 50, 60, 90]
  root_system: [A2, A1, A1]
  roots:
  - type: B2
    scale: -1
    simple_roots:
    - [0, 0, 1, 0, 0]
    - [0, 1, -1, 0, 0]
  - type: G2
    scale: -1
    simple_roots:
    - [0, 0, 0, 0, 1]
    - [0, 0, 0, 1, -1]
  - type: A1
    scale: -1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-1, -2]
morphisms:
- target: 5ALI
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5ALI
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5ALI
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5ALI
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5ALI
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 3ID0.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 3ID0.
