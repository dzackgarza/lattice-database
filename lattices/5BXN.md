---
tag: 5BXN
name: Constructed lattice 5BXN
latex: L_{\mathrm{5BXN}}
certifications:
  derive: 081df6ed2cb08d4a9ee0475fee7c9ac251ede5c146a1ed8698c57c8bb470ee7f
  form.integer_valued: c8a70b00fcb31f112971290dd481094120685f71b82e42617e8d93bc50f287f2
  integral.elementary_primes: a32c7f6a8d219f3c1679fc105d3985e8b123c1099717de6334c8567f7945861b
  integral.genus_symbol: 69ee3d709e7bb8041bc329963bdd2b9e51563dedd7843ebd3ad14e166de8d56e
  integral.genus_class_count: c3d514eca8a47b01caee617ecfee8bdb586a027e95b5b1a1e43947f420ac1f12
  integral.overlattice_count: cae204a388a3303517de1dfb6b71ce2d82da728fc66a4176034517dd46e7e249
  integral.spinor_genus_count: 87c267d2d248ff3081d0fa152132d3b87c90cc5309321d592c3e0b669c7f4650
  integral.spinor_genera: 4b220af6c8a1d4796056d59cb8ca734586f39d926287663da03b092cf94ae241
  integral.hyperbolic_index: 95ce4d87b5a224f054527350d80f9be3594569676f54b1fa38991ab3e8b700ed
  automorphisms.automorphism_group_generator_morphisms: 087c6849a2ec00e160c36c99813c0cd6300eeadc254c9a27a7729c08a4535ad2
  automorphisms.automorphism_group_order: dd55db0128c1aa78c111ff7689ecc385281e00234d7a1c9d33374cbb7775ae63
  integral.modular_scale: d8ecf447dc94b7948d5a157592940b2cfffc56ced9d3e29b558b9df07e42fdfc
  integral.anisotropic_primes: a3d0d6bcc74d9be858565bfc1ed1c59a35406e50ae61ee83a76757d4891feec4
  integral.local_representations: b98b8c66f33f038cdc3d63f10ec8dc271d43196bf6996e24c32078247bdb8b4c
  integral.local_densities: ffe9dcceec0e1965dcbb962b288abc4c44e86ab54f8d65e24568db56c66f728f
rank: 4
gram_tensor:
- [-1, 0, 0, 0]
- [0, -2, 0, 0]
- [0, 0, 0, 2]
- [0, 0, 2, 0]
signature: [1, 3]
determinant: -8
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0]
- [0, -1/2, 0, 0]
- [0, 0, 0, 1/2]
- [0, 0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  bad_reduction_primes: [2]
  quadratic_character: -8
  genus_symbol: 'I_{1,3} (2: [1^1 2^3]_6)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1/2, 3/4, 1/2, 7/8, 3/2, 3/4, 3/2, 15/16, 1/2, 5/4, 1/2, 7/8]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8]
indefinite:
  isotropic: true
morphisms:
- target: 5BXN
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 5BXN
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, -2]
  - [0, 2, 1, 2]
  - [0, 0, 0, 1]
  scale: 1
- target: 5BXN
  name: O(L) generator 3
  matrix:
  - [-17, -24, -24, -24]
  - [-12, -15, -16, -16]
  - [12, 16, 17, 16]
  - [12, 16, 16, 17]
  scale: 1
- target: 5BXN
  name: O(L) generator 4
  matrix:
  - [-1, -4, -2, -4]
  - [-2, -3, -2, -4]
  - [2, 4, 3, 4]
  - [1, 2, 1, 3]
  scale: 1
- target: 5BXN
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 5BXN
  name: O(L) generator 6
  matrix:
  - [-1, -4, -2, -4]
  - [-2, -3, -2, -4]
  - [1, 2, 1, 3]
  - [2, 4, 3, 4]
  scale: 1
- target: 5BXN
  name: O(L) generator 7
  matrix:
  - [-17, -12, -18, -20]
  - [-6, -5, -6, -8]
  - [10, 8, 11, 12]
  - [9, 6, 9, 11]
  scale: 1
- target: 5BXN
  name: O(L) generator 8
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 0013.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICX, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICX, 0013.
