---
tag: 4QID
name: Constructed lattice 4QID
latex: L_{\mathrm{4QID}}
certifications:
  derive: 7b1e00c2905ab75fd68d205f04bb3c84b21f4e67c7153b4842f60b1e96cac9d0
  form.integer_valued: 1f0b6a81dcc01f5da78396594537070e197e5912d4864f6284e531ccdbb0b59c
  integral.elementary_primes: c7087e33d6ac2db8676ac5c6592aef1710a2fdd227a3c8a9788be5dfd0bd8a2b
  integral.genus_symbol: 7c7952739c6fc7d325b6a2a945e79ebbfc676bdf961be5c4a4efd36b898eb57a
  integral.genus_class_count: 8da681d8ff4c6167051571320dc04788caf628b7a87aed9263af08ebeb3614e9
  integral.overlattice_count: 3dd8254490c6841676a53a66a3333fe78b9a3b00514f4b12799add006558ec22
  integral.spinor_genus_count: 973dbd755a8f3a2ad2091b7d7da8e89614e98360f152ce8053396e86cbbf8143
  integral.spinor_genera: c0a9661c89bc28e958adcebb22b2b5297cbc791f413c91a7e3b81ec78a3de2f2
  integral.hyperbolic_index: e8a1cd77d70790d73c5cf67aeccd61009522e3c975b4a5b9dcf4f0f1c98edd7d
  definite.automorphism_group_order: 0f89505a27bac7a855cc823b0800ba6d0333470099b836b335189f458efa5488
  definite.automorphism_group_generator_morphisms: 21977c759ecd88046be6db591c832646b64f51cc9b49fae52e7d74d678471961
  integral.discriminant_sequence: 8e4085caca1c2734522803587d69460d79cf3c25dfb8260a0827909ec32fdf69
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 4, -2, 0, 0]
- [0, -2, 4, 0, 0]
- [0, 0, 0, 2, -3]
- [0, 0, 0, -3, 6]
signature: [5, 0]
determinant: 36
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1/3, 1/6, 0, 0]
- [0, 1/6, 1/3, 0, 0]
- [0, 0, 0, 2, 1]
- [0, 0, 0, 1, 2/3]
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
    - ['0', 1/6, -1/6, '0', '0']
    - ['0', -1/2, '0', '0', -1/3]
    discriminant_quadratic_gram:
    - [1/3, 1/2]
    - [1/2, 2/3]
    discriminant_group_order: 24
    discriminant_generators:
    - - [5, 3]
      - [3, 4]
    - - [5, 3]
      - [0, 1]
    - - [5, 3]
      - [0, 5]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 5]
    - - [1, 0]
      - [0, 5]
    - - [5, 3]
      - [3, 4]
    - - [5, 3]
      - [0, 1]
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
    scale: 1
    simple_roots:
    - [0, 0, 0, 1, 0]
    - [0, 0, 0, 0, 1]
  - type: G2
    scale: 2
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
- target: 4QID
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4QID
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4QID
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4QID
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4QID
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID2, 3ID4.
- tag: 3ID2
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID2, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID2, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ID2, 3ID4.
