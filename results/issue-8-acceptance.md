# Issue #8 — acceptance, item by item

Contract: the body and the **Accepted when** clause of dzackgarza/lattice-database#8
(`genus.applies` decides on the database side which owner calls are made). Closed on
`36221922f9`; this record checks the acceptance against the tree at `2d10112a85`/`8654c89ad0`.

Runtime: the pinned research image (`$HOME/sage-image/run.sh`, Python 3.14.10) with
sage-extensions `main` (`8b434511fc`) bound at `/repos/sage-extensions`. The image's baked
checkout is `cf656f8c` and cannot import this tree at all — `src/latticedb/graphs.py:36` dies on
`ImportError: cannot import name 'QQ' from 'sage_extensions.rings'` — so every probe below binds
the current checkout over it.

A dispatched workflow run is not available to this session (the GitHub connection carries no
`workflows` permission). The run below is the same entry point a dispatched job runs,
`python -m latticedb certify`, one card, one worker, against a copy of the card so that the run
has something to ask and no corpus card is minted outside a job.

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

`automorphism_group_order` is **not** requested on an indefinite card, and the reason is the
schema, not an owner domain: `BLOCKS` files it under `definite` (`src/latticedb/genus.py:58`), the
block gate rejects a card with no `definite` block (`src/latticedb/genus.py:179`), `Automorphisms`
holds the generators alone (`src/latticedb/invariant_models.py:936`), the adapter serializes no
order for an indefinite lattice (`src/latticedb/sage_genus.py:70`), and README.md:255 states that
there is no order field to fill. Read as "the automorphism fields this card can hold", item 1 is
met for the generators; read as "order as well", it is not, and cannot be without adding a field
the documentation says the schema does not have.

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
raise. Logs: `.scratch/probe8/run-orbit-clean.log`, `.scratch/probe8/run-generators.log`.

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

Test run: `python -m pytest tests/test_genus.py -q` in the image —

    49 passed in 213.10s (0:03:33)

including `tests/test_genus.py:586` `test_certification_stores_an_indefinite_card_automorphism_generators`,
which runs `certify` for the generator field on a copy of U and checks that the stored generators are
isometries spanning a group of order $|O(U)| = 4$.

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
