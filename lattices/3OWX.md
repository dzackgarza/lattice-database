---
tag: 3OWX
name: Constructed lattice 3OWX
latex: L_{\mathrm{3OWX}}
certifications:
  derive: 7889ccb793d270dd6bdd26aea58f9b7881c52a1606a7e17a2eb6acfb14d7a041
  form.integer_valued: ced06705ed4f6ed3f5da4dbd796157c21c0245927ad15c103567073de7c4515c
  integral.elementary_primes: be6f18f75126586ed6c18bbcb28c1069ddbead4df8549b3ea950e5ce2a22d68f
  integral.genus_symbol: 0f255db16dd34ad99bb31aeac498688d7fd59784fdc8062a996ac41acbdc6ff5
  integral.genus_class_count: e537d9c388b39eebe0eaac5fe9acbc0ab77ecfa8f2598d2d47a473ffbce63b31
  integral.overlattice_count: b03a0a17de822710ebc5f6a5302f3096fe181db2228f196d6d90ae88639c76d7
  integral.spinor_genus_count: 5d212e61cc5297e7cfd503a1cc5055c04905d6d30efebf8ea2662c813ae4c85d
  integral.spinor_genera: bb29ecba072719d500a1b37fa9bca849983f3f8a3927f4b85ed6513862cee88d
  integral.hyperbolic_index: 8d2f9db7ca770f57cb9dfe1a36624392bcab92a8cacbf03062d69716395a6aee
  definite.automorphism_group_order: 47ec45d0611e57c643da52cd29f0963af243efce3f4786f04a269eb3078755e5
  definite.automorphism_group_generator_morphisms: be84ac6cc0102b0184455386d45b957c8d5224677f6de5da86f364c0dae429ad
  integral.discriminant_sequence: dcf9817a15c94c45a4fe0e3f1cc4ac4dbf81015de3009390e38316d320b1479b
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 0, 0, 2, -1]
- [0, 0, 0, -1, 2]
signature: [5, 0]
determinant: 3
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 0, 0, 2/3, 1/3]
- [0, 0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  discriminant_group: [3]
  discriminant_sequence:
    discriminant_factors: [3]
    discriminant_basis_lifts:
    - ['0', '0', '0', -1/3, 1/3]
    discriminant_quadratic_gram:
    - [2/3]
    discriminant_group_order: 2
    discriminant_generators:
    - - [2]
    image_generators:
    - - [1]
    - - [1]
    - - [1]
    - - [2]
    - - [2]
    image_order: 2
    kernel_order: 288
    coset_representatives:
    - - [1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0]
    quotient_multiplication:
    - [0]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{5,0} (2: [1^-5]_3; 3: 1^-4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 6
  automorphism_group_order: 576
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 6, 18, 44, 78, 72, 66, 180, 234]
  root_system: [A3, A2]
  roots:
  - type: B3
    scale: 1/2
    simple_roots:
    - [1, -1, 0, 0, 0]
    - [0, 1, -1, 0, 0]
    - [0, 0, 1, 0, 0]
  - type: G2
    scale: 1
    simple_roots:
    - [0, 0, 0, 0, 1]
    - [0, 0, 0, 1, -1]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [1, 2]
morphisms:
- target: 3OWX
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3OWX
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3OWX
  name: O(L) generator 3
  matrix:
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3OWX
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 3OWX
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
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0001, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0001, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0001, 0012.
