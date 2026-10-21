---
tag: 3GEF
name: watson 3:562
latex: watson 3:562
aliases: []
certifications:
  definite.regular: 352b9109e940f100e24f9beeb90ac2bc6e71dbe4b9401f25a9c2fd00603c3e5d
  definite.spinor_regular: 7e53b6913a4d0e64d85757f18fa2c1304c86ea3475a0025b4dc4775ec99eb4b6
  derive: 76bce326cf6be6959600bb635afd8bfe319b220171b6bbcc8f696cf20283e943
  form.integer_valued: b3fee20467a52b39bf327bb2ec49bd8ac24d12d88cb736ecd5393582182e86cc
  definite.automorphism_group_order: 85094cc8f8324350278f65af0dd3eb696ff655528b5283ed19299c7573357725
  definite.automorphism_group_generator_morphisms: 6eb2f89bcc1b6a48c8ab658c266a251ef6afbd591008a9e3b561eac83cffcba5
rank: 3
gram_tensor:
- [8, 0, 4]
- [0, 12, 6]
- [4, 6, 23]
signature: [3, 0]
determinant: 1728
definiteness: positive_definite
dual_gram_tensor:
- [5/36, 1/72, -1/36]
- [1/72, 7/72, -1/36]
- [-1/36, -1/36, 1/18]
form:
  integer_valued: true
integral:
  parity: odd
  level: 144
  discriminant_group: [24, 72]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 8
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2]
  root_system: []
  roots:
  - type: A1
    scale: 6
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 4
    simple_roots:
    - [1, 0, 0]
  - type: A1
    scale: 36
    simple_roots:
    - [1, 1, -2]
root_sublattice:
  invariant_factors: [1, 1, 2]
morphisms:
- target: 3GEF
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GEF
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, -1]
  - [0, 0, 1]
  scale: 1
- target: 3GEF
  name: O(L) generator 3
  matrix:
  - [1, 0, 1]
  - [0, 1, 1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:562.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 455, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 455, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:562` gives this Gram tensor.
