---
tag: 3VVJ
name: Constructed lattice 3VVJ
latex: L_{\mathrm{3VVJ}}
certifications:
  derive: 80796c6bb514585588068fe045817d793367ee860d5cb21af020c9cec9f98dd9
  form.integer_valued: 64e17713760cab24598e4675c44e41db6c58dac038f06b17d22edfd0bd8ef976
  integral.elementary_primes: 9c99822647de44505eee8de716d3de09774b3deb9ddcca0adad2b502fa527601
  integral.genus_symbol: 113ca38d40ac2db4c24a21bc84f78ce76e3bbf34a4138b77a14742d48058b212
  integral.genus_class_count: 6a840b7f5e2a6b8bb7219946280afc2810424a7e55f03562248321d410f74ba3
  integral.overlattice_count: d02040679b12692f7ec038f7871e986620fb7ab5793a479b88605a45cac00ea3
  integral.spinor_genus_count: 7317178f975e26690cf6a5f16e4f3b4d6caca15e7fcd65f7b03ac7be26dd34d3
  integral.spinor_genera: 01d62ffe3fd7d23ded67067b7f8f0894e70f6321b0749c3319ef8980e8b92605
  integral.hyperbolic_index: 5ed5cbe64f214e45024f8eae5d22d05116855befaa70a639faf92f60aa4c8b20
  definite.automorphism_group_order: 112e58ff4f22068c2598cd2b53c98357fb054723633e9cfd8f03eaa12f3c159c
  definite.automorphism_group_generator_morphisms: aa0242fd976acdd70240a927b744fd0d356222044b49ca6dbe316dbcb6073888
  integral.discriminant_sequence: a8aaccf9c3ae8361a3e16fbad506e0781371865f19e52b7b13974993435f0bce
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 0, 0, 2, -1]
- [0, 0, 0, -1, 2]
signature: [5, 0]
determinant: 6
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 0, 0, 2/3, 1/3]
- [0, 0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  discriminant_group: [6]
  discriminant_sequence:
    discriminant_factors: [6]
    discriminant_basis_lifts:
    - ['0', '0', -1/2, 1/3, -1/3]
    discriminant_quadratic_gram:
    - [1/6]
    discriminant_group_order: 2
    discriminant_generators:
    - - [5]
    image_generators:
    - - [1]
    - - [1]
    - - [5]
    - - [5]
    - - [1]
    image_order: 2
    kernel_order: 96
    coset_representatives:
    - - [1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0]
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{5,0} (2: [1^-4 2^1]_3; 3: 1^4 3^-1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 4
  automorphism_group_order: 192
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 4, 12, 32, 48, 56, 86, 88, 96]
  root_system: [A2, A1, A1, A1]
  roots:
  - type: B2
    scale: 1/2
    simple_roots:
    - [0, 1, 0, 0, 0]
    - [1, -1, 0, 0, 0]
  - type: G2
    scale: 1
    simple_roots:
    - [0, 0, 0, 0, 1]
    - [0, 0, 0, 1, -1]
  - type: A1
    scale: 1
    simple_roots:
    - [0, 0, 1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [1, 2]
morphisms:
- target: 3VVJ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3VVJ
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3VVJ
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 3VVJ
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3VVJ
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 0012.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0002, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0002, 0012.
