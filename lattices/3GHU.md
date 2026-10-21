---
tag: 3GHU
name: watson 3:685
latex: watson 3:685
aliases: []
certifications:
  definite.regular: f84f0b090c8312a38f704ae87ac1359ab7125864145265466eebcd8d90dee04f
  definite.spinor_regular: df10e63c6da0739b2d9aa224778333c0fd624de3feacde95c831263b5d22de2b
  derive: 08466b6fa9d21b81cdf91ab44ff16a1d8dd5056306383d1472389cef38340d77
  form.integer_valued: 632ff4856341c89f3b4f42243f6b13554fb4fe3e53a57eacf7f4d037740ea1b5
  definite.automorphism_group_order: 08004f370721465b333b5fec8879fe60cb08f3a384e6697d2c50318f7b1f8cc5
  definite.automorphism_group_generator_morphisms: 7b7cd1570ae058857042f58dbc6262036285860bfa1144ccf625c963ef2b5eab
rank: 3
gram_tensor:
- [5, 0, 0]
- [0, 8, 0]
- [0, 0, 40]
signature: [3, 0]
determinant: 1600
definiteness: positive_definite
dual_gram_tensor:
- [1/5, 0, 0]
- [0, 1/8, 0]
- [0, 0, 1/40]
form:
  integer_valued: true
integral:
  parity: odd
  level: 80
  discriminant_group: [40, 40]
  bad_reduction_primes: [2, 5]
definite:
  minimum: 5
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
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
    scale: 20
    simple_roots:
    - [0, 0, 1]
  - type: A1
    scale: 4
    simple_roots:
    - [0, 1, 0]
  - type: A1
    scale: 5/2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1]
  norms: [5, 8, 40]
morphisms:
- target: 3GHU
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GHU
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3GHU
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:685.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 433, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 433, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:685` gives this Gram tensor.
