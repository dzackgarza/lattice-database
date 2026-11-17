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
  automorphisms.automorphism_group_generator_morphisms: d06defddc759e07a229ad8d0747b8648e23f229698206ed60f1265cf2f373bee
  integral.discriminant_form: d30873a7b42c0b321512aed99257cbdca3cb441d49cd9b320c90e0ffce0a0363
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
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4, O(L) generator 5]
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
related:
- tag: '0013'
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID6.
- tag: 3ID6
  relation: This presentation is obtained by orthogonal sum of 0013, 3ID6.
---

The selected Gram tensor is obtained by orthogonal sum of 0013, 3ID6.
