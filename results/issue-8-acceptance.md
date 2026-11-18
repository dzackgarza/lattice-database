# Issue #8 — acceptance, item by item

Contract: the body and the **Accepted when** clause of dzackgarza/lattice-database#8
(`genus.applies` decides on the database side which owner calls are made). Closed on
`36221922f9`; this record checks the acceptance against the tree at `2d10112a85`/`8654c89ad0`.

Runtime: the pinned research image (`$HOME/sage-image/run.sh`, Python 3.14.10) with
sage-extensions `main` (`8b434511fc`) bound at `/repos/sage-extensions`. The image's baked
checkout is `cf656f8c` and cannot import this tree at all — `src/latticedb/graphs.py:36` dies on
`ImportError: cannot import name 'QQ' from 'sage_extensions.rings'` — so every probe below binds
the current checkout over it.

A dispatched workflow run is not available to this session: the connected GitHub repository is
exposed through an interface that offers PR and issue reads, branch fetch and push, PR creation and
title/body edits, and label changes — no workflow dispatch — so the "dispatched" half of item 1 is
blocked at the tool boundary, not at the code. What runs below is the same entry point a dispatched
job runs, `python -m latticedb certify`, one card, one worker, against a copy of the card so that
the run has something to ask and no corpus card is minted outside a job.

## Item 1 — an indefinite `certify` run requests `primitive_orbits` and the automorphism fields

Smallest input: **U = `lattices/0016.md`**, indefinite, even, rank 2, hyperbolic index 1, with
`integral.primitive_orbits` and `automorphisms.automorphism_group_generator_morphisms` removed
and its `derive` certificate current. Queue read from `genus.requests`, which is what a run works.

    applies(primitive_orbits)        = True
    applies(automorphism_generator)  = True
    applies(automorphism_order)      = False
    stored_in(automorphism_generator)= automorphisms
    stored_in(automorphism_order)    = definite
    requested: ... automorphism_group_generator_morphisms ...
               primitive_orbits[O] primitive_orbits[O+] primitive_orbits[SO] primitive_orbits[SO+]
               primitive_orbits[Otilde] primitive_orbits[Otilde+] primitive_orbits[SOtilde]
               primitive_orbits[SOtilde+]

Where each step is decided:

- `src/latticedb/genus.py:125` `applies` — no definiteness case remains for these fields.
- `src/latticedb/genus.py:276` `stored_in` — the generators of an indefinite card go to
  `automorphisms`, not to `definite`.
- `src/latticedb/genus.py:426` `requests` — an indefinite card's `primitive_orbits` leaves as one
  request per standard subgroup (`orbit_rows_to_ask`, `src/latticedb/genus.py:336`).
- `src/latticedb/sage_genus.py:401` — the worker re-filters the request with the same predicate and
  keeps both.

`automorphism_group_order` is **not** requested on an indefinite card. That is not an owner-domain
guard and not an assumption: it was measured. With the block gate opened by hand so the queue
carries the field (`.scratch/probe8/order_probe.py`, card 0016 with every value certified):

    queue with the gate opened: ['automorphism_group_order', 'roots', 'norms']
    stored_in(order, indefinite) = definite
    0016 {'automorphism_group_generator_morphisms': [[[-1, 0], [0, -1]], [[0, -1], [-1, 0]]]}
    certify returned normally
    card automorphisms block: {'automorphism_group_generator_morphisms': ['O(L) generator 1', 'O(L) generator 2']}
    card certifications has the order: False
    exceeded.yaml: 0016 definite.automorphism_group_order:
      hash: b3827d6184a979b96951484f729460822f3299a93d5aa6fbdcf90b0c70dee9d3
      seconds: 13

The field is requested, the worker answers the generator field of the same computation and no
order, the run ends normally, and the card gains neither a value nor a certificate while
`exceeded.yaml` holds `0016 definite.automorphism_group_order` — a block the card does not have —
for every run that asks it. Three lines make that the only possible outcome:

- `src/latticedb/sage_genus.py:76-80` — `_orthogonal_group_data` serializes no order for an
  indefinite lattice, so the owner never returns one for this field.
- `src/latticedb/invariant_models.py:936` — `Automorphisms` has no order field; `BLOCKS`
  (`src/latticedb/genus.py:58`) files the field under `definite`, and the block gate
  (`src/latticedb/genus.py:179`) therefore rejects it on a card with no `definite` block.
- README.md:255 — "there is no order field to fill", the design this encodes.

**Verdict on item 1:** met for `primitive_orbits` and for the automorphism generators, which is
every automorphism field an indefinite card has a block for. The order is **blocked** with the
evidence above; making it requestable means adding a field (an `aleph0` value, `|O(L)|` infinite
for an indefinite lattice) and an adapter branch, which is a schema decision this issue's Fix does
not authorize ("keep only the database's own facts — a field the schema has no block for").

Probe: `.scratch/probe8/request_probe2.py` (git-ignored).

## Item 2 — the run's log shows the owner's answer or its raise for each

