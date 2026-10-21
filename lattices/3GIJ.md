---
tag: 3GIJ
name: watson 3:710
latex: watson 3:710
aliases: []
certifications:
  definite.regular: da09e284c53d0d62a072304a15005a05e655687501d989cc5e9f1830995508da
  definite.spinor_regular: ffaffbe8a52fe4d702b8aa744762f0e48720b7d06292ca56bec86d44c615d47a
  derive: 88d8c32e38145b4e1eccaa8a6da0efc10fcb8bc2d0270dbc07c7c9898ab4e6ad
  form.integer_valued: 79334e84f0dabe183dcff46e45983a6d0d5eaf8ecad58e82aa1782a146277018
  definite.automorphism_group_order: 750a840f6506a1cc6968641b25f53072cf08fd585126d3202ede82e0c758928a
  definite.automorphism_group_generator_morphisms: 809f31ee97730d131add13fd8999515ba66b12d3d788e0dc191f92c5ec484641
rank: 3
gram_tensor:
- [3, 0, 1]
- [0, 8, 0]
- [1, 0, 11]
signature: [3, 0]
determinant: 256
definiteness: positive_definite
dual_gram_tensor:
- [11/32, 0, -1/32]
- [0, 1/8, 0]
- [-1/32, 0, 3/32]
form:
  integer_valued: true
integral:
  parity: odd
  level: 64
  discriminant_group: [8, 32]
  bad_reduction_primes: [2]
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
  theta_series: [1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 6, 4]
  root_system: []
  roots:
  - type: A1
    scale: 4
    simple_roots:
    - [0, 1, 0]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GIJ
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GIJ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:710.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 241, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 241, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:710` gives this Gram tensor.
