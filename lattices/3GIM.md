---
tag: 3GIM
name: watson 3:713
latex: watson 3:713
aliases: []
certifications:
  definite.regular: 1e1a858668ba7e2442f005578f3d6ba23ad6ab3cd0f1d2139aa359aa192f530e
  definite.spinor_regular: d55fd6c2a4132856791f47a1fced35eb979c979e64ebe53b2c991dea724452cc
  derive: 4f62733bcf1dbc70fbc314dd4a2246caa17664b67952dc207117e44080fb237b
  form.integer_valued: 603f044fb7eb5409646c7cfefd322d9ae9e80823a12bc355d6af241065920f93
  definite.automorphism_group_order: 3516c4f475d92e43e94176f85bd3fb6f36c4cb10fa1ec25f058686a4540ed975
  definite.automorphism_group_generator_morphisms: 44018bf78b1e651f5c1d8ec1c188697476b2972f13f24dffbff23e3dd21ebe2b
rank: 3
gram_tensor:
- [3, 1, 1]
- [1, 11, -5]
- [1, -5, 19]
signature: [3, 0]
determinant: 512
definiteness: positive_definite
dual_gram_tensor:
- [23/64, -3/64, -1/32]
- [-3/64, 7/64, 1/32]
- [-1/32, 1/32, 1/16]
form:
  integer_valued: true
integral:
  parity: odd
  level: 128
  discriminant_group: [8, 64]
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
  theta_series: [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 4]
  root_system: []
  roots:
  - type: A1
    scale: 32
    simple_roots:
    - [1, -1, -2]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GIM
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GIM
  name: O(L) generator 2
  matrix:
  - [1, 0, 1]
  - [0, 1, -1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:713.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 317, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 317, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:713` gives this Gram tensor.
