---
tag: 3HIS
name: BGF.2.314 (union:131)
latex: BGF.2.314
aliases: [BGF.2.314]
certifications:
  derive: 6d30adcda37a4368154268c559750f338e05eb95d80114cd15a6421f6b37a7cc
  form.integer_valued: 7dc3b0222d4565f06c7ffb3153a784e19cdb10a34047f627dec703094a9e7bed
  integral.elementary_primes: 63b3227b32eff934ec7bd7d328efffcbc2710db0fb4020f5ece239a2fcbee3c6
  integral.genus_symbol: b4682881c285efe744897fb893f79dafcf51b6043fc64994c0778249cd58d3ae
  integral.genus_class_count: 6989cb3359423589fbb7006b0cfc5cf93ebe336b8a2c1452c4ee0a0fcdb02add
  integral.overlattice_count: 07357f73d6c3e6da381005d1eb0df328c74e97a206775557d70bdcdfac9b29b0
  integral.hyperbolic_index: 381fa919e850cdee55ac0dcb54188e1ae5476b11d40d720ff3a81aaaefa82a7c
  definite.automorphism_group_order: 5175ec26e57d6b3b869114121abaac8e4f29842a57c5db33fd73e26da0c4a314
  definite.automorphism_group_generator_morphisms: 38168c44d364561441e421ae5e018908efdb3ffe75fae3760862ce540c7129f2
  integral.primitive_orbits: fb75fa91210ccf93b429576ab226c32e7f37d4e977556af5aa38ad05d7fd97e6
  integral.modular_scale: 5add4b4eb90c4734ddfc56b6bd2678ecd2ce5bc1227210ed44e8c1afd91cc444
  definite.genus_theta_series: 2991c9c89c9ddd6b0cf424a8509272008e1b809adfd6df4951d629ed9db328dc
  definite.theta_series_cuspidal_component: ee7508b56d15115d623e6fc17f5c3e64ff27e78c042f2a8f1a1b610112bb873f
  definite.siegel_eisenstein_coefficients: 9ecacbb8f9e5038ce166de02bbcc75a92ae394622df3401c5b94651ec23804fa
  integral.anisotropic_primes: 0869229cf40f2509fe96c2ba225e37b51df02598fd84ccc6909a11239fe22826
  integral.local_representations: 9999da8395c9523238d7c746785d3ea2a5e12ce6f1a14e982a33d5d2423d4182
  integral.local_densities: 6e05fabb4706256c7ea10b8618eedb343469777573b5c1ac53b0476184253291
rank: 2
gram_tensor:
- [3, 1]
- [1, 4]
signature: [2, 0]
determinant: 11
definiteness: positive_definite
dual_gram_tensor:
- [4/11, -1/11]
- [-1/11, 3/11]
form:
  integer_valued: true
integral:
  elementary_primes: [11]
  parity: odd
  level: 22
  modular_scale: 11
  discriminant_group: [11]
  overlattice_count: 1
  bad_reduction_primes: [2, 11]
  quadratic_character: -11
  genus_symbol: 'I_{2,0} (2: [1^-2]_4; 11: 1^1 11^1)'
  genus_class_count: 2
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 0, 2, 2]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 0, 2, 2]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 1, 1]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 2, 2]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 2, 2]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2, 11]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 0
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 0
  - prime: 11
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 11
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 3]
  - prime: 11
    densities: [2, 0, 2, 2, 2, 0, 0, 0, 2, 0, 2, 2]
definite:
  minimum: 3
  kissing_number: 2
  automorphism_group_order: 2
  automorphism_group_generator_morphisms: [O(L) generator 1]
  minimal_vectors:
  - [-1, 0]
  - [1, 0]
  perfect: false
  theta_series: [1, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 4]
  genus_theta_series: [1, 2/3, 0, 4/3, 2, 4/3, 0, 0, 0, 2, 0, 2/3, 4]
  theta_series_cuspidal_component: [0, -2/3, 0, 2/3, 0, 2/3, 0, 0, 0, 0, 0, -2/3, 0]
  siegel_eisenstein_coefficients: [2/3, 0, 4/3, 2, 4/3, 0, 0, 0, 2, 0, 2/3, 4]
  root_system: []
  roots: []
root_sublattice:
  invariant_factors: []
morphisms:
- target: 3HIS
  name: O(L) generator 1
  matrix:
  - [-1, 0]
  - [0, -1]
  scale: 1
families: []
related: []
references:
- citation: G. Nebe and N. J. A. Sloane, Catalogue of Lattices, archive entry union:131.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz
---

Catalogue of Lattices archive entry `union:131` names `BGF.2.314`.
