---
tag: 3TAD
name: Constructed lattice 3TAD
latex: L_{\mathrm{3TAD}}
certifications:
  derive: 495f8e501109c597af44e32c54b030f6e4416221ae3386b71be1fe1cfee98621
  form.integer_valued: 238be68f2002223953ec37a3dfe1ad498b38501454f1c7605da310c5f101efff
  integral.elementary_primes: e7de3bf90b18df27ac3ff7e480ec52164b8426aac9f28701c994b4cf8740b187
  integral.genus_symbol: bcfc456f5f8b4f304847407a0b94a1ddf915a0a46fc58947618f9aba3f4744a0
  integral.genus_class_count: a756edfe30403e8261a0f0490242e8b1ca1749d54d9a2acfa98edf7652748adf
  integral.overlattice_count: 21ba266bbaedcb2bd72672fdd70d24a1c35853257964d73f4f912b670f0028a8
  integral.spinor_genus_count: 171632958e2d2b86f8ac32329b8e89cca4339d272f9b647f156d823c2ab62277
  integral.spinor_genera: 6a4b4ff67b2e2aaa6104fc2ff0f39bd651908756c703d93d4193b4297a683d34
  integral.hyperbolic_index: 13c0c66737fcffb4ddbc5bb96878ae629298f806faba918527977c01c0421f8e
  automorphisms.automorphism_group_order: 863d48f25964da8245e489ba8ae5f60bae5c5c4e3a0b0c5d6c3e4caf29e9c933
  automorphisms.automorphism_group_generator_morphisms: b833cd095f2b6adddb1bd5af8dd61e2e7a1ed486b18efd2c58e33b791ad51005
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, -4, 2]
- [0, 0, 0, 2, -4]
signature: [2, 3]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, -1, 0, 0]
- [0, 0, 0, -1/3, -1/6]
- [0, 0, 0, -1/6, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{2,3} (2: [1^-3]_5 2^2; 3: 1^4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16, O(L) generator 17, O(L) generator 18, O(L) generator 19, O(L) generator 20, O(L) generator 21, O(L) generator 22, O(L) generator 23, O(L) generator 24, O(L) generator 25, O(L) generator 26, O(L) generator 27, O(L) generator 28]
indefinite:
  isotropic: true
morphisms:
- target: 3TAD
  name: O(L) generator 1
  matrix:
  - [2, 1, -2, 0, 0]
  - [1, 2, -2, 0, 0]
  - [2, 2, -3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 2
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 3
  matrix:
  - [0, -1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 3TAD
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0, 0]
  - [-1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 5
  matrix:
  - [0, 3, -2, -2, -2]
  - [-1, 0, 0, 0, 0]
  - [0, 2, -1, -2, -2]
  - [0, 0, 0, -1, 1]
  - [0, -1, 1, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 6
  matrix:
  - [-7, 0, 0, -12, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [-2, 0, 0, -3, -1]
  - [2, 0, 0, 4, -1]
  scale: 1
- target: 3TAD
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 8
  matrix:
  - [-3, 0, 2, 2, 2]
  - [0, -1, 0, 0, 0]
  - [-2, 0, 1, 2, 2]
  - [0, 0, 0, -1, 1]
  - [-1, 0, 1, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 9
  matrix:
  - [3, -2, 0, -6, 0]
  - [-2, 3, 0, 6, 0]
  - [0, 0, -1, 0, 0]
  - [-1, 1, 0, 3, -1]
  - [1, -1, 0, -2, -1]
  scale: 1
- target: 3TAD
  name: O(L) generator 10
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 3, -2, 2, 2]
  - [0, -2, 1, -2, -2]
  - [0, 0, 0, -1, 1]
  - [0, 1, -1, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 11
  matrix:
  - [-1, 6, 6, 0, 0]
  - [-6, -1, 0, 12, -6]
  - [-6, 0, 1, 12, -6]
  - [0, -3, -3, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 12
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 13
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -3, -2, 2, 2]
  - [0, -2, -1, 2, 2]
  - [0, 0, 0, -1, 1]
  - [0, -1, -1, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 14
  matrix:
  - [-2, 1, -2, 0, 0]
  - [-1, 2, -2, 0, 0]
  - [2, -2, 3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 15
  matrix:
  - [-4, -1, 4, 0, 0]
  - [1, -4, 0, -4, -4]
  - [0, -4, 1, -4, -4]
  - [0, 0, 0, -1, 1]
  - [-2, 0, 2, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 16
  matrix:
  - [1, 6, 0, 12, -6]
  - [-6, 7, 6, 12, 0]
  - [0, 6, 1, 12, -6]
  - [3, -2, -3, -3, -1]
  - [0, 2, 0, 4, -1]
  scale: 1
- target: 3TAD
  name: O(L) generator 17
  matrix:
  - [-1, -2, 0, -2, -2]
  - [-2, -1, 0, -2, -2]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 1]
  - [-1, -1, 0, -2, -1]
  scale: 1
- target: 3TAD
  name: O(L) generator 18
  matrix:
  - [-1, -2, 0, -4, 2]
  - [-2, -1, 0, -4, 2]
  - [0, 0, -1, 0, 0]
  - [1, 1, 0, 3, -1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 19
  matrix:
  - [7, -8, -6, -16, 2]
  - [10, 11, -8, 6, 18]
  - [8, -6, -7, -14, 4]
  - [-1, -4, 1, -5, -3]
  - [4, 3, -3, 0, 7]
  scale: 1
- target: 3TAD
  name: O(L) generator 20
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 7, -6, 0, -6]
  - [0, 6, -5, 0, -6]
  - [0, 1, -1, 1, -1]
  - [0, 2, -2, 0, -1]
  scale: 1
- target: 3TAD
  name: O(L) generator 21
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, -1]
  - [0, 0, 0, -1, 0]
  scale: 1
- target: 3TAD
  name: O(L) generator 22
  matrix:
  - [-1, 2, 0, 2, -4]
  - [2, 7, -4, 6, -12]
  - [0, 4, -1, 4, -8]
  - [0, 0, 0, 1, 0]
  - [1, 3, -2, 3, -5]
  scale: 1
- target: 3TAD
  name: O(L) generator 23
  matrix:
  - [-1, 2, 0, 2, -4]
  - [2, -1, 0, -2, 4]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [1, -1, 0, -1, 3]
  scale: 1
- target: 3TAD
  name: O(L) generator 24
  matrix:
  - [7, 0, 0, 12, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-4, 0, 0, -7, 0]
  - [-2, 0, 0, -4, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 25
  matrix:
  - [1, 8, -4, 12, -12]
  - [8, 17, -12, 28, -20]
  - [4, 12, -7, 20, -16]
  - [-2, -6, 4, -9, 8]
  - [2, 2, -2, 4, -1]
  scale: 1
- target: 3TAD
  name: O(L) generator 26
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 3TAD
  name: O(L) generator 27
  matrix:
  - [1, 8, -6, 8, -10]
  - [4, -1, 0, 4, 4]
  - [2, -4, 3, 0, 6]
  - [1, 4, -3, 5, -5]
  - [2, 2, -2, 4, -1]
  scale: 1
- target: 3TAD
  name: O(L) generator 28
  matrix:
  - [1, -8, 6, -10, 8]
  - [10, 41, -32, 36, -54]
  - [4, 6, -5, 2, -10]
  - [-4, -19, 15, -17, 24]
  - [1, 3, -2, 3, -5]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID1.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID1.
- tag: 3ID1
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID1.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 3ICW, 3ID1.
