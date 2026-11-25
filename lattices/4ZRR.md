---
tag: 4ZRR
name: Constructed lattice 4ZRR
latex: L_{\mathrm{4ZRR}}
certifications:
  derive: 5b0e32c807e96a52f1c03481cd9dd6be4316bbe912e8349abff44799a7ac1ab9
  form.integer_valued: 759068139e8aab9a88b156a71507c3d82c80fc7eaf95fbcf9667f44bfa6067c6
  integral.elementary_primes: 426bd2e2a3a671f07c96b78b771ca8b67027838b344e417637e966a3af34da3c
  integral.genus_symbol: e711f948360677f5d2a5d9c6b298f068504481b2b538293a7834b48f0f5ab684
  integral.genus_class_count: ddcbbe5c0b8c3c1748b7ded5a943795171324fe1fc6acb8e9361b398d01b724b
  integral.overlattice_count: 3d57c866eb5e2532c88eab47da07e95dbd48ea59ec53bf31d4895f322ce3e09b
  integral.spinor_genus_count: e71de574d712ecf0fdd09f5c2e7ee2b7ad215db02b6bc227d8dfe5d7afb4fb90
  integral.spinor_genera: 8384f61c3dcffbd640d74cacaf1d36529fe7db7f526ade441a8cfbc6e0d3e43a
  integral.hyperbolic_index: 08565b9441af4803dd1876f2eac1cd354caafa4ca82699c4af8c7e033cd87100
  definite.automorphism_group_order: 3a715d4d1e23bb8506de7bf43bc3fdbeba15bba68dae1a52c9ff856832ac6538
  definite.automorphism_group_generator_morphisms: d59a5f93e5eae0d37b673a0f4f37d91a6b5fd7d3d07ea15b33b784af06a21180
  integral.discriminant_sequence: 9e6d22546c66888fed4c769c8af607197c3d99895387ed9e5984d13228e1837d
  integral.primitive_orbits: c7685c0814e793c9a0209a379698cb5fa7589a15953cdbbda3421eb0669f0914
  integral.modular_scale: 6925267fcd5f7e48989c58a13532db59858f172aafae95f062a67ca914695e01
  definite.genus_theta_series: a577a8aed1a2089600fda0cb69c95c7e692739a3274a0a7cea16d9e858de943e
  definite.theta_series_cuspidal_component: 0e642eaaeb9ad88328f3c12068be275bbdf9e3509f145322517ea86b2a6cb6a1
  integral.anisotropic_primes: 086301d31174bb8094b80c2b6f75705223083d4edd4944ebbaed751068d63368
  integral.local_representations: 9349cdb2fd68f622e9bf69788146cc7e92e520b34e8aefcdeff9ff3314eb6a62
  integral.local_densities: 84a3baf1f3cb3173953cdc8e41cb067fb1e155f9af39dc9105d4358476d9e44f
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, -2, 3]
- [0, 0, 0, 3, -6]
signature: [0, 5]
determinant: -6
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, -2, -1]
- [0, 0, 0, -1, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 12
  modular_scale: false
  discriminant_group: [6]
  discriminant_sequence:
    discriminant_factors: [6]
    discriminant_basis_lifts:
    - ['0', '0', -1/2, '0', -1/3]
    discriminant_quadratic_gram:
    - [5/6]
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
  genus_symbol: 'I_{0,5} (2: [1^-4 2^1]_5; 3: 1^4 3^1)'
  genus_class_count: 2
  spinor_genus_count: 1
  spinor_genera: [2]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 3, 2, 3]
    SO:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 3, 2, 3]
    Otilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 3, 2, 3]
    SOtilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 3, 2, 3]
    O+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 3, 2, 3]
    SO+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 3, 2, 3]
    Otilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 3, 2, 3]
    SOtilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 3, 2, 3]
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1, 15/16, 1, 9/8, 1, 9/8, 1, 111/128]
  - prime: 3
    densities: [8/9, 8/9, 34/27, 8/9, 8/9, 32/27, 8/9, 8/9]
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
  genus_theta_series: [1, 24/5, 72/5, 32, 216/5, 272/5, 442/5, 432/5, 456/5]
  theta_series_cuspidal_component: [0, -4/5, -12/5, 0, 24/5, 8/5, -12/5, 8/5, 24/5]
  root_system: [A2, A1, A1, A1]
  roots:
  - type: B2
    scale: -1/2
    simple_roots:
    - [0, 1, 0, 0, 0]
    - [1, -1, 0, 0, 0]
  - type: G2
    scale: -1
    simple_roots:
    - [0, 0, 0, 1, 0]
    - [0, 0, 0, 0, 1]
  - type: A1
    scale: -1
    simple_roots:
    - [0, 0, 1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 1, 1]
  norms: [-1, -2]
morphisms:
- target: 4ZRR
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4ZRR
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4ZRR
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4ZRR
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4ZRR
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICX, 3ID3.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICX, 3ID3.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICX, 3ID3.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICW, 3ICX, 3ID3.
