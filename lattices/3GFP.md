---
tag: 3GFP
name: watson 3:608
latex: watson 3:608
aliases: []
certifications:
  definite.regular: a64325dcf71d357b09b62bf0ba4f39f4711335f787ca0bf133daa1c2a375e67a
  definite.spinor_regular: cc9809033e71e8efa94f0034e3f94ecaeb87fb454dcf584247a03a22c7f9354c
  derive: 3f660a2d717f380310c1866f80ddef9e5d2f1c540cde0b8e8ee10f495854e03f
  form.integer_valued: 44e12d8112623b9b7895965613ecd141c347c772a4f1dae6a20ab41033bd769c
  definite.automorphism_group_order: 8ea22aac040818ef4d91010e1f73ea84fa7bdb9f1784ab5a38cd25a6904a0eb7
  definite.automorphism_group_generator_morphisms: 4c5cde93bc6c35127dd59cb6afb00db42369a1564f3b3c6dea81494b864d108c
rank: 3
gram_tensor:
- [4, 0, 0]
- [0, 7, 3]
- [0, 3, 15]
signature: [3, 0]
determinant: 384
definiteness: positive_definite
dual_gram_tensor:
- [1/4, 0, 0]
- [0, 5/32, -1/32]
- [0, -1/32, 7/96]
form:
  integer_valued: true
integral:
  parity: odd
  level: 192
  discriminant_group: [4, 96]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 4
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 4, 0]
  root_system: []
  roots:
  - type: A1
    scale: 2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GFP
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GFP
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:608.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 274, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 274, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:608` gives this Gram tensor.
