# Two certificate defects the recovered tree reports, both pre-existing on main

Found while verifying the cards run 42363689427 recovered (#20). Nothing here is the recovery's
doing, and nothing here is fixed in this item: an existing contradiction is reported, not waived.

## How these were found and classified

`results/verify-current-chunks.py` runs the repository's own `checks.records.problems` — the
certificate half of `latticedb verify` — over every recovered card, 400 cards to a process
(`results/evidence-20-verification.log`). Its first chunk reports 26 contradictions on 15 cards.

Each was then read as a **pair**: the card *and* its own `certificates/<group>.yaml`, both taken from
the same revision, at the pre-recovery revision `934a1324ee` and in the current tree
(`results/triage-verification-problems.py`, log `results/evidence-20-triage-preexisting.log`):

    pre-existing 26, recovered 0, INDUCED 0, neither 0

Splitting them by what is actually wrong with the pair
(`results/classify-certificate-contradictions.py`, log `results/evidence-20-contradiction-classes.log`):

| class | count | what it is |
| --- | --- | --- |
| `uncited` | 11 fields | the shard's hash **is** the hash of the value the card stores, and the card cites nothing |
| `unstated` | 15 fields | the card states **no** value, and the shard holds a certificate for that field |
| `stale` | 0 | no case where the shard commits to a value the card no longer states |

## Defect 1 — `uncited`: a finished computation the card does not cite

    0021  root_span.norms, root_span.roots
    0024  hyperbolic.reflective, root_span.norms, root_span.roots
    0026  hyperbolic.reflective, root_span.norms, root_span.roots
    0268  hyperbolic.reflective, root_span.norms, root_span.roots

The value and the hash agree — e.g. `0268 root_span.roots` is `[[-1,0,0],[0,-1,0],[0,0,-1]]` on the
card and `ea519209c021…` in the shard, which is exactly the hash recomputed from that value and that
Gram tensor — but the card's `certifications` has no entry for the field, so `is_certified` is false
and verification reports a contradiction. The repair is the card's reference, not the computation.
This is the class #21 owns; it is not only 0268.

## Defect 2 — `unstated`: a certificate for a value the card does not state

    0023  definite.regular, definite.spinor_regular
    02AE  definite.regular, definite.spinor_regular
    02AF  definite.regular, definite.spinor_regular
    02AG  definite.regular, definite.spinor_regular
    02AH  definite.regular, definite.spinor_regular
    02AN  definite.regular, definite.spinor_regular
    02BQ  definite.regular
    02BS  definite.regular
    02BT  definite.regular

For each, the card has no value for the field (`definite.regular` is absent, not null) while
`certificates/<group>.yaml` holds `«tag» definite.regular`. A certificate commits to a result; a
result that is not on the card means either the value was removed after certification and the
certificate was left behind, or the value never landed while the certificate did. Either way the
ledger of what was proved and the card now disagree, and verification cannot tell which is stale.

This is a different defect from Defect 1: there is no value whose citation is missing, and the repair
is not simply to cite. It needs the owner's decision — recompute and store the value, or retract the
orphaned certificate — and it is not #21's subject.

## Reproduction

    # the contradictions, through the production checker
    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/verify-current-chunks.py --size 400
    # the same-revision classification of each
    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/triage-verification-problems.py results/evidence-20-verification.log
    PYTHONPATH="$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
      /sage/.venv/bin/python results/classify-certificate-contradictions.py results/evidence-20-verification.log

    0268 root_span.roots, for instance:
      stored   [[-1,0,0],[0,-1,0],[0,0,-1]]
      cited    none
      shard    ea519209c021…  == recomputed from the stored value and Gram tensor

## Not filed from here

This session's GitHub connection reads issues and PRs and writes branches, PR titles/bodies and
labels; it cannot publish issues. #21 already owns Defect 1 for 0268. Defect 2 needs its own owner
issue with the table above as its body.
