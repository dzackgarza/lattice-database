---
tag: 3GQO
name: watson 4:209
latex: watson 4:209
aliases: []
certifications:
  derive: 1f4b80bdbb975e4da83b14685897d211d23c5f4e63d34e6f803ec576c9d66b1b
  form.integer_valued: cfe535b1bc7b8952a79038e0c491544862e23808af73641262a5122345ff1a15
  integral.elementary_primes: f26e60461a352bf21fa2b03ddc820202897ae4090bd1afc3122bcedab14012d7
  integral.genus_symbol: 6d95fdc43a546e6040388be7d2a473ccdc7e83bba925309ee46c1cfafa1eea71
  integral.genus_class_count: 33661a38f191e4f512a1805f0ccbeefce672852a48c961e631b507e760d33e63
  integral.overlattice_count: 4f97097c61471c913e4e01654483d3d034d644627670ba45c182ba64c79c8aa6
  integral.spinor_genus_count: c025a740446141c3845b89fed23f8426e046e659e56c0b52f3a6a7cecc499b24
  integral.spinor_genera: 4d5bca9e0ea27f8316a39c1aa65a4e6280cdc3905a3dcf94279dbbf3ccb09c40
  integral.hyperbolic_index: 7fa4db0500f10d7039c9a39d7f2171bee58c6fdee7ec12d229ab98af55c36010
  definite.automorphism_group_order: 7a86e931271b12d18fa74b944908fbe6cc86eb318c67b98d4a8087158c60c722
  definite.automorphism_group_generator_morphisms: 110d22cdf2f9f25f2462215c0fa6c2e0a0e360388288fc4291d0662b8a31bbd4
rank: 4
gram_tensor:
- [2, 0, 0, -1]
- [0, 10, 0, -5]
- [0, 0, 10, -5]
- [-1, -5, -5, 18]
signature: [4, 0]
determinant: 2500
definiteness: positive_definite
dual_gram_tensor:
- [13/25, 1/50, 1/50, 1/25]
- [1/50, 3/25, 1/50, 1/25]
- [1/50, 1/50, 3/25, 1/25]
- [1/25, 1/25, 1/25, 2/25]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 50
  discriminant_group: [5, 10, 50]
  overlattice_count: 56
  bad_reduction_primes: [2, 5]
  quadratic_character: 1
  genus_symbol: 'II_{4,0} (2: 1^-2:2^-2; 5: 1^-1 5^2 25^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 2
  kissing_number: 2
  automorphism_group_order: 32
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 4, 0, 8]
  root_system: [A1]
  roots:
  - type: B2
    scale: 5
    simple_roots:
    - [0, 0, 1, 0]
    - [0, 1, -1, 0]
  - type: A1
    scale: 1
    simple_roots:
    - [1, 0, 0, 0]
  - type: A1
    scale: 25
    simple_roots:
    - [1, 1, 1, 2]
root_sublattice:
  invariant_factors: [1, 1, 1, 2]
morphisms:
- target: 3GQO
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3GQO
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3GQO
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 1]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3GQO
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, -1]
  - [0, 1, 0, -1]
  - [0, 0, 1, -1]
  - [0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 4:209.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:4:209` gives this Gram tensor.
