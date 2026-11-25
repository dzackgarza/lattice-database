---
tag: 4ICO
name: Constructed lattice 4ICO
latex: L_{\mathrm{4ICO}}
certifications:
  derive: 49860b647f3181cc3f95acb1a50c8f1af0ba8507d09f9b7ddbd6915796a1746d
  form.integer_valued: 7107194ab7f1b1264e769c990f9cd220915192a3cc26e0d27bfaab455bdbfdbc
  integral.elementary_primes: d9b90c56ae56cc4962112fd86b8d6634e8c514e5840503b1632038029a32916b
  integral.genus_symbol: 3b5afcc3121a0a3ba17ea54229dab06a7dacbfff1f674219e1db1b2dd7ba16f6
  integral.genus_class_count: ae60fce8d2bdab09f989228e19b91a2830f07d36ef3367c310317c49101371d2
  integral.overlattice_count: 2b42123e0af869c49dd4ee6ad40ddb22a7b6369294c3061410c824371ea3e410
  integral.spinor_genus_count: f4e4fd1fb4dcb410022f8cdc6f3a0766ee43a8803b86c55ffd466077d68e1ef7
  integral.spinor_genera: bf362b5a41c51a136bac5073e554785ba8f0d131224796c743fd51f422503f28
  integral.hyperbolic_index: e4f2598a08ccdc24f88ef5e653657d346bef33e7566b986bc0aef2f5f73e4465
  definite.automorphism_group_order: 20a90cdf6c917d85c744ab367a762ba6d224e1857924e2b364fd1f10fb3252e4
  definite.automorphism_group_generator_morphisms: fc4b06717982ae95b6c4a16089c1611a51889a7da28e42403b55c4d08b9dbc0c
  integral.discriminant_sequence: 5372ddb4dca51f37db5bdb4be98ce6ed0d05a741556620c6361ee6be8b4c5ba6
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 2, -1, 0]
- [0, 0, -1, 2, -1]
- [0, 0, 0, -1, 2]
signature: [5, 0]
determinant: 8
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 3/4, 1/2, 1/4]
- [0, 0, 1/2, 1, 1/2]
- [0, 0, 1/4, 1/2, 3/4]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 8
  discriminant_group: [2, 4]
  discriminant_sequence:
    discriminant_factors: [2, 4]
    discriminant_basis_lifts:
    - ['0', 1/2, -1/2, '0', 1/2]
    - ['0', '0', 1/4, 1/2, -1/4]
    discriminant_quadratic_gram:
    - [1/2, 1/2]
    - [1/2, 3/4]
    discriminant_group_order: 2
    discriminant_generators:
    - - [1, 0]
      - [0, 3]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 3]
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 1]
    image_order: 2
    kernel_order: 96
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0]
    quotient_multiplication:
    - [0]
  overlattice_count: 2
  bad_reduction_primes: [2]
  genus_symbol: 'I_{5,0} (2: [1^3 2^1 4^1]_5)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 192
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
  minimal_vectors:
  - [-1, 0, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  perfect: false
  theta_series: [1, 2, 14, 28, 32, 60, 64, 72, 122]
  root_system: [A3, A1]
  roots:
  - type: C3
    scale: 1
    simple_roots:
    - [0, 0, 0, 1, 0]
    - [0, 0, 0, 0, 1]
    - [0, 0, 1, 0, -1]
  - type: A1
    scale: 1
    simple_roots:
    - [0, 1, 0, 0, 0]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [1, 2]
morphisms:
- target: 4ICO
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4ICO
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, -1, 1]
  - [0, 0, 1, -1, 0]
  scale: 1
- target: 4ICO
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, -1, 1]
  - [0, 0, 0, -1, 0]
  - [0, 0, 1, -1, 0]
  scale: 1
- target: 4ICO
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, -1, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 4ICO
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4ICO
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0023.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0023.
- tag: '0023'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0023.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 0023.
