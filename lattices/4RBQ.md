---
tag: 4RBQ
name: Constructed lattice 4RBQ
latex: L_{\mathrm{4RBQ}}
certifications:
  derive: 256c26cca89f17285777e872329977f61574ab3ce7d818fced557c7b9ff56696
  form.integer_valued: c006a8c325f57cc52f2f7c7cbccf328d9fe96908f508a4bb8792a8770be3f794
  integral.elementary_primes: 66c461e6037a08b9b7481673a4fed2459bc86997227e7c22e476a37ef13dff74
  integral.genus_symbol: 773baacb67cdaec01bf6fa28b8656860adb2209eb96ef0d2b318c36fa1acd391
  integral.genus_class_count: 1e73bb4cd5f9b6b49f2b27a59e444cbeb47ae482156a243b4958bea42e2fe20c
  integral.overlattice_count: 25a0a35d18a6d35fb4715ba372939ff57603a9811053f5ecd11a7bc694732cfe
  integral.spinor_genus_count: 86e20ab77342d1079874a083d5cdfb9757750094e774bd10ab2c2cefce830b18
  integral.spinor_genera: cf08d5b78814c5ba1cb7b50f06ff175368d23c23f0ca567fca4ec5f066241bb2
  integral.hyperbolic_index: 516c39f2328b32ccb60abe1b904ec66afe9d6454544dc33a9deab43c43b057cb
  automorphisms.automorphism_group_order: 3678154d3bd8d23b6e7762c21e34fd57b556f9a66fd90e50fa199ce9f33c5823
  automorphisms.automorphism_group_generator_morphisms: a7e24a0b17bc3ad49a7e6541fb88ecc22db6f14a9dfcecd20db5b4e38c1ccda0
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -4, 2, 0, 0]
- [0, 2, -4, 2, 0]
- [0, 0, 2, -4, 2]
- [0, 0, 0, 2, -4]
signature: [1, 4]
determinant: 80
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -2/5, -3/10, -1/5, -1/10]
- [0, -3/10, -3/5, -2/5, -1/5]
- [0, -1/5, -2/5, -3/5, -3/10]
- [0, -1/10, -1/5, -3/10, -2/5]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 10
  discriminant_group: [2, 2, 2, 10]
  overlattice_count: 31
  bad_reduction_primes: [2, 5]
  genus_symbol: 'I_{1,4} (2: [1^-1]_5 2^4; 5: 1^-4 5^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11]
indefinite:
  isotropic: true
morphisms:
- target: 4RBQ
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, -1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4RBQ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4RBQ
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4RBQ
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 1, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4RBQ
  name: O(L) generator 5
  matrix:
  - [3, 0, 4, -2, 2]
  - [-1, 1, -2, 1, -1]
  - [-2, 0, -3, 2, -2]
  - [-1, 0, -2, 2, -1]
  - [-1, 0, -2, 1, 0]
  scale: 1
- target: 4RBQ
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4RBQ
  name: O(L) generator 7
  matrix:
  - [5, 6, 2, 0, 0]
  - [-3, -4, -1, 0, 0]
  - [-2, -3, 0, -1, 1]
  - [-1, -2, 1, -1, 0]
  - [-1, -1, 0, -1, 0]
  scale: 1
- target: 4RBQ
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 1, 0, 0, -1]
  - [0, 0, 1, 0, -1]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4RBQ
  name: O(L) generator 9
  matrix:
  - [3, 0, 4, -2, 2]
  - [-1, 0, -2, 1, 0]
  - [-2, 0, -3, 1, -1]
  - [-2, 0, -3, 2, -2]
  - [-1, 1, -2, 1, -1]
  scale: 1
- target: 4RBQ
  name: O(L) generator 10
  matrix:
  - [5, 8, 0, -2, 2]
  - [0, 0, 0, 1, -1]
  - [-3, -5, 0, 2, -2]
  - [-2, -3, 0, 1, -2]
  - [-1, -2, 1, 0, -1]
  scale: 1
- target: 4RBQ
  name: O(L) generator 11
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3IF6.
- tag: 3IF6
  relation: This presentation is obtained by orthogonal sum of 0001, 3IF6.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3IF6.
