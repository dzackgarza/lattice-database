---
tag: 3IEU
name: Constructed lattice 3IEU
latex: L_{\mathrm{3IEU}}
certifications:
  derive: 2e127fa40424820dbf79b24bcd8593c37020bff24a59cb08a190e57cb6ea9f62
  form.integer_valued: 2b747b4e83a1768d3020597dfbcccd6ba06b4c46ce53abea48ef5b6715e0d41a
  integral.elementary_primes: 1011f878d257073bdd297a1114f482bd71faee724b226eba6fb1b519a843dfcc
  integral.genus_symbol: 9065aebdcd4fdb28c0f931e3089bb0c69bbef0c9948bc4fc307539813a84cdf5
  integral.genus_class_count: bbbffc39b6470e822b6252c5d390a38f3fd08fcff2a4af5cb239f7d2c433fe56
  integral.overlattice_count: 4c7d2f4a1f3b388e6bc009f5b9071c81de494b8c5895ae0478f85da746df70f7
  integral.spinor_genus_count: 1187052cf2ccaf9f697bd77ce42464dfe65fa12f5bae25384ac12f9a3efa0939
  integral.spinor_genera: 8344329e95604237fb4fe2e528b65f613913addd69b07be84641fb7a1772b529
  integral.hyperbolic_index: c97fc615fc8909fe1f02b691d04a83958563390e533f503db5d9c692aff650ba
  automorphisms.automorphism_group_generator_morphisms: 2f3943e8aa66f68d481b250bdbbda92c68a0ce2c8e125496671426aa3f52281e
  integral.discriminant_form: cd4d7df4374433c363c053ff58331bd2fa2e78f53fe0c87b53021bd93fb1d015
  integral.primitive_orbits: 3d82c7a7dd20a92f2e70c1f13f531b9955babed5401829451f195e34dbe081d3
  integral.modular_scale: 9989284968e10c4d55cce030f368cdee7f66ebafae7e838658093c80fe62a3bd
  integral.anisotropic_primes: d05ea55c4e0135c763285590dd0e9b7281316db5e6b559954fee0cd0c17524bc
  integral.local_representations: 12e1978a628023df13a2017d40c8a5ec76aee6c1fca547ef5bdad5085fd75202
  integral.local_densities: 223c7c19d32e3d878204f6b8546267c6eb0258a0d11912253aecab8e04b65abe
rank: 3
gram_tensor:
- [-2, 0, 0]
- [0, 0, -1]
- [0, -1, 0]
signature: [1, 2]
determinant: 2
definiteness: indefinite
dual_gram_tensor:
- [-1/2, 0, 0]
- [0, 0, -1]
- [0, -1, 0]
form:
  integer_valued: true
integral:
  elementary_primes: [2]
  parity: even
  level: 4
  modular_scale: false
  discriminant_group: [2]
  overlattice_count: 1
  delta: 1
  bad_reduction_primes: [2]
  genus_symbol: 'II_{1,2} (2: 1^2 [2^1]_7)'
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
      constant: 1
      z: []
      w: []
  discriminant_form:
    orthogonal_group_order: 1
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
    densities: [0, 3/2, 0, 3/2, 0, 2, 0, 9/4, 0, 3/2, 0, 3/2]
automorphisms:
  automorphism_group_generator_morphisms: [O(L) generator 1, O(L) generator 2, O(L) generator 3, O(L) generator 4]
indefinite:
  isotropic: true
morphisms:
- target: 3IEU
  name: O(L) generator 1
  matrix:
  - [-1, 0, -1]
  - [-2, 1, -1]
  - [0, 0, 1]
  scale: 1
- target: 3IEU
  name: O(L) generator 2
  matrix:
  - [-1, 1, 0]
  - [0, 1, 0]
  - [2, -1, 1]
  scale: 1
- target: 3IEU
  name: O(L) generator 3
  matrix:
  - [1, 0, 1]
  - [-2, 1, -1]
  - [0, 0, 1]
  scale: 1
- target: 3IEU
  name: O(L) generator 4
  matrix:
  - [-1, 0, 0]
  - [0, -1, 0]
  - [0, 0, -1]
  scale: 1
related:
- tag: 3ICX
  relation: This presentation is obtained by orthogonal sum of 3ICX, 3ICY.
- tag: 3ICY
  relation: This presentation is obtained by orthogonal sum of 3ICX, 3ICY.
---

The selected Gram tensor is obtained by orthogonal sum of 3ICX, 3ICY.
