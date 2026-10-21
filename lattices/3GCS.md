---
tag: 3GCS
name: watson 3:503
latex: watson 3:503
aliases: []
certifications:
  definite.regular: 25ec7db6baae6193fc4ba5cd56d616b8d812760375f075b5fec62f12de11c4ba
  definite.spinor_regular: a43ad5cbca8efaac6a7e734c847418e4af5039895ac633e4757d10ebb1ebc519
  derive: 9c40edb5d9a3f99645eaf762c13ef66aedfe69486c336ce35c8586d33da76a53
  form.integer_valued: 2cd4a32a7ff3eab2ab25a60db2fcda47ae7f6cefc253f4ab7cb074f88ff66e46
  definite.automorphism_group_order: bca0a18b691fe525bddd40d4d93bc4e7e2260c2b4bbba4e6832b5ef037dfcb27
  definite.automorphism_group_generator_morphisms: d2b8856897c1db2345e51d11f0144527402dde9cdcb07a38ef6729fade34549b
rank: 3
gram_tensor:
- [4, 2, 2]
- [2, 7, 1]
- [2, 1, 19]
signature: [3, 0]
determinant: 432
definiteness: positive_definite
dual_gram_tensor:
- [11/36, -1/12, -1/36]
- [-1/12, 1/6, 0]
- [-1/36, 0, 1/18]
form:
  integer_valued: true
integral:
  parity: odd
  level: 72
  discriminant_group: [12, 36]
  bad_reduction_primes: [2, 3]
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
  theta_series: [1, 0, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 12
    simple_roots:
    - [1, -2, 0]
  - type: A1
    scale: 36
    simple_roots:
    - [1, 0, -2]
  - type: A1
    scale: 2
    simple_roots:
    - [1, 0, 0]
root_sublattice:
  invariant_factors: [1, 2, 2]
morphisms:
- target: 3GCS
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GCS
  name: O(L) generator 2
  matrix:
  - [1, 1, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3GCS
  name: O(L) generator 3
  matrix:
  - [1, 0, 1]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:503.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 295, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 295, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:503` gives this Gram tensor.
