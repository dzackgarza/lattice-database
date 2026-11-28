---
tag: 4NFC
name: Constructed lattice 4NFC
latex: L_{\mathrm{4NFC}}
certifications:
  derive: 141be66ae45b3ea9d1f4268cb61c3ccd56abdd67a65dec774206c727180da2fc
  form.integer_valued: fd71caf2e18025a300ef9b9d31568d36ead5697a6fb02d00455464bf156fc0b2
  integral.elementary_primes: fbe1bd75239394d5d9042b5b036eedc88f19bcd104aabdc1fa6ef1ef6cbce939
  integral.genus_symbol: 0023854fa4df282c731954f3d59f6549a012d324d9b2c05be2aaa87539da6f12
  integral.genus_class_count: 22b2f80a66d85ab76db3ec8a914bf72c1f28b737a138760088b6d63126032ea8
  integral.overlattice_count: 0268dbb95db6c9180a05e2ada888d67b7f4fa263d0039c19d620ffc9d4fd1da0
  integral.spinor_genus_count: 7abcbc0f4db3820acb761a02e74d2481b08119565da28b7496ab2f593300a78e
  integral.spinor_genera: 8724d72a5abce28b3b66c7944f94eab4f47cb25b4aa3041017d9844c0efbe487
  integral.hyperbolic_index: 0ca890dd11dc685ba7f57307a2a03bd5e07f5e7d46718cb3a758fa6146ffefb7
  automorphisms.automorphism_group_order: e478518b9867e0230a7512c758cd4d92b368051d941fcb5b779930231730dba7
  automorphisms.automorphism_group_generator_morphisms: 46776a247321495f408fef4f0960f067a12b1383220a64efa7e84e4a41142b08
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 0, 4, -6]
- [0, 0, 0, -6, 12]
signature: [4, 1]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, 0, 1, 0, 0]
- [0, 1, 0, 0, 0]
- [0, 0, 0, 1, 1/2]
- [0, 0, 0, 1/2, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{4,1} (2: [1^-3]_5 2^2; 3: 1^-4 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 4NFC
  name: O(L) generator 1
  matrix:
  - [-5, -6, 6, 0, -12]
  - [6, 7, -6, 0, 12]
  - [-6, -6, 7, 0, -12]
  - [-6, -6, 6, 1, -12]
  - [-4, -4, 4, 0, -7]
  scale: 1
- target: 4NFC
  name: O(L) generator 2
  matrix:
  - [-1, 0, 2, 0, 0]
  - [2, 1, -2, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NFC
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NFC
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 4NFC
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4NFC
  name: O(L) generator 6
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -2, 2, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 2, -1, 0]
  - [0, 0, 1, -1, 1]
  scale: 1
- target: 4NFC
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0016, 3ID6.
- tag: '0016'
  relation: This presentation is obtained by orthogonal sum of 0001, 0016, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 0001, 0016, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0016, 3ID6.
