---
tag: 4OQA
name: Constructed lattice 4OQA
latex: L_{\mathrm{4OQA}}
certifications:
  derive: e93c3aa2cc3fb62c1dc47e2def5a67afcde372f0ef6cb81e1b976ce1a34bae55
  form.integer_valued: a901457d443c3f3cb9156a2643e1b8386e59e00cfbc685c7afcf5466deabb722
  integral.elementary_primes: c8d14180a5338da04450563043a26428d141c0b1809fa5da1f2df3a8d5f74dc2
  integral.genus_symbol: 1c7e5a0ecc791f54767367b1fb3ef6476db7b8f21d3917f8f4ae7fc2c7fa5919
  integral.genus_class_count: 733fa29389ebd3eb772c69a45758e66afdcb494ff789397bf18e8320e35bc362
  integral.overlattice_count: 5a5efe854c806e49bfaf6dfb194442db9214d5c73c583aec7f1fed8188ed090d
  integral.spinor_genus_count: 711a4eb4e32b450af0cc9923112414affa7a413958aca9674ec15d47ee59d06c
  integral.spinor_genera: a3946906c3d324f0d8d6f8675a59ff458103595c58864cfa547f45796a026e50
  integral.hyperbolic_index: 7a4beac84dd48fb14715332595a1f7d6dbd9a14ca53deb6a3fd8f1d3c0d604bf
  automorphisms.automorphism_group_order: 4dc32a4eebcb6524fcaeb85ffad1536cc1c9e9a6c5d969f6dd52188168ae3aa1
  automorphisms.automorphism_group_generator_morphisms: af9ee232056e455ce64950c62913d344373079b40fb9518042edff3eda29659f
  integral.modular_scale: 19626defbb66379efbb8cff3038c94c5b8e356b9636030846e0539efb474a9f9
  integral.anisotropic_primes: 61a32d77067ca476531170e453db234f4378e7e659c1745dda2cc1eaa67b3228
  integral.local_representations: 1ad6cc4df05e1bf7807bb07b6f11a5d569d1d3ad2b35fb1af190af341b81ee54
  integral.local_densities: d36d114829162eefdbe9b3928bfca998c69b13f38ce24a4ba5535208f534d4c3
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 0, -4, 6]
- [0, 0, 0, 6, -12]
signature: [2, 3]
determinant: -48
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 0, -1, -1/2]
- [0, 0, 0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [2, 2, 2, 6]
  overlattice_count: 31
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{2,3} (2: [1^-1]_5 2^4; 3: 1^4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 2
    - representative: 2
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [3/2, 0, 0, 33/16, 5/2, 0, 0, 15/8]
  - prime: 3
    densities: [8/9, 8/9, 32/27, 8/9, 8/9, 34/27, 8/9, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20]
indefinite:
  isotropic: true
morphisms:
- target: 4OQA
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 2
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4OQA
  name: O(L) generator 3
  matrix:
  - [1, 0, 2, 0, 0]
  - [-1, 1, 0, 1, -3]
  - [0, 0, 1, 0, 0]
  - [0, 0, -1, 1, 0]
  - [0, 0, -1, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 4
  matrix:
  - [1, -2, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [-1, 0, -1, -1, 0]
  - [0, 2, 0, 1, 0]
  - [0, 1, 0, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, -1, -1, -2, 3]
  - [0, 1, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 6
  matrix:
  - [1, 0, 2, 0, 0]
  - [-1, 1, 2, -3, 3]
  - [0, 0, 1, 0, 0]
  - [0, 0, -3, 1, 0]
  - [0, 0, -1, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 7
  matrix:
  - [1, 0, 2, 0, 0]
  - [-1, 1, 0, -1, 3]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, 1, 0]
  - [0, 0, 1, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 8
  matrix:
  - [7, 0, 0, -12, 24]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-6, 0, 0, 10, -21]
  - [-4, 0, 0, 7, -14]
  scale: 1
- target: 4OQA
  name: O(L) generator 9
  matrix:
  - [7, 0, 0, -12, 12]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-6, 0, 0, 10, -9]
  - [-2, 0, 0, 3, -2]
  scale: 1
- target: 4OQA
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, -1, -1, 2, -3]
  - [0, -1, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 11
  matrix:
  - [1, 2, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [1, 0, -1, 1, 0]
  - [0, -2, 0, 1, 0]
  - [0, -1, 0, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, 1, -1, 3]
  - [0, 1, 0, 1, 0]
  - [0, 1, 0, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 13
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -2]
  scale: 1
- target: 4OQA
  name: O(L) generator 14
  matrix:
  - [3, -2, 2, 2, 0]
  - [1, 0, 1, 1, 0]
  - [-1, 1, 0, -1, 0]
  - [-2, 2, -2, -1, 0]
  - [-1, 1, -1, -1, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 15
  matrix:
  - [9, -4, 4, -8, 24]
  - [2, 0, 1, -2, 6]
  - [-2, 1, 0, 2, -6]
  - [-4, 2, -2, 5, -12]
  - [-4, 2, -2, 4, -11]
  scale: 1
- target: 4OQA
  name: O(L) generator 16
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 3, 1, -3, 6]
  - [0, -3, 0, 2, -3]
  - [0, -1, 0, 1, -1]
  scale: 1
- target: 4OQA
  name: O(L) generator 17
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 18
  matrix:
  - [-1, 6, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [3, 0, 1, 3, 0]
  - [0, -6, 0, -1, 0]
  - [0, -3, 0, -1, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 19
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4OQA
  name: O(L) generator 20
  matrix:
  - [9, -22, 2, -12, 18]
  - [1, -3, 0, -2, 3]
  - [-1, -2, -1, 0, -3]
  - [-8, 20, -2, 10, -15]
  - [-5, 13, -1, 7, -10]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0013, 3ID5.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0001, 0013, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 0001, 0013, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0013, 3ID5.
