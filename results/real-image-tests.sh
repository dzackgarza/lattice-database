#!/usr/bin/env bash
# Run the database's own tests in the published Sage image, on a checkout of this repository.
# No synthetic owner package and no rewritten source: supported runtime, real import graph.
set -euo pipefail

# `latticedb`'s supported interpreter is Sage's /sage/.venv/bin/python (see .github/actions/sage);
# these tests exercise its storage and merge code, not its lattice mathematics.
docker exec -i --workdir "$GITHUB_WORKSPACE" \
  --env "PYTHONPATH=$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
  sage-env /sage/.venv/bin/python -m pytest -q \
  tests/test_failures.py tests/test_merge.py tests/test_persist.py

# The owner adapter's 026E request: emitted JSON is printed with the constant as its exact number.
docker exec -i --workdir "$GITHUB_WORKSPACE" \
  --env "PYTHONPATH=$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
  sage-env /sage/.venv/bin/python results/026e-real-adapter-request.sage.py

# And the ordinary certification path, which writes the card's certificate and value:
docker exec -i --workdir "$GITHUB_WORKSPACE" \
  --env "PYTHONPATH=$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
  sage-env /sage/.venv/bin/python -m latticedb certify --tag 026E --phase fields --minutes 30 --workers 1
