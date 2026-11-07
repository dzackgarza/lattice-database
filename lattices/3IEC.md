---
tag: 3IEC
name: Constructed lattice 3IEC
latex: L_{\mathrm{3IEC}}
certifications:
  derive: e41f258a7d9dfcc361b3b5a355d09e1e9e291d85453568dc2699c2dac8169cb4
  form.integer_valued: 5f35f3c301b48a2bafb03dfcc926468db9e2a794c40f9e3bbc3dac481572afaa
  integral.elementary_primes: a5437103e20d4a538fa04e3f474a2dc315ad199af1d70cc4948f0626a3ba4ecb
  integral.genus_symbol: c487f579007b8babfd5e56cd1db0b11699f7ae57dbbdcf50bf5b5f51d1f5d948
  integral.genus_class_count: 5aa72d34f46003d84f75801347519a93f204fe65933cf4a6c254a677763bb8fe
  integral.overlattice_count: 43a164f8508e24d2af6f41c7aec1f884dbc9cd92ef0556ed1dc9b444d48691ee
  integral.spinor_genus_count: 5dcae05ae38a95be0fa035bfb3614ec807daeab1cc64b620a27c9bea3cd9d789
  integral.spinor_genera: 3dff3bdf2f572ba77ce0210b500ec38554e776e334698fe7f1861e2a16ebfcf4
  integral.hyperbolic_index: b6062ba2057b78427172a8a2fd5e120258c17b506fdcb549649da6252afa26fa
  automorphisms.automorphism_group_generator_morphisms: 3d771956cc435832403ce1cd781dea55075f7883b9c7e3166b75e67876eba61e
  integral.primitive_orbits: b9af8d6b865e4297d518cb471289339d8477ca3b6ec743c163acad256a59011c
  integral.modular_scale: dbfec2af7cd2b872618769322f226ab579555aa458a29e25fd70c8816a631791
  integral.anisotropic_primes: f959c2b1e91358f576e33c2d84c5e1f8de44e6d1458dfb90d45e8f2d809edcad
  integral.local_representations: 9074b35a351eda94dd836f29ce7b99b363317dafe1a38af01c2a89b09f637fe3
  integral.local_densities: 3637e023704dcdc30830ebeeb426744f59e51bcd752186b843005ef4571192ef
rank: 3
gram_tensor:
- [-1, 0, 0]
- [0, 4, -6]
- [0, -6, 12]
signature: [2, 1]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [-1, 0, 0]
- [0, 1, 1/2]
- [0, 1/2, 1/3]
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
  genus_symbol: 'I_{2,1} (2: [1^-1]_3 2^2; 3: 1^-2 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
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
      constant: 3
      z: []
      w: []
    SOtilde:
      constant: 3
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
      constant: 3
      z: []
      w: []
    SOtilde+:
      constant: 6
      z: []
      w: []
  anisotropic_primes: []
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 2
    - representative: 3
      least_valuation: 0
    - representative: 5
      least_valuation: 2
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
    densities: [0, 0, 3, 3/2, 0, 0, 1, 3/2, 0, 0, 3, 3]
  - prime: 3
    densities: [2/3, 2/3, 2, 2/3, 2/3, 4/3, 2/3, 2/3, 14/9, 2/3, 2/3, 2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IEC
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 3]
  - [0, 0, 1]
  scale: 1
- target: 3IEC
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 2, -3]
  - [0, 1, -1]
  scale: 1
- target: 3IEC
  name: O(L) generator 3
  matrix:
  - [7, 0, -12]
  - [6, 1, -12]
  - [4, 0, -7]
  scale: 1
- target: 3IEC
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 3ICW, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICW, 3ID6.
