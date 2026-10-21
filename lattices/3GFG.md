---
tag: 3GFG
name: watson 3:599
latex: watson 3:599
aliases: []
certifications:
  definite.regular: 9f2409501d3532ccdc1f78fd8c9c8b9316801cc9c5935a74ebd2122e08a83c4a
  definite.spinor_regular: e688e068e282bf5aaff173fadc2f6b5def17a77cdefc2efba12ff781db311534
  derive: b06146cbbd7f97adcb9ed390151f72e3f9cf20ca373cc1703a3df9c347f3e6a5
  form.integer_valued: 8dacdab497b5639b9960709cfa0b52fe15eee08acefbb3f1a751ee974046679c
  definite.automorphism_group_order: b4852002bdf3b467c47d5e637241d1c766baf4bb5b5c0be4ef4e5f0fe7464b59
  definite.automorphism_group_generator_morphisms: 84dcc6ae1b0ac4b87b49960b50b0ebc748d890dd8ec30eacab0d5ade130d1a0e
rank: 3
gram_tensor:
- [7, 1, 1]
- [1, 23, -9]
- [1, -9, 23]
signature: [3, 0]
determinant: 3072
definiteness: positive_definite
dual_gram_tensor:
- [7/48, -1/96, -1/96]
- [-1/96, 5/96, 1/48]
- [-1/96, 1/48, 5/96]
form:
  integer_valued: true
integral:
  parity: odd
  level: 192
  discriminant_group: [32, 96]
  bad_reduction_primes: [2, 3]
definite:
  minimum: 7
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
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
    scale: 32
    simple_roots:
    - [0, 1, -1]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GFG
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GFG
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:599.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 499, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 499, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:599` gives this Gram tensor.
