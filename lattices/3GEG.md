---
tag: 3GEG
name: watson 3:563
latex: watson 3:563
aliases: []
certifications:
  definite.regular: 186925c3ba3418c746ea5685248cf1de943d4b8aa6f4e36f3b7d8a0a806e556b
  definite.spinor_regular: af5f4b6e1678b682f760e3ef1f000e5258e783f46efc8c358c98b88a58acdc33
  derive: a4efee98693d98169bcfc564845b27880350358c70f29acdc2fdc5d5346b8999
  form.integer_valued: 1982eb74a24f7e6390771fa2c155f0022e9f834683c7ca05bf5a036a5718afb4
  definite.automorphism_group_order: f9dc7d488c40a7f5a3d7dbe2b981369a840673569fbe89562c3b1d65123e9e39
  definite.automorphism_group_generator_morphisms: 6a71fde465255a4799eef71e3c15201018ed9d675056dff34781230bd8e6c16a
rank: 3
gram_tensor:
- [3, 0, 0]
- [0, 8, 0]
- [0, 0, 72]
signature: [3, 0]
determinant: 1728
definiteness: positive_definite
dual_gram_tensor:
- [1/3, 0, 0]
- [0, 1/8, 0]
- [0, 0, 1/72]
form:
  integer_valued: true
integral:
  parity: odd
  level: 144
  discriminant_group: [24, 72]
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
  theta_series: [1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 4, 2]
  root_system: []
  roots:
  - type: A1
    scale: 36
    simple_roots:
    - [0, 0, 1]
  - type: A1
    scale: 4
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 3/2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1]
  norms: [3, 8, 72]
morphisms:
- target: 3GEG
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GEG
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3GEG
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:563.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 445, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 445, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:563` gives this Gram tensor.
