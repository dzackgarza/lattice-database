---
tag: 4AXD
name: Constructed lattice 4AXD
latex: L_{\mathrm{4AXD}}
certifications:
  derive: 64c28e1100e99c3e42c9cac50978303074c1dfb3645e24e1dad557094704cb53
  form.integer_valued: 3c50705e02a18d20afeeeefcd14622a56659418c7b4164d9f529cee9b28b6316
  integral.elementary_primes: d95fa5570fdc0ce5f767826501941f0b69c15498dd56d20e67128716c1cdfa0c
  integral.genus_symbol: bb08bd66c0488da776f0f92482f36e334bdd04c2ac3f01e460a42b48a7442f57
  integral.genus_class_count: e4a8d992a2c2c0472a1ff729b5494b23dab7dc0287138b07314bbd4d9f3cf785
  integral.overlattice_count: 0389341b8210e455e674c6344caa82f3bfd91191ef074c8562d29b9a6828276e
  integral.spinor_genus_count: 079314d5b301f5a19dd18dcffedc7a803c62f82c0fbeb35b068a051de8afd172
  integral.spinor_genera: 212b134188c58bf12b35efdbb5fcb60054b52f1e922b964894fae0e29bf29329
  automorphisms.automorphism_group_order: ae7884356ebefddf52059c4520c0f11011a4e0838dbabe33c8a829c374a2c0af
  automorphisms.automorphism_group_generator_morphisms: 45d1ceced5695630e9e62f56bec56f35e5e9cee32b622d46e269120175d1302f
  integral.primitive_orbits: db05cef4e18a61efb3b375a9d3b7a383a8d6d4017abbcdcaa310b9e455be461d
  integral.modular_scale: a3313fa0132eb53042980a38cf1f95de16c30fd92508066659a38768cb586282
  integral.anisotropic_primes: 281828cdd5b7888f060b53291f7c2ac7baeac522faad9b86289249d33add43e0
  integral.local_representations: a7bd440051ec66af092a2085e33a9730dd2dfec9d34fc639bd1e93e4fb110857
  integral.local_densities: 6595ea5bb6810e52c8723092b20d20bd838c07c3f3acb77581bcf80317f593b0
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, -4, 2]
- [0, 0, 2, -4]
signature: [1, 3]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, -1/3, -1/6]
- [0, 0, -1/6, -1/3]
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
  quadratic_character: -3
  genus_symbol: 'I_{1,3} (2: [1^-2]_4 2^2; 3: 1^3 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  primitive_orbits:
    O:
      constant: 2
      z: []
      w: []
    O+:
      constant: 2
      z: []
      w: []
    SO:
      constant: 2
      z: []
      w: []
    SO+:
      constant: 2
      z: []
      w: []
    Otilde+:
      constant: 4
      z: []
      w: []
  anisotropic_primes: []
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
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [1, 0, 1, 5/2, 1, 0, 1, 5/4, 1, 0, 1, 5/2]
  - prime: 3
    densities: [2/3, 4/3, 8/9, 2/3, 4/3, 10/9, 2/3, 4/3, 26/27, 2/3, 4/3, 8/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6, O(L) generator 7]
indefinite:
  isotropic: true
morphisms:
- target: 4AXD
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4AXD
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 1, -1]
  scale: 1
- target: 4AXD
  name: O(L) generator 3
  matrix:
  - [3, -2, 2, 2]
  - [2, -1, 2, 2]
  - [-1, 1, 0, -1]
  - [-1, 1, -1, 0]
  scale: 1
- target: 4AXD
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 0, 1]
  - [0, 0, 1, 0]
  scale: 1
- target: 4AXD
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4AXD
  name: O(L) generator 6
  matrix:
  - [9, -2, 16, -2]
  - [2, -1, 4, -2]
  - [-5, 1, -9, 1]
  - [-3, 1, -5, 0]
  scale: 1
- target: 4AXD
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID1.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID1.
- tag: 3ID1
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID1.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICW, 3ID1.
