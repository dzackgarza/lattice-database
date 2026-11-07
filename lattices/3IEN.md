---
tag: 3IEN
name: Constructed lattice 3IEN
latex: L_{\mathrm{3IEN}}
certifications:
  derive: 8d936cd8f3376f6d5b31fa1bea5e3206586e4bd464f6429cf0be5ff0b363eb74
  form.integer_valued: 552abd5dfc402d4d1bf22cb511ccaa768beff16c852928fae7a056771b1a16e6
  integral.elementary_primes: 4dd0bb4fa28fbbece5ee4fff82c6f3de3aee197ba7cc2514c3c8fe027651ddff
  integral.genus_symbol: 23ffd05221af6068a2215d52c6514537140a837d275867d97683b1e47d23f9df
  integral.genus_class_count: 9fb44484e961fd0197b09653b716f9054b46e42267eb17acf350726acb636e94
  integral.overlattice_count: 7a88dcd28953a0cb188e5db9122a8d1cd103017c4538b17dc50a67921df2c6e6
  integral.spinor_genus_count: d9ecf59c7dd4a527ba58613a5c02050c4bdc2973ec46438c9573326dc2ef0544
  integral.spinor_genera: 99fc538581e272b57de3579e51ca117e2a563c1a53690f18450e13a15a250f1b
  integral.hyperbolic_index: bc04e36cc9209b0537d1a1bdc3dcf50f61596b904ea53973f8a2acbe5e46fa09
  automorphisms.automorphism_group_generator_morphisms: 86dfb141b0826b387e63795d970373e0db015f3f09666209f4363c4201450049
  integral.discriminant_form: 5b2a1a14b3af1dcf826139ea07df3f4756bd2111e88281ed4936e086abe5f24d
  integral.primitive_orbits: 80ac3f5f2e3ea77c58f4f8e8ca5507cd5bae267bb143bac0e3e91afb28405968
  integral.modular_scale: 8f59cb5a705002878faa88c8da4805ed678bc3ef4fd89303ff8bf3d9de5efd59
  integral.anisotropic_primes: 434af8c5be6fc78c851af8f7dfe2bfc66ee021873535c111d348ade85812f875
  integral.local_representations: 264ff9c3eaf547328e4d8614c548e76e8bfcef887cb746c0bf9564de693cc2b9
  integral.local_densities: a88097e4e9795f0766ad60789a021792f010d1f3a07db51c4045f072377cb066
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, -2, 3]
- [0, 3, -6]
signature: [1, 2]
determinant: 6
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, -2, -1]
- [0, -1, -2/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 12
  modular_scale: false
  discriminant_group: [6]
  overlattice_count: 1
  bad_reduction_primes: [2, 3]
  genus_symbol: 'II_{1,2} (2: 1^-2 [2^1]_1; 3: 1^-2 3^1)'
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
      constant: 2
      z: []
      w: []
  discriminant_form:
    orthogonal_group_order: 2
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
    densities: [0, 2, 0, 3/2, 0, 3/2, 0, 5/2, 0, 3, 0, 3/2]
  - prime: 3
    densities: [2/3, 2/3, 2, 2/3, 2/3, 4/3, 2/3, 2/3, 14/9, 2/3, 2/3, 2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 3IEN
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, -1, 1]
  scale: 1
- target: 3IEN
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, -1, 3]
  - [0, 0, 1]
  scale: 1
- target: 3IEN
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3IEN
  name: O(L) generator 4
  matrix:
  - [1, 0, 0]
  - [0, 2, -3]
  - [0, 1, -2]
  scale: 1
- target: 3IEN
  name: O(L) generator 5
  matrix:
  - [7, -6, 12]
  - [-12, 10, -21]
  - [-4, 3, -7]
  scale: 1
- target: 3IEN
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID3.
- tag: 3ID3
  relation: This presentation is obtained by orthogonal sum of 0002, 3ID3.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ID3.
