---
tag: 3GDM
name: watson 3:533
latex: watson 3:533
aliases: []
certifications:
  definite.regular: 5b08c89ace15d3e6bcea1e2e6f24114e1ce3b88d6849ed1d333995ae92d090b1
  definite.spinor_regular: 0009982922c9aa8847b44b21ec24b6ac1b36ab04e516ef9c6da8f01f17fd60e9
  derive: 9d9fabacc3e0fc755b581961a9cba3a239dd4cadd987eac4172c1c7079367745
  form.integer_valued: 8ce81c4c1fc28aa7a0e13adae19762fa2132ca0ccde1ee11073d38765837b512
  integral.elementary_primes: 011d7da817cda8a6172e242354562666ef89e1fd48d1b640e7e99a1c9f6efb07
  integral.genus_symbol: 6d562ba846a11c897bec13ef146680076e51f5320262cea6499cddd0b0e10d85
  integral.genus_class_count: ab5f94fdc3ea011b160ccfd48dda243891e25ade0ac2ef9972a308d92b096b7d
  integral.overlattice_count: 5edab0c7bff9a8a28d2da09900a6db72a0f7458630a4dd92dfd74dffd158e4b8
  integral.spinor_genus_count: e31eade7fbbf1b06e0dd2d80e41f75410c23f701f519dfeb392e35bb45439161
  integral.spinor_genera: 6ecad89506b5172a999457714425e862516c74192b6b61f8f17633a175e48843
  integral.hyperbolic_index: 71aeb90745948dadd3290eac570c68d31994f552490031721653061eb4d31b6a
  definite.automorphism_group_order: 37eb25a743014b03622f4dc92d60ec560d710b33243941391abce916521d27e2
  definite.automorphism_group_generator_morphisms: 98f863877e6ffc9ec2018579899c3ed760ae5a65ab48eb8936efef7933442f04
  integral.primitive_orbits: 58724d96e2d16a6ecdca9cb87a1c80b4bf6e4187caf639c21dbf7b5d3688f6b0
  integral.modular_scale: 8aa5b2bbfce610eecc6871675c33968fa74d8f83ae7abd6dd178b5cd97465ead
  definite.genus_theta_series: 2770bbc2286d1619a0adc0b0b3bafac0a7b8497d3c9591835397ceb53fd0b45d
  definite.theta_series_cuspidal_component: d33cb652eff4effc54403d2aa9e48b4b0dc845366607ecc732f343c257ace32a
  definite.siegel_eisenstein_coefficients: 136954d2118894d2c18ba0b5776f6e0a717104a614ab9d887767834ea5ad8c64
  integral.anisotropic_primes: e8cd13291faa010ef5ebfe809578113e4040bd6ac207ac795381c75f368b6a86
  integral.local_representations: 92662fa035f60252d0c805dc2f32e16622730aedfa47952892a6a88b129def8b
  integral.local_densities: 568be75d11611e735b795e9ee2939f3c2fa7483c5c5e4edcd3a112df5a422101
rank: 3
gram_tensor:
- [3, 1, 1]
- [1, 11, -5]
- [1, -5, 27]
signature: [3, 0]
determinant: 768
definiteness: positive_definite
dual_gram_tensor:
- [17/48, -1/24, -1/48]
- [-1/24, 5/48, 1/48]
- [-1/48, 1/48, 1/24]
form:
  integer_valued: true
integral:
  elementary_primes: []
  parity: odd
  level: 96
  modular_scale: false
  discriminant_group: [16, 48]
  overlattice_count: 15
  bad_reduction_primes: [2, 3]
  genus_symbol: 'I_{3,0} (2: [1^-1]_3:[16^2]_6; 3: 1^-2 3^-1)'
  genus_class_count: 1
  spinor_genus_count: 1
  spinor_genera: [1]
  hyperbolic_index: 0
  primitive_orbits:
    O:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    SO:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    Otilde:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
    SOtilde:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
    O+:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    SO+:
      constant: 0
      z: [0, 0, 1, 0]
      w: [0, 0, 0, 0]
    Otilde+:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
    SOtilde+:
      constant: 0
      z: [0, 0, 2, 0]
      w: [0, 0, 0, 0]
  anisotropic_primes: [2]
  local_representations:
  - prime: 2
    classes:
    - representative: 1
      least_valuation: 4
    - representative: 3
      least_valuation: 0
    - representative: 7
      least_valuation: 2
    - representative: 2
      least_valuation: 5
    - representative: 6
      least_valuation: 5
    - representative: 10
      least_valuation: 5
    - representative: 14
      least_valuation: 5
  local_densities:
  - prime: 2
    densities: [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 4]
  - prime: 3
    densities: [2/3, 2/3, 4/3, 2/3, 2/3, 2, 2/3, 2/3, 14/9, 2/3, 2/3, 4/3]
definite:
  minimum: 3
  kissing_number: 2
  automorphism_group_order: 4
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2]
  minimal_vectors:
  - [-1, 0, 0]
  - [1, 0, 0]
  perfect: false
  regular: true
  spinor_regular: true
  theta_series: [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 4]
  genus_theta_series: [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 4]
  theta_series_cuspidal_component: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  siegel_eisenstein_coefficients: [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 4]
  root_system: []
  roots:
  - type: A1
    scale: 48
    simple_roots:
    - [1, -1, -2]
root_sublattice:
  invariant_factors: [1]
morphisms:
- target: 3GDM
  name: O(L) generator 1
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
- target: 3GDM
  name: O(L) generator 2
  matrix:
  - [1, 0, 1]
  - [0, 1, -1]
  - [0, 0, -1]
  scale: 1
families: []
related: []
references:
- citation: Watson, primitive lattices of class number one, 3:533.
  url: https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 356, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
- citation: 'W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341, form 356, as tabulated in A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2; regular by W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341; hence spinor regular, since a form is spinor regular if it represents all the positive integers represented by its spinor genus (A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018), Abstract) and the spinor genus lies in the genus.'
  url: https://math.colgate.edu/~integers/t45/t45.pdf
---

Source entry `watson:3:533` gives this Gram tensor.
