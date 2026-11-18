# #43: the three cusped rows on the owner's current `main`, and the one 029J problem the gate does report

Card 029J holds one row of `integral.cusp_root_orbits`: Sterk's (4.3.6), p. 21, at $e'$, one class of $K_J$, one
orbit, hash `2e158f6bf6a8ec4e6276ae3baf3355ae85bdbaf7e12ffaec9441003515479055`. The three rows that do not exist
are (4.3.7) with two root classes of $K_J$, (4.3.8) with two, and (4.3.9) with four; the fifth cusp (4.3.5) has no
root class and so no row. This file records, in one place and against the owner's current `main`, what stands
between those three rows and a value, and the one stored-card problem the repository's own gate reports on 029J
meanwhile. Nothing here writes a value.

## The owner's issues, as they stand today

| issue | state | what it is |
| --- | --- | --- |
| dzackgarza/sage-extensions#312 | **closed**, completed | the group that $\mathrm{Stab}_\Gamma(v)$ induces on $v^\perp/\langle v\rangle$; it supplied `isotropic_vector_reduction_image`, `contains` and the discriminant-side membership test, and no generator family |
| dzackgarza/sage-extensions#459 | closed | the Enriques line stabilizer's generator family did not return |
| dzackgarza/sage-extensions#603 | **open**, filed 2026-11-18T18:27:36Z, blocks 2 | "Certified generators of the stabilizer of a vector in an indefinite lattice" |
| dzackgarza/sage-extensions#72 | open | the inventory of disabled entry points, among them the ambient indefinite vector-equivalence entry point |

#603's acceptance, quoted: "a public call returns, for a primitive vector v of an indefinite lattice L, generators
of Stab_{O(L)}(v) built by the library's own construction, as for lines and planes; on a lattice-database card with
a cited or certified stabilizer (an orbit count of vectors that the stabilizer determines), the call reproduces the
card value."

## The probe, stage by stage

`results/probe-43-dependency-603.py`, run in the pinned image with the owner's `main` `d667a7c` bound over
`/repos/sage-extensions`, at the card's own cusp and its own walls for (4.3.8). Each stage is bounded by its own
alarm, so a stage that does not return is a line in the log and not a lost run.

| stage | what was asked | what came back |
| --- | --- | --- |
| A | the card's row, the reduction image at its cusp, the class-level entry point | built in 3.2 s; **11 wall classes, 2 of them roots of $K_J$** (the card's own numbers); `vectors_are_equivalent` is absent from `IsotropicVectorReductionImage`, at class and instance level |
| B | the family the image acts with | `generators_are_certified_complete()` is `False`; `generation_obstruction()` is the same sentence as before, naming the line; and `generators()` does not return empty — it **raises** `ValueError: the parabolic construction here is stated for a primitive isotropic plane, but Integral lattice of rank 1 and signature (0, 0) has rank 1` (`isotropic_parabolics.py:1836`) |
| C | `Stab_{O(L)}(v)`'s generators, #603's own subject | **returned 27 generators in 7.7 s** (`vector_stabilizer_generators(image.vector())`). The family exists; its own docstring says what it is: for an indefinite lattice "the generators are the apex isometries that the lattice category's marked-diagram decision supplies (`sage-indefinite-port`); they are untrusted engine output" |
| D | the two classes' lifts, under $O(T_{\mathrm{En}})$ and under $\Gamma_{\mathrm{En},2}$ | the ambient witness **returned** (so the two classes are one $O(L)$-orbit, as the card's prose says); the subgroup's call reached `predicate_subgroups.py:600` → `orthogonal_quotients.py:3601` → `:3189 adjust_witness_into_subgroup` → `:234 _double_coset_adjustment` → `libgap.DoubleCoset(...)` membership, and **did not return in 180 s** |

## What stage D changes in the record

