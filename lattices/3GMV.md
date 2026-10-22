---
tag: 3GMV
name: watson 4:72
latex: watson 4:72
aliases: []
certifications:
  derive: 32bc7469a8346ca7904a9df5ffed002b32e293511e09f1a3ceca4cc198d510d9
  form.integer_valued: 708d70e00c4efdd024422b26217655b1c9eee81a395e0a14aa0ec3fd6c024353
  integral.elementary_primes: 536f0fb30daf83aacfc35b431640090824440677459fd18a2a5db5aebe052d47
  integral.genus_symbol: efedbb8dd04884c5cc7417afbcbc71cc3909aaa02ad6b443f17545e4c10a91cd
  integral.genus_class_count: c50319f69e9c84f7d23e010b10bcf89f52ce69463f6dbba1ce6342f84e2c6bd6
  integral.overlattice_count: 3f852e8d2816fd349cb53c7cc61fa0411a8688a8c4027daff7064ade4ca15927
  integral.spinor_genus_count: 4183d520afe9629065100a65f1e372b850cea1e1277d080697bb04784c4ed5cc
  integral.spinor_genera: 50218e69d9aa429833522b9c0430a6038ee7d84f7e6e7b533091b829990e8623
  integral.hyperbolic_index: 37a1f8915fed01bcc93b8caeeb0197ee0c7e5c15d7ea948250ad39e5b4ae94bc
  definite.automorphism_group_order: bf91c3f863cfbc47a12f77b968e33b7920fa64cb0db8f40885fa8e8982d3024f
  definite.automorphism_group_generator_morphisms: a7460c9a8bd6ab23a0cc5a45ed7355fec223487ca84dabcb78d5a4a5b6a1ee40
rank: 4
gram_tensor:
- [6, -1, -1, 2]
- [-1, 6, -1, 2]
- [-1, -1, 6, 2]
- [2, 2, 2, 10]
signature: [4, 0]
determinant: 1372
definiteness: positive_definite
dual_gram_tensor:
- [3/14, 1/14, 1/14, -1/14]
- [1/14, 3/14, 1/14, -1/14]
- [1/14, 1/14, 3/14, -1/14]
- [-1/14, -1/14, -1/14, 1/7]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 28
  discriminant_group: [7, 14, 14]
  overlattice_count: 18
  bad_reduction_primes: [2, 7]
  quadratic_character: 28
  genus_symbol: 'II_{4,0} (2: 1^2 [2^2]_2; 7: 1^-1 7^-3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 6
  kissing_number: 6
  automorphism_group_order: 24
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 1, 0]
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 0, 0, 0, 0, 6, 0, 0, 0, 10, 0, 14]
  root_system: []
  roots:
  - type: A2
    scale: 7
    simple_roots:
    - [0, 1, -1, 0]
    - [1, -1, 0, 0]
  - type: A1
    scale: 14
    simple_roots:
    - [1, 1, 1, -2]
root_sublattice:
  invariant_factors: [1, 1, 1]
morphisms:
- target: 3GMV
  name: O(L) generator 1
  matrix:
  - [0, 0, -1, 0]
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3GMV
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3GMV
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 1]
  - [0, 1, 0, 1]
  - [0, 0, 1, 1]
  - [0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 4:72.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:4:72` gives this Gram tensor.
