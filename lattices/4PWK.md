---
tag: 4PWK
name: Constructed lattice 4PWK
latex: L_{\mathrm{4PWK}}
certifications:
  derive: 6a3b1a7b39b3ac627fc99e05eaa2f37f6e91b24c0039e4c6e9b02fe226077caa
  form.integer_valued: 2928f53c03491a28d5ad2f0747e624d88ccf611116a5fc5d2d95b3dba965982c
  integral.elementary_primes: be7baf42e771c6b00fb38e06d428b250b43b87aa8c3e63ada0cf902fa1734335
  integral.genus_symbol: b05f26be226a0a6c1c5ca9a2db25f46b84a833e04e9a7ef0cce643f8bfe79a90
  integral.genus_class_count: 623e7067d8fe1374ea2e9671205270412ef7c19df7ccd1d026d428ec7ac67fe7
  integral.overlattice_count: 5635167a9459becf6e5e62622f11e0096b10a27f32113b32938444320a34d911
  integral.spinor_genus_count: 25a95e3a7bdbf5181644da5e676747689a5b228964ce4da5082c94ceed4e5f29
  integral.spinor_genera: e3f3f5e85bd3538991cee5735413d37a7a3e775942bf30a5d6a7889dbbe4ea46
  integral.hyperbolic_index: c0d7cb874f3ac116c89d25c5088cd5eca39cf71fba36dc68b849481e26f63a1c
  definite.automorphism_group_order: efdb21e59e567fe043646cf111de25c7ec91e5c982c8847bb8d43e66f58e50fa
  definite.automorphism_group_generator_morphisms: 5d6c25a42fdef49e8b09a4c4ccccad6c59dfdf2292dee720231f4f2083bb5baf
  integral.discriminant_sequence: fcc92187af39af7f3bc4bf920e607eb035a66b62d264bafe5c268088468d9406
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, -1, 0, 0]
- [0, -1, 2, 0, 0]
- [0, 0, 0, 4, -2]
- [0, 0, 0, -2, 4]
signature: [5, 0]
determinant: 36
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2/3, 1/3, 0, 0]
- [0, 1/3, 2/3, 0, 0]
- [0, 0, 0, 1/3, 1/6]
- [0, 0, 0, 1/6, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  discriminant_group: [6, 6]
  discriminant_sequence:
    discriminant_factors: [6, 6]
    discriminant_basis_lifts:
    - ['0', -1/3, 1/3, 1/6, 1/3]
    - ['0', '0', '0', -1/6, 1/6]
    discriminant_quadratic_gram:
    - ['0', 1/6]
    - [1/6, 1/3]
    discriminant_group_order: 24
    discriminant_generators:
    - - [2, 3]
      - [3, 5]
    - - [5, 4]
      - [0, 1]
    - - [5, 4]
      - [3, 1]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [5, 4]
      - [0, 1]
    - - [5, 4]
      - [0, 1]
    - - [4, 5]
      - [3, 5]
    - - [1, 2]
      - [3, 5]
    image_order: 24
    kernel_order: 12
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 12
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{5,0} (2: [1^3]_5 2^2; 3: 1^-3 3^-2)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 288
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 6, 12, 8, 12, 54, 84, 18]
  root_system: [A2]
  roots:
  - type: G2
    scale: 2
    simple_roots:
    - [0, 0, 0, 0, 1]
    - [0, 0, 0, 1, -1]
  - type: G2
    scale: 1
    simple_roots:
    - [0, 0, 1, 0, 0]
    - [0, 1, -1, 0, 0]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [1, 2, 4]
morphisms:
- target: 4PWK
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PWK
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PWK
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PWK
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 4PWK
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0012, 3ID2.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 0012, 3ID2.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 0001, 0012, 3ID2.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0012, 3ID2.
