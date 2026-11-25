# #34: 6JRR's `certifications` block and 0012's generator morphisms in `test_catalogue_schemas`

At `1224b1b184` (and with the source before it) `tests/test_catalogue_schemas.py` was 17 passed, 2
failed. Both failures are rules in the test that outran the cards, not claims on the cards that
contradict a certificate. The evidence below is the reason neither card's value and neither
certificate was touched.

## 0012's generator morphisms: both are isometries, and the row is the certificate's value

The card states `definite.automorphism_group_generator_morphisms: ['O(L) generator 1', 'O(L) generator 2']`
and the two morphisms it names are

    O(L) generator 1: [[0, 1], [1, 0]]        O(L) generator 2: [[1, 0], [1, -1]]

`genus.certified_value` commits to the *matrices* of the named scale-1 self-morphisms, sorted, not to
their names. Recomputing that value from the card's Gram tensor `[[2, -1], [-1, 2]]` gives

    [[[0, 1], [1, 0]], [[1, 0], [1, -1]]]

whose SHA-256, in `certificates.certification_hash`'s own JSON, is

    9eccb879b3f91766bebe1d7c7693ae2de7d5a44802809520e36438621a1f0cc6

— the hash the card cites and the hash `certificates/2f.yaml` holds. Each matrix satisfies
$M^{T} G M = G$, and the two generate a group of order 12, which is the card's own
`definite.automorphism_group_order`. So there is no generator morphism that contradicts a certificate.

The reported problem was the fixture's: the test copies 0012 into `tmp_path` and never gives that
corpus a `certificates/` directory, so `checks.report` holds no certificate at all and reports every
cited value of 0012 — twenty of them — as contradicting one. The fix is in the fixture
(`tests/test_catalogue_schemas.py` writes 0012's certificate shard into the copy), and the test then
also asserts what it means: no certificate problem at all, and no problem mentioning a generator.

## 6JRR's `certifications` block: a certified value the schema allows

6JRR states

    certifications:
      integral.discriminant_form: 0be391409303d25f25d126795ee881040661b4883ad7473272b34b60b8c414da
    integral:
      parity: even
      discriminant_form:
        orthogonal_group_order: 46998591897600
        isotropic_classes: 528
        isotropic_orbits: 2

`certificates/e1.yaml` holds that hash with `by: research preamble`, and the card's value hashes to it:
`records.problems` on the card, with its shard loaded, reports nothing. The schema documents the
`certifications` map (`README`, "Certifications"; `model.py`), and `genus.applies` admits
`integral.discriminant_form` on 6JRR — an even card with `|det| = 2048 ≤ 4096`. So the card states a
value the schema lets it state and certifies it; the test's `assert "certifications" not in card` was a
snapshot of a card that had not been certified yet, and `set(card["integral"]) == {"parity"}` with it.

The test now states the rule that holds in either case: every field of the card beyond its defining
data (`integral.parity`, `indefinite.isotropic`) is one it certifies, every certificate names a stated
field, and the blocks #7 leaves to `certify` and to sage-extensions#286 (`definite`, `root_span`,
`root_sublattice`, `morphisms`) are still absent. It cannot pass by the card losing a value, and it does
not break when the next field is certified.

## What was checked about 6JRR's value, and what was not

6JRR's `isotropic_classes = 528` is exact: with $q_L(x) = b(x,x)/2$ and every class of $A_L$ enumerated
from the rows of $G^{-1}$ (2048 classes of $(\mathbb{Z}/2)^{11}$), exactly 528 have $q_L = 0$. 029J's
1024 classes give 528 as well, so the identical count on the two cards is a fact of the two forms and
not a copy.

`orthogonal_group_order = 46998591897600` is the same number on 029J, whose $A_L$ is
$(\mathbb{Z}/2)^{10}$ and not $(\mathbb{Z}/2)^{11}$; that is worth an owner's eye. It was not
recomputed here: `lattice.discriminant_quadratic_form().orthogonal_group().order()`, the adapter's own
call, had not finished after 28 minutes on this 15 GiB VM, so no comparison is stated. A certified value
was not changed on suspicion: the certificate commits to the value (`certificates.certification_hash`
hashes name, Gram tensor and result), so it proves what the preamble returned, not that a hand-written
number is right, and replacing one requires the owner's computation, not a guess.

## Gate

`tests/test_catalogue_schemas.py`: 17 passed. `just test` (`tests/test_model.py`,
`tests/test_card_merge.py`): 71 passed, in the research image, `/sage/.venv/bin/python` 3.14.10.
