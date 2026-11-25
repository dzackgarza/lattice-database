# #29: the certify queue asks A2 for fields the owner defines elsewhere

Run `44304988129` (`workflow_dispatch`, head `0ab2ba44`) failed its suite step on three tests and its
step 9 on a checkout. The three tests are one mechanism, and it is the queue.

## The one mechanism

`A2` (card `0012`, rank 2, definite) is asked for the three spinor fields and for the
discriminant-group series. The owner defines the spinor fields at rank at least three and refuses a
rank-2 card by raising, and a raise ends the worker holding the card:

    AssertionError: the spinor-genus count of Genus of even integral lattices of signature (2, 0) and
    determinant 3 is taken here in rank at least three, and the rank is 2
    AssertionError: spinor genera of Integral lattice of rank 2 and signature (2, 0) require a
    nondegenerate lattice of finite rank at least three        (also reached by is_spinor_regular)

`genus.certify` records the refusal and raises `ChildProcessError` when the queue is done, so the run
the test started ends as an exception rather than as a verdict:

| test | where it stops | what it reads |
| --- | --- | --- |
| `test_failures.py::test_successful_retry_computes_and_resolves_its_failure:147` | `genus.certify` | `ChildProcessError: … failed on 0012 (exit status 1)` ×3 |
| `test_certify_process.py::test_a_search_that_never_ends_does_not_hold_back_other_cards:132` | `genus.certify` | the same, on `0016` and `0012` |
| `test_certify_process.py::test_finishing_a_previously_interrupted_computation_clears_its_log:106` | the queue assertion | `['genus_class_count', 'spinor_genus_count', 'spinor_genera', 'discriminant_orbits'] != ['genus_class_count']`, and a searches request `['spinor_regular']` |

The third is the same ask read before the run: the fixture is the state an interrupted run leaves —
`0012` certified everywhere except the one computation `exceeded.yaml` names — and the card is **not**
certified everywhere, because these four fields have no certificate and, for the spinor three, cannot
have one.

The fourth field is `integral.discriminant_orbits`. `theory/orbits.md:151` gives the two series to two
kinds of card: $F_{L,\Gamma}$ is enumerated from a definite card's vectors and stored in
`integral.primitive_orbits`, and $F_{A_L,\Gamma}$ is the series on the discriminant group of an even
lattice of hyperbolic index at least two. The corpus agrees — the only two cards that carry the second
series, `0040` ($U^2$) and `0283` ($U^3 \oplus \langle -6 \rangle$), are indefinite. Asked of A2 the
owner answers (a constant-1 series over the eight subgroups), so the value lands on a card whose own
row belongs in `primitive_orbits`, and it stays uncertified in the queue of every run over A2.

## The fix, and the one assertion it inverts

`genus.applies` now reads both domains off the card's own data: `rank` for the spinor fields, and
definiteness for the discriminant-group series (`b2ac28d8bd`). Nothing else moves — a card of rank
three or more is asked for the spinor fields as before, and every other refusal is still recorded by
`failures.record` and reported once.

One test still asserted the opposite, and it is red against that fix on `main`:

    tests/test_genus.py::test_a_definite_binary_lattice_requests_regularity_and_its_spinor_fields:355
    assert "spinor_regular" in fields
    AssertionError: where spinor genera are defined is the owner's answer, not the database's
    assert 'spinor_regular' in ['integer_valued', 'elementary_primes', 'genus_symbol', …]

so that test is inverted here with the fix, and its second half — the refusal recorded and then
quarantined — goes with it, because the computation is never asked. The three tests above are
untouched.

## Measured

The venue is the pinned image (`dzackgarza/sage` config `332aebe9…`, revision `6301b4e4`, Python
3.14.10, Sage 11.0.beta5) run under its PRoot launcher, with the workflows' own collectors
(`-p qc_sage_session -p qc_unique_inventory`) and `sage-extensions` main `0c914d83` on `PYTHONPATH`.
The tree under test is `main`'s own bytes with the four files of this commit applied, so it is the
tree this lands, not a working copy.

    before, the three tests, on main before the fix:  3 failed in 180.34s
    after,  the three tests:                          3 passed in 213.06s
    after,  tests/test_certify_process.py and tests/test_failures.py, whole files:
                                                      17 passed in 219.33s
    after,  tests/test_genus.py, the applies/queue/worker selection:
                                                      11 passed, 39 deselected in 33.64s
    after,  tests/test_model.py tests/test_card_merge.py:
                                                      76 passed, 2 failed

The last two failures are the scratch tree's, not the code's: `tests/test_card_merge.py` reads
`.gitattributes`, which a tree assembled from `git archive` of selected paths does not carry, and the
same two fail on the untouched tree.

The queue itself, for the `#42` fixture the third test builds (`genus.requests` over its fixture):

    before:  ['genus_class_count', 'spinor_genus_count', 'spinor_genera', 'discriminant_orbits']
             searches: ['spinor_regular']
    after:   ['genus_class_count']

