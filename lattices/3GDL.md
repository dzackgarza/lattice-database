---
tag: 3GDL
name: watson 3:532
latex: watson 3:532
aliases: []
certifications:
  definite.regular: db7cc0cb9ee63ab608e37d2a942d587a26819a923941af9725917358b22b050c
  definite.spinor_regular: c0d9284ba004fa5280168354be44c536af834907e7ae4bf5c382bfcbc4ef28da
  derive: 4929b8b7bff8096279c0dc7c6f7753699cec832a84b2b0e8f93a05a1dd134634
  form.integer_valued: 433dff1392d43761fe58596b2e438d4fc7c4e6d094402c3831ef831354b501ef
  definite.automorphism_group_order: 49e955799c57af1a7e61d2a4ea33492e33277cd0b8bba91add860f121e99f28a
  definite.automorphism_group_generator_morphisms: 88822de39123c215e985522b432bd2fe76b6c24c87e2722d02b49a2423ebca9d
rank: 3
gram_tensor:
- [7, 2, 2]
- [2, 12, -4]
- [2, -4, 12]
signature: [3, 0]
determinant: 768
definiteness: positive_definite
dual_gram_tensor:
- [1/6, -1/24, -1/24]
- [-1/24, 5/48, 1/24]
- [-1/24, 1/24, 5/48]
form:
  integer_valued: true
integral:
  parity: odd
  level: 96
  discriminant_group: [16, 48]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 7
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 4]
  root_system: []
  roots:
  - type: A1
    scale: 16
    simple_roots:
    - [0, 1, -1]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GDL
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GDL
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:532.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 359, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 359, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:532` gives this Gram tensor.
