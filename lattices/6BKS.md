---
tag: 6BKS
name: Constructed lattice 6BKS
latex: L_{\mathrm{6BKS}}
certifications:
  derive: 49e70cc0c440487f5ce87bb1ad1572e38a60ca3235ebf22fc9c612461125eae7
  form.integer_valued: d591371b9f815f50a94aee4a7d29cfe80fa5cdbb5f279f613f489ac5417b505c
  integral.elementary_primes: 37cbf2b6ac4397540c8cefe8dceeeb45fba53104633952982df60a79cf146d13
  integral.genus_symbol: 2061a0c1bb51db51c6211dae8140aea1158d9457805e0375a92397f097b360c0
  integral.genus_class_count: 9e567aa290b926b474b6bbd5dde5514661b737d4a03fadc2e06ff6f9d405a08d
  integral.overlattice_count: 17920077a2acd81d4f0333afaf3eb097aa732ebc5a60e000b853ab57af5ac8da
  integral.spinor_genus_count: 550baa196c77a1f01f90cf4b7f6907420c4f91cf68eafc65dc8afa0e3a07c075
  integral.spinor_genera: d06f0d100f44cb633d0dc2326f8dbc3d80ed662a991ec6d28ae830cd7fa23ca4
  integral.hyperbolic_index: d8044bf030db29561a55047db38bc6c48e2dca92cd81c9bc0208dea35ef47b2a
  automorphisms.automorphism_group_order: 6c17f5812faaeac173f8d4f5f191db8b0931d56f8f6a282169ab4a0ca9166161
  automorphisms.automorphism_group_generator_morphisms: c1f0b565b880158bb899defae23f75f78104ca2405ae77603e0c1527fce3afeb
rank: 4
gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, -2, 3]
- [0, 0, 3, -6]
signature: [1, 3]
determinant: -3
definiteness: indefinite
dual_gram_tensor:
- [0, -1, 0, 0]
- [-1, 0, 0, 0]
- [0, 0, -2, -1]
- [0, 0, -1, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: even
  level: 3
  discriminant_group: [3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{1,3} (2: 1^-4; 3: 1^-3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6BKS
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, -1, 1]
  scale: 1
- target: 6BKS
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [-1, 1, 1, -3]
  - [-1, 0, 2, -3]
  - [-1, 0, 1, -2]
  scale: 1
- target: 6BKS
  name: O(L) generator 3
  matrix:
  - [1, -1, -2, 3]
  - [0, 1, 0, 0]
  - [0, -1, -1, 3]
  - [0, 0, 0, 1]
  scale: 1
- target: 6BKS
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0]
  - [-1, 1, -1, 0]
  - [0, -1, -1, 3]
  - [0, 0, -1, 2]
  scale: 1
- target: 6BKS
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID3.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 3ICY, 3ID3.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICY, 3ID3.
