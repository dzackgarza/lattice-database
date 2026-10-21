---
tag: 3GAT
name: watson 3:432
latex: watson 3:432
aliases: []
certifications:
  definite.regular: 336c5581d52b6df926dbd0a95b3e8de75542aca6ce3d348b2e8a1a9259018c60
  definite.spinor_regular: 24fa7c98015acf7c36b9fefe6ece66bf2965e711f2d9b7863ebaddba38957c01
  derive: 4aa7efc8b000e97a6cc1c8275f813b46f7a87caa6f32f195a8bdb3520ac8c559
  form.integer_valued: 46908148d309ba464aaa5c9638bd16ca8977d321d5dbfe28b792603b5a823e9b
  definite.automorphism_group_order: b00796476a8960ffadabeabb264f8d85c38280f26cdff3c5b0aee451d43fde24
  definite.automorphism_group_generator_morphisms: 7b617e74c3ab8ed7d6ba852180744f56fe4ce4a00000055e2406dccc3f9c5d64
rank: 3
gram_tensor:
- [5, 2, 0]
- [2, 8, 0]
- [0, 0, 12]
signature: [3, 0]
determinant: 432
definiteness: positive_definite
dual_gram_tensor:
- [2/9, -1/18, 0]
- [-1/18, 5/36, 0]
- [0, 0, 1/12]
form:
  integer_valued: true
integral:
  parity: odd
  level: 72
  discriminant_group: [12, 36]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 5
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2]
  root_system: []
  roots:
  - type: A1
    scale: 6
    simple_roots:
    - [0, 0, 1]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GAT
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GAT
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:432.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 297, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 297, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:432` gives this Gram tensor.
