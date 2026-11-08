---
tag: 3IDD
name: Constructed lattice 3IDD
latex: L_{\mathrm{3IDD}}
certifications:
  derive: eda636dfcb2d9a43e0a2432230d12f3cfa109f04875b97e659038a45a8e5c87d
  form.integer_valued: 67b39b84f89bc79db4e48770d20d9723393aad92965e861ad6fda5da0dc93fcc
  integral.elementary_primes: b87ab1c6678015a581b6ea9f1653b3be68076e43653e39e7761de25a7d044e1e
  integral.genus_symbol: 8bd548ce75a59d53251c21b85a6f7924dc6f54d48b2e98a194fe9c46136b8fee
  integral.genus_class_count: e31fa57c98297360c519c318e86df3390c2009b22277c2b37696bf09cd094392
  integral.overlattice_count: ff574b7de95e3e8806abc4f32acc65a316e8f90e74fd995832cf5739b41e84ee
  integral.spinor_genus_count: 18a7162c3f2aae7599b68b4358c0e996609fdb719afbc81f1a3d8a056a76b593
  integral.spinor_genera: cdc25e3146fcba4ab2c0beebc22079bf0d42ca89dd53e86893c33ce8c1c6bcae
  automorphisms.automorphism_group_generator_morphisms: ce2bdda8af751cdc2311b18c3edc7ead411e0c46c58bc372dd0b1dc0023a9376
  integral.primitive_orbits: f976c8a91b124afc8e735941fc69a857eef071910d8542edf2538edbf44fb0c2
  integral.modular_scale: 329ab7736633e936c157ff8017743b88e6a49c92717b52591c8d906fb85435b6
  integral.anisotropic_primes: 2816622ce9ddc04b25d82e7259fcc8f66d5f236dbd96c26016421365e3fb88f1
  integral.local_representations: 19aa3998c8010fb03c78d137db8251fe71175345786b0a9822cd91060396ee84
  integral.local_densities: 3b9afbe97e5284939ff006dfe2d7739dbde0e7851f37baf28eccc497721cd36d
rank: 3
gram_tensor:
- [1, 0, 0]
- [0, -1, 0]
- [0, 0, -2]
signature: [1, 2]
determinant: 2
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0]
- [0, -1, 0]
- [0, 0, -1/2]
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
- target: 3IDD
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, 1]
  scale: 1
- target: 3IDD
  name: O(L) generator 2
  matrix:
  - [2, -1, 2]
  - [1, 0, 2]
  - [-1, 1, -1]
  scale: 1
- target: 3IDD
  name: O(L) generator 3
  matrix:
  - [3, 0, 4]
  - [0, 1, 0]
  - [2, 0, 3]
  scale: 1
- target: 3IDD
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ICX.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ICX.
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ICX.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICW, 3ICX.
