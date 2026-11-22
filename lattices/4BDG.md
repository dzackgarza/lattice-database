---
tag: 4BDG
name: Constructed lattice 4BDG
latex: L_{\mathrm{4BDG}}
certifications:
  derive: a8edab57b78408dac21ec401352b92f9bd67e8f9cc95ad44e2b2d7e765ce1b34
  form.integer_valued: 6eb7579c8b0762b560c99263900d0ff5f44aec48bd0e78c9f176cbc53da3d709
  integral.elementary_primes: a7ef85a27c0a5c4ccc464580a584857ea4a66c19f7fb444a36472f937e2fd8d2
  integral.genus_symbol: 4c96cd0f7ea89d655606bdb50ef3cbf2f7c02e174c139b3aa092f7c524ce48b8
  integral.genus_class_count: 85704446cc901dded84a8eb7d0dd7b393be331704713833c6c0976d8aeee155d
  integral.overlattice_count: 9fbefc52b20945c455272c72d47e1ffbb84a022c660ec8fe7f561943113018ef
  integral.spinor_genus_count: 9b53154c7fde7e01e10e9708c9cc3403d86eb24fc0f5160cb100b42804cc626a
  integral.spinor_genera: 50c0dd99fde2b697e5a4f8379b748bc6382c724ed9bfce354461ede69597ac7b
  automorphisms.automorphism_group_order: 02d0a7824985417a922342b3dc031df7e725d41fa99848fbd2391f2607d5d49d
  automorphisms.automorphism_group_generator_morphisms: 7c392e847af98e383f39b1a2f724caa34e32385d2137ac70be25b8b143e18bd1
  integral.primitive_orbits: a87f59b8d4540f4f9ed557797d71317f5ef2bce54cdda15682e4882fb1de8521
  integral.modular_scale: 37b0dda70004c1c9cce718fc1b71b1f263bbfc0460d08bbe0bf13b7403b37132
  integral.anisotropic_primes: 70618ac1f07998c5a2fc1c7a7a1dd5270e00d56bc96ad0b72ac0784680d2c7d8
  integral.local_representations: 8f256003a2e666890206a205f2746581bb532d06164cf60527e440e12c274320
  integral.local_densities: 34f809d244eda0e8f03e4be55f72986012b233b3d88da0454f858951c10ba510
rank: 4
gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, -4, 6]
- [0, 0, 6, -12]
signature: [1, 3]
determinant: -12
definiteness: indefinite
dual_gram_tensor:
- [1, 0, 0, 0]
- [0, -1, 0, 0]
- [0, 0, -1, -1/2]
- [0, 0, -1/2, -1/3]
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
- target: 4BDG
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4BDG
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -2]
  scale: 1
- target: 4BDG
  name: O(L) generator 3
  matrix:
  - [3, -2, 2, 0]
  - [2, -1, 2, 0]
  - [-2, 2, -1, 0]
  - [-1, 1, -1, 1]
  scale: 1
- target: 4BDG
  name: O(L) generator 4
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 3]
  - [0, 0, -1, 2]
  scale: 1
- target: 4BDG
  name: O(L) generator 5
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 1, 0]
  - [0, 0, 0, 1]
  scale: 1
- target: 4BDG
  name: O(L) generator 6
  matrix:
  - [9, -2, 14, -12]
  - [2, -1, 2, 0]
  - [-8, 2, -13, 12]
  - [-3, 1, -5, 5]
  scale: 1
- target: 4BDG
  name: O(L) generator 7
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
related:
- tag: '0001'
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID5.
- tag: 3ICW
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID5.
- tag: 3ID5
  relation: This presentation is obtained by orthogonal sum of 0001, 3ICW, 3ID5.
---

The selected Gram tensor is obtained by orthogonal sum of 0001, 3ICW, 3ID5.
