---
tag: 3GPK
name: watson 4:169
latex: watson 4:169
aliases: []
certifications:
  derive: f39d1eb69eb4f6dd7b145ccd6789c002f47cef67804844e1d73e5fa48d490361
  form.integer_valued: 2ded3e3cf9bfbffb1c6618e8ab02a5f9e16e287eb9ed1aaae416421e9218c1df
  integral.elementary_primes: a0cdcfd5b435d363fc31852d0ada4077827f1c9e60f40b8c3de7afd6693af97e
  integral.genus_symbol: cee7a1488c23add2642bd7a67a947f68d6839f888570016099f8fdd6cd73556b
  integral.genus_class_count: a4d9509906a16badd372d9070c856d2cf5d541b1fe450419a0b6134f8f2449ed
  integral.overlattice_count: 1595fd39049385f80aaf2111174f561acafa9b17a12a6916a63c1c073712b336
  integral.spinor_genus_count: c6da8b78c36351535b85c7a6a799419fb37b72fbe836a4d001151f3a7d1f319f
  integral.spinor_genera: 313dc999e8d0a7dd3e02285e902095abaa2ecc092f36cbb98f64677be9b038dd
  integral.hyperbolic_index: 6d0594f61c8ccfb19e09aeef7fdae8c8ae2f27733fe9a2c675f0e2f4c1745606
  definite.automorphism_group_order: a66c459a07ab65f76db0e8d0a6320ed7c2cd6b42611d5f5ffc1824e0d87029c1
  definite.automorphism_group_generator_morphisms: f594fd55c83011199f093353440706906816f4041363eafedba1c58a595b24a0
rank: 4
gram_tensor:
- [6, -3, -3, -3]
- [-3, 14, 4, -1]
- [-3, 4, 14, 4]
- [-3, -1, 4, 14]
signature: [4, 0]
determinant: 10125
definiteness: positive_definite
dual_gram_tensor:
- [2/9, 2/45, 1/45, 2/45]
- [2/45, 4/45, -1/45, 1/45]
- [1/45, -1/45, 4/45, -1/45]
- [2/45, 1/45, -1/45, 4/45]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 45
  discriminant_group: [15, 15, 45]
  overlattice_count: 70
  bad_reduction_primes: [2, 3, 5]
  quadratic_character: 5
  genus_symbol: 'II_{4,0} (2: 1^-4; 3: 1^-1 3^-2 9^-1; 5: 1^1 5^3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 6
  kissing_number: 2
  automorphism_group_order: 24
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]
  root_system: []
  roots:
  - type: A2
    scale: 15
    simple_roots:
    - [1, 0, 1, 1]
    - [0, 1, 0, -1]
  - type: A1
    scale: 3
    simple_roots:
    - [1, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1]
morphisms:
- target: 3GPK
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3GPK
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  - [0, 1, 0, 0]
  scale: 1
- target: 3GPK
  name: O(L) generator 3
  matrix:
  - [1, -1, -1, 0]
  - [0, 0, 0, 1]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  scale: 1
- target: 3GPK
  name: O(L) generator 4
  matrix:
  - [1, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  - [0, -1, 0, 0]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 4:169.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:4:169` gives this Gram tensor.
