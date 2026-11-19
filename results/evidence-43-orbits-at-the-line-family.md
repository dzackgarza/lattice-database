# #43: the three cusped rows, decided by the chamber's own symmetry

Card 029J now states all four cusps it can decide: (4.3.6) with one root class, and (4.3.7), (4.3.8), (4.3.9) with
two, two and four, each **one orbit**. This file records how, what the earlier readings had missed, and the two
measurements that stand behind it.

## What decides it

Sterk prints the chamber at each cusp together with its Coxeter diagram, and states that the diagram's symmetry is
realized **inside the cusp stabilizer**:

- (4.3.7), p. 22: "It can be checked that the symmetry of the diagram comes from an element in $\Gamma_v$ (see
  (4.3.10)). We find $G_v = \{\pm1\}W_v \rtimes \mathbb{Z}/2$."
- (4.3.8), p. 23: "and the symmetry is induced by an element of $\Gamma_v$ (see (4.3.10))."
- (4.3.9), p. 24: "Symmetries of the graph can be lifted to $\Gamma_v$ (see (4.3.10))."

An element of $\Gamma_v$ that carries one wall of the chamber to another carries the first wall's root class in
$K_J = v^\perp/\mathbb{Z}v$ to the second's, which is exactly the identification a row states. Read as page images
(pp. 22 and 24) as well as text, because the two sentences are one line each and the text layer is an OCR of a scan.

The symmetry is computed from the card's own Gram tensor --- the walls' squares and their pairings --- by
`results/store-43-cusp-orbits.py`:

| row | walls | root walls | symmetries of the diagram | orbits of the root walls |
| --- | --- | --- | --- | --- |
| (4.3.7), p. 22 | 12 | $\alpha_9$, $\alpha_{13}$ | 2 | one, exchanging them |
| (4.3.8), p. 23 | 11 | $\alpha_9$, $\alpha_{11}$ | 2 | one, exchanging them |
| (4.3.9), p. 24 | 14 | $\alpha_{11}$, $\alpha_{12}$, $\alpha_{13}$, $\alpha_{14}$ | 8 | one, transitive |

The computed orders agree with Sterk's own count of the symmetries where he states one, which is what ties the card's
transcription of the walls to the printed diagram: at (4.3.5) he writes $S_e \cong \mathbb{Z}/2 \times \mathbb{Z}/2$
and the computation gives 4; at (4.3.6) he writes "As there are no symmetries" and it gives 1; at (4.3.7)
$G_v = \{\pm1\}W_v \rtimes \mathbb{Z}/2$ and it gives 2. `tests/test_cusp_root_orbits.py`
`test_the_three_cusped_rows_are_one_orbit_because_the_chamber_is_symmetric` recomputes all of it from the shipped card.

Stored through `genus.store_cusp_root_orbits`, which certifies the whole field: hash
`1491eec6cdfb74d658ea0afe48e1d44637d55068cdf1460e23ae5239fafd709f`, provenance naming Sterk's three statements
and the program. `transporter_order` is the number of classes the exhibited symmetry carries the representative to,
one per class, as the model defines it for a proof by exhibited transporters.

## Why the earlier readings did not find it

The chamber Sterk prints is a fundamental chamber for the **reflection subgroup** $W_v$, not for all of $G_v$ --- his
own words at (4.3.5), p. 19: "The diagram of the reflection group $W_e \subset G_e$ is as follows", and Alexeev et al.
state the same object for the folded diagrams, Corollary 3.12, p. 595: "the Coxeter diagrams for the reflection groups
$W(\Gamma_{En,2,e})$". So the reflections in the chamber's walls cannot move a root class to another, which is what
the earlier turns measured: the root walls' orthogonal neighbour sets differ pairwise, so no word in $W_v$ carries one
to the other. The identification lies in the finite part $\{\pm1\} \rtimes S_v$ that $W_v$ is extended by, and it is
what the diagram's symmetry supplies.

Two further measurements at sage-extensions `41b75d7`, for the record:

- the library's own line-stabilizer family (26, 28 and 23 members at the three cusps) moves no root class either, and
  neither does the part of it the exact membership test puts in $\Gamma_v$ (25, 13 and 20 members): components of
  sizes 2, 2 and 4, one class each, at every row
  (`results/probe-43-stabilizer-orbits.py`, `results/probe-43-line-family.py`). `generation_obstruction()` still
  refuses to certify that family as complete at a primitive isotropic line, so those walks decide nothing on their
  own --- they are consistent with the rows above, not a second proof of them;
- $O(K_J)$ reports a selected generating resolution of its own ($23$ generators, 5.7 s,
  `results/probe-43-okj-generators.py`), so the chain the line family is built from is library-owned end to end.

## What is still open

Nothing on this card's rows. The library's class-level operation (`IsotropicVectorReductionImage.vectors_are_equivalent`)
remains absent and `generation_obstruction()` still refuses at a line; those matter to a *search* for such orbits, not
to these four rows, which the chamber's printed symmetry decides.
