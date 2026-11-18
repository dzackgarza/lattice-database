# #43: the index card `gamma-en-2` states is printed by Sterk's Remark 2.12, and is now cited there

The previous turn left one problem open on card 029J, and it was the gate's:

```
/lattices/029J.md: arithmetic group gamma-en-2: the stated index_in_orthogonal_group is not established by a
completed computation certificate
```

`arithmetic-groups/gamma-en-2.md` states `data.index_in_orthogonal_group: 67456`; no certificate named
`029J arithmetic-group.gamma-en-2.index_in_orthogonal_group` existed under `certificates/`; and `certify` cannot
produce one, because `genus.arithmetic_requests` skips a card without a `standard_name` (`src/latticedb/genus.py:293`,
"no owner operation that presents it") while `checks.records.arithmetic_problems` has no such guard
(`src/latticedb/checks/records.py:62`). Both halves arrived together in `35efa5a8ea`. The value itself came in with
the corpus import (`287b70c979`).

## The correction: a source does print it

That turn also wrote that no source states the number, on a search for the digits `67456`. The search was wrong,
because the paper prints the number in factored form. H. Sterk, *Compactifications of the period space of Enriques
surfaces, Part I*, Math. Z. 207 (1991), 1-36, **Remark 2.12, p. 8**:

> It is straightforward to compute the degree of the natural map $\Omega_-/\Gamma \to \Omega_-/O(L_-)$, i.e. the
> index $[O(L_-):\Gamma]$. As the map $O(L_-) \to O(L_-^*/L_-)$ is surjective, see (1.4), we have
> $[O(L_-):\Gamma] = (O(L_-^*/L_-) : \operatorname{Image}(\Gamma \to O(L_-^*/L_-)))$ and by [2], p. 388, we find that
> this last index equals
> $$(2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31)/(2\cdot2^{13}\cdot3^5\cdot5^2\cdot7) = 2^7\cdot17\cdot31,$$

and $2^7\cdot17\cdot31 = 128\cdot527 = 67456$. The page was read as an image (`.scratch/pages/sterk-08.png`), not
from the text layer, which renders the formula as `(221 - 35 9 52 . 7 . 1 7 . 3 1 )/( 2 . 2 1 3 9 35 . 52. 7)": the
text layer's `9` is the multiplication dot and its `221` is $2^{21}$.

The $\Gamma$ of that remark is the group the card describes, not a different one: Sterk's Proposition 2.7, pp. 6-7,
identifies the image in $O(L_-)$ of
$\{g \in O(L) : g\circ I = I\circ g,\ g(e+f, e+f, 0) = (e+f, e+f, 0)\}$ — isometries of the $K3$ lattice commuting
with the Enriques involution and fixing the polarization — with the set of $g \in O(L_-)$ whose induced map on
$L_-^*/L_-$ respects the two-summand decomposition. That is the card's `abstract_structure`, and card 029J's Gram
tensor is $T_{\mathrm{En}} = L_-$.

## What was stored

The value is therefore **cited**, and the certificate's provenance says where:

```
029J arithmetic-group.gamma-en-2.index_in_orthogonal_group:
  hash: 41ae84a7a265c27c7252d0d625ad1b97e07e6db6aafef8552944909736785143
  by: 'H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991),
    1-36, Remark 2.12, p. 8: [O(L_-):Gamma] = (2^21 3^5 5^2 7 17 31)/(2 2^13 3^5 5^2 7) = 2^7 17 31 = 67456,
    Gamma being the image in O(L_-) of the isometries of the K3 lattice that commute with the Enriques
    involution and fix the polarization, identified with the congruence condition of Proposition 2.7,
    pp. 6-7. The number is reproduced by results/certify-43-gamma-en2-index.py, which returns the same index
    from the library (`group.index()`, sage-extensions d667a7c, research ec1333eeb0) on an ambient lattice
    whose Gram tensor is card 029J''s'
```

- `certificates/70.yaml`: one entry added, 11 lines; the group holds 9,422 other entries and is rewritten whole with
  no other change (`git diff --stat` is additions only).
- `lattices/029J.md`: one line added to `certifications`, the hash above. No card value changed.
- `arithmetic-groups/gamma-en-2.md`: the `data.reference.citation` gains one sentence for the index; the card's
  values are untouched and the record validates as an `ArithmeticGroup`.
- `results/certify-43-gamma-en2-index.py`: the computation, in the manner `genus.store_cusp_chambers` and
  `genus.store_cusp_root_orbits` fill the two fields `certify` never asks for — it asserts, before writing, that the
  group's ambient lattice has card 029J's Gram tensor, that the invariant lattice of $I_{\mathrm{En}}$ has exactly
  one polarization mark (so the $h$ the card names is determined), and that the library's index equals the stored
  value. The hash commits to the value and the Gram tensor, not to `by`, so naming the citation did not move it.

## Red, then green

- `tests/test_genus.py::test_the_enriques_group_states_the_index_its_certificate_establishes` fails on the
  pre-change card with exactly the verification message above (`1 failed, 50 deselected in 2.73s`) and passes after
  (`1 passed … in 3.79s`); it now also asserts that the provenance names Remark 2.12, p. 8.
- `pytest tests/test_model.py tests/test_card_merge.py tests/test_cusp_root_orbits.py tests/test_catalogue_schemas.py`
  — **103 passed in 14.69s**, on a full checkout of the worktree.
- `results/verify-43-scoped.py` through the tagged readers `#30` added, on 029J and 6JRR: **107 problems before,
  106 after, and no arithmetic-group problem at all**. The 106 are the references the narrowing removes — 96 + 2
  ambient Lie-group cards and 8 morphism targets, all thirteen present on disk.

## The other red test in that file, and its stale premise

`tests/test_genus.py::test_certification_stores_an_indefinite_card_automorphism_generators` fails on `omm/main`
before this change, and it is not this card's: `1 failed, 50 passed in 95.76s`, with `'automorphism_group_order'`
missing from the set of fields the test expects `genus.requests` to ask for. The cause is a data change, not code:
`8474ec9817` ("certify computed card values (shard 13/16)") certified the order on card 0016, so
`automorphisms.automorphism_group_order: 4` is now stated and its certificate holds, and the field the test meant to
watch being *asked for* is no longer missing. `without` exists for exactly this, and says so in its own docstring:
"a test whose subject is 'a missing field is requested and certified' must create that missing field, or it
silently stops exercising certification". The repair is that field added to the ones the test strips from its own
copy, so the order is asked for and certified again; the values it then asserts (order 4, two generators spanning
$O(U)$) are unchanged. The file is **51 passed in 104.73s** with both changes.

## What was not done

`checks.records.arithmetic_problems` was not relaxed to skip a card without a `standard_name`. Its sibling cannot ask
for that field, but the ledger's rule is that a stated value is cited or certified, and the right repair was to
establish the value rather than to stop reporting it. The three cusped rows are unchanged and still wait on the
owner's class-level decision (sage-extensions#603); `results/evidence-43-603-dependency.md` is that measurement.
