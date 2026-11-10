# #27: `tests/validation/test_construction.py` holds three things it does not need

Killed at about eight minutes in a 15 GiB VM (exit 137) before #25's import repair let it collect. In
the image, measured on this tree, it now runs to completion: **3 passed in 20 min 37 s**, the parent's
peak 0.87 GiB and the heaviest chunk of card constructions 2.86 GiB.

## What it held

1. **The whole corpus, as validated models.** A module-scoped `corpus.load(REPOSITORY)` fixture built
   all 302,504 `Lattice` models and kept them for the file — about 7.5 GiB, measured. Every check then
   copied them again into a `cards` dict.
2. **A dict of preamble lattices for every morphism endpoint.** `owned = {tag: _owned(cards[tag]) ...}`
   built one lattice per endpoint of every stored morphism — 122,341 cards state morphisms — and kept
   them all.
3. **Preamble structures that the preamble itself never releases.** This is the one that does not go
   away by reading less: `latticedb/checks/__init__.py` records that the preamble memoizes every
   structure it constructs for the life of the process, and `latticedb verify` splits the corpus into
   shards for exactly that reason. Measured per stage over the first 20,000 cards:

   | stage | peak RSS |
   | --- | --- |
   | read the front matter only | 0.70 GiB |
   | read and validate the card | 0.73 GiB |
   | read, validate, and construct every stored morphism | 1.94 GiB |

   The construction, not the reading, is what accumulates: about 1.2 GiB per 20,000 cards, so 302,504
   cards reach about 19 GiB — the kill, whatever the test itself holds.

## What it holds now

1. `corpus.load` is gone: each check reads one card with `corpus.read_card` + `corpus.front_matter`,
   validates it with `Lattice.model_validate`, and keeps nothing after the card's own morphisms, root
   span or monodromy. The endpoint dict is gone with it.
2. The morphism check, the only one that constructs half a million structures, runs in a fixed number
   of fresh processes: `WORKERS = 8` chunks of the tag-sorted corpus, `CONCURRENCY = 2` at a time. Each
   chunk is a subprocess of the same file (`_construct`), so the preamble's retained structures die
   with it. A chunk that ends without reporting its result, or with a nonzero status, is a failure —
   the exit status is part of the verdict, which is the lesson of #22.
3. Every assertion is the one the file made: `stored.scale is not None` for every stored morphism, a
   constructed `category.Mor(source, target)(images)` for every one of them, every root-span embedding
   as a morphism from the orthogonal sum of its summands, and every monodromy generator as an
   automorphism of its fibre lattice. Nothing is deselected, sampled or skipped.

Measured on this tree:

| | |
| --- | --- |
| whole file | 3 passed in 1237.88 s (20 min 37 s), a process per chunk, 2 at a time |
| parent process peak | 0.87 GiB |
| heaviest chunk (37,813 cards) | 2.86 GiB |
| lightest chunk (37,813 cards, the sparse tag tail) | 0.29 GiB |

Worst case while two chunks overlap is therefore about 0.9 + 2 × 2.9 ≈ 6.7 GiB, against the 19 GiB the
single pass needed.

## The one owner API this moved

The root-span check called `category.biproduct(summands)`. sage-extensions main still names
`biproduct` but raises `NotImplementedError: orthogonal sums do not supply categorical biproducts for
form-preserving maps`, and gives `orthogonal_sum(summands)` for what a card states — the orthogonal sum
that retains the module biproduct. That is this repository calling a renamed operation, so it is fixed
here: `test_construction.py` now calls `orthogonal_sum`, and the assertion is the same construction.
