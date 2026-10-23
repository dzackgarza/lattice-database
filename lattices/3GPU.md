---
tag: 3GPU
name: watson 4:179
latex: watson 4:179
aliases: []
certifications:
  derive: 163af2337f9a847fa3044afe5041233e906f33b730a08813a4427be64a4d2705
  form.integer_valued: 1173c350e9b17cfaf929d157af07eaf321f8879c3ff14695ce5a78514d1420e6
  integral.elementary_primes: 2555eae7ee67e94e7f27694a2031509721d5ee183e328756d259fe5fdecc4568
  integral.genus_symbol: cfff0bd4342dc13796aea2b1d3865fe1905a6c26da5f0435324ffa723881c07d
  integral.genus_class_count: 8db8fe85c5939d92584099f100ad5880bc82f4377326cda13494538ebb90e8a1
  integral.spinor_genus_count: ab2c47f743bc17f3d8f425c6aa85bf0d488d9874428f2ee770483ca1312777d5
  integral.spinor_genera: 8e59392bfcb198c68ef45d14c7dab8770a42d81bf524c6ab3ff12f379127b6a3
  integral.hyperbolic_index: 6c095648f2ad65281296f5714aaad79f7e221c1515c67e219e598383f41fa794
  definite.automorphism_group_order: fb3bfa14e3552046ba51f2cb3da9ff4ba8a3a8203e56467a4ceae98d07b22dab
  definite.automorphism_group_generator_morphisms: e72a3e99ca4c1cbfa1727a05bfc1f99ba21899349843b9fe5d4f172b087ffce8
rank: 4
gram_tensor:
- [10, 5, -4, 4]
- [5, 14, -2, 2]
- [-4, -2, 20, 3]
- [4, 2, 3, 20]
signature: [4, 0]
determinant: 36501
definiteness: positive_definite
dual_gram_tensor:
- [10/69, -1/23, 2/69, -2/69]
- [-1/23, 2/23, 0, 0]
- [2/69, 0, 4/69, -1/69]
- [-2/69, 0, -1/69, 4/69]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 69
  discriminant_group: [23, 23, 69]
  bad_reduction_primes: [2, 3, 23]
  quadratic_character: 69
  genus_symbol: 'II_{4,0} (2: 1^-4; 3: 1^3 3^-1; 23: 1^-1 23^-3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 10
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 23
    simple_roots:
    - [0, 0, 1, 1]
  - type: A1
    scale: 23
    simple_roots:
    - [1, -2, 0, 0]
root_sublattice:
  invariant_factors: [1, 1]
morphisms:
- target: 3GPU
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3GPU
  name: O(L) generator 2
  matrix:
  - [1, 1, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 0, -1]
  - [0, 0, -1, 0]
  scale: 1
- target: 3GPU
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, -1]
  - [0, 0, -1, 0]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 4:179.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:4:179` gives this Gram tensor.
