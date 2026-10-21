---
tag: 3GGV
name: watson 3:650
latex: watson 3:650
aliases: []
certifications:
  definite.regular: c6a6cf906dcec0eb116065f1c48a1d5f6ac1121639d0b818c9529f37724b2d2b
  definite.spinor_regular: 08933c5fcfb3e5640ab6d04ad82fc4e6b73819983d4c2ff4d4d422380e6257e9
  derive: 243baea548bf85473c4efe9123009ae32c4599a3302c8c80b99f53fe2785e99f
  form.integer_valued: 72ed1510e04b08994693ff554b49f2cbdf6178281bc26eacf647980664dbcd79
  definite.automorphism_group_order: b0a524dbda38b8e3a197bf98bbfa1eff026a556ae0c0af81565c458645253bc8
  definite.automorphism_group_generator_morphisms: ef179f9a294cf7379083eeb729b29d1732b452565a0f4a944f7de93c7354af4f
rank: 3
gram_tensor:
- [5, 0, 2]
- [0, 8, 0]
- [2, 0, 20]
signature: [3, 0]
determinant: 768
definiteness: positive_definite
dual_gram_tensor:
- [5/24, 0, -1/48]
- [0, 1/8, 0]
- [-1/48, 0, 5/96]
form:
  integer_valued: true
integral:
  parity: odd
  level: 192
  discriminant_group: [8, 96]
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
  theta_series: [1, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 4
    simple_roots:
    - [0, 1, 0]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GGV
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GGV
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:650.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 358, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 358, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:650` gives this Gram tensor.
