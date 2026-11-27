---
tag: 4VJV
name: Constructed lattice 4VJV
latex: L_{\mathrm{4VJV}}
certifications:
  derive: 9294496cc1a34c20aeb551742c1f1167f44fe9319640e28a5d5e978d48b066fa
  form.integer_valued: a5763b6efad4b0a691527f36e31a8cdd3cde4c2a2a72dd71e01d017d5e868a4a
  integral.elementary_primes: f560691b153d3d526d4d7c7c5936e259e6cd4cc30cf0d5aa0cf27db6216e48b0
  integral.genus_symbol: ea7f8bbf7563923881d936494e479aa55d0b7296e1c81c0be8d2a1d28f0c12e7
  integral.genus_class_count: 727ca618ac18339587adfe8d6139c9288cfc07798aaf36cf6fcc1a8a182ec5ea
  integral.overlattice_count: ca62d42f51d0f6f1f6ba417214b3bc108ddc9c36068459623f45cc621682ddc1
  integral.spinor_genus_count: 1af33572ef37a4a6b75afd4d359e5b1364dde7c397529f1318fd7c5bbcc93239
  integral.spinor_genera: 0702f20abecaebe823414a7f1ad2c8f14d1f329da5194ebc13772afd8ad90075
  integral.hyperbolic_index: 436599a85a80c0bbbb95eda248c32e2edf9f1e6140fdb773104028978e218313
  definite.automorphism_group_order: 6661d857ce702abd22d44e357a04ecdb442093f91318cce1cf73fddab8eedc3f
  definite.automorphism_group_generator_morphisms: a9c2edc989f1349602c02510320b0fad9deda8b1a8219d415740e42eb2c6e8ef
  integral.discriminant_sequence: 473848bce86f06b45fab4541dd63e7d1b3d43e3c6afd1779b659c996b61c5274
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, -2, 3]
- [0, 0, 0, 3, -6]
signature: [0, 5]
determinant: -3
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, -2, -1]
- [0, 0, 0, -1, -2/3]
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
    - ['0', '0', '0', '0', 1/3]
    discriminant_quadratic_gram:
    - [1/3]
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
  genus_symbol: 'I_{0,5} (2: [1^-5]_5; 3: 1^-4 3^1)'
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
    scale: -1/2
    simple_roots:
    - [1, -1, 0, 0, 0]
    - [0, 1, -1, 0, 0]
    - [0, 0, 1, 0, 0]
  - type: G2
    scale: -1
    simple_roots:
    - [0, 0, 0, 1, 0]
    - [0, 0, 0, 0, 1]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-1, -2]
morphisms:
- target: 4VJV
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4VJV
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4VJV
  name: O(L) generator 3
  matrix:
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4VJV
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4VJV
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 3ID3.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 3ID3.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 3ID3.
