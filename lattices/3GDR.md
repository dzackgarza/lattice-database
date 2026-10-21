---
tag: 3GDR
name: watson 3:538
latex: watson 3:538
aliases: []
certifications:
  definite.regular: d012b8931b6269e88f09adc00de0d6450692e679060871fdb48a07fd0a6ef7b8
  definite.spinor_regular: fe8ae0e082d735c01756fda9426714ff19432c95ba580f9c88e4026cc6deba65
  derive: ab79e89cd4e85d7a130a609618335f90c2750f2143c77ab9307814eb990250d6
  form.integer_valued: a85461e7ffb5c50517f4e96556b5fd86f3ebf262fe5854d129877510c943e0a1
  definite.automorphism_group_order: 7bb62a315460e3b24940f8823922e8fee822fd3903a1536063fc4a92acf1674f
  definite.automorphism_group_generator_morphisms: f5139b14a14ce56912e0ec1a5f5e009def75a746507a134daa8ee40ecd3e3e2c
rank: 3
gram_tensor:
- [7, 0, 0]
- [0, 24, 4]
- [0, 4, 24]
signature: [3, 0]
determinant: 3920
definiteness: positive_definite
dual_gram_tensor:
- [1/7, 0, 0]
- [0, 3/70, -1/140]
- [0, -1/140, 3/70]
form:
  integer_valued: true
integral:
  parity: odd
  level: 140
  discriminant_group: [28, 140]
  bad_reduction_primes: [2, 5, 7]
definite:
  minimum: 7
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 20
    simple_roots:
    - [0, 1, -1]
  - type: A1
    scale: 28
    simple_roots:
    - [0, 1, 1]
  - type: A1
    scale: 7/2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 2]
morphisms:
- target: 3GDR
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GDR
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3GDR
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:538.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 523, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 523, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:538` gives this Gram tensor.