`certify --tag 0016 --minutes 4 --workers 1 --field primitive_orbits` on that copy:

    0016 {'primitive_orbits[O]': {'O': {'constant': 1, 'z': [], 'w': []}}}
    0016 {'primitive_orbits[O+]': {'O+': {'constant': 1, 'z': [], 'w': []}}}
    0016 {'primitive_orbits[Otilde]': {'Otilde': {'constant': 1, 'z': [], 'w': []}}}
    0016 {'primitive_orbits[Otilde+]': {'Otilde+': {'constant': 1, 'z': [], 'w': []}}}
    ArithmeticError: the stabilizer of Integral lattice of rank 1 and signature (0, 0) in
    Orthogonal group O(Integral lattice of rank 2 and signature (1, 1)) has character image of
    order at least 1, and the stabilizer of its divided discriminant data has order 2; no exhibited
    stabilizer element closes the index 2, so the exact image chi(Stab) is not certified
    ChildProcessError: /repo/src/latticedb/sage_genus.py failed on 0016 (exit status 1), ... x4

Four rows answered (constant 1, as the card states), four raised — `SO`, `SO+`, `SOtilde`,
`SOtilde+` — at `sage_extensions/categories/orthogonal_quotients.py:1807`, reached from
`src/latticedb/sage_genus.py:124`. The four raises are the owner's refusal, recorded by the
existing triage as `0016 integral.primitive_orbits[SO+]` … with `disposition: open` in the copy's
`failures/ad.yaml`; the run reports them and exits 1, which is the path
`src/latticedb/genus.py:1132` documents.

`certify --tag 0016 --minutes 3 --workers 1 --field automorphism_group_generator_morphisms` on a
fresh copy:

    0016 {'automorphism_group_generator_morphisms': [[[-1, 0], [0, -1]], [[0, -1], [-1, 0]]]}

exit 0. The copy's card then states the two generators by name and certifies them under
`automorphisms.automorphism_group_generator_morphisms` with hash
`32f92a52697d25f697c5c1e7deb04e354f078d4c5ca12a9c56476f4fa8eeda0e`, the hash the corpus card
already carries.

So for each field the run asks on an indefinite card, the log shows the owner's answer or its
raise. Both runs were repeated in a later session on fresh copies with identical results
(`.scratch/probe8/run-orbit-2.log`, `.scratch/probe8/run-gen-2.log`), which is the pair of logs
this record stands on; the first pair is `.scratch/probe8/run-orbit-clean.log` and
`.scratch/probe8/run-generators.log`. The one field whose log shows neither an answer nor a raise
is `automorphism_group_order`, and item 1 records what it shows instead: `exceeded.yaml`.

## Item 3 — the predicate test is replaced by one that asserts the request

`tests/test_genus.py:198` `test_the_database_asks_the_owner_on_every_card_of_the_operations_class`
asserted `genus.applies(...)` for `definite`-block fields on the indefinite card — including
`assert not genus.applies("automorphism_group_order", indefinite)` and
`assert not genus.applies("regular", indefinite)` — and is replaced by:

- `tests/test_genus.py:199` `test_an_indefinite_card_requests_its_orbit_rows_and_its_automorphism_generators`
  — asserts on `genus.requests` that the indefinite card's queue carries
  `automorphism_group_generator_morphisms` and all eight `primitive_orbits[...]` rows, and that
  `regular` and `automorphism_group_order` are absent.
- `tests/test_genus.py:229` `test_a_field_is_withheld_by_its_block_and_by_the_domain_the_owner_states`
  — the filters the code still keeps, asserted where they live.

The new test is sensitive to the defect: with `applies` restored to its pre-#8 answer
(`False` for those two fields on a card with no `definite` block) the queue carries **no**
`primitive_orbits[...]` row and no generator field, so the test fails. Probe:
`.scratch/probe8/red_probe.py`.

Test runs: `python -m pytest tests/test_genus.py -q` in the image, twice —

    49 passed in 213.10s (0:03:33)
    49 passed in 529.48s (0:08:49)   # same suite, run alongside other sessions' jobs

including `tests/test_genus.py:586` `test_certification_stores_an_indefinite_card_automorphism_generators`,
which runs `certify` for the generator field on a copy of U and checks that the stored generators are
isometries spanning a group of order $|O(U)| = 4$.

No `applies` assertion for a `definite`-block field on an indefinite card survives anywhere in
`tests/`: the remaining ones (`tests/test_genus.py:239-253`, `:260`) are on the definite card, on
`integral`- or `root_span`-block fields, or on a card with no `integral` block.

## Left undone, and why

The body's **Fix** also says to delete the domain cases from `applies`, not only the definiteness
cases. Five of them remain, each answering from the owner's stated domain:

- `src/latticedb/genus.py:200-203` rank ≥ 3 for `reflective`, `spinor_regular`, `spinor_genus_count`, `spinor_genera`
- `src/latticedb/genus.py:204-207` rank ≥ 2 for `siegel_eisenstein_coefficients`
- `src/latticedb/genus.py:208-209` a definite even card for `discriminant_sequence`
- `src/latticedb/genus.py:210-211` an even card of hyperbolic index ≥ 2 for `discriminant_orbits`
- `src/latticedb/genus.py:191-199` `|det L| ≤ 4096` for `discriminant_form`

They are not touched here: no acceptance item asks for them, and deleting them makes every
rank-2 card raise four owner errors per run (the failure `36221922f9` was written to repair, and
the four raises above show what a raise costs a worker). Removing them is a corpus-wide cost change
that wants a measured run, not a silent edit.
