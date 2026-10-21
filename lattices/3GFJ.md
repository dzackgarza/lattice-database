---
tag: 3GFJ
name: watson 3:602
latex: watson 3:602
aliases: []
certifications:
  definite.regular: 29b8d450eb602a80bb4b4115863df1c0474f8c827f988e6b44c6b495272851e6
  definite.spinor_regular: f390a5eed45d38b04ca286c907960bc142699f705bb32816590908a38aee3d70
  derive: 3df4b77d51698df7985828c899ab46c73c3ce62f7ce6114abe17f0f63f6b8f55
  form.integer_valued: e3c7fda62f04ce9f1188d30dc0c2530028d35b5763f6c89f8bf639af702f435e
  definite.automorphism_group_order: 86622352345b2ad525c3e068de4ed34be41bd6c0485e259ec7dc56098c190194
  definite.automorphism_group_generator_morphisms: 7d468157d634948a002642e88b3a3b995064b0da8bb4676db6463244f7b5f3b5
rank: 3
gram_tensor:
- [3, 0, 0]
- [0, 8, 0]
- [0, 0, 12]
signature: [3, 0]
determinant: 288
definiteness: positive_definite
dual_gram_tensor:
- [1/3, 0, 0]
- [0, 1/8, 0]
- [0, 0, 1/12]
form:
  integer_valued: true
integral:
  parity: odd
  level: 48
  discriminant_group: [12, 24]
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
  theta_series: [1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 4, 4]
  root_system: []
  roots:
  - type: A1
    scale: 6
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
  norms: [3, 8, 12]
morphisms:
- target: 3GFJ
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GFJ
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3GFJ
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:602.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 247, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 247, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:602` gives this Gram tensor.
