---
tag: 5MAC
name: Constructed lattice 5MAC
latex: L_{\mathrm{5MAC}}
certifications:
  derive: f2b04babd82a7d3e9faae1dc20a145272151301621a9f399f7541c984d9909f8
  form.integer_valued: 87958ce00131d291a69c93420093619e430de37947e33e6bea40a44cefb6a448
  integral.elementary_primes: 8c5a46719d65e49b6c8a5acb54c4ea6809c67988c2fce841a2449efb9595f656
  integral.genus_symbol: 760ca18e381471728554b7514ec9119e6aafbd285b4f28de5b4b719507e0c95b
  integral.genus_class_count: d86467cbf8cfb8b5f2a2d69fc647134a43ee7e7899a0efe940095e3523ca3339
  integral.overlattice_count: adcd01a7d4955033801c4d9dd0539a82052a993247e7cd364c9660f5119f4c8f
  integral.spinor_genus_count: 2e83c7dd36b43d823b8904a2b11a6eea9dac4a7489b54aca0b1d8d6c6aba5001
  integral.spinor_genera: 48492501084c701dca508803abd7c0917c6ed6ffc14a7dba141c220bd16b007c
  integral.hyperbolic_index: ecb5147a0f1428d6e9c8b3ea208362eb1565a94850cbc1da88be610e35e7ccbe
  automorphisms.automorphism_group_order: ff244e921e9d555eb36c794ebd46ca316fc0854fe79f6ae8601cadb8e0bb7f8e
  automorphisms.automorphism_group_generator_morphisms: 609de51bb9cbe0c818040bce8f308725d09b43a34b969e74e945782e1dc61aae
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, 2, -1]
- [0, 0, 0, -1, 2]
signature: [4, 1]
determinant: -24
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, 2/3, 1/3]
- [0, 0, 0, 1/3, 2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  discriminant_group: [2, 2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{4,1} (2: 1^-2 [2^3]_1; 3: 1^-4 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16]
indefinite:
  isotropic: true
morphisms:
- target: 5MAC
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MAC
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MAC
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MAC
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5MAC
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5MAC
  name: O(L) generator 6
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MAC
  name: O(L) generator 7
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5MAC
  name: O(L) generator 8
  matrix:
  - [0, -1, 2, -2, 1]
  - [-1, 0, 2, -2, 1]
  - [-2, -2, 5, -4, 2]
  - [-2, -2, 4, -3, 2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MAC
  name: O(L) generator 9
  matrix:
  - [-1, 0, 2, -2, 1]
  - [0, 1, 0, 0, 0]
  - [-2, 0, 3, -2, 1]
  - [-2, 0, 2, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MAC
  name: O(L) generator 10
  matrix:
  - [-1, -2, 2, 0, 0]
  - [-2, -1, 2, 0, 0]
  - [-2, -2, 3, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MAC
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5MAC
  name: O(L) generator 12
  matrix:
  - [-3, 4, 6, -3, 3]
  - [-4, 3, 6, -3, 3]
  - [-6, 6, 11, -6, 6]
  - [-4, 4, 8, -5, 5]
  - [-2, 2, 4, -2, 3]
  scale: 1
- target: 5MAC
  name: O(L) generator 13
  matrix:
  - [-10, -17, 20, -3, 0]
  - [-7, -12, 14, -2, 1]
  - [-16, -26, 31, -5, 1]
  - [-12, -18, 22, -4, 1]
  - [-6, -8, 10, -1, 0]
  scale: 1
- target: 5MAC
  name: O(L) generator 14
  matrix:
  - [-25, -24, 38, -13, -1]
  - [-24, -25, 38, -13, -1]
  - [-38, -38, 59, -20, -2]
  - [-18, -18, 28, -9, -2]
  - [-10, -10, 16, -6, -1]
  scale: 1
- target: 5MAC
  name: O(L) generator 15
  matrix:
  - [-5, 0, 6, -3, 0]
  - [-6, -1, 8, -5, 1]
  - [-12, -2, 15, -8, 1]
  - [-10, -2, 12, -6, 1]
  - [-2, 0, 2, -1, 1]
  scale: 1
- target: 5MAC
  name: O(L) generator 16
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 0012.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 3ICX, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0002, 3ICX, 0012.
