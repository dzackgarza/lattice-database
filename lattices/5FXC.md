---
tag: 5FXC
name: Constructed lattice 5FXC
latex: L_{\mathrm{5FXC}}
certifications:
  derive: 9c227d6638d018ab07ba40200eef7c7b234f7c16b001d0eb21ef740d252825be
  form.integer_valued: 0c10c89e97757cb7f4a2b16c7c8d89cb17ac33e0549f2d179dec265bc37fbee5
  integral.elementary_primes: b4697877e085eabe9133329e4077ddf3ec56538fd679b01e4dc89835ec230435
  integral.genus_symbol: bf624453ca64824554ae432a0308fcda6dc6843b52ff145376b732081480bf09
  integral.genus_class_count: 12a61ec350f5a0a48547dddd6ebe15dafd7d56e6b1e76e6e6b3c5e38b7d86da4
  integral.overlattice_count: 125d99daa57609e14cf2a465eb4302d4132ec9fb686d419e6bb08fd0c02b69d9
  integral.spinor_genus_count: 4b51a34eeade82730f4c6e63b43446956d830e57d67d447284d026274777ab20
  integral.spinor_genera: 15b198612be5fc306142287c4fe78398350eb6b1a9a19ab36cbb7d052befa2b7
  automorphisms.automorphism_group_order: 5153fea3845db2d283a24c64bcabc763fd8228ab6a97a14d61d7c600ee54e9ce
  automorphisms.automorphism_group_generator_morphisms: a26886f2f11f7b4b0051b5dd556a8ded5343aa05bdbcb067f0f3aa3cb4f87f24
  integral.primitive_orbits: 43a7c184cafeefa921de84262c7b56761a528f7d3531941fba200ca0ccac7104
  integral.modular_scale: 161b4282db04ff0bbb0913c9e93427504aa4cbc5e472e4db6bf825b9625813d7
  integral.anisotropic_primes: d7939119aae503e98f31e975cada45a36b19a4acc8aa40a2e83559e67429edb3
  integral.local_representations: eb10223f55c87bdaf38e748c4c4b4b9802a573dfcf623943391b865e5a50b08a
  integral.local_densities: bd4a3d443279b04d5ca68cebfe3f258be2483e0d7394cd4c8d04722d577ebc62
rank: 5
gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, -2, 0, 0]
- [0, -2, 0, 0, 0]
- [0, 0, 0, -2, 1]
- [0, 0, 0, 1, -2]
signature: [1, 4]
determinant: 12
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0, 0, 0]
- [0, 0, -1/2, 0, 0]
- [0, -1/2, 0, 0, 0]
- [0, 0, 0, -2/3, -1/3]
- [0, 0, 0, -1/3, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 6
  modular_scale: false
  discriminant_group: [2, 6]
  overlattice_count: 4
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{1,4} (2: [1^-3]_7 2^2; 3: 1^4 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  primitive_orbits:
    O:
      constant: 1
      z: []
      w: []
    O+:
      constant: 1
      z: []
      w: []
    SO:
      constant: 1
      z: []
      w: []
    SO+:
      constant: 1
      z: []
      w: []
    Otilde:
      constant: 3
      z: []
      w: []
    Otilde+:
      constant: 3
      z: []
      w: []
    SOtilde:
      constant: 3
      z: []
      w: []
    SOtilde+:
      constant: 3
      z: []
      w: []
  anisotropic_primes: []
  local_representations: []
  local_densities:
  - prime: 2
    densities: [3/2, 3/2, 1/4, 9/16, 3/2, 3/2, 3/4, 9/16]
  - prime: 3
    densities: [8/9, 8/9, 34/27, 8/9, 8/9, 32/27, 8/9, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7, O(L) generator 8, O(L) generator 9, O(L) generator 10, O(L) generator 11, O(L) generator 12, O(L) generator 13, O(L) generator 14, O(L) generator 15, O(L) generator 16]
indefinite:
  isotropic: true
morphisms:
- target: 5FXC
  name: O(L) generator 1
  matrix:
  - [-7, 12, -12, -12, 0]
  - [-6, 10, -9, -9, 0]
  - [6, -9, 10, 9, 0]
  - [-8, 12, -12, -11, 0]
  - [-4, 6, -6, -6, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 2
  matrix:
  - [-3, 4, -8, -6, 0]
  - [-4, 5, -8, -6, 0]
  - [2, -2, 5, 3, 0]
  - [-4, 4, -8, -5, 0]
  - [-2, 2, -4, -3, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 3
  matrix:
  - [-17, 24, -24, -24, 12]
  - [-12, 17, -16, -16, 8]
  - [12, -16, 17, 16, -8]
  - [-12, 16, -16, -15, 8]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, -2, 1, 2, -1]
  - [0, 2, 0, -1, 1]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 5
  matrix:
  - [-1, 0, -2, 0, 0]
  - [-1, 1, -1, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 6
  matrix:
  - [-1, 2, -4, -4, 2]
  - [-2, 3, -4, -4, 2]
  - [1, -1, 3, 2, -1]
  - [-2, 2, -4, -3, 2]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 7
  matrix:
  - [-3, 8, -4, -6, 0]
  - [-2, 5, -2, -3, 0]
  - [4, -8, 5, 6, 0]
  - [-4, 8, -4, -5, 0]
  - [-2, 4, -2, -3, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 8
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 1, -1]
  scale: 1
- target: 5FXC
  name: O(L) generator 9
  matrix:
  - [-1, 4, -6, -6, 0]
  - [-3, 7, -9, -9, 0]
  - [2, -4, 7, 6, 0]
  - [-4, 8, -12, -11, 0]
  - [-2, 4, -6, -6, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 10
  matrix:
  - [-1, 6, -4, -6, 0]
  - [-2, 7, -4, -6, 0]
  - [3, -9, 7, 9, 0]
  - [-4, 12, -8, -11, 0]
  - [-2, 6, -4, -6, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 11
  matrix:
  - [1, 0, 0, 0, 0]
  - [0, 1, 0, 0, 0]
  - [0, 0, 1, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 12
  matrix:
  - [-1, 2, 0, 0, 0]
  - [-1, 1, -1, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, 0, 1, 0]
  - [0, 0, 0, 0, 1]
  scale: 1
- target: 5FXC
  name: O(L) generator 13
  matrix:
  - [-3, 8, -4, -6, 0]
  - [-4, 8, -5, -6, 0]
  - [4, -9, 6, 8, -1]
  - [-4, 8, -6, -7, 0]
  - [2, -4, 2, 3, -1]
  scale: 1
- target: 5FXC
  name: O(L) generator 14
  matrix:
  - [-1, 0, -2, 0, 0]
  - [-2, 2, -3, -2, 1]
  - [1, -1, 3, 2, -1]
  - [-2, 2, -4, -3, 1]
  - [0, 0, 0, 0, -1]
  scale: 1
- target: 5FXC
  name: O(L) generator 15
  matrix:
  - [3, -4, 4, 4, -2]
  - [-2, 2, -3, -2, 1]
  - [2, -3, 2, 2, -1]
  - [-2, 2, -2, -1, 1]
  - [-2, 2, -2, -1, 0]
  scale: 1
- target: 5FXC
  name: O(L) generator 16
  matrix:
  - [-1, 0, 0, 0, 0]
  - [0, -1, 0, 0, 0]
  - [0, 0, -1, 0, 0]
  - [0, 0, 0, -1, 0]
  - [0, 0, 0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICZ, 3ID0.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICZ, 3ID0.
- tag: 3ID0
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ICZ, 3ID0.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ICZ, 3ID0.
