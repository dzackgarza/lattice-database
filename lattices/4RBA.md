---
tag: 4RBA
name: Constructed lattice 4RBA
latex: L_{\mathrm{4RBA}}
certifications:
  derive: f8c3d21496173b20eddc2060e0705504de740bf8ebe2295b6c61defd6d3aa839
  form.integer_valued: f4a7ed8252851a7815dc16d432fe9f7705bc898f9206e43c542abf19d977b230
  integral.elementary_primes: 4ff08d33ff55d34f14a2545579acd5a0ec7d2bb330259139da1a413f1eac7413
  integral.genus_symbol: 9d233abd0eb0bc33aa70de6199617b0d47931bafe76a094a6ad5fe15d34a757b
  integral.genus_class_count: 976192308c923ccc75042b0937b1ebe12647e2973cb0d90b5bf73a3069fd179d
  integral.overlattice_count: 768b50863c67d9d98b944a4af17dea7028ceaf297881a926e50397cc03435767
  integral.spinor_genus_count: f0573eef20bf0ff593d6322f58706fafc6547dba27d36448601ff5dddcc9c6e3
  integral.spinor_genera: 70002dac1981b7fb7c54dd48da651819013c11ed0b7474cac8c3feb8fc68d050
  integral.hyperbolic_index: e11ac7528f41bec0ccf8327df0d8a038cfc863374c827d6cc147a6c6f3f1e90d
  definite.automorphism_group_order: 533a3e2385a8eebf70afed8c1bbf8b91822bac25e3ce8051d9dfcbec77cae0b3
  definite.automorphism_group_generator_morphisms: 2b4b870a462ef31a5f663fd797da9d9730ea561448d62e1d7787781fe6ab052b
  integral.discriminant_sequence: 08737882c75c9780811f74e59178e496924eb0a1661c3c614c1c8a49b8e20e8a
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, -1, 0, 0]
- [0, -1, 2, -1, 0]
- [0, 0, -1, 2, -1]
- [0, 0, 0, -1, 2]
signature: [5, 0]
determinant: 5
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 4/5, 3/5, 2/5, 1/5]
- [0, 3/5, 6/5, 4/5, 2/5]
- [0, 2/5, 4/5, 6/5, 3/5]
- [0, 1/5, 2/5, 3/5, 4/5]
form:
  integer_valued: true
integral:
  elementary_primes: [5]
  parity: odd
  level: 10
  discriminant_group: [5]
  discriminant_sequence:
    discriminant_factors: [5]
    discriminant_basis_lifts:
    - ['0', -1/5, -2/5, -3/5, 1/5]
    discriminant_quadratic_gram:
    - [4/5]
    discriminant_group_order: 2
    discriminant_generators:
    - - [4]
    image_generators:
    - - [1]
    - - [1]
    - - [1]
    - - [4]
    image_order: 2
    kernel_order: 240
    coset_representatives:
    - - [1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0]
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2, 5]
  genus_symbol: 'I_{5,0} (2: [1^-5]_1; 5: 1^4 5^1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 480
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 20, 40, 32, 60, 100, 120, 120]
  root_system: [A4]
  roots:
  - type: A4
    scale: 1
    simple_roots:
    - [0, 0, 0, 0, 1]
    - [0, 0, 0, 1, 0]
    - [0, 0, 1, 0, 0]
    - [0, 1, 0, 0, 0]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [1, 2]
morphisms:
- target: 4RBA
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4RBA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 1, 0, 0, -1]
  - [0, 1, -1, 1, -1]
  - [0, 1, -1, 0, 0]
  scale: 1
- target: 4RBA
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, -1, 1, -1]
  - [0, 1, -1, 1, -1]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4RBA
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, -1, 1, -1]
  - [0, 0, -1, 1, 0]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0034.
- tag: '0034'
  relation: This presentation is obtained by orthogonal sum of 0001, 0034.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0034.
