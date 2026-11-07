# Run 42326648686: value and persistence verification checkpoints

These commands run in the existing published research image on a checkout of the repository at these
revisions. No package beyond the image's repository-provisioned dependencies is required. The original
bundle and these commands must stay intact:

```sh
export PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src"
```

1. **The database's own storage, reconciliation, and persistence tests.** Failure storage entries are
   keyed by their owning shard (hex), two different computations of one tag share a shard without being
   a duplicate, and `persist.sh` completes the ordinary concurrent push.

   ```sh
   docker exec -i --workdir "$GITHUB_WORKSPACE" sage-env \
     /sage/.venv/bin/python -m pytest -q \
     tests/test_failures.py tests/test_merge.py tests/test_persist.py
   ```

2. **The artifact value/certificate verifier.** For every one of the 60 retained artifacts, the base's
   own card and its certificate shard are materialized and `git apply` proves the original patch. Each
   recovered card's Gram tensor is required to match the base's, stored values must not have been lost,
   and certificates are recomputed only through the owned projection `genus.certified_value`,
   `records.derived_projection`. The stored certificate's `hash` field is compared, not provenance text.
   Distinguish later superseding fields from proofs in the patches; expected fields/certificates that
   are missing must fail, not be skipped.

   ```sh
   docker exec -i --workdir "$GITHUB_WORKSPACE" sage-env \
     /sage/.venv/bin/python results/verify-recovered-values.py \
       attachments/you-work-the-github-s6pa/extracted/openmath-certify-42326648686
   ```

3. **The actual 026E adapter/certify request (#16)**. `results/026e-real-adapter-request.sage.py`
   prints `EMITTED_JSON` with the owner's finite `constant` serialized exactly as `1`, then:

   ```sh
   docker exec -i --workdir "$GITHUB_WORKSPACE" sage-env \
     /sage/.venv/bin/python results/026e-real-adapter-request.sage.py
   docker exec -i --workdir "$GITHUB_WORKSPACE" sage-env \
     /sage/.venv/bin/python -m latticedb certify --tag 026E --phase fields --minutes 30 --workers 1
   ```

4. **Persistence**. `results/persist-recovered-changes.py` stages exactly `lattices certificates
   exceeded.yaml failures` in this worktree and commits locally, without any remote push. Check manager
   acceptance by reading the pushed revision before these new tests count as acceptance.

   ```sh
   docker exec -i --workdir "$GITHUB_WORKSPACE" sage-env \
     /sage/.venv/bin/python results/persist-recovered-changes.py
   ```
