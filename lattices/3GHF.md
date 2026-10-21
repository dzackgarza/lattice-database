---
tag: 3GHF
name: watson 3:670
latex: watson 3:670
aliases: []
certifications:
  derive: 241f24e0fd759a22d0c8cbb4260412b2194c489658e34e4fab8322b76007924a
  form.integer_valued: 3d549ad406c809a6b4a5f02531c2a47d8015ce479138923ce663e961af6cfd04
  integral.elementary_primes: 1608bcf1b65b9e9bb1239e541807d2d25f01caee953a910efbdfea061232aaed
  integral.genus_symbol: 70605af52678b4284ab43ce5b49f78d2a100d86957e4f058dbf6afa10c26b6ec
  integral.genus_class_count: 8aaf6712ea5f29e2b9dd8ad1184bb3bda48017a088c0f0f9066f3e7a51bebbaf
  integral.overlattice_count: b10f6e41ed75d0f7d84ff20d0f644df929e51109c79a4d07559c6b6e022ac9b3
  integral.spinor_genus_count: 64c42af65fb9442ff4531bf39a40d97ab3418860b382c43cbd8b8c52c94357fc
  integral.spinor_genera: 771c11add1a849c856791e6021fc572e0bdd3281c7b3aa6c722be24dc59e7db0
  integral.hyperbolic_index: 7f2e0139022bbb5928126f8668ae762080899e09446ad933c855217dbe00f245
  definite.automorphism_group_order: b4bc61953fc1ee3b242800627990a7786409ca2a462cfae9aa4d38b3d07f696b
  definite.automorphism_group_generator_morphisms: 56c12dfae75340ac1d5867b7217b243ce479ecc68ebe1c260e6dbb32918e3d86
  integral.primitive_orbits: 8bc521133a083fb860f4219238ff1a276d5782b87a790505108c5ac44e65931f
  integral.modular_scale: 4f95c054abc44a3c0d6837bccb2eb3a1e37b06ec2bc72b24a6f8cbf7d1d520fb
  definite.genus_theta_series: 696f1eac22f48a0ee1b432f0806822a7e631fdc4d1222a4e1c222f1b1894d6c1
  definite.theta_series_cuspidal_component: 45afdf4be80c2f0fb931d25fa0c80f8cba557fd4ccb25ba08069a756c918e7ff
  definite.siegel_eisenstein_coefficients: d8a67383982ce3a1dac6eca84fbd28fdf2d7e7b856d203bff494c8bc57592c60
  integral.anisotropic_primes: 1aa91da63934646bafa618563f79188a5792f5c0d2dddbc4e6b65b92af3faaea
  integral.local_representations: 065de6adedbaab58f582a113629b856dea51198f5fdcc2aaa9c2d2063c07776e
  integral.local_densities: c875814511870f4484f2e5750b901a47067c8ecf8c17d04cc440c620f0f480af
rank: 3
gram_tensor:
- [3, -1, 0]
- [-1, 5, 0]
- [0, 0, 7]
signature: [3, 0]
determinant: 98
definiteness: positive_definite
dual_gram_tensor:
- [5/14, 1/14, 0]
- [1/14, 3/14, 0]
- [0, 0, 1/7]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 28
  modular_scale: false
  discriminant_group: [7, 14]
  overlattice_count: 3
  bad_reduction_primes: [2, 7]
  genus_symbol: 'I_{3,0} (2: [1^2 2^1]_3; 7: 1^-1 7^-2)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 0
    - representative: 5
      least_valuation: 0
    - representative: 7
      least_valuation: 0
    - representative: 2
      least_valuation: 1
    - representative: 6
      least_valuation: 1
    - representative: 10
      least_valuation: 1
  - prime: 7
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 0
    - representative: 7
      least_valuation: 1
    - representative: 21
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [1, 3/2, 1, 3/2, 1, 1, 1, 3/4, 1, 3/2, 1, 3/2]
  - prime: 7
    densities: [0, 0, 2, 0, 2, 2, 6/7, 0, 0, 2, 0, 2]
definite:
  minimum: 3
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  theta_series: [1, 0, 0, 2, 0, 2, 2, 2, 0, 0, 6, 0, 6]
  genus_theta_series: [1, 0, 0, 2, 0, 2, 2, 2, 0, 0, 6, 0, 6]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [0, 0, 2, 0, 2, 2, 2, 0, 0, 6, 0, 6]
  root_system: []
  roots:
  - type: A1
    scale: 7/2
    simple_roots:
    - [0, 0, 1]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GHF
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GHF
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:670.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
---

Source entry `watson:3:670` gives this Gram tensor.