The previous turn recorded the subgroup's equivalence as "walks the coset of an infinite stabilizer at
`orthogonal_quotients.py:3403`-`:3423`", killed at 18 min 20 s. Today's traceback says something narrower and more
useful: the ambient witness is found, and the decision then enters `_double_coset_adjustment`
(`orthogonal_quotients.py:234`), a **finite** permutation-group double-coset membership test handed to GAP. So the
work the rows wait on is finite, and it is a libgap algorithm's cost on a permutation group of the finite character
quotient, not an enumeration of an infinite group. That is a library-side matter, in #603 and #72's territory.

For the card, the consequence is unchanged: a class is identified with another by an exhibited isometry, a
singleton component is not a proof of inequivalence, and with `generators_are_certified_complete()` `False` the
three rows stay empty. `genus.applies` refuses the field for exactly this reason (its docstring, now citing #603),
and `latticedb certify` therefore never asks for it.

## The gate

`latticedb verify --shard 0/16` — 029J's shard — is one process that reads the whole corpus: `checks.one_shard`
(`src/latticedb/checks/__init__.py:64`-`:65`) calls `corpus.load(root)` and `certificates.load(root)`, both untagged.
The repository's own measurements put those at 7.29 GiB and 9.08 GiB, and the module's docstring says the same ("the
whole corpus is read, because a claim is checked against the cards it names", `checks/__init__.py:14`-`:16`). This VM
has 15 GB and hosts other sessions' work; the run was started, reached 3.64 GiB peak inside `corpus.load` at 173 s,
and was stopped rather than left to be killed for memory. So the gate's stored-card verification did not run here,
and no green line is claimed for it.

What did run, in the pinned image on this worktree:

- `pytest tests/test_model.py tests/test_card_merge.py tests/test_cusp_root_orbits.py` — **86 passed in 4.18 s**;
- `results/verify-43-scoped.py`, the same checks through the tagged readers `#30` added (`corpus.cards`,
  `certificates.load(tags=...)`), on card 029J and 6JRR.

The scoped run reports 107 problems, 106 of which are the references the narrowing removes and the full corpus
satisfies — 96 `ambient Lie group o-2-10 is not in the corpus`, 2 for `o-2-9`, and 8 `morphism target … is not in the
corpus`, all thirteen cards present on disk. The hundred and seventh is not an artefact:

```
/repo/lattices/029J.md: arithmetic group gamma-en-2: the stated index_in_orthogonal_group is not established by a
completed computation certificate
```

`arithmetic-groups/gamma-en-2.md` states `data.index_in_orthogonal_group: 67456`; no certificate names
`029J arithmetic-group.gamma-en-2.index_in_orthogonal_group` anywhere under `certificates/`, and 029J's
`certifications` block does not either. It cannot be requested either: `genus.arithmetic_requests`
(`src/latticedb/genus.py:293`) skips a card without a `standard_name`, because "a card without a `standard_name`,
such as a named subgroup defined by a source, has no owner operation that presents it", while
`checks.records.arithmetic_problems` (`src/latticedb/checks/records.py:62`) has no such guard and reports the value.
The value is old, from the corpus import (`287b70c979`); it is not the cusp rows' business, but it is a 029J
problem a full `latticedb verify` reports, and it is the one item that stands between this card and the gate's second
acceptance clause. Two repairs exist and they are a data decision, not a code one: establish the number by the
mechanism a cited value uses (a `certificates/*.yaml` entry whose `by` is the source that states
$[O(T_{\mathrm{En}}) : \Gamma_{\mathrm{En},2}]$, with the hash over the value), or drop a value no source here
establishes. Neither was done.

## What is owed

One input, and it is the owner's: an exact decision of two classes of $K_J$ in one $\Gamma_v$-orbit — the
`IsotropicVectorReductionImage.vectors_are_equivalent` the previous turns named, or the finite double-coset
membership in `_double_coset_adjustment` fast enough to answer, or #603's certified family, which turns the
certified-generator walk into a decomposition. Until one of those exists, (4.3.7), (4.3.8) and (4.3.9) have no
value that this repository may write, and the card states no row for them.
