---
tag: 5ISH
name: Constructed lattice 5ISH
latex: L_{\mathrm{5ISH}}
certifications:
  derive: 29973700ced981b2c8d0e36da467c3ad411183df174b866f19e41eb03e0f210a
  form.integer_valued: c69fafe02d1bb211fc7df782b3d206cda2e440cf8542cc3f5fb23831fbe19a4f
  integral.elementary_primes: 5548e75534b899b8f6455025ef22ca4f8d087fbd81ddf396ea71366363223e1c
  integral.genus_symbol: 187c2cbf674b6793e23df7dcedbfe24859bd52ca1868a2d3192cc8f40fe5c262
  integral.genus_class_count: 9892f35b2dbddcd3fea3b4394837a9968bb45abb345692978ea230dbb3815f61
  integral.overlattice_count: 40f9be36ca280c1dc2903052a6ca496f9e0cb5ad02ef064a734575782b766288
  integral.spinor_genus_count: d70328f1df34e599e75093a50d42eed7e980788431c811bfdf7817738515f7a0
  integral.spinor_genera: 150420d6a4daf3f4527da5802a386b2222a4e53f6f0aa8d536e42d7fcb662581
  integral.hyperbolic_index: cdeb35c3e0b01601230acff22de0216e0207b817809635bea4a6523e69822846
  automorphisms.automorphism_group_order: 64359ce0d368c0664772667f37f4c8c86ac6fb490070d1cf23eb0964fa992e55
  automorphisms.automorphism_group_generator_morphisms: c6f9ca50a56fb354a738edfe7c9e56b00eb12c8e53d6e05427cbfd2ac48e1f60
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 0, 0, 2, 0]
- [0, 0, 0, 0, -2]
signature: [4, 1]
determinant: -32
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 0, 0, 1/2, 0]
- [0, 0, 0, 0, -1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  discriminant_group: [2, 2, 2, 2, 2]
  overlattice_count: 31
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{4,1} (2: [2^5]_3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 5ISH
  name: O(L) generator 1
  matrix:
  - [0, -1, -1, 0, -1]
  - [-1, 0, -1, 0, -1]
  - [-1, -1, 0, 0, -1]
  - [0, 0, 0, 1, 0]
  - [1, 1, 1, 0, 2]
  scale: 1
- target: 5ISH
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5ISH
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5ISH
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5ISH
  name: O(L) generator 5
  matrix:
  - [0, 1, 0, 0, 0]
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 0002, 0002, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 0002, 0002, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0002, 0002, 0002, 3ICX.
