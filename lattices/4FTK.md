---
tag: 4FTK
name: Constructed lattice 4FTK
latex: L_{\mathrm{4FTK}}
certifications:
  derive: 23f40778c13dab35494a642a8069882a5c75b201160932da7c9abb51cb39dd20
  form.integer_valued: 71e86a69faf0cc90e0149263feef404adc6aabe1e0a3795e220db79f803b6093
  integral.elementary_primes: 82cfcb81107d2824e094862be2a3473c09c5d75d9deec0b3d27808d17cb5bd16
  integral.genus_symbol: d67ebd986f5af694ab2a0cae1a4c432f1148cd931f4b091d6f89927f3a97a882
  integral.genus_class_count: 5a3d70e8533657fea1d5917eacfa2cdecf20a3a9ff1f9a4685815b776927712e
  integral.overlattice_count: 56d061b63da945bd4b4254fd902851934e9569b9d0a64cf59b60e2b40234a287
  integral.spinor_genus_count: 124167d6b1ad029a70af29f872ba8b8b9f85cfe9747e7f8d6035afe28c1e9579
  integral.spinor_genera: 58fa4ddfacd5b227d6ff12dea66b245c4d7c017305671eaee4404debb621adc4
  integral.hyperbolic_index: c31bf19a45c8f2fe84a12a33739250a6089c2248901d7dd72bd01bc04a2534f8
  automorphisms.automorphism_group_generator_morphisms: c918e41c2936ef55d19bcb7aadfae517923f3c6fe929914bcc74acd2096f7fd7
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 2, 0, 0]
- [0, 0, 0, 1]
- [0, 0, 1, 0]
signature: [3, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1/2, 0, 0]
- [0, 0, 0, 1]
- [0, 0, 1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  discriminant_group: [2]
  overlattice_count: 1
  bad_reduction_primes: [2]
  quadratic_character: -8
  genus_symbol: 'I_{3,1} (2: [1^3 2^1]_2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 4FTK
  name: O(L) generator 1
  matrix:
  - [-1, -4, 2, -2]
  - [-2, -3, 2, -2]
  - [-2, -4, 3, -2]
  - [2, 4, -2, 3]
  scale: 1
- target: 4FTK
  name: O(L) generator 2
  matrix:
  - [-3, -4, 4, -2]
  - [-2, -1, 2, -1]
  - [-2, -2, 3, -1]
  - [4, 4, -4, 3]
  scale: 1
- target: 4FTK
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, -1]
  - [0, 0, -1, 0]
  scale: 1
- target: 4FTK
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 2]
  - [0, 1, 0, 0]
  - [-2, 0, 1, -2]
  - [0, 0, 0, 1]
  scale: 1
- target: 4FTK
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, -2]
  - [0, -1, 0, 0]
  - [-2, 0, 1, -2]
  - [0, 0, 0, 1]
  scale: 1
- target: 4FTK
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0016.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0016.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0001, 0002, 0016.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0002, 0016.