## One neighbouring test is a coin toss in this venue

`test_an_early_termination_does_not_blacklist_a_computation_for_a_whole_job` waits for U's root
search to be announced, kills the run, and then requires a searches request in the queue. Its premise
is that the search has not returned. Measured on this tree, it does return on some runs, and then
there is nothing left to ask:

    0016 roots: applies=True stored=yes held=yes pending=False log=(0, False)   run killed at 26.5s
    0016 roots: applies=True stored=yes held=no  pending=True  log=(0, False)   run killed at  5.4s

It was green before this fix only because the refusals held the run back long enough for the kill to
land inside the search; it is now reached sooner. It is not one of the three tests, it is not made
worse by anything in `genus.applies` (the search is the preamble's), and it passed on the clean
whole-file run of this tree (`17 passed`) and failed on another — a flake, recorded here rather than
changed.

## Step 9, which is not a checkout problem

Step 9 does not die because the checkout is missing or at the wrong ref. It dies because the owner's
suite records the commit it ran at, and the record cannot read the checkout:

- `sage-extensions/pyproject.toml` `[tool.pytest.ini_options] addopts` loads
  `sage_extensions.testing.timing_record`, whose `pytest_sessionfinish` calls
  `sage_extensions.timing.current_commit()`;
- `sage_extensions/timing.py:239` resolves it as `subprocess.run(("git", "-C", str(_source_tree()),
  "rev-parse", "HEAD"), check=True)` — `check=True`, so a non-zero exit is a `CalledProcessError`
  inside the pytest hook, and the step ends on that traceback in ten seconds;
- `_source_tree()` is the package's own path, and step 9 puts `$GITHUB_WORKSPACE/sage-extensions/src`
  first on `PYTHONPATH`, so the tree asked about is the checkout at step 8. `actions/checkout` writes
  it as the runner; `sage-env` runs as root; git refuses a repository it cannot vouch for and exits
  **128**. That is the same code and the same container as step 7, where `sage_extensions` is imported
  from the image's own `/repos/sage-extensions` (root-owned) and the record is written without
  complaint — which is the fingerprint of ownership rather than of a path.

The step now names the checkout safe for the container's git (`safe.directory` through
`GIT_CONFIG_COUNT`/`GIT_CONFIG_KEY_0`/`GIT_CONFIG_VALUE_0`: the image sets no `HOME`, so the
environment's config is where `-c` lives), and it reads the commit first, so that a checkout that is
absent, or a path that is not itself a repository, is reported as that sentence and not as the
library's traceback. Case (c) is the trap this guards: `git -C` walks up, and the checkout sits
inside the database's own repository, so a missing `sage-extensions` would otherwise answer with the
*database's* commit.

The workflow half rides as `results/tests-workflow-safe-directory.patch`, as this repository's earlier
workflow changes do (`results/tests-workflow-record-checks.patch`,
`results/tests-workflow-owner-time-gates.patch`): the connection this was written on may not update a
file under `.github/workflows/`, and GitHub answers such a push with "refusing to allow a GitHub App to
create or update workflow … without `workflows` permission". The patch applies to this commit's
`.github/workflows/tests.yml` — `git apply --check` clean, and the applied file is byte-identical to
the one measured below.

    (a) the checkout present:      "The owner's contracts run at sage-extensions 0c914d83…"   exit 0
    (b) no checkout at the path:   "::error::… is not a repository this environment can read
                                    (git resolves the path to 'nothing') …"                    exit 1
    (c) the path inside the database checkout, no sage-extensions there:
                                   "::error::… (git resolves the path to
                                    '…/repo') …"                                               exit 1

## Not measured here

- **The run's own log.** The run keeps no artifacts (`…/runs/44304988129/artifacts`: `total_count 0`)
  and both log endpoints answer 403 without repository admin, so the failures above were not read
  from it; they were reproduced on its tree instead, in the image, by the same collectors.
- **The refusal itself.** This VM has no root and no container runtime, and the image runs under PRoot,
  which reports the caller's own uid for every file; a repository owned by another user cannot be
  staged here, so the ownership refusal (and its repair) is decided from git's documented behaviour
  and the step-7/step-9 asymmetry above, not from a local reproduction.
- **The whole suite**, and the owner contracts' own verdict: `tests.yml` is the full proof. On this
  tree step 9's selection is `1 failed, 12 passed`, the failure being
  `test_integral_hyperbolic_index_is_owned_by_the_lattice`
  (`AttributeError: '_SelectedFinitePresentationModules…' object has no attribute 'list'`), which is
  the owner's and lands there.
- **The step 9 change end to end**, because the container it changes cannot be started here. Its three
  branches were run against the image through its PRoot launcher with a stand-in for `docker exec`; the
  ownership refusal it repairs could not be staged, and the step runs for the first time on the next
  `tests` run that `results/tests-workflow-safe-directory.patch` is applied to.
