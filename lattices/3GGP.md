---
tag: 3GGP
name: watson 3:644
latex: watson 3:644
aliases: []
certifications:
  definite.regular: c9e5046ce9316cf5365275b57f69ab1ac8c6914a5cb7441bebf992da7c57a41e
  definite.spinor_regular: 68da7b708386740e1eefa3eeb6e49b36f0186a8c6a5796b6c2596caec3a5c24b
  derive: 9408a422032111cf04c59d4d7f570e6263748fe89229e7c923005274e110fe1b
  form.integer_valued: 6f65bec944d91ec7afdf52df7b2f95d431c26348b51e4becc46f48556e2d4e95
  definite.automorphism_group_order: cfd1ccaf952d3fd6c1342f73e6033d2d0b5c9a1dc4b03b101f17e797b7df6067
  definite.automorphism_group_generator_morphisms: af319c48654789b5943d175c1ec53a152779e070d2dbfc9e7cb94f5c104c2e16
rank: 3
gram_tensor:
- [3, 0, 0]
- [0, 8, 4]
- [0, 4, 14]
signature: [3, 0]
determinant: 288
definiteness: positive_definite
dual_gram_tensor:
- [1/3, 0, 0]
- [0, 7/48, -1/24]
- [0, -1/24, 1/12]
form:
  integer_valued: true
integral:
  parity: odd
  level: 96
  discriminant_group: [6, 48]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 3
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 4, 2]
  root_system: []
  roots:
  - type: A1
    scale: 24
    simple_roots:
    - [0, 1, -2]
  - type: A1
    scale: 4
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 3/2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 2]
morphisms:
- target: 3GGP
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GGP
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GGP
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:644.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 248, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 248, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:644` gives this Gram tensor.
