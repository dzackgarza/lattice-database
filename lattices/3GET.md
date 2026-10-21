---
tag: 3GET
name: watson 3:576
latex: watson 3:576
aliases: []
certifications:
  definite.regular: 6639b043afd75ceedf4868219c5c5c66929195a758b20bda08c29dfb5210882d
  definite.spinor_regular: 6da5a0d7fe4c0e21c8235ed750489fa707205880546f19c28b6c30af21e7b5ca
  derive: bd23a871792b814889eed6ec7d3ff0760a5d50dc713a9fb0d1b14254095318ca
  form.integer_valued: 77cad1cd929341ea7b4793219592d8ab16b5496d885250c0c4da11d86b63a76e
  definite.automorphism_group_order: 4bf20523de0ef48240b63176931625681bfd9d27606f02d06f2ef469bbd5ad95
  definite.automorphism_group_generator_morphisms: 41e3a76e4f028c9b53213b3c6359011578e2978bca4d6716c9ad17f523f36229
rank: 3
gram_tensor:
- [5, 2, 0]
- [2, 8, 0]
- [0, 0, 24]
signature: [3, 0]
determinant: 864
definiteness: positive_definite
dual_gram_tensor:
- [2/9, -1/18, 0]
- [-1/18, 5/36, 0]
- [0, 0, 1/24]
form:
  integer_valued: true
integral:
  parity: odd
  level: 144
  discriminant_group: [12, 72]
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
  theta_series: [1, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 12
    simple_roots:
    - [0, 0, 1]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GET
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GET
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:576.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 369, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 369, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:576` gives this Gram tensor.
