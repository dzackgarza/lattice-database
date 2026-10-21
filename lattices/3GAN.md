---
tag: 3GAN
name: watson 3:426
latex: watson 3:426
aliases: []
certifications:
  definite.regular: 5e4c7ec0b904993d7689189837885360310070f900c14d068a72391a542e3e40
  definite.spinor_regular: b10ba2f39e4d0a067afbb6db57f6b9040c29b4c468089ec1a06bf54e53940e93
  derive: 3dbdda63c24cea42983b4b230bf23671988b87117c886e0556f7280d9bbeb80f
  form.integer_valued: 0e4aa5c65d194bed124f07415a788756c2c68360b374d6b7431ab04fc3864bd7
  definite.automorphism_group_order: a9a3ef5791365367502cc088c1d1d1d33dd48a2b2ad623c97f1221c6f109a052
  definite.automorphism_group_generator_morphisms: 4eea46dfab2c4e34e6f693546060703376e81f63de97dcb1f84613fde379093c
rank: 3
gram_tensor:
- [4, 0, 2]
- [0, 12, 6]
- [2, 6, 13]
signature: [3, 0]
determinant: 432
definiteness: positive_definite
dual_gram_tensor:
- [5/18, 1/36, -1/18]
- [1/36, 1/9, -1/18]
- [-1/18, -1/18, 1/9]
form:
  integer_valued: true
integral:
  parity: odd
  level: 36
  discriminant_group: [12, 36]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 4
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2]
  root_system: []
  roots:
  - type: A1
    scale: 6
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 2
    simple_roots:
    - [1, 0, 0]
  - type: A1
    scale: 18
    simple_roots:
    - [1, 1, -2]
root_sublattice:
  invariant_factors: [1, 1, 2]
morphisms:
- target: 3GAN
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GAN
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, -1]
  - [0, 0, 1]
  scale: 1
- target: 3GAN
  name: O(L) generator 3
  matrix:
  - [1, 0, 1]
  - [0, 1, 1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:426.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 294, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 294, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:426` gives this Gram tensor.
