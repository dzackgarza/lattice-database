---
tag: 3GRU
name: watson 4:251
latex: watson 4:251
aliases: []
certifications:
  derive: 9dc65e664b049b90e65e09fbf0e1fbba26ab470dd90725ced27ea70e8f89c03e
  form.integer_valued: aa7332520edde7b72518e0506a91686cb58539d097c7a89e471629bcb2928f17
  integral.elementary_primes: 64c1c7d61aa30ce6ac778433afb9109f6b6b1888e6f0778319d8d9ad16cbea23
  integral.genus_symbol: 4fca3dd16913586d493fc661eed02413b46dc4d8b7d2e8518a301d46f8ea23df
  integral.genus_class_count: c01f1085b547910d9494c42caa685dd0a54882519aa6514dc371128f9b3c712b
  integral.spinor_genus_count: 242d3dec511f6af78abf8e9b3fbb60cf66d22605fe043833dd8559151039a06a
  integral.spinor_genera: 59be37cf8c633a991384e82e8615c5847f90e55b4de3b0d113dd5bc38be3a0c5
  integral.hyperbolic_index: b229e8c63220a2cf3d8117ed70bb67ab118dba4ae7405e2940f65b41187c983e
  definite.automorphism_group_order: 65b9eee8a64d41dd920aff049997db5a32c85e41c7016f5437cc85b522035e3c
  definite.automorphism_group_generator_morphisms: 48c9a0bf2b2f6cff138d25f2e66780ac227eb44c726e8c25fcb303417606466b
rank: 4
gram_tensor:
- [6, 3, -3, 0]
- [3, 14, -4, 0]
- [-3, -4, 14, 0]
- [0, 0, 0, 60]
signature: [4, 0]
determinant: 54000
definiteness: positive_definite
dual_gram_tensor:
- [1/5, -1/30, 1/30, 0]
- [-1/30, 1/12, 1/60, 0]
- [1/30, 1/60, 1/12, 0]
- [0, 0, 0, 1/60]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 120
  discriminant_group: [15, 60, 60]
  bad_reduction_primes: [2, 3, 5]
  quadratic_character: 60
  genus_symbol: 'II_{4,0} (2: 1^-2:[4^-2]_2; 3: 1^-1 3^3; 5: 1^1 5^-3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 6
  kissing_number: 2
  automorphism_group_order: 16
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
  minimal_vectors:
  - [-1, 0, 0, 0]
  - [1, 0, 0, 0]
  perfect: false
  theta_series: [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]
  root_system: []
  roots:
  - type: A1
    scale: 30
    simple_roots:
    - [0, 0, 0, 1]
  - type: A1
    scale: 10
    simple_roots:
    - [0, 1, 1, 0]
  - type: A1
    scale: 15
    simple_roots:
    - [1, -1, 1, 0]
  - type: A1
    scale: 3
    simple_roots:
    - [1, 0, 0, 0]
root_sublattice:
  invariant_factors: [1, 1, 1, 2]
morphisms:
- target: 3GRU
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3GRU
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 3GRU
  name: O(L) generator 3
  matrix:
  - [1, 1, -1, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3GRU
  name: O(L) generator 4
  matrix:
  - [1, 1, -1, 0]
  - [0, 0, 1, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 4:251.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:4:251` gives this Gram tensor.
