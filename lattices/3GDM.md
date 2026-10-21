---
tag: 3GDM
name: watson 3:533
latex: watson 3:533
aliases: []
certifications:
  definite.regular: 5b08c89ace15d3e6bcea1e2e6f24114e1ce3b88d6849ed1d333995ae92d090b1
  definite.spinor_regular: 0009982922c9aa8847b44b21ec24b6ac1b36ab04e516ef9c6da8f01f17fd60e9
  derive: 9d9fabacc3e0fc755b581961a9cba3a239dd4cadd987eac4172c1c7079367745
  form.integer_valued: 8ce81c4c1fc28aa7a0e13adae19762fa2132ca0ccde1ee11073d38765837b512
  definite.automorphism_group_order: 37eb25a743014b03622f4dc92d60ec560d710b33243941391abce916521d27e2
  definite.automorphism_group_generator_morphisms: 98f863877e6ffc9ec2018579899c3ed760ae5a65ab48eb8936efef7933442f04
rank: 3
gram_tensor:
- [3, 1, 1]
- [1, 11, -5]
- [1, -5, 27]
signature: [3, 0]
determinant: 768
definiteness: positive_definite
dual_gram_tensor:
- [17/48, -1/24, -1/48]
- [-1/24, 5/48, 1/48]
- [-1/48, 1/48, 1/24]
form:
  integer_valued: true
integral:
  parity: odd
  level: 96
  discriminant_group: [16, 48]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 3
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 4]
  root_system: []
  roots:
  - type: A1
    scale: 48
    simple_roots:
    - [1, -1, -2]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GDM
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GDM
  name: O(L) generator 2
  matrix:
  - [1, 0, 1]
  - [0, 1, -1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:533.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 356, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 356, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:533` gives this Gram tensor.
