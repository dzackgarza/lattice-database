---
tag: 3GRG
name: watson 4:237
latex: watson 4:237
aliases: []
certifications:
  derive: 35fe14139ac45b15242fca5a7986e7a364131f28b158c1f5bb0d38fc6e797801
  form.integer_valued: ecf5c90ddf73a2847c485fb7a9d855c1b9b43497c203a677abda07ecff81031e
  integral.elementary_primes: 04c010fcf8c374c4d23865db4feb8b4d1aedbbf411ab70304dbf25a31c34b008
  integral.genus_symbol: af706c5b941001a450cf72ab811581503d7211daeae936a4849b9741ea995c9e
  integral.genus_class_count: 6a75c44419ac9ee9547cf62f8f3826aad728352510b444c40e10d8b0ab65cf69
  integral.spinor_genus_count: 89ef8d0f003a57579dd3729ba72a290d10804eb34701151e3a6530370ec78dad
  integral.spinor_genera: dbc2304038ef9dc5b330bc68d8d7cc8701c45938b7e3de0bc88d0d5668b26e00
  integral.hyperbolic_index: 8efea4dc47acfbf66d2f835fa0d71ce470d34846774dc6aefd3cc12cda644fd8
  definite.automorphism_group_order: bb1440e18a6ef0ef2e0e34b2bd2a2e48e57ce9ce868b4ae12089638d4da55970
  definite.automorphism_group_generator_morphisms: cdfb8a6e837ecf5546bfb4e1272bb86839d4d1dc8f9cf86d7f26bf7ab247a0d1
rank: 4
gram_tensor:
- [14, 3, 2, -1]
- [3, 14, 2, -1]
- [2, 2, 16, -8]
- [-1, -1, -8, 26]
signature: [4, 0]
determinant: 63888
definiteness: positive_definite
dual_gram_tensor:
- [5/66, -1/66, -1/132, 0]
- [-1/66, 5/66, -1/132, 0]
- [-1/132, -1/132, 5/66, 1/44]
- [0, 0, 1/44, 1/22]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 132
  discriminant_group: [11, 44, 132]
  bad_reduction_primes: [2, 3, 11]
  quadratic_character: 33
  genus_symbol: 'II_{4,0} (2: 1^-2:4^-2; 3: 1^3 3^-1; 11: 1^1 11^3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 14
  kissing_number: 4
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
  root_system: []
  roots:
  - type: A1
    scale: 44
    simple_roots:
    - [0, 0, 1, 2]
  - type: A1
    scale: 11
    simple_roots:
    - [1, -1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1]
morphisms:
- target: 3GRG
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3GRG
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3GRG
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, -1]
  - [0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 4:237.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:4:237` gives this Gram tensor.
