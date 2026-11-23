---
tag: 6DLO
name: Constructed lattice 6DLO
latex: L_{\mathrm{6DLO}}
certifications:
  derive: e5ac42ca9ee7997826a098110d0ac1b3c8487593137bb8ca5898f8f20368ff69
  form.integer_valued: 1ae740a3a49755f7e47e2cae8a1aae04b5b67e9ad26dd542f2bed6f863f81634
  integral.elementary_primes: e0f0f564e70ff6459e5288d9e08c24466996175cd38ad25b346f0da3c05775e5
  integral.genus_symbol: daf1983910b4174e0f0ab56090fa06054ff5f3f0be30b8f8c1504bbe9a51cc56
  integral.genus_class_count: 46f2aec5536bba5f841fddc4f5140c672ddb9704d04c7dcf8bf2108aba70c96d
  integral.overlattice_count: 33865f0afe79dac150887882fb2508dd278ff480f2ae0d01d636b87c8572c5a7
  integral.spinor_genus_count: e12bff22952ac44c92a95473241616b554ea3b02b5d324d85d8e7c7fa5af68d6
  integral.spinor_genera: 8f38933a749038930240bb4e0f055da07a7763c77a86806d4c64c259cac674ff
  integral.hyperbolic_index: 9d190e1e462a23be3bbea32c164630f219f48cfda9af7e7c972aab592c444155
  automorphisms.automorphism_group_order: 82c8b7682269cf4f78637eb32acd59acec643a52616a646421de9a5d68f1b58b
  automorphisms.automorphism_group_generator_morphisms: 448ff643d86cb4c8424a2fa391b0ab24df08e43c1453702f962e87ed19bd1e53
rank: 5
gram_tensor:
- [0, 2, 0, 0, 0]
- [2, 0, 0, 0, 0]
- [0, 0, 2, -1, 0]
- [0, 0, -1, 2, -1]
- [0, 0, 0, -1, 2]
signature: [4, 1]
determinant: -16
definiteness: indefinite
dual_gram_tensor:
- [0, 1/2, 0, 0, 0]
- [1/2, 0, 0, 0, 0]
- [0, 0, 3/4, 1/2, 1/4]
- [0, 0, 1/2, 1, 1/2]
- [0, 0, 1/4, 1/2, 3/4]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 8
  discriminant_group: [2, 2, 4]
  overlattice_count: 11
  bad_reduction_primes: [2]
  genus_symbol: 'II_{4,1} (2: 1^-2:2^-2 [4^1]_7)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 6DLO
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 1, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 6DLO
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 6DLO
  name: O(L) generator 3
  matrix:
  - [1, -2, -2, 1, 0]
  - [0, 1, 0, 0, 0]
  - [0, -2, -1, 1, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 6DLO
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 6DLO
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [-1, 1, 1, -1, 1]
  - [1, 0, 0, 1, -1]
  - [0, 0, 0, 1, 0]
  - [1, 0, -1, 1, 0]
  scale: 1
- target: 6DLO
  name: O(L) generator 6
  matrix:
  - [6, -1, -3, 0, 1]
  - [-11, 3, 7, 0, -3]
  - [14, -3, -8, 0, 3]
  - [10, -2, -5, -1, 3]
  - [6, -1, -3, 0, 2]
  scale: 1
- target: 6DLO
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0013, 0023.
- tag: '0023'
  relation: This presentation is obtained by orthogonal sum of 0013, 0023.
---

The selected Gram tensor is obtained by orthogonal sum of 0013, 0023.
