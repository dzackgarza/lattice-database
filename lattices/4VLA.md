---
tag: 4VLA
name: Constructed lattice 4VLA
latex: L_{\mathrm{4VLA}}
certifications:
  derive: 86da9b837a0d01ec53fda1197814b712d5340e50fe28e3b46886f1dcd3772bc0
  form.integer_valued: a811819e358a4cf4a96d75abd3153436511eae13bf747b7e64298b0df40488de
  integral.elementary_primes: 8e878eb10a41d9190a4e438f17c6f025328317d2feae184a9646f68d6974ea6b
  integral.genus_symbol: 809f8d8be565e4c3298b3ad04abfd88ffa3e7e41f0a42fd296f12c2f519463a6
  integral.genus_class_count: 04b850e5166a5bcb954e625f0002a95c4f97298937156226798690fa6d520d4e
  integral.overlattice_count: b65e6aa5632eeac930d8c75f1fe80f1b47313b57732d8ef1380796ae656918d9
  integral.spinor_genus_count: 6eb6b1260d2065d04dae4e7b663388063d3cf05c478a29de87539d520564bb5b
  integral.spinor_genera: 09c20f3e1d943df5453a0e46b87ddeea1838872c3391c3d75bda22ee13ba286a
  integral.hyperbolic_index: 09a74e1ede3bf2dd08625fb0255470b625098ea5c85fd75d2a36a283f0040549
  automorphisms.automorphism_group_order: 76195daebc9d049d693b116df694c668a36a5de4777201bc0e0883ff28bbad6c
  automorphisms.automorphism_group_generator_morphisms: 9434845cef2bb754abbd3661c75c5d976e1d217396f92fd37d532f7112ab25c3
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 2, -3]
- [0, 0, 0, -3, 6]
signature: [2, 3]
determinant: -3
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, 2, 1]
- [0, 0, 0, 1, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{2,3} (2: [1^-5]_5; 3: 1^4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 2
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17]
indefinite:
  isotropic: true
morphisms:
- target: 4VLA
  name: O(L) generator 1
  matrix:
  - [0, -1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4VLA
  name: O(L) generator 2
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4VLA
  name: O(L) generator 3
  matrix:
  - [0, 0, -1, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4VLA
  name: O(L) generator 4
  matrix:
  - [1, 1, -1, -1, 3]
  - [-1, 1, -1, -2, 3]
  - [1, -1, -1, 1, 0]
  - [-1, -1, 2, 2, -6]
  - [-1, 0, 1, 0, -2]
  scale: 1
- target: 4VLA
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, -3]
  - [0, 0, 0, 1, -2]
  scale: 1
- target: 4VLA
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -3, 0, -4, 6]
  - [0, -4, 0, -6, 9]
  - [0, -2, 0, -3, 4]
  scale: 1
- target: 4VLA
  name: O(L) generator 7
  matrix:
  - [-1, 1, -1, 2, -3]
  - [-1, -1, 1, -1, 0]
  - [-1, 1, 1, 1, -3]
  - [-2, 1, 1, 2, -6]
  - [-1, 0, 1, 0, -2]
  scale: 1
- target: 4VLA
  name: O(L) generator 8
  matrix:
  - [0, -1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4VLA
  name: O(L) generator 9
  matrix:
  - [-4, -4, -1, -8, 12]
  - [5, 4, 4, 10, -18]
  - [4, -1, 4, 4, -12]
  - [10, 4, 8, 16, -33]
  - [6, 4, 4, 11, -20]
  scale: 1
- target: 4VLA
  name: O(L) generator 10
  matrix:
  - [0, 0, 1, 0, 0]
  - [-3, 0, 0, 4, -6]
  - [0, 1, 0, 0, 0]
  - [-2, 0, 0, 3, -6]
  - [-2, 0, 0, 3, -5]
  scale: 1
- target: 4VLA
  name: O(L) generator 11
  matrix:
  - [5, 5, 7, -13, 15]
  - [-5, -1, -5, 10, -15]
  - [-5, -5, -5, 11, -12]
  - [-11, -10, -13, 26, -30]
  - [-7, -5, -8, 16, -20]
  scale: 1
- target: 4VLA
  name: O(L) generator 12
  matrix:
  - [-8, 0, 3, 6, -18]
  - [0, 1, 0, 0, 0]
  - [3, 0, 0, -2, 6]
  - [6, 0, -2, -3, 12]
  - [6, 0, -2, -4, 13]
  scale: 1
- target: 4VLA
  name: O(L) generator 13
  matrix:
  - [-1, 5, 1, 2, -9]
  - [-1, -1, -1, 1, 0]
  - [1, -7, -5, 1, 9]
  - [1, -10, -7, 2, 12]
  - [1, -7, -4, 0, 10]
  scale: 1
- target: 4VLA
  name: O(L) generator 14
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -5, 0, 6, -6]
  - [0, 0, 1, 0, 0]
  - [0, -6, 0, 7, -6]
  - [0, -2, 0, 2, -1]
  scale: 1
- target: 4VLA
  name: O(L) generator 15
  matrix:
  - [20, -4, -19, 28, -18]
  - [-16, 5, 16, -22, 12]
  - [-19, 4, 16, -26, 18]
  - [-38, 8, 34, -53, 36]
  - [-26, 6, 24, -36, 23]
  scale: 1
- target: 4VLA
  name: O(L) generator 16
  matrix:
  - [-8, 0, -3, -12, 18]
  - [0, 19, 24, 12, -54]
  - [-3, 24, 32, 12, -66]
  - [6, 30, 42, 29, -102]
  - [0, 24, 32, 16, -71]
  scale: 1
- target: 4VLA
  name: O(L) generator 17
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 3ID4.
- tag: 3ID4
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 3ID4.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICW, 3ICW, 3ID4.
