# The reason `029J`'s cusp rows wait (#43 → sage-extensions#312)

Text prepared for sage-extensions#312; it is **not posted** (this agent's GitHub connection reads the lattice
repository and cannot comment on another repository's issues).

---

`dzackgarza/lattice-database` #43 asks card `029J` to carry, per Sterk cusp under `gamma-en-2`, the orbits of the
cusp's root classes in $K_J = \eta^\perp/\mathbb{Z}\eta$ under the cusp stabilizer, with the count, one
representative per orbit, and the order of the transporter group. The field is on the card
(`integral.cusp_root_orbits`, keyed by the eight standard subgroups as `integral.primitive_orbits` is); the values
are not, and this issue is the reason.

`generation_obstruction()` at a primitive isotropic line reports that the parabolic's constructed generator family
is stated for a primitive isotropic plane and refuses rank one, and that the port's line stabilizer is not a
computational route at Sterk's first Enriques cusp. With the acting family incomplete, `root_class_orbits` returns
identifications: at `029J`'s fourth cusp (Sterk (4.3.8), p. 23) it returned two components of one class each, and a
component of one class is no proof of inequivalence, as its docstring says.

We tried the way round that avoids the missing generators: separate the root classes by an invariant of $O(K_J)$,
the largest group that acts, since $\Gamma_v \subseteq O(K_J)$ and an invariant of the larger group is a lower bound
for the count. For a primitive root $r$ of square $-2$, $K_J = \langle r\rangle \perp r^\perp$ orthogonally, so
$r_1$ and $r_2$ are $O(K_J)$-equivalent iff $r_1^\perp \cong r_2^\perp$; the complements are even 2-elementary of
rank 9 and determinant $\pm 2^9$, each genus a single symbol `[2^9]_1` with one class. **Every root class of every
cusped row is $O(K_J)$-equivalent to every other** --- at (4.3.7) two, at (4.3.8) two, at (4.3.9) four --- so the
whole of $O(K_J)$ acts in one orbit on each row's family, and no invariant of any group containing $\Gamma_v$ can
separate two classes there.

What is left is the index of $\Gamma_v$'s image in $O(K_J)$, which is exactly what a generating family of
$\Gamma_v$ at a primitive isotropic line would supply. Until that exists, `029J`'s four cusped rows cannot be
filled from a computation, and the count of $\Gamma_v$-orbits at (4.3.8) is known only to be 1 or 2.

Evidence: `dzackgarza/lattice-database`, `results/evidence-43-okj-complement.md`,
`results/probe-43-okj-complement-invariant.py` and `results/evidence-43-okj-complement.log`.
