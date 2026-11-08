---
tag: 3IDU
name: Constructed lattice 3IDU
latex: L_{\mathrm{3IDU}}
certifications:
  derive: e99b12cab1b921eba5fde47f3d055f909c6ef3b38be257507ac88eb21492b53b
  form.integer_valued: 4a3a6d312b8d3600c73a9de01b3ba625b257327a07442f256a2a334dadf1eb3a
  integral.elementary_primes: 70605108657efadf55b17d1fde104edf9acc55f7067011815c3b6977cf11dd81
  integral.genus_symbol: 1ee4d6e4ad4429cdb4242f33240108fdbf9a459ad240e5493c7b45a529a25baf
  integral.genus_class_count: a1490e95c43279ac8c10cf21ac601fb8a79e505398f9a67bb263a58b1404e5e7
  integral.overlattice_count: 3643479c57da9c52a74e3c05a144c5fb2283a1f099421c64329edb78d602fd90
  integral.spinor_genus_count: 9875eda8352f549f1f465fc2700d07950b3916c10020bd02eeff633700ad3ceb
  integral.spinor_genera: ff85b575a7280e4099b0f2ee612d7a9814879de94c2945c8bc4ffb5a97a8a599
  automorphisms.automorphism_group_generator_morphisms: 71a9ab596293e67e7164d723ad3ffef7a70bc8035c5e471743f2d2135a00477d
  integral.primitive_orbits: 9d23ac644071d1e2acc750d99d638240963d79e52f64ab2eb55a4d901e1d276e
  integral.modular_scale: aae140c1d0fe8a0ae9f3ab60569c967ea38b47f3cbec572ca7c58303e097c499
  integral.anisotropic_primes: abed6de5a3521813c7ac5def2f4aa6ca14222b816be9e10fae0e1d954240abd7
  integral.local_representations: c5d2f8a0eb427d1900d2e6449279286ab7ed9b43b55b12375dfbb4d0a6ea338c
  integral.local_densities: c4b78e33291fd956ef76358f9de2c37d0a4acb4ca1934cc3257854a64eca7b52
rank: 3
gram_tensor:
- [-1, 0, 0]
- [0, -1, 0]
- [0, 0, 2]
signature: [1, 2]
determinant: 2
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0]
- [0, -1, 0]
- [0, 0, 1/2]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 4
  modular_scale: false
  discriminant_group: [2]
  overlattice_count: 1
  bad_reduction_primes: [2]
  genus_symbol: 'I_{1,2} (2: [1^2 2^1]_7)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  primitive_orbits:
    O:
      constant: 1
      z: []
      w: []
    SO:
      constant: 1
      z: []
      w: []
    Otilde:
      constant: 1
      z: []
      w: []
    SOtilde:
      constant: 1
      z: []
      w: []
    O+:
      constant: 1
      z: []
      w: []
    SO+:
      constant: 1
      z: []
      w: []
    Otilde+:
      constant: 1
      z: []
      w: []
    SOtilde+:
      constant: 1
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [1, 1/2, 1, 1/2, 1, 1, 1, 5/4, 1, 1/2, 1, 1/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IDU
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDU
  name: O(L) generator 2
  matrix:
  - [-8, -3, -12]
  - [-3, 0, -4]
  - [6, 2, 9]
  scale: 1
- target: 3IDU
  name: O(L) generator 3
  matrix:
  - [0, 1, 0]
  - [-3, 0, -4]
  - [2, 0, 3]
  scale: 1
- target: 3IDU
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 0002.
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICW, 0002.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICW, 0002.
