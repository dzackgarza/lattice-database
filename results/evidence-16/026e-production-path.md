# 026E's missing `integral.primitive_orbits`: what the production path does now

#16. Measurements only; no code, card or certificate changed. Every claim below names how it was
established, so it can be re-checked rather than believed.

## 1. The request is built and it is in the fields phase

`genus.requests(corpus, certificates, exceeded, ("026E",))` on a one-card corpus holding 026E and
its own certificate shard (`certificates/f1.yaml`) prints

    tag: 026E | fields: ['primitive_orbits'] | searches marker: False | integral: True | series_bound: 8
    tag: 026E | fields: ['roots', 'norms']     | searches marker: True  | integral: True | series_bound: 8
    phase fields   -> ["026E:['primitive_orbits']"]
    phase searches -> ["026E:['roots', 'norms']"]
    applies(primitive_orbits) = True
    026E signature/det: (1, 6) 8 definiteness: indefinite

So `certify.yml`, which runs `--phase fields`, does ask for `primitive_orbits`: it is not skipped by
the phase split. `primitive_orbits` is not in `genus.SEMI_DECISIONS`. The card is indefinite,
signature (1, 6). Its other requested fields are already certified, so this is the only request the
card makes.

## 2. The real production path fails before any serialization, in 0.27 s

`/sage/.venv/bin/latticedb certify --tag 026E --phase fields --minutes 20 --workers 1 --root <that
corpus>` in the published image, with the owner library imported from `/repos/sage-extensions` at
`7b222e8621`:

    ValueError: primitive bounded orbit series requires a definite lattice,
                not Integral lattice of rank 7 and signature (1, 6)
      sage_genus.py:332 <lambda> -> sage_genus.py:207 _orbit_series(lattice.primitive_orbit_series())
      sage_extensions/categories/lattices.py:3305 primitive_orbit_series
      sage_extensions/categories/lattice_orbit_invariants.py:136

`results/evidence-16/production-request-026E.log` is that run; `recorded-failure-026E.yaml` is the
entry `certify` wrote into the failure ledger through `failures.save` -- the same machinery CI uses,
with `run_url: null` because it did not run in CI. The attempt hash `b2c2caa2...` equals the one in
`failures/f1.yaml` because the hash is of the input, not of the result.

There is no value, so no count, so nothing to convert and nothing to serialize. At this owner
revision the emitter cannot be either exercised or refuted.

## 3. The image's attribution to "worker serialisation" has no referent in the source

`results/026e-and-corpus-failures.md` at `dzackgarza/sage@087adc21` says the emitter does convert the
constant and that "the worker serialises the provider's raw value to JSON on the way back", making
the defect the worker's rather than the emitter's. Reading the source:

- `src/latticedb/sage_genus.py` has exactly three `json.dumps` calls: `_start` (a list of field
  names), `_emit` (the computed values), and the final `{"tag": ..., "done": true}`.
- `_run` calls `_emit(tag, values)` with `values = compute()`, and `compute()` is the lambda
  `{field: SERIES[field](...) if field in SERIES else VALUES[field](lattice)}`.
- `VALUES["primitive_orbits"]` is `lambda lattice: _orbit_series(lattice.primitive_orbit_series())`.

So the only value that reaches `json.dumps` is the one the emitter returned. There is no second
serialization of a raw provider value, and no place for one. The ledger's traceback at database
`78ef8ce628` is fully explained by `VALUES["primitive_orbits"]` being unwrapped at that revision:
the same frame chain ends at `_emit` -> `json.dumps` on the owner's own series. `git log -S
"_orbit_series" -- src/latticedb/sage_genus.py` gives `c3b3db0db2` as the commit that wraps it, so
the wrapping is the fix for that error and it is in the emitter, which is where the image says the
defect is not.

Whether `_orbit_count`'s `aleph0` branch is the right contract is untouched by all this: it has
still never run on a real owner answer, at this or any revision available here.

## 4. Why the ledger entry, the current source and a green workflow cannot be reconciled

`primitive_orbit_series` requires a definite lattice at all three owner revisions on hand:
`49b401659a`, `240cd3f845fe` and the pinned `7b222e8621`. A run that recorded
`Cardinalities.parent_class` for an indefinite card therefore used owner code that admitted
indefinite lattices, and that code is not any of these.

Production does not pin the owner library. `research/pyproject.toml` declares

    "sage-extensions @ git+https://github.com/dzackgarza/sage-extensions",

with no ref, and `.github/actions/sage/action.yml` installs it with `uv pip install --requirements
research/pyproject.toml`. Every run therefore resolves whatever the default branch holds at that
moment. `LATTICEDB_RESEARCH_REVISION`, recorded in the ledger, pins `dzackgarza/research` and not the
owner library -- so the ledger cannot say which owner code produced any given entry, and two runs can
legitimately disagree.

## 5. Scale: this is not one card

Of the corpus's 219 indefinite cards (`definiteness: indefinite`, nonzero determinant), 206 have no
`primitive_orbits` row. Each of them is in 026E's position: the database asks, and the owner refuses.
The ledger shows only the handful that a run has reached, because the runs have been ending early.

## 6. The decision this needs

Two consistent ways out, and the choice is the owner's:

- Narrow the request to the owner's stated domain, as `genus.applies` already claims to do ("a card
  outside a domain gets no field rather than a failure queued every run"). `primitive_orbits` would
  then be asked only on definite cards. This contradicts #8's stated goal of asking it on indefinite
  cards and flips the assertion `genus.applies("primitive_orbits", indefinite)` in
  `tests/test_genus.py`.
- Keep asking, and have `primitive_orbit_series` admit indefinite lattices on sage-extensions --
  then pin the owner revision, so that the answer can be reproduced and the ledger can say what
  computed it.

No code is changed for either. The missing value is real and cannot be produced from any owner
revision on hand.
