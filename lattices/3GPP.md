---
tag: 3GPP
name: watson 4:174
latex: watson 4:174
aliases: []
certifications:
  derive: 0adc2bddd82ee9dda442dc3049e39f7059aec986aaad355b64e5b249f99a2241
  form.integer_valued: 1a0618b23dd6121857263c21bef90208cc7026f1864d132860c68a65e2a6d020
  integral.elementary_primes: e82f479fe46135640e2171b2ce540913dcebd4b0eabbb5e29018bc4c22a9d9c7
  integral.genus_symbol: 1be3ccc442822d6f30162fe206b76adac4b7d7e1dde076f24071d35888812118
  integral.genus_class_count: 1ebe8276816c14c2ae37764dd79a47bd5f09c703c983ac8ba7db72cb16600de0
  integral.overlattice_count: b344b7acb9c40b7e393366ebc8f5661daedb1f03ea344538f46ef21033ea696f
  integral.spinor_genus_count: 67ec5e4662996e6dc8163eaa6ee3932953ab68eb77738c6d32a64ba63dbb28e1
  integral.spinor_genera: b29b7549a167360bc1d185749fa85af7072057fbe90b1677ec6872115181f223
  integral.hyperbolic_index: a24361906d0361d456c60b7e9ee16becbc0a4b7b4cc2c1629851456761d83fb4
  definite.automorphism_group_order: 31d7f2ed547180e0bd3ef845c841bd7c3e7d7ac97f88111788fa231100bcace1
  definite.automorphism_group_generator_morphisms: 707b1d53a77cd645d31681498fb95b00917b06a3e980ca5e608d247cc5f3b56e
rank: 4
gram_tensor:
- [2, -1, 0, 0]
- [-1, 8, 0, 0]
- [0, 0, 30, -15]
- [0, 0, -15, 30]
signature: [4, 0]
determinant: 10125
definiteness: positive_definite
dual_gram_tensor:
- [8/15, 1/15, 0, 0]
- [1/15, 2/15, 0, 0]
- [0, 0, 2/45, 1/45]
- [0, 0, 1/45, 2/45]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 45
  discriminant_group: [15, 15, 45]
  overlattice_count: 14
  bad_reduction_primes: [2, 3, 5]
  quadratic_character: 5
  genus_symbol: 'II_{4,0} (2: 1^-4; 3: 1^-1 3^2 9^1; 5: 1^-1 5^-3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 2
  kissing_number: 2
  automorphism_group_order: 48
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 2, 0, 0, 0, 0, 0, 6, 0, 0, 0, 4]
  root_system: [A1]
  roots:
  - type: G2
    scale: 15
    simple_roots:
    - [0, 0, 0, 1]
    - [0, 0, 1, -1]
  - type: A1
    scale: 1
    simple_roots:
    - [1, 0, 0, 0]
  - type: A1
    scale: 15
    simple_roots:
    - [1, 2, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 2]
morphisms:
- target: 3GPP
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3GPP
  name: O(L) generator 2
  matrix:
  - [1, -1, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 3GPP
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 3GPP
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 4:174.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:4:174` gives this Gram tensor.
