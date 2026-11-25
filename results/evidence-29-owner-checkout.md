# The owner-contract step's sage-extensions checkout, and why this is a patch file

`tests` run `44304988129` (head `0ab2ba44`) has two failures outside the suite, and this is the
second: step 8 checks out `dzackgarza/sage-extensions` at `$GITHUB_WORKSPACE/sage-extensions` and
step 9, the owner contracts, dies on

    git -C …/sage-extensions rev-parse HEAD   →   exit 128

## What reads that path

`sage_extensions.timing.current_commit` (`timing.py:245`) runs exactly that command, on the tree
`_source_tree()` walks up to from the `sage_extensions` package it imported (`timing.py:202`). Step
9's `PYTHONPATH` puts `$GITHUB_WORKSPACE/sage-extensions/src` in front of the image's own copy, so
the tree it reads is the checkout step 8 leaves. `_source_tree` asserts `pyproject.toml` is there, and
the traceback this repository already holds for that assertion is in the ledger: `failures/09.yaml`,
`5922 integral.primitive_orbits`, from the *tests* step, where the imported copy was the installed
one under `/sage/.venv/lib/python3.14/site-packages` and the walk-up found
`/sage/.venv/lib/python3.14`.

## Why 128 rather than an assertion

Two conditions, either of which makes git refuse the tree, and both of which the step can rule out:

- step 8 carries `if: always()`, so a checkout that failed leaves no tree at that path at all, and
  step 9 runs anyway;
- `actions/checkout` leaves the tree owned by the runner, and the container's user is not that user,
  so git refuses the repository as dubious. `certify.yml:90` and `certify-searches.yml:43` add the
  workspace to `safe.directory` for exactly this reason; `tests.yml` has no such line, and its
  in-container git use is new here.

## The change

`results/tests-workflow-owner-checkout.patch` (`git apply` against `main`): step 9 names the tree,
checks it holds `pyproject.toml` and `.git`, adds it to the container's `safe.directory`, and reads
`rev-parse HEAD` through the container before pytest starts. A tree that is missing or unreadable is
the step's own failure, printed as that sentence, instead of an unhandled `CalledProcessError` raised
from inside a contract.

## Why it is a file

The GitHub connection this work runs through is a GitHub App without the `workflows` permission:
pushing a commit that touches `.github/workflows/tests.yml` is rejected (`refusing to allow a GitHub
App to create or update workflow … without workflows permission`). The same boundary produced
`results/tests-workflow-record-checks.patch`, `results/tests-workflow-owner-contracts.patch`,
`results/tests-workflow-owner-time-gates.patch` and `results/tests-workflow-warm-owner-bridge.patch`,
each landed later by a commit that applies it. So this patch needs the same hand, and until it lands
step 9 stays red as it was.
