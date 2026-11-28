---
tag: 5AEX
name: Constructed lattice 5AEX
latex: L_{\mathrm{5AEX}}
certifications:
  derive: 692bd5df394df37c05b3351147055fead79d7c846a03d793a5bb3ee33318efe7
  form.integer_valued: 8c1a19e95555bbfa21ccb3317b5f9db2b12326c5ea409360ac644fff434d0ed8
  integral.elementary_primes: b3d0de5ec953f1fd77b3bf84148e14d09c712652366e5b373245a1a49d13e0c3
  integral.genus_symbol: eed26807988c6ce55d3588db25a0eaa4992284ca8ce66041c8606e2136c59285
  integral.genus_class_count: 9bdf73cb8758c42fc3b827d4e124b2e6823966afb50bffbf37861b29f2af3a6d
  integral.overlattice_count: 7fd696b535836bdd2d971b176861f500be5ac1e9a66b02bc0a508ec5ef0c5be4
  integral.spinor_genus_count: 0a91af2fe3fb0a3429c939d47046b1929895787e5b3ab4f2db87af375877d496
  integral.spinor_genera: d35c023955c48e1d0a30b7ddf26506ea630a02801862e900bc786852e45898fb
  integral.hyperbolic_index: 9cbbe772578c47f69aa3f310c71927f8610a33ea79b767981463d170af883fdf
  automorphisms.automorphism_group_order: 63e33ec5bf90592c163485ea12e61dc28e1290520cdaf3d681755061ec39c0f0
  automorphisms.automorphism_group_generator_morphisms: d4b00cec42f3a1775971eb88d567c3896c1c8fbf5ece793849c81806a5cb3259
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, 0, 0, 0, 2]
- [0, 0, 0, 2, 0]
signature: [1, 4]
determinant: 16
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, 0, 0, 0, 1/2]
- [0, 0, 0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  discriminant_group: [2, 2, 2, 2]
  overlattice_count: 11
  bad_reduction_primes: [2]
  genus_symbol: 'I_{1,4} (2: [1^1 2^4]_5)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 5AEX
  name: O(L) generator 1
  matrix:
  - [-1, -2, -2, -2, -2]
  - [-1, 0, -1, -1, -1]
  - [-1, -1, 0, -1, -1]
  - [1, 1, 1, 2, 1]
  - [1, 1, 1, 1, 2]
  scale: 1
- target: 5AEX
  name: O(L) generator 2
  matrix:
  - [-1, 0, 0, -4, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [2, 0, 0, 4, 1]
  scale: 1
- target: 5AEX
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5AEX
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5AEX
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5AEX
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0, -2]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [1, 0, 0, 1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 0013.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICX, 3ICX, 0013.
