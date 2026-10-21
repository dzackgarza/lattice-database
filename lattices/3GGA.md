---
tag: 3GGA
name: watson 3:629
latex: watson 3:629
aliases: []
certifications:
  definite.regular: 735cb4391b89232dff677a8c216c418031bd9c3a35e79f1797e0900ebae2eabf
  definite.spinor_regular: c8508f172758589ffc6da1b6bbbd0a5f236b5aa555994d084d634fff03bee40c
  derive: b1b8772cc155c601a2d3862313071d18001fd5408877a844f0eafcc6b23bf591
  form.integer_valued: 65d3a6ac1175fcfca621f9d00c1c20f282b89011fbf8bba2efa36d5119b618e2
  definite.automorphism_group_order: abcd1b667d0bdaeaa880c8f79c954ac3a8158604a56e34ea0912f0e3217e5b46
  definite.automorphism_group_generator_morphisms: beabb4d26b3c8096735e73a16b9d52761830194a69987f00161d06ca62ac4044
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 16, 0]
- [0, 0, 24]
signature: [3, 0]
determinant: 384
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0]
- [0, 1/16, 0]
- [0, 0, 1/24]
form:
  integer_valued: true
integral:
  parity: odd
  level: 96
  discriminant_group: [8, 48]
  bad_reduction_primes: [2, 3]
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
  theta_series: [1, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 12
    simple_roots:
    - [0, 0, 1]
  - type: A1
    scale: 8
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1]
  norms: [1, 16, 24]
morphisms:
- target: 3GGA
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GGA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3GGA
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:629.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 271, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 271, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:629` gives this Gram tensor.
