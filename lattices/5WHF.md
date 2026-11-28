---
tag: 5WHF
name: Constructed lattice 5WHF
latex: L_{\mathrm{5WHF}}
certifications:
  derive: 0f2f8313414667764f5a6de0b5d61c46269bb28f4e5baad5b7e2450802e8ff2a
  form.integer_valued: 94986a9f4b618151ed8a3b697bed3a54401650fda5485af9b3c18789e3370a7f
  integral.elementary_primes: d09ae2cc8a1623364ff8f51ae850f0d17ae1dab64ffd974ebb3c7692549c3197
  integral.genus_symbol: 40d59a584a805b24671e2724d933539590a13dffe81fbc7e022e450c033001fd
  integral.genus_class_count: 466f6ce98ab6e1df233db82733c53de058dd4e2e15c17029829ed6a105cddd1b
  integral.overlattice_count: aa86cdd406fe25edb7e228852a0dd95166565858a83bdbca1981a819a9645568
  integral.spinor_genus_count: 67619f35df60f2ee4a65455734903150ad7350bf83d6131962fb407e76c79b65
  integral.spinor_genera: 231c7d6d6f1c088aad2540ac70bd1962b7c1e80edb3b8f3845fbf9e4c68eb7f2
  integral.hyperbolic_index: 4c542c4cdcd63f34f66fbd5e01f8c4573140b5046065002fc7b095f3f407aeea
  automorphisms.automorphism_group_order: 0a8b5c8eac8684f1e193e70853ec745383d49e9c183ea18ee34dc100ba82bfa8
  automorphisms.automorphism_group_generator_morphisms: e5bdc2845a32c3013ddd62ba75f8d73d5512f81c99a888a52529385504dd5b41
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, -2, 1, 0, 0]
- [0, 1, -2, 0, 0]
- [0, 0, 0, -4, 6]
- [0, 0, 0, 6, -12]
signature: [1, 4]
determinant: 72
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, -2/3, -1/3, 0, 0]
- [0, -1/3, -2/3, 0, 0]
- [0, 0, 0, -1, -1/2]
- [0, 0, 0, -1/2, -1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  discriminant_group: [2, 6, 6]
  overlattice_count: 12
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{1,4} (2: 1^2 [2^3]_5; 3: 1^3 3^-2)'
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
- target: 5WHF
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5WHF
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5WHF
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 3]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5WHF
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, -1, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5WHF
  name: O(L) generator 5
  matrix:
  - [3, 0, 0, 2, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-4, 0, 0, -3, 0]
  - [-2, 0, 0, -2, 1]
  scale: 1
- target: 5WHF
  name: O(L) generator 6
  matrix:
  - [5, 4, -2, 2, 0]
  - [-4, -3, 2, -2, 0]
  - [0, 0, 1, 0, 0]
  - [-4, -4, 2, -1, 0]
  - [-2, -2, 1, -1, 1]
  scale: 1
- target: 5WHF
  name: O(L) generator 7
  matrix:
  - [7, 6, 0, 0, 0]
  - [-8, -7, 0, 0, 0]
  - [-4, -4, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID0, 3ID5.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID0, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID0, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ID0, 3ID5.
