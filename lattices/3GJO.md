---
tag: 3GJO
name: watson 3:751
latex: watson 3:751
aliases: []
certifications:
  definite.regular: f5f9363ba2c1790753551bdc2254f3e665a614d593e31c32b82b6b742d67e25d
  definite.spinor_regular: 6dbe6715e6ffb7f2bc0e7ca08acacdcb3e47e8909b696d6a3333f1c3ab91faa2
  derive: 4847b0b0ee16a73541285afbd49a19999058b04e65f13ca676464fe1f3c1d5b1
  form.integer_valued: 3d811019acad7f4f57cd291e0bf5fbd9f987273daa1b51ae304010434c30d721
  definite.automorphism_group_order: 8fb7ce948a08b12e5ebc0c64abe15f0808627baad924436f9da0897b9d2cf12b
  definite.automorphism_group_generator_morphisms: cc644092a7dae39f4133be32a549cd05bc7b240790573b2433af5ba792667429
rank: 3
gram_tensor:
- [4, 2, 0]
- [2, 5, 0]
- [0, 0, 16]
signature: [3, 0]
determinant: 256
definiteness: positive_definite
dual_gram_tensor:
- [5/16, -1/8, 0]
- [-1/8, 1/4, 0]
- [0, 0, 1/16]
form:
  integer_valued: true
integral:
  parity: odd
  level: 32
  discriminant_group: [16, 16]
  bad_reduction_primes: [2]
definite:
  minimum: 4
  kissing_number: 2
  automorphism_group_order: 8
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 8
    simple_roots:
    - [0, 0, 1]
  - type: A1
    scale: 8
    simple_roots:
    - [1, -2, 0]
  - type: A1
    scale: 2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 2]
morphisms:
- target: 3GJO
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GJO
  name: O(L) generator 2
  matrix:
  - [1, 1, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3GJO
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:751.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 242, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 242, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:751` gives this Gram tensor.
