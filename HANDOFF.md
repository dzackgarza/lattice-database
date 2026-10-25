# Handoff: lattice construction corpus

## Ambient task

Populate the lattice database with individual cards for the bounded constructions of known untwisted indecomposable integral lattices. The research preamble owns every lattice construction and mathematical test. This repository owns cards, exact Gram-tensor identity, construction relations, inclusion maps, indices, and persistence.

The requested working range is rank at most 10 and total form scale at most 2. Include canonical orthogonal sums, twists, tensor products, and proper integral overlattices. Store each produced Gram presentation on one permanent card or join an existing card with that exact Gram tensor. Isometric presentations with different Gram tensors can have different cards. Tag allocation must continue beyond four base-36 digits.

The preamble's construction enumeration is unbounded. A database run may select a finite prefix or source set. The indecomposable and untwisted subcategories are property categories; their known objects supply specimens, not the full class.

## Completion condition

1. The preamble supplies the known standard families and property predicates. Every seed used by the corpus passes the untwisted and indecomposable predicates. **Status:** the authoring command checks each seed; verify the full rank-10 family before claiming coverage.
2. The canonical unordered sum family through rank 10 and form content 2 is stored as cards. Each card has a valid defining Gram tensor. Exact duplicate tensors join one card. Every stored construction link has a reciprocal link. **Status:** population is in progress.
3. Tensor products of the known scaled seed presentations, in both factor orders, are stored through the same rank and content bounds. The corpus also stores selected compositions from the preamble's unbounded construction iterator. **Status:** authoring commands exist; live corpus coverage is pending.
4. Proper integral overlattices of the selected seed, tensor, and sum presentations are stored within the bounds. Each computed inclusion is recorded as a morphism on its source card and passes preamble-backed map verification. **Status:** authoring commands exist; live corpus coverage is pending.
5. The whole newly generated family, Gram index, and disk use are validated at one persisted revision. The actual coverage is stated. A finite prefix or run budget does not establish exhaustive closure. **Status:** pending.

Full gluing at rank 10 exceeds the present card layout. For \(U(2)^5\), the discriminant bilinear group is a 10-dimensional symplectic space over \(\mathbb F_2\). Its isotropic subgroup counts by dimension are \(1, 1023, 86955, 782595, 782595, 75735\), obtained by counting ordered isotropic bases and dividing by the number of bases of each subspace. Hence this one source has 1,728,903 proper overlattice inclusions. The current schema stores each inclusion matrix on the source card; the matrices alone would exceed [GitHub's 100 MiB single-object limit](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits). A complete rank-10 gluing corpus needs a storage representation for this family before it can be published. Run budgets give a selected corpus in the current schema.

## Next work, ranked

1. Finish the canonical sum population. Check the complete generated tag interval against the index and schema, and check every new reciprocal construction link.
2. Run the ordered tensor and proper-overlattice authoring commands on the known family. Then sweep the sum and tensor card intervals for proper overlattices, starting at low rank. Record the exact source and inclusion ranges covered.
3. Compare the resulting coverage with the requested rank and content bounds. Extend the corpus while storage permits. Keep the unbounded preamble enumeration available for further deterministic prefixes.
