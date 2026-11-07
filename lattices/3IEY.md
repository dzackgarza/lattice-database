---
tag: 3IEY
name: Constructed lattice 3IEY
latex: L_{\mathrm{3IEY}}
certifications:
  derive: 6f99ec9c3e4495dec3676576119d5067ea73b3076ac58ab13adc97cf6e0c8f06
  form.integer_valued: a5973be6ab7fcfde8f70dc4891994378d96d33d82f079f09d8fceb30e0311f5b
  integral.elementary_primes: 9096c79c93d7a43a506a813c8b4a62aba99992872db4736ded30bf2057b66ac8
  integral.genus_symbol: e294fe94fd85110c581c2480e36496e7a9076431a32965af56b6c56644c95217
  integral.genus_class_count: fd0a9bb45bb438e6f7315fd1bed99224935d1f8a49c0f23ec2f4b76edae70fc3
  integral.overlattice_count: 688a03a6a89952fff26e4919041b564547236f1dd6da1ad800c1b14cd12db12b
  integral.spinor_genus_count: 0afaacb7a0f993db37896cf353e5fd6b7c6d28295e81fb6a9f9f96367581ce14
  integral.spinor_genera: 465a6e3738294f4bcdeba3973914e12a24cdc5afc1f28c6dde763179448d832c
  integral.hyperbolic_index: 8604b0b36631d072be76fbe0993bd013d2854a03a890b70c206ee10ef0297a7f
  automorphisms.automorphism_group_generator_morphisms: e262a2d19eb9a7587da890c0f7765f1e6ef91a6405694da4a51a26e321de3009
  integral.discriminant_form: 89fe92726e13169c8e3fd039ed21359392379365cc5c5bf53919d4d4f33782dc
  integral.primitive_orbits: 3800cb9d0a9261fde38639485053a2aca06a0dfec0351335acc792f307f6c76a
  integral.modular_scale: c7442a38099e8e9e3b5def39a73a2ee9c6e9329429be9619e8bbc050db78d82a
  integral.anisotropic_primes: e7f5bdcb329b885ea91ca23e89fcfe4ab5e330dd643b1da5b855c85a720206ba
  integral.local_representations: edc40d27656d0c7ae7a0741858e23e74bb6c9eb600800145e017be0614bf38a5
  integral.local_densities: ee8944a56ad784771186b6be5f5752225c96520c426dc2e57047973bb58dd909
rank: 3
gram_tensor:
- [-2, 0, 0]
- [0, 2, -1]
- [0, -1, 2]
signature: [2, 1]
determinant: -6
definiteness: indefinite
dual_gram_tensor:
- [-1/2, 0, 0]
- [0, 2/3, 1/3]
- [0, 1/3, 2/3]
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
  genus_symbol: 'II_{2,1} (2: 1^-2 [2^1]_7; 3: 1^-2 3^-1)'
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
    densities: [0, 3/2, 0, 3/2, 0, 3, 0, 9/4, 0, 3/2, 0, 3/2]
  - prime: 3
    densities: [2/3, 2/3, 4/3, 2/3, 2/3, 2, 2/3, 2/3, 14/9, 2/3, 2/3, 4/3]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5, O(L) generator 6]
indefinite:
  isotropic: true
morphisms:
- target: 3IEY
  name: O(L) generator 1
  matrix:
  - [1, 0, 0]
  - [0, -1, 1]
  - [0, 0, 1]
  scale: 1
- target: 3IEY
  name: O(L) generator 2
  matrix:
  - [1, 0, 0]
  - [0, 1, 0]
  - [0, 1, -1]
  scale: 1
- target: 3IEY
  name: O(L) generator 3
  matrix:
  - [1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3IEY
  name: O(L) generator 4
  matrix:
  - [1, 0, 0]
  - [0, 0, 1]
  - [0, 1, 0]
  scale: 1
- target: 3IEY
  name: O(L) generator 5
  matrix:
  - [7, 6, 0]
  - [8, 7, 0]
  - [4, 3, 1]
  scale: 1
- target: 3IEY
  name: O(L) generator 6
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICX, 0012.
- tag: '0012'
  relation: This presentation is obtained by orthogonal sum of 3ICX, 0012.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICX, 0012.
