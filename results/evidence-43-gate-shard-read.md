# #43: the gate's shard reads what it checks, so `latticedb verify` runs here

`latticedb verify` could not complete in this VM, for any shard: `checks.one_shard` read the whole corpus and every
certificate (`corpus.load(root)`, `certificates.load(root)`), which the repository measures at 7.29 GiB and 9.08 GiB,
against 15 GB of memory. The previous turn's attempt was stopped at 3.64 GiB and 173 s, still inside `corpus.load`.
This turn's change makes a shard read its own cards, and a slice of the corpus now verifies end to end.

## What changed

- `corpus.load(root, tags=...)` reads the cards named and leaves the catalogues, the families and the retired tags
  whole. Without `tags` it is the read it always was (`src/latticedb/corpus.py:228`).
- `checks.referenced_tags` and `checks.shard_closure` (`src/latticedb/checks/__init__.py`): a shard reads its own
  cards, the cards **they** name, and the lattices **every catalogue record** names, transitively. The reference
  checks compare a record with the record it names, so a read that is not closed under naming would report every
  target outside the shard as absent. Catalogue names are read as data, not by field name, so a field the schemas add
  later is read too; a citation is skipped, because a tag is four characters of `0-9A-Z` and a citation prints years.
- `records.duplicate_gram_problems(root, loaded, cards)` (`src/latticedb/checks/records.py`): the one check that is
  corpus-wide by nature now reads the durable index of Gram tensor to tags, so a shard still reports every duplicate
  pair that one of its own cards belongs to. It reads it through the new `corpus.stored_gram_index`, which *never
  writes*: `gram_index` promotes a card that gained a tensor and rebuilds the file when the card set has changed, and a
  verification check may not — `checks` reports and never writes. An index that no longer describes the cards on disk
  is not read at all, and the duplicates among the cards at hand are reported instead.
- `relations.problems(..., known=...)` (`src/latticedb/checks/relations.py`): a `related` tag is checked against the
  cards on disk rather than against the read. Card 0013 alone states 23,322 related tags, and reading a card so that
  another card may say it is related to it is not what the check is for.

## Measured

| what | value |
| --- | --- |
| shard 0/16: cards | 18,988 |
| shard 0/16: closure | 19,206 (+218 named cards) |
| reading a shard's cards | 0.75 GiB (`results/probe-verify-shard-size.py`) |
| with its certificates | 1.44 GiB |
| `verify --shard 0/64`, end to end | 4,752 cards, 1.0 GiB peak, 5 m 39 s, **0 problems**, exit 0 |
| the same slice again, after the read-only fix | 4,752 cards, 1.1 GiB peak, 3 m 45 s, **0 problems**, exit 0, and `gram-index.json` unchanged |
| `verify --shard 1/64` | 4,736 cards, 1.0 GiB peak, 7 m 06 s, **3 problems**, exit 1 |
| `verify --shard 17/64` | 4,636 cards, 1.2 GiB peak, 7 m 58 s, **10 problems**, exit 1 |
| `verify --shard 33/64` | 4,810 cards, 1.3 GiB peak, 9 m 39 s, **7 problems**, exit 1 |

The runs were three at a time on four cores, so their minutes are an upper bound on one slice alone.

The earlier read cost 7.29 + 9.08 GiB for the same work. What remains is time, not memory: at 5 m 39 s and 1.0 GiB
per 4,752 cards, a 1/16 shard is about 22 minutes and under 2 GiB, and the whole corpus is about six hours of this VM.
That is why the shards are the gate's unit: CI runs them (`verify.yml`), and this VM now runs any of them.

## What the gate reports, now that it runs

Three of the four slices report ledger inconsistencies, and they are of one kind: a **certificate with no value on the
card that it belongs to**. Twenty lines, on eight cards — `02LP`, `3ICA`, `02BW`, `02O9`, `02YE`, `0353`, `03UB`,
`04R0` — each `definite.regular` or `definite.spinor_regular`:

```
lattices/02LP.md: definite.regular contradicts its completed computation certificate
lattices/02LP.md: definite.spinor_regular contradicts its completed computation certificate
```

The pair behind the first line, checked by hand: `certificates/01.yaml` holds `02LP definite.regular` with hash
`1b875662…4861` and `02LP definite.spinor_regular` with hash `66f4850…`; card `02LP` states neither value nor a
citation for either, and `checks.records.problems` reports a certificate that no card cites — its docstring's "cites a
certificate for a value it no longer states", read from the other side. That is a stored-card finding for the
certification pipeline to settle (a value the card does not carry, or a certificate minted for a value since dropped),
not something this change may decide: deleting a certificate or a value is a data decision, and the gate's office is
to report it.

None of the 20 lines is a reference problem, so none of them is an artefact of the narrowed read.

## What the union of the shards still checks, and what it no longer does

Every card of the corpus is checked exactly once (`cards` is the shard), and every reference **from** a checked card
is checked, because its targets are in that shard's closure. Every catalogue record is read and checked in every
shard, against the lattices it names, which the closure carries. Duplicate Gram tensors are corpus-wide.

Two checks are now within a shard's closure rather than the whole corpus, and they are named here rather than
silently weakened: a duplicate card *name* between two cards of different shards, and the `hyperbolic_index` bound
that a morphism stored on another shard's card would supply. Both were reported by the corpus-wide read this VM could
not run; with the durable index named above this is the last of it.

## Tests

`tests/test_verification.py` — **12 passed in 33.43 s**, three of them new: a shard reads the card its own card names
and reports no absent reference; a related tag outside the read is decided from the cards on disk, and reported when
the card is gone; a duplicate Gram tensor is reported across shards from the index.
