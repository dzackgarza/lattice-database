---
tag: 3IEG
name: Constructed lattice 3IEG
latex: L_{\mathrm{3IEG}}
certifications:
  derive: aaf89e7315653075363082506b48cddb3c1a1f4329c911ee26af8f169b9eea7b
  form.integer_valued: b57a5be5b665fe50b1db6afae50d7d85913f1d21bb49f51c2cdb7b610c884215
  integral.elementary_primes: 1f05f1bd27f27f919baae72cf34e0e87fd890e6cf96743b0dfd90d9d21ce763d
  integral.genus_symbol: 0a6fca9b837500ff3c93c122ad9623c74cb6e5a3616a065def788e7cb176032a
  integral.genus_class_count: 2a661b4f49fc83c1abe9f1797907d31127da2d20c903c7c82daa5f6e77b46d2e
  integral.overlattice_count: 72e86133b1b183b430911e567d4b0de9e6a9b77a11ea09f3750ec86baab63caf
  integral.spinor_genus_count: b75a38fa8a92c878fe31c229f48c17c6bb92f43f55c97c8f2127cc21f2114488
  integral.spinor_genera: e73182aee08a679e8a575cc32383f73da3669d1ec9bc409f6a5ead3453b45b04
  integral.hyperbolic_index: 9fed74e6d86926b46ef2f20a97a146e735e9a296311352ad3c4d956ede3475a6
  automorphisms.automorphism_group_generator_morphisms: b60c8d810748ddbafd573c6b01e023799b3c90c4769a4cfa8f92e5f3baceab2a
  integral.discriminant_form: 5a55b7c6a45e827dac8cfff631631edb92c94c09a8cd66517d4acc4423b320a2
  integral.primitive_orbits: f882f31e5cf0b5f66890afff17a22511563c2096806b2e04abeb3d7ba7a876c0
  integral.modular_scale: a1875687bfc53e1a257fa03305263a69f18f090c1f0f6eb557fe670af13c249d
  integral.anisotropic_primes: 018da0f88d86f5683c9559c931be9910f1e84bd10a808da45ccef7884473adbb
  integral.local_representations: 05a5684076e746e737f46eb146e802fb9537c7e25b3c18c995667eb61f31bd64
  integral.local_densities: 0597d04af3fc1519619804ca6f8e85d986461feb08f9a159d3a60a8f130e2abe
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, 0, -1]
- [0, -1, 0]
signature: [2, 1]
determinant: -2
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, 0, -1]
- [0, -1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: false
  discriminant_group: [2]
  overlattice_count: 1
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{2,1} (2: 1^2 [2^1]_1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 1
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
  discriminant_form:
    orthogonal_group_order: 1
    isotropic_classes: 1
    isotropic_orbits: 1
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 2
    - representative: 7
      least_valuation: 2
    - representative: 2
      least_valuation: 1
    - representative: 6
      least_valuation: 1
    - representative: 10
      least_valuation: 1
    - representative: 14
      least_valuation: 1
  local_densities:
  - prime: 2
    densities: [0, 3, 0, 3/2, 0, 3/2, 0, 3, 0, 2, 0, 3/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IEG
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IEG
  name: O(L) generator 2
  matrix:
  - [-1, 0, -1]
  - [2, 1, 1]
  - [0, 0, 1]
  scale: 1
- target: 3IEG
  name: O(L) generator 3
  matrix:
  - [1, 0, 1]
  - [2, 1, 1]
  - [0, 0, 1]
  scale: 1
- target: 3IEG
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICY.
