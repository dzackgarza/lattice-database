---
tag: 3GKM
name: watson 3:785
latex: watson 3:785
aliases: []
certifications:
  definite.regular: 7b43b2ab13856cb2b9c2aed4a02a5e0c4f5ea3b6fc1617055cd00bc2811fdf36
  definite.spinor_regular: f0d9c51408a804eda2663b323514b267aaa54469270b33648f14a020c06f0f5d
  derive: faca15494a0a51f24a292656b1890f352eb279de27e1302d7a29523628df45c6
  form.integer_valued: 4ec389095df247c8ba02a9c930a165921c3f6108ff0c219c7f429e77e5a4c253
  definite.automorphism_group_order: fbfd18b9497bf2554473e98c9184304f1df430803a9dad49e91708c8a875f8a3
  definite.automorphism_group_generator_morphisms: 2c15f95712de58b1a533985e54d680be7b852aa91fb7dc5ef2241ad8b02c39f7
rank: 3
gram_tensor:
- [5, 0, 2]
- [0, 8, 4]
- [2, 4, 12]
signature: [3, 0]
determinant: 368
definiteness: positive_definite
dual_gram_tensor:
- [5/23, 1/46, -1/23]
- [1/46, 7/46, -5/92]
- [-1/23, -5/92, 5/46]
form:
  integer_valued: true
integral:
  parity: odd
  level: 92
  discriminant_group: [4, 92]
  bad_reduction_primes: [2, 23]
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
  theta_series: [1, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 4]
  root_system: []
  roots:
  - type: A1
    scale: 4
    simple_roots:
    - [0, 1, 0]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GKM
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GKM
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, -1]
  - [0, 0, 1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:785.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 267, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 267, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:785` gives this Gram tensor.
