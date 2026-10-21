---
tag: 3GGG
name: watson 3:635
latex: watson 3:635
aliases: []
certifications:
  definite.regular: 1215da22a3d6a92200ece524e236d2a9f35f535808a00d4b84a33938cf5660bb
  definite.spinor_regular: 602a94aeafc9753f70cb6d49dd45d77907a481b4bc5cd791c68010cd9db71ced
  derive: 11b62159073c04da648fa46da5b4ad1852d040f47bbc2d57ef390021649055dd
  form.integer_valued: f352f749c11bcbbe2eb40f7ae0176da93d4d0827b010b0904f0e3de0d52fb050
  definite.automorphism_group_order: 389ff990c7a973c10bf23c4d4b9a64e65ca638736d475f7ab3f3cf2b2d685d5b
  definite.automorphism_group_generator_morphisms: 09f4ede06a90b7067ed1a34edbad2211a45137ca13b730289197674f33491f99
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, 12, 6]
- [0, 6, 15]
signature: [3, 0]
determinant: 288
definiteness: positive_definite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, 5/48, -1/24]
- [0, -1/24, 1/12]
form:
  integer_valued: true
integral:
  parity: odd
  level: 96
  discriminant_group: [6, 48]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 2
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2]
  root_system: [A1]
  roots:
  - type: A1
    scale: 24
    simple_roots:
    - [0, 1, -2]
  - type: A1
    scale: 6
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 1
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 2]
morphisms:
- target: 3GGG
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GGG
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GGG
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:635.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 245, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 245, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:635` gives this Gram tensor.
