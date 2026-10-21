---
tag: 3GAP
name: watson 3:428
latex: watson 3:428
aliases: []
certifications:
  definite.regular: c892dabb91c0f1964b5e74dfb847e50a94dbaf33cd68dc3e9443412a16c536dc
  definite.spinor_regular: 66bff7ab6fd56533486ab80831cd1089d225fb9c4b48285971e8a7789c0c516a
  derive: 97afa4703cc16e02c79a568fef38d589054af43d38051cb546ed2b50aa027fab
  form.integer_valued: 54fd58fee55db15c655b30c7222471341a1941a49b3cdbca429122300746dd6d
  definite.automorphism_group_order: 801ae3df208f76b898980041a5e507f8489ce3a683963939e484df73eec80f46
  definite.automorphism_group_generator_morphisms: 2f3084ba29bfa0968a6ade52d9dc199cf9665072b896219b7fd6cc6236e7b80c
rank: 3
gram_tensor:
- [3, 0, 0]
- [0, 4, 0]
- [0, 0, 36]
signature: [3, 0]
determinant: 432
definiteness: positive_definite
dual_gram_tensor:
- [1/3, 0, 0]
- [0, 1/4, 0]
- [0, 0, 1/36]
form:
  integer_valued: true
integral:
  parity: odd
  level: 72
  discriminant_group: [12, 36]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 3
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 2, 2, 0, 0, 4, 0, 0, 0, 0, 2]
  root_system: []
  roots:
  - type: A1
    scale: 18
    simple_roots:
    - [0, 0, 1]
  - type: A1
    scale: 2
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 3/2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1]
  norms: [3, 4, 36]
morphisms:
- target: 3GAP
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GAP
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3GAP
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:428.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 292, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 292, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:428` gives this Gram tensor.
