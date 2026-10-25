---
tag: 3HJR
name: D2 (union:166)
latex: D2
aliases: [D2]
certifications:
  derive: 6ce582cd08eb562134d4be73386b3bb30888a14e3620258d8ec5c068d5d34b2d
  form.integer_valued: 1f164f309ef06df657c73b4f2f4f7805ec5e72531211722d9abeac7b2f51844d
  integral.elementary_primes: 2e5dbd93cbbbe62b22db3fe6fa6573829a92105465b4b69a8a7ce2a4db8c069a
  integral.genus_symbol: a9a7dbd2adee1c0bd57a13f36426c3cffa4dcc74a55645d211b99f1ae33eaab5
  integral.genus_class_count: 986f1d2839fdcab69d468975e25a3dd8a5ee90bb7d7efef3efa8c69a698c1527
  integral.overlattice_count: 6e342e577fb798c79b26cbce66b448609aab75046c932f9666ce103aa069f764
  integral.hyperbolic_index: d6d39829c59624be347724996f9ad0b5f12eba8ac45c0de124d8a04a75ffb4bc
  definite.automorphism_group_order: 2cff4b4353c7488ec3d4cf7de1868246da739295e736d685dfab75767ff122f5
  definite.automorphism_group_generator_morphisms: d5945e35656e0abe1593c70d975b730a3a680b001992205d35f700c812db0c9a
  integral.discriminant_sequence: c7720f67d25678141d4113549eb4c762d3d257b3a6532299b3ad4e79881f7ad9
  integral.primitive_orbits: 4e8bfddde0a5beb16fd5c4c2f2c3bfcc58218f2f5b7c440be73052b103347a7a
  integral.modular_scale: ac642a16466aea97fdbb2e1838a6ed1c80b16e3fcba0f51f435c57313971e97e
  definite.genus_theta_series: 6d9b4bf0a8ecc04d7e5c98bee69a91eae9745ab34c1568307b6058aad4031374
  definite.theta_series_cuspidal_component: 3bb34004a293fbdd79bb50c7ea45dbb6a9d0fa315aeb6c1430eb1862e59495f0
  definite.siegel_eisenstein_coefficients: e03b79efe22a534d2e9c56a85c423f731442d6471a970ae2aca195ebfab8dbff
  integral.anisotropic_primes: 1e941932dcb3999c80588726621b7b76616166586fbfab8f5f5fa75e0b6acc36
  integral.local_representations: 2826e619c03b2ab837fea47601888c9ffd237ac7f7c2840f278ae98d6579c570
  integral.local_densities: e19a58431fdd69080f98cdecdc485067b9008d330b02219998cdf072b5d2252a
rank: 2
gram_tensor:
- [2, 0]
- [0, 2]
signature: [2, 0]
determinant: 4
definiteness: positive_definite
dual_gram_tensor:
- [1/2, 0]
- [0, 1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: 4
  discriminant_group: [2, 2]
  discriminant_sequence:
    discriminant_factors: [2, 2]
    discriminant_basis_lifts:
    - [1/2, '0']
    - ['0', 1/2]
    discriminant_quadratic_gram:
    - [1/2, '0']
    - ['0', 1/2]
    discriminant_group_order: 2
    discriminant_generators:
    - - [0, 1]
      - [1, 0]
    image_generators:
    - - [1, 0]
      - [0, 1]
    - - [0, 1]
      - [1, 0]
    - - [1, 0]
      - [0, 1]
    image_order: 2
    kernel_order: 4
    coset_representatives:
    - - [1, 0]
      - [0, 1]
    mm_trivial: true
    image_normal: true
    quotient_generator_cosets: [0]
    quotient_multiplication:
    - [0]
  overlattice_count: 2
  delta: 1
  bad_reduction_primes: [2]
  quadratic_character: -4
  genus_symbol: 'II_{2,0} (2: [2^2]_2)'
  genus_class_count: 1
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 1, 0, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 1, 0, 1]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 2, 0, 1]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 2, 0, 2]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 1, 0, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 1, 0, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 2, 0, 2]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 2, 0, 2]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 5
      least_valuation: 2
    - representative: 2
      least_valuation: 1
    - representative: 10
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0]
definite:
  minimum: 2
  kissing_number: 4
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0]
  - [0, -1]
  - [0, 1]
  - [1, 0]
  perfect: false
  theta_series: [1, 0, 4, 0, 4, 0, 0, 0, 4, 0, 8, 0, 0]
  genus_theta_series: [1, 0, 4, 0, 4, 0, 0, 0, 4, 0, 8, 0, 0]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [0, 4, 0, 4, 0, 0, 0, 4, 0, 8, 0, 0]
  root_system: [A1, A1]
  roots:
  - type: B2
    scale: 1
    simple_roots:
    - [0, 1]
    - [1, -1]
root_sublattice:
  invariant_factors: [1, 1]
  norms: [2]
morphisms:
- target: 3HJR
  name: O(L) generator 1
  matrix:
  - [-1, 0]
  - [0, -1]
  scale: 1
- target: 3HJR
  name: O(L) generator 2
  matrix:
  - [0, 1]
  - [1, 0]
  scale: 1
- target: 3HJR
  name: O(L) generator 3
  matrix:
  - [1, 0]
  - [0, -1]
  scale: 1
families: []
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002.
references:
- citation: G. Nebe and N. J. A. Sloane, Catalogue of Lattices, archive entry union:166.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz
---

Catalogue of Lattices archive entry `union:166` names `D2`.

The simple square lattice
