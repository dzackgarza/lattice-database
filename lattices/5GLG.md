---
tag: 5GLG
name: Constructed lattice 5GLG
latex: L_{\mathrm{5GLG}}
certifications:
  derive: 490aa16a0772c228b53a4e26aa7a21877f232bfe746949c99d0d40bd653813af
  form.integer_valued: 2847dbdf5fc9f9736fbce2d280a9b0be781c057c2ff30745e800273b20c10312
  integral.elementary_primes: dc630a973f5b8481435552d21dfd64ac75c6284a27298ac0fad514b197761081
  integral.genus_symbol: 5e45cda27659819e6f2bbbf5a34a2b59a268626ae3cf7e93dd1486983d2181bc
  integral.genus_class_count: aa20989fea7e326ef0301673a0e82c03cc9993140ac9170fdefde29f6d899dc9
  integral.overlattice_count: f634dc304786cd1816bf5dbf9811c5e15d9dee62df0357fb50552012104a358c
  integral.spinor_genus_count: 51187a745a5da93b0c85d9253c201427f4132526d5d17e45e7d0bbbec41df6ff
  integral.spinor_genera: d44e57dcbe852e4df1bff07e3195cb6608b7bc29b7cf1080e533ab78fad02f7e
  integral.hyperbolic_index: 75cd3e2210d47b82a92923993734e7eac49b1030625ee2a678ce5bbbdba09790
  definite.automorphism_group_order: 001bedefafcf5213fbc373556029286e0dfc9eee713a0a99e1b15cb224a791cc
  definite.automorphism_group_generator_morphisms: eeab402b59a510a234f4222756944993845e6f95b2daebea3978e00217ac6a3f
  integral.discriminant_sequence: f0edaff4f18564495bbe847c11c1e080a9b20db1e7f6f033ea961804129d4635
  integral.primitive_orbits: 8961299efc482f427540c7410436cbaf95a58dd7b43518865e60d3750c244528
  integral.modular_scale: 3e9463ebb59483fecbaef4a4d11159025be4127c315ed2f572fb3065146a83f6
  definite.genus_theta_series: d9c497e4223e104f8ee5c2ea8b7b27cf42854434c615332887bc6bc9ee4bbda0
  definite.theta_series_cuspidal_component: 570e2f10eec56c1eb8e47fbc3cedcdd812f56fd51c25dca0c7b2ad959c74b001
  integral.anisotropic_primes: 9ae4a4ed3f2f39e08e7e92784ae7aad88798376974cb02ee40ff56491bcbc92d
  integral.local_representations: 294310bdf59c268e0289451f4cf918098111ac55139c81ebb5e244df9f2b420b
  integral.local_densities: ff3ae22677ce739ca666ebeec5462deec79c4d7a451b24bc264b5b10150786ef
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2, 1, 0, 0]
- [0, 1, -2, 0, 0]
- [0, 0, 0, -2, 3]
- [0, 0, 0, 3, -6]
signature: [0, 5]
determinant: -9
definiteness: negative_definite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2/3, -1/3, 0, 0]
- [0, -1/3, -2/3, 0, 0]
- [0, 0, 0, -2, -1]
- [0, 0, 0, -1, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [3, 3]
  discriminant_sequence:
    discriminant_factors: [3, 3]
    discriminant_basis_lifts:
    - ['0', 1/3, -1/3, '0', '0']
    - ['0', '0', '0', '0', 1/3]
    discriminant_quadratic_gram:
    - [1/3, '0']
    - ['0', 1/3]
    discriminant_group_order: 8
    discriminant_generators:
    - - [0, 1]
      - [2, 0]
    - - [2, 0]
      - [0, 1]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [1, 0]
      - [0, 2]
    - - [1, 0]
      - [0, 2]
    - - [0, 1]
      - [1, 0]
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
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    SO:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    Otilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    SOtilde:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    O+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    SO+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 1, 1, 1]
    Otilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
    SOtilde+:
      constant: 0
      z: [0, 0, 0, 0]
      w: [1, 2, 2, 1]
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [3/4, 3/4, 9/8, 39/32, 3/4, 3/4, 11/8, 39/32]
  - prime: 3
    densities: [4/3, 2/3, 28/27, 4/3, 2/3, 28/27, 4/3, 2/3]
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
  genus_theta_series: [1, 22/5, 12, 84/5, 166/5, 72, 252/5, 192/5, 156]
  theta_series_cuspidal_component: [0, -12/5, 0, 36/5, 24/5, 0, -72/5, -72/5, 0]
  root_system: [A2, A2]
  roots:
  - type: G2
    scale: -1
    simple_roots:
    - [0, 0, 0, 1, 0]
    - [0, 0, 0, 0, 1]
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
- target: 5GLG
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5GLG
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5GLG
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5GLG
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, -1, 2]
  - [0, 2, -1, 0, 0]
  - [0, 1, 0, 0, 0]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID0, 3ID3.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID0, 3ID3.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID0, 3ID3.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ID0, 3ID3.
