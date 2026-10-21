---
tag: 3GEB
name: watson 3:558
latex: watson 3:558
aliases: []
certifications:
  definite.regular: ca7e9bfaf02f4b8f5c0f99cdcafef99ac5f02bf75dcfa0ed9316ac9e8689d71c
  definite.spinor_regular: 33133082444966de3ef43405fd2bc119a3b2c16d4b10de301a8f29e62356c494
  derive: 5e6d636fdaf828f5288c30ac6689e1d9f1d5a8d2804644f7000599b4a9c23727
  form.integer_valued: 71adaff6cd1f953d4deaa23ebf30be77afd20d6a59c951a51abf38babc6ea280
  definite.automorphism_group_order: c007c92d30bc3752a88d9ca5c2c65e5ab41b1bb2511377d4eab31a1a1cf0d166
  definite.automorphism_group_generator_morphisms: c92b83ca8dd387ed1aa24040376a32a2fd9f0caaf34cd0146f34ccc409f555bd
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 24, 0]
- [0, 0, 24]
signature: [3, 0]
determinant: 576
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0]
- [0, 1/24, 0]
- [0, 0, 1/24]
form:
  integer_valued: true
integral:
  parity: odd
  level: 48
  discriminant_group: [24, 24]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 1
  kissing_number: 2
  automorphism_group_order: 16
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
  - type: B2
    scale: 12
    simple_roots:
    - [0, 0, 1]
    - [0, 1, -1]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1]
  norms: [1, 24]
morphisms:
- target: 3GEB
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GEB
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3GEB
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:558.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 330, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 330, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:558` gives this Gram tensor.
