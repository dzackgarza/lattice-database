---
tag: 3GDN
name: watson 3:534
latex: watson 3:534
aliases: []
certifications:
  definite.regular: dab09223dc85c0bb997b383ab9b7de1fdb7d5918e2da2516f8095710f4305076
  definite.spinor_regular: 79122ee007a9829e7a1d72c7ff495e698ab1e5cb98e824570d1f1a84dfecf33a
  derive: 27ebc48c7405942af3b8467fb17b2c25ccccccf1982d4e49e402f6048d7834ce
  form.integer_valued: 07ec43bec86304f198be3c7c17ffa430d92554614c2d68f0a700cf0a88fe3a56
  definite.automorphism_group_order: 11f925b5a3cb4fa26315e4db48a9dd299c6cffea71c76c252543d32ee4a64e8b
  definite.automorphism_group_generator_morphisms: ac96fe5510319cfa328188a446b5194376aba1a7a35a9fcb378effec166c14b8
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, 8, 4]
- [0, 4, 72]
signature: [3, 0]
determinant: 560
definiteness: positive_definite
dual_gram_tensor:
- [1, 0, 0]
- [0, 9/70, -1/140]
- [0, -1/140, 1/70]
form:
  integer_valued: true
integral:
  parity: odd
  level: 140
  discriminant_group: [4, 140]
  bad_reduction_primes: [2, 5, 7]
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
    scale: 140
    simple_roots:
    - [0, 1, -2]
  - type: A1
    scale: 4
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 1/2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 2]
morphisms:
- target: 3GDN
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GDN
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GDN
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:534.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 327, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 327, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:534` gives this Gram tensor.
