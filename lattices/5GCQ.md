---
tag: 5GCQ
name: Constructed lattice 5GCQ
latex: L_{\mathrm{5GCQ}}
certifications:
  derive: 1494c12a9cec11fa6b5bfe1c77de852d05052e74d1cc5803f993173ce87fd4a5
  form.integer_valued: 3306512c3985b0a8e6eb6d20d42d539dc28d1d3c093f3bc2665b384086445f5c
  integral.elementary_primes: 0b949c4491f35c1dac1a3fc276c26bc04ad79c9a5f7b358599fff83db826edfc
  integral.genus_symbol: ff822c3df3490fea41e9e03ae043bc93fec2dd827492ee70f074d2170454cb7f
  integral.genus_class_count: 3246317a2f8660a4e026d4f42efb205ee2c8cf1eb62354a2315118ca05000f9b
  integral.overlattice_count: 4d1b06530495f9fc8464d34232db2ae216881cf7c48b2625fff24e9f37736897
  integral.spinor_genus_count: 92f83a14dd1a29b6c8fba11b48c064819d6b5666c4f222016fb3474ec9511363
  integral.spinor_genera: 65a3ef827e8716dc89495e4ee17761223eaa0024be7548fb6e39e2e56072f96d
  integral.hyperbolic_index: 9268278efa99a4c081069e839b12c49c819fc116d08531136b13446e502b6bec
  definite.automorphism_group_order: b710d77753f641119cbdc89041cc3e455da63dcc5500c6195f1b8277d15ca98a
  definite.automorphism_group_generator_morphisms: 6f626c9cf52ae06dcbc801bf7628ce1d7c77a9821e78d4fb20238c65ef7c3244
  integral.discriminant_sequence: b65cde54a989713d1ba4950c380e3647825b2a0d679b48ac98884f9b7dd3e37e
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2, 1, 0, 0]
- [0, 1, -2, 0, 0]
- [0, 0, 0, -2, 1]
- [0, 0, 0, 1, -2]
signature: [0, 5]
determinant: -9
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2/3, -1/3, 0, 0]
- [0, -1/3, -2/3, 0, 0]
- [0, 0, 0, -2/3, -1/3]
- [0, 0, 0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  discriminant_group: [3, 3]
  discriminant_sequence:
    discriminant_factors: [3, 3]
    discriminant_basis_lifts:
    - ['0', -1/3, 1/3, -1/3, 1/3]
    - ['0', '0', '0', -1/3, 1/3]
    discriminant_quadratic_gram:
    - [2/3, 1/3]
    - [1/3, 1/3]
    discriminant_group_order: 8
    discriminant_generators:
    - - [2, 2]
      - [2, 1]
    - - [2, 2]
      - [0, 1]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [1, 1]
      - [0, 2]
    - - [1, 1]
      - [0, 2]
    - - [2, 0]
      - [2, 1]
    image_order: 8
    kernel_order: 72
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0, 0]
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{0,5} (2: [1^5]_7; 3: 1^-3 3^2)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 576
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 12, 24, 38, 72, 36, 24, 156]
  root_system: [A2, A2]
  roots:
  - type: G2
    scale: -1
    simple_roots:
    - [0, 0, 0, 0, 1]
    - [0, 0, 0, 1, -1]
  - type: G2
    scale: -1
    simple_roots:
    - [0, 0, 1, 0, 0]
    - [0, 1, -1, 0, 0]
  - type: A1
    scale: -1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-1, -2]
morphisms:
- target: 5GCQ
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5GCQ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5GCQ
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5GCQ
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, -1, 1]
  - [0, 1, -1, 0, 0]
  - [0, 1, 0, 0, 0]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID0, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID0, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ID0, 3ID0.
