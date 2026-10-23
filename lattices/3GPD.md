---
tag: 3GPD
name: watson 4:162
latex: watson 4:162
aliases: []
certifications:
  derive: 086b5c0ebf30becca06c3143cb4effb2bebdfeb42d9224404eeff21de12ff200
  form.integer_valued: 14e0c4305309c0ff7b752da4df46783e7420dcd5b34f8eb0b57f122fd94af6e4
  integral.elementary_primes: 9b93fa8e4564bf75dfcc865dd183023056065ba5695c097266bfdac2dd882d9e
  integral.genus_symbol: d72c958f329726927373da11a02920ad01f597b0ebdf3643f37fbba388276344
  integral.genus_class_count: f7c52a23c322012988ced963c321e7ce7d20a165e9c3945805ed1efc2597ec4b
  integral.overlattice_count: 77fcbef5e6474b86baf16e44a3f1172efa40856a78b22b51c432c637676213d5
  integral.spinor_genus_count: 2ba23cb5789c4d841979fa181a5b7de74742df772f32dabd67f3963bd0cc4000
  integral.spinor_genera: 89640ad30ed4fcade58b69489995a50c70f724f8cd311c543c0274f68c0eb1b3
  integral.hyperbolic_index: 8e98597ab0df5f9fc3a4037260ead71863f87206c650e28365f545737df28d2d
  definite.automorphism_group_order: 78ae3f01676d0970d601530a77b6233b61cb9873df4dc27f0845f65787c948d4
  definite.automorphism_group_generator_morphisms: 9778a9aa947b42d428f657a57a54a8ed8fd6834cc911a86651c1f246250310fd
rank: 4
gram_tensor:
- [10, -3, 4, 5]
- [-3, 10, 3, 2]
- [4, 3, 10, 2]
- [5, 2, 2, 20]
signature: [4, 0]
determinant: 9261
definiteness: positive_definite
dual_gram_tensor:
- [4/21, 2/21, -2/21, -1/21]
- [2/21, 10/63, -5/63, -2/63]
- [-2/21, -5/63, 10/63, 1/63]
- [-1/21, -2/63, 1/63, 4/63]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 63
  discriminant_group: [7, 21, 63]
  overlattice_count: 18
  bad_reduction_primes: [2, 3, 7]
  quadratic_character: 21
  genus_symbol: 'II_{4,0} (2: 1^-4; 3: 1^2 3^1 9^1; 7: 1^-1 7^3)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
definite:
  minimum: 10
  kissing_number: 8
  automorphism_group_order: 16
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3]
  minimal_vectors:
  - [-1, -1, 1, 0]
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 1, 0]
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [1, 1, -1, 0]
  perfect: false
  theta_series: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 2]
  root_system: []
  roots:
  - type: A1
    scale: 7
    simple_roots:
    - [0, 1, -1, 0]
  - type: A1
    scale: 7
    simple_roots:
    - [1, 1, 0, 0]
root_sublattice:
  invariant_factors: [1, 1]
morphisms:
- target: 3GPD
  name: O(L) generator 1
  matrix:
  - [0, 0, 1, -1]
  - [0, -1, 0, -1]
  - [1, 0, 0, 1]
  - [0, 0, 0, 1]
  scale: 1
- target: 3GPD
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [1, 0, 1, 0]
  - [-1, 1, 0, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3GPD
  name: O(L) generator 3
  matrix:
  - [1, -1, 0, 1]
  - [0, -1, 0, 0]
  - [0, 1, 1, 0]
  - [0, 0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 4:162.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:4:162` gives this Gram tensor.
