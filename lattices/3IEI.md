---
tag: 3IEI
name: Constructed lattice 3IEI
latex: L_{\mathrm{3IEI}}
certifications:
  derive: 8fad4a588402d01c3fd67873d2196c9eabcf26372d01c2737950b856533de1e2
  form.integer_valued: aeb19d24d6d8d147e384201c3539b4cdfde6e39002fbf163b3ada69769aea61e
  integral.elementary_primes: e97727df4f5d0be41f69c9d8b5ed88a3db389cad3227dba619c9ad4045c5ce95
  integral.genus_symbol: 2268a0cee3ff827498a7d92cabe37ceb7cf632efe8c7f12a6ecc32c43ea1f385
  integral.genus_class_count: ead8ab1b841abf8dd1f24a3b110d2025c2cd7208648528dccf8e07d676d5aa22
  integral.overlattice_count: 8b420ec76804fc75655b271623fdb206590512dae545f42dd8973e1d4c747c36
  integral.spinor_genus_count: d790f62fa53acbcd475561dd4ff629e4caf3a82bce8600058ccc957bdbca7756
  integral.spinor_genera: d8be5f5943358c514dee9f95958ec928b30f93163d5ea6a7bedd2530f1db4374
  integral.hyperbolic_index: 3e69338948f3bbfa93473c38e3d6c6937ef24b41e1f33b4028b34a3190c352fc
  automorphisms.automorphism_group_generator_morphisms: e83f59ac4b8abefb7f760de41edd2df13f1bc83231919ef2090cddbb4c2b7e3a
  integral.discriminant_form: 100b80a6d3766e71f428164670499aa145a0beefdc5b17dec7f91df9021d7569
  integral.primitive_orbits: 7049df81608cfc44ee85a591a9ee1b16a257616ec177c49fa03a5746567a90c3
  integral.modular_scale: 678bc305258482360f06429625cecb1102414594ac34d50571102025778e1058
  integral.anisotropic_primes: d54e00b8b98307fd87d35c75f9d447cff898cc3a67ff67f8bf018d18cfdbb5b7
  integral.local_representations: 7ed5064cae83967c61f938c5e87037011ef66650ca46b7de0cd6878d190550a5
  integral.local_densities: 85c8edbfbeb868d58400a7d62a5486abf36e7db869a96702d9b19adcf26510fb
rank: 3
gram_tensor:
- [2, 0, 0]
- [0, 0, -2]
- [0, -2, 0]
signature: [2, 1]
determinant: -8
definiteness: indefinite
dual_gram_tensor:
- [1/2, 0, 0]
- [0, 0, -1/2]
- [0, -1/2, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: 4
  discriminant_group: [2, 2, 2]
  overlattice_count: 4
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{2,1} (2: [2^3]_1)'
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
      constant: 2
      z: []
      w: []
    SOtilde:
      constant: 2
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
      constant: 2
      z: []
      w: []
    SOtilde+:
      constant: 2
      z: []
      w: []
  discriminant_form:
    orthogonal_group_order: 2
    isotropic_classes: 3
    isotropic_orbits: 2
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
    densities: [0, 4, 0, 1, 0, 1, 0, 4, 0, 2, 0, 1]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IEI
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IEI
  name: O(L) generator 2
  matrix:
  - [-1, -2, 0]
  - [0, 1, 0]
  - [2, 2, 1]
  scale: 1
- target: 3IEI
  name: O(L) generator 3
  matrix:
  - [1, 0, 2]
  - [2, 1, 2]
  - [0, 0, 1]
  scale: 1
- target: 3IEI
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: '0002'
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICZ.
- tag: 3ICZ
  relation: This presentation is obtained by orthogonal sum of 0002, 3ICZ.
---

The selected Gram tensor is obtained by orthogonal sum of 0002, 3ICZ.
