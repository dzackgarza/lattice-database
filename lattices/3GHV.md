---
tag: 3GHV
name: watson 3:686
latex: watson 3:686
aliases: []
certifications:
  definite.regular: cc1c2ee2dd4038e3df454d94d500d891f1fcbb9a9b51ecd67e3dd695108c1305
  definite.spinor_regular: e16efae82f5fd13cf35228a844937a02780314ad0d6c8a20d63015105fac5990
  derive: 65b938ca0de835cef65af3b81dfdbe2be16ba6ebe0ff1a591f30ee7d70edbd99
  form.integer_valued: d64c5559e7c8f218c68bb9a41212950660dec7b5f2d84965d3b0e2046a4d234e
  definite.automorphism_group_order: 80ff6efb985612ab027ae90ce52963eb1a87bdb83b08bcd5f95bf91cc8d0bc86
  definite.automorphism_group_generator_morphisms: 0b74fad277ed4d2ae1cb32d9918e768c7521679833969fa6b8db7063a7048b60
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 8, 0]
- [0, 0, 40]
signature: [3, 0]
determinant: 320
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0]
- [0, 1/8, 0]
- [0, 0, 1/40]
form:
  integer_valued: true
integral:
  parity: odd
  level: 80
  discriminant_group: [8, 40]
  bad_reduction_primes: [2, 5]
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 2, 0, 0, 2, 0, 0, 0, 2, 6, 0, 0, 4]
  root_system: []
  roots:
  - type: A1
    scale: 20
    simple_roots:
    - [0, 0, 1]
  - type: A1
    scale: 4
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1]
  norms: [1, 8, 40]
morphisms:
- target: 3GHV
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GHV
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3GHV
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:686.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 255, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 255, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:686` gives this Gram tensor.
