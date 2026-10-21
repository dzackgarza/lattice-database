---
tag: 3GDB
name: watson 3:522
latex: watson 3:522
aliases: []
certifications:
  definite.regular: 930cedd0b83816d1d17a11b3cf77acc076b844398f5fafc8756d02a432d22353
  definite.spinor_regular: 4383537aff1b66d3956b0a76ffff2189608ac05d5d6d865f7d3820e5d2b0504d
  derive: 5911871026ec4c8bfd14dc5f582c05438341bb96544d269d78dc0900978d8b3f
  form.integer_valued: c0ee93d4318c2cfb6ec848f4ace6d753ab6b41917a3034dd9b9b95ef978a2aaa
  definite.automorphism_group_order: 2f8baffaeb30a361b34ee468559cbf21ebd65d4ec1edab42c0e1b301240d1db3
  definite.automorphism_group_generator_morphisms: 3e5e94a5b38ad4cbff10efca60ad7b3c7c9dbbff0624e9f785a4d5375cba23ec
rank: 3
gram_tensor:
- [11, 3, 4]
- [3, 27, -12]
- [4, -12, 32]
signature: [3, 0]
determinant: 6912
definiteness: positive_definite
dual_gram_tensor:
- [5/48, -1/48, -1/48]
- [-1/48, 7/144, 1/48]
- [-1/48, 1/48, 1/24]
form:
  integer_valued: true
integral:
  parity: odd
  level: 288
  discriminant_group: [48, 144]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 11
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
  root_system: []
  roots:
  - type: A1
    scale: 48
    simple_roots:
    - [1, -1, -2]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GDB
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GDB
  name: O(L) generator 2
  matrix:
  - [1, 0, 1]
  - [0, 1, -1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:522.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 568, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 568, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:522` gives this Gram tensor.
