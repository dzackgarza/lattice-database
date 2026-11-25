---
tag: 6DJH
name: Constructed lattice 6DJH
latex: L_{\mathrm{6DJH}}
certifications:
  derive: 1af15626b48fcc12a3e740d446e400862023baed6598a30dedf53949a7d514bd
  form.integer_valued: 537fb2bbc863c7e534cb869f0258ccff32a5920b2e88e19e12110f08b6722856
  integral.elementary_primes: c4cf13e916b480400adb1e047bd712c45f0494dfa2c863fc589f8cd1b80e6c7c
  integral.genus_symbol: 859392353716dd43a1a3f6dafb53f27ff72c281a855df5f5f2a6f7655959439a
  integral.genus_class_count: 735f327fd6f69e72a19dc80f6b65bb773eaa9ff1ee02941f74eb80cc0c6a87f0
  integral.overlattice_count: 56d2732490f93d4bdc623373b4eaf8374d66fbd09312ac1aadad4ca7aeb6be94
  integral.spinor_genus_count: 9ffc7c73444c5db7252f32e9eab1a95fd525ba8f7ca9193ef17da52930be0c8f
  integral.spinor_genera: a2f2decf43f4cc802505af03438bb761d50803475ebbe183f63a19f63bfb108a
  integral.hyperbolic_index: 7eca6a724846bf6eb0572760b7fe87b72162586c462fa432b1f9573e058a358a
  automorphisms.automorphism_group_generator_morphisms: 192bce3f88c27b91c2cac5a276cb0273b66115db45a1461c0105ddf41efc409f
  integral.discriminant_form: d30873a7b42c0b321512aed99257cbdca3cb441d49cd9b320c90e0ffce0a0363
  automorphisms.automorphism_group_order: c97cad72db91337f3bbca8bdf237bcb2df4f38153da6d10b47c66bcf7ec8e44f
  integral.discriminant_orbits: 9d589bf1f1ce14c2f268c8fb4a3f2811e99345b2bae626f4619c1072bce49c25
  integral.modular_scale: a1fa2fbcd6b219f1309f56e983e34d2483d487dfb28c5de65adee5a6e8b96391
  integral.anisotropic_primes: d2fb48a460f050bcaf0f5c394ea4a9e03c7634bf7d817ee659f722593087ae8d
  integral.local_representations: c7c65766a5d7d264bc8c8245bda0b703115c0e1506ffd61ac0d372af3bfab45f
  integral.local_densities: ba69a848de421eb5a90097ee3ee9a67498222d566e5670756c744729df67f62b
rank: 4
gram_tensor:
- [0, 2, 0, 0]
- [2, 0, 0, 0]
- [0, 0, 4, -6]
- [0, 0, -6, 12]
signature: [3, 1]
determinant: -48
definiteness: indefinite
dual_gram_tensor:
- [0, 1/2, 0, 0]
- [1/2, 0, 0, 0]
- [0, 0, 1, 1/2]
- [0, 0, 1/2, 1/3]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: even
  level: 6
  modular_scale: false
  discriminant_group: [2, 2, 2, 6]
  overlattice_count: 31
  bad_reduction_primes: [2, 3]
  quadratic_character: -3
  genus_symbol: 'II_{3,1} (2: 2^-4; 3: 1^-3 3^1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  discriminant_form:
    orthogonal_group_order: 240
    isotropic_classes: 6
    isotropic_orbits: 2
  discriminant_orbits:
    Otilde:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    SOtilde:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    Otilde+:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    SOtilde+:
      constant: 6
      z: [0, 1, 0, 11]
      w: [0, 1, 0, 11]
    O:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    O+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
    SO+:
      constant: 2
      z: [0, 1, 0, 2]
      w: [0, 1, 0, 2]
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
      least_valuation: 3
    - representative: 6
      least_valuation: 3
    - representative: 10
      least_valuation: 3
    - representative: 14
      least_valuation: 3
  local_densities:
  - prime: 2
    densities: [0, 0, 0, 5, 0, 0, 0, 5/2, 0, 0, 0, 5]
  - prime: 3
    densities: [4/3, 2/3, 10/9, 4/3, 2/3, 8/9, 4/3, 2/3, 28/27, 4/3, 2/3, 10/9]
automorphisms:
  automorphism_group_order: aleph0
  automorphism_group_generator_morphisms: ['O(L) generator 1 #2', O(L) generator 2, 'O(L) generator 3 #2', 'O(L) generator 4 #2', O(L) generator 5]
indefinite:
  isotropic: true
morphisms:
- target: 6DJH
  name: O(L) generator 1
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, -1, 1]
  scale: 1
- target: 6DJH
  name: O(L) generator 2
  matrix:
  - [1, 0, 0, 0]
  - [-1, 1, 2, -3]
  - [1, 0, -1, 3]
  - [0, 0, 0, 1]
  scale: 1
- target: 6DJH
  name: O(L) generator 3
  matrix:
  - [1, -1, -1, 3]
  - [0, 1, 0, 0]
  - [0, 1, 2, -3]
  - [0, 1, 1, -2]
  scale: 1
- target: 6DJH
  name: O(L) generator 4
  matrix:
  - [0, -1, 0, 0]
  - [-1, 1, 1, 0]
  - [0, 1, 2, -3]
  - [0, 1, 1, -1]
  scale: 1
- target: 6DJH
  name: O(L) generator 5
  matrix:
  - [-1, 0, 0, 0]
  - [0, -1, 0, 0]
  - [0, 0, -1, 0]
  - [0, 0, 0, -1]
  scale: 1
- target: 6DJH
  name: 'O(L) generator 1 #2'
  matrix:
  - [1, 0, 0, 0]
  - [0, 1, 0, 0]
  - [0, 0, 2, -3]
  - [0, 0, 1, -2]
  scale: 1
- target: 6DJH
  name: 'O(L) generator 3 #2'
  matrix:
  - [1, -1, -1, 0]
  - [0, 1, 0, 0]
  - [0, -2, -1, 0]
  - [0, -1, -1, 1]
  scale: 1
- target: 6DJH
  name: 'O(L) generator 4 #2'
  matrix:
  - [0, -1, 0, 0]
  - [-1, 1, 1, -3]
  - [0, -2, -1, 3]
  - [0, -1, -1, 2]
  scale: 1
related:
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 0013, 3ID6.
