# #23: the regularity values were written, then deleted by another run's derivation

## Reproduction: each card and its own shard

The report's nine tags, each against the certificate group its tag hashes to. Every certificate commits
to a **decision**, not to an absent value — the hash is over the computation name, the Gram tensor and
the stored result, so the three candidates `absent`, `true`, `false` are distinguishable:

| card | group | `definite.regular` | `definite.spinor_regular` |
| --- | --- | --- | --- |
| 0023 | 61 | `d360fdfe735a` = hash(**true**) | `f2da1be258e8` = hash(**true**) |
| 02AE | 44 | `99a69f071970` = hash(**false**) | `40cd726d0c62` = hash(**false**) |
| 02AF | f3 | `dbd4695ed1e2` = hash(**false**) | `9029f4badd28` = hash(**false**) |
| 02AG | 49 | `f12f92b3ff5f` = hash(**false**) | `00b85fed2baf` = hash(**false**) |
| 02AH | 2c | `631dec0373e0` = hash(**false**) | `a30653a36268` = hash(**false**) |
| 02AN | 71 | `cd3a978b6bf3` = hash(**false**) | `ec6f7528a479` = hash(**false**) |
| 02BQ | 96 | `1bdfaf6d7f1a` = hash(**false**) | — (rank 2, outside the owner's domain) |
| 02BS | f5 | `96e87b80f6dd` = hash(**true**) | — |
| 02BT | 8a | `34f62c479fed` = hash(**true**) | — |

No certificate matches `hash(absent)`. So the value was **computed and stored, then lost**; the issue's
open question ("whether the value was omitted at storage or removed later") is the second.

The owner confirms the same answers independently — `Lattices(ZZ)(card.gram_tensor).is_regular()` and
`is_spinor_regular()` at sage-extensions `5fc4e0119b`, computed for this issue in the image: 0023
true/true, 02AE–02AN false/false, 02BQ false, 02BS true, 02BT true.

## The lost step

    $ git log -S"  regular:" -- lattices/0023.md
    7b7402ed2e 10-21 15:53 feat: certify computed card values (shard 1/16)   + regular: true
    5017c44c2b 10-21 21:43 feat: certify computed card values (shard 1/16)   - regular: true

`7b7402ed2e` added the values and their citations; `5017c44c2b`, 5 h 50 min later — one job's window —
removed exactly those four lines (two values, two citations) and nothing else on the card, while
`certificates/` kept both entries, because that file merges key by key and a card did not yet.

The step is `genus.certify`'s derivation branch:

    derived = records.derive(request["record"])       # the run's read of the card when it was queued
    derived["certifications"] = {**stored_lattice.certifications, "derive": certificate_hash}
    storage.write_text(entry.path, records.record_text(derived, entry.prose))

`request["record"]` is the card as the run read it when it queued that card — up to 350 minutes earlier.
`records.derive` rebuilds the blocks it owns (`integral`, `definite`, …) **from that record**, and the
`definite` block it produces is the stale one: no `regular`, no `spinor_regular`, and no citation for
either. Writing it replaces the whole card, so a value another run had written in the meantime is
deleted, and its certificate is left naming a value that is no longer there.

## The repair

`genus.keep_other_computations(path, derived)` now stands between the derivation and the write: a field
the stored card states and the derivation does not is carried over, with its citation. Those fields
belong to computations of their own — each has its own certificate — so a derivation does not decide
them. A derivation whose Gram tensor differs from the stored card is another lattice and carries
nothing over.

    kept[block_name] = {**carried_fields, **produced}          # the derivation's own values win
    citations[local_name] = stored_citations[local_name]       # carried fields keep their citation

Two tests hold it (`tests/test_genus.py`):

- `test_a_derivation_keeps_a_result_another_computation_wrote` — a stale derivation without the two
  regularity fields keeps both values and both citations, and its own values still win;
- `test_a_derivation_of_another_lattice_carries_nothing_over` — a Gram tensor that differs carries
  neither.

## The nine cards

`results/repair-23-regularity.py` reads each card's own shard, takes the value whose hash the
certificate carries, refuses a card where no candidate or more than one matches, and writes the value
with its citation. No value was guessed and none was left behind: 15 fields on 9 cards, all additions.

Verified through the verifier that reported the defect, in the image, on the current cards and
shards: `checks.records.problems` → **0 problems** on 0023, 02AE, 02AF, 02AG, 02AH, 02AN, 02BQ, 02BS,
02BT. The certificates are unchanged; the cards now state what they certify.
