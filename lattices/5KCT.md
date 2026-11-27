---
tag: 5KCT
name: Constructed lattice 5KCT
latex: L_{\mathrm{5KCT}}
certifications:
  derive: 3c8713472993f65f22756b1e684c37d0265b091959d63665d9c95f8c3b4d3a4a
  form.integer_valued: 0c3fa0a6b6c7fde7ebcee6b564c1e8929c35ff160bf254e4241abf0e3ef2e535
  integral.elementary_primes: 1a19edd67d445add35042c109e87ff476499f3efdbe5531851e494a9e4e9d6e5
  integral.genus_symbol: 5a97d68bbafdc40eaebaf0971cae3b7e7ff5ca44adb83678eb420dfcf4a81b3c
  integral.genus_class_count: 09ee195969c8eccea16bc84204db7381dbb5d5fb57b6d10857462a6bf4f130f0
  integral.overlattice_count: afe71bf133cdb487509a78b561215df904a00ec36a132f8259484c8e0e979264
  integral.spinor_genus_count: 627e95356d26ab4344263ef627b16c6c3e7ecb8e693a6e13644e48c97f9365d6
  integral.spinor_genera: 626be7fd0e603f63c65f646a0c91cb556058e4dab2c2c5b3ca2bbc80ad645d26
  integral.hyperbolic_index: 5aa97679726997830d7edbb79ee6a46fcaf2b4bff8395bbd4041731b0042372d
  automorphisms.automorphism_group_order: 78f882572dea806a3abbe6c32d396e577f5dd7c84855d7123e1e6818d9ac366b
  automorphisms.automorphism_group_generator_morphisms: f0917c016771fdea33462b1eac5692b2b6aabf9972ae08c039b3e0a7d93226b7
rank: 5
gram_tensor:
- [2, 0, 0, 0, 0]
- [0, 2, 0, 0, 0]
- [0, 0, 2, 0, 0]
- [0, 0, 0, 0, -1]
- [0, 0, 0, -1, 0]
signature: [4, 1]
determinant: -8
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0, 0, 0]
- [0, 1/2, 0, 0, 0]
- [0, 0, 1/2, 0, 0]
- [0, 0, 0, 0, -1]
- [0, 0, 0, -1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{4,1} (2: 1^2 [2^3]_3)'
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
- target: 5KCT
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0, 1]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [-2, 0, 0, 1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5KCT
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 0, 1]
  - [0, 0, 0, 1, 0]
  scale: 1
- target: 5KCT
  name: O(L) generator 3
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5KCT
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5KCT
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
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 0002, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0002, 0002, 0002, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 0002, 0002, 3ICY.
