---
tag: 3YPA
name: Constructed lattice 3YPA
latex: L_{\mathrm{3YPA}}
certifications:
  derive: 8a0d8aecd258313a41c3115b3a32929b98c72feb1defac15f0c6b086949f6070
  form.integer_valued: 621a24cd91536243937ea47cff037818682e2954c5022d1d6bfafae293ff520b
  integral.elementary_primes: e01dd9e788a73297cc43f4c07f8a476a4ef33109c819a013d48dc43aa09ac91e
  integral.genus_symbol: 057cb1b5e6dcdafd240a72338c6bd8faf28a59cfedd1a8b7975652b4d486cbfe
  integral.genus_class_count: 28373dcb1e5764802b63c699bc3fdd6b11b97309993bbd052e23f862cb811c59
  integral.overlattice_count: 8612094ba03039db85073b1bd4c52e66d8b19a6b9598400d6cd4bd7cc4beda14
  integral.spinor_genus_count: 2f711fdeeae3eae7afeccb92207b6a33947d0f227a93724d737f193f61ba7367
  integral.spinor_genera: d2af11cdbfd285d6c5df977c3c3d071b4164e0ca9e7c36805d24115ab417ca71
  automorphisms.automorphism_group_order: 02f6f7f18812b7b446fab55db9db7915580880b3fa5ab76ce5dcd0b11f42471d
  automorphisms.automorphism_group_generator_morphisms: f4ad4413460deb0aceb526d78f3eec4ad64429708855fa128295170500935750
  integral.primitive_orbits: 650a72aa03465fc61055f4d4f4f8641f5b3c0fe6762d43c2355d131ee7839e2e
  integral.modular_scale: 154d803b3cbe7d382e8d65b98c95306e38eb213286a1a6981792bc1283359446
  integral.anisotropic_primes: a7052687ca024a48a78d9ed07c612f175b3a4af86b232d591f8a13df46e9fcb7
  integral.local_representations: 315582cbdb8b89eeffe0132a158398ba7763266bb1d5c370f8e630b936417ef5
  integral.local_densities: 9651ddf96a10a2f43c6e1dfadc22d7705369cf532a75ae48268f686e76888c28
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 0, 2]
- [0, 0, 2, 0]
signature: [3, 1]
determinant: -4
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, 1, 0, 0]
- [0, 0, 0, 1/2]
- [0, 0, 1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: odd
  level: 2
  modular_scale: false
  discriminant_group: [2, 2]
  overlattice_count: 4
  bad_reduction_primes: [2]
  quadratic_character: -4
  genus_symbol: 'I_{3,1} (2: [1^2]_2 2^2)'
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
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 0
    - representative: 3
      least_valuation: 2
    - representative: 5
      least_valuation: 0
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
    densities: [2, 3/2, 0, 5/4, 2, 1/2, 0, 9/8, 2, 3/2, 0, 3/4]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 3YPA
  name: O(L) generator 1
  matrix:
  - [0, 1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3YPA
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 2, 0]
  - [0, 0, 1, 0]
  - [0, 1, -1, 1]
  scale: 1
- target: 3YPA
  name: O(L) generator 3
  matrix:
  - [-1, -2, 2, -2]
  - [-2, -1, 2, -2]
  - [-1, -1, 2, -1]
  - [1, 1, -1, 2]
  scale: 1
- target: 3YPA
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0]
  - [1, 0, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 3YPA
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0013.
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0001, 0001, 0013.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 0001, 0013.
