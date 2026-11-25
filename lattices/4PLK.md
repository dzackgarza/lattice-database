---
tag: 4PLK
name: Constructed lattice 4PLK
latex: L_{\mathrm{4PLK}}
certifications:
  derive: 8ca63fd4c6da991ebb74aaea41ffce1b166e8f164b4c11e041d6372b0e117709
  form.integer_valued: 6e8d8007432087a9779eef29a3d06d4c7e88c1ef0567813e98c1e89362162e92
  integral.elementary_primes: c2efab742938dd548a31978ef11f3556c9799cc1c5c157557af476cc1a42dcae
  integral.genus_symbol: 3907f7e5619c1bb0980552214142ad6f6d6d9807f39ebcc93e7feb00adf73772
  integral.genus_class_count: 0bf68992323c4297370e528bab05bf23dfbd88896226a9f08ce46927bc7980ba
  integral.overlattice_count: 5753b5be2d8d72713dd4e449d2ab2a43b952d278ff0fe22643354ab0bfbe908b
  integral.spinor_genus_count: d7dba849781cf5fdd776d60817aa3b8fb03b7a2fc6b2120bef64bc16f820b032
  integral.spinor_genera: cea9f06c75d908a08aa50914e2a26bf88f75180721eafb1ca044999e9af89762
  integral.hyperbolic_index: a09c793cb68035dafa3221440dba3d290e897c583fd0e2509f1fc5d03f9e9181
  automorphisms.automorphism_group_order: 751757b66810b3b622e850246b5101519d41aad53193ddfd940500d713c9d38e
  automorphisms.automorphism_group_generator_morphisms: 611001916f774c5ed1a48a4be2d138cfce55d05e818b5cba42369eb165e8f3c3
rank: 5
gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -2, 1, 0, 0]
- [0, 1, -2, 0, 0]
- [0, 0, 0, -2, 3]
- [0, 0, 0, 3, -6]
signature: [1, 4]
determinant: 9
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0, 0]
- [0, -2/3, -1/3, 0, 0]
- [0, -1/3, -2/3, 0, 0]
- [0, 0, 0, -2, -1]
- [0, 0, 0, -1, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: [3]
  parity: odd
  level: 6
  discriminant_group: [3, 3]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{1,4} (2: [1^5]_1; 3: 1^3 3^2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10]
indefinite:
  isotropic: true
morphisms:
- target: 4PLK
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PLK
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, -1, 1]
  scale: 1
- target: 4PLK
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 2, -3]
  - [0, 0, 0, 1, -2]
  scale: 1
- target: 4PLK
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 4PLK
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PLK
  name: O(L) generator 6
  matrix:
  - [3, 2, 2, 0, 0]
  - [-2, -1, -2, 0, 0]
  - [-2, -2, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PLK
  name: O(L) generator 7
  matrix:
  - [5, 6, 0, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, -1, 2]
  - [6, 8, -1, 0, 0]
  - [4, 5, 0, 0, 0]
  scale: 1
- target: 4PLK
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 4PLK
  name: O(L) generator 9
  matrix:
  - [7, 6, 0, -6, 12]
  - [-4, -3, 0, 4, -8]
  - [-2, -2, 1, 2, -4]
  - [6, 6, 0, -5, 9]
  - [4, 4, 0, -3, 6]
  scale: 1
- target: 4PLK
  name: O(L) generator 10
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID0, 3ID3.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID0, 3ID3.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 0001, 3ID0, 3ID3.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ID0, 3ID3.
