# #30: a per-tag certification read the whole corpus, and was killed before it computed

## The step that read the corpus, measured

`sage-extensions` main `5fc4e0119b`, the image, the full repository (302,504 cards), in one process:

    peak before any read                                   0.38 GiB
    corpus.load   302,504 entries, 421 s                   7.29 GiB peak
    certificates.load  2,449,746 entries, 556 s            9.08 GiB peak

Two reads, ~16 minutes, ~9 GiB of the runner's 15 GiB — for a request that names one tag. With the
image's own footprint on top, the command was killed (exit 137) before a worker started; the same
command certified 026E when it ran over a root holding 026E alone (`results/evidence-16-cardinality.md`).

The step is in `cli.certify`:

    loaded = corpus.load(root)          # every card
    held = certificates.load(root)      # every certificate group

while `genus.certify` selects by tag from `loaded.entries` and reads `held` for that tag's
computations only.

## The repair, at the owner of each read

    corpus.cards(root, tags)                  the cards of `tags` alone, as `load` validates them;
                                              the families, retired tags and catalogues are empty,
                                              because a computation neither reads nor writes them
    certificates.load(root, tags=None)        the groups `tags` hash to, when `tags` is given
    cli.certify                               uses both when `--tag` is given, and `load` without it

`certificates.save` writes a group whole, so the command passes the same tags there: the groups it
writes are the ones it read in full, and no other tag's entries can be dropped.

## Peak memory, before and after

| | before | after |
| --- | --- | --- |
| `certify --tag 026E --phase fields --shard 0/1 --workers 1`, full repository | killed at 15 GiB, no computation | **0.55 GiB peak, 48 s**, one card computed |

Verified on the real card with its certificate taken out of the ledger first, so the command had to
compute the value again:

    certificates/f1.yaml: 026E integral.primitive_orbits removed
    $ certify --minutes 20 --shard 0/1 --workers 1 --phase fields --tag 026E
    026E {'primitive_orbits': {'O': {'constant': 1, 'z': [], 'w': []}, …}}
    peak RSS: 0.55 GiB in 48s

and the recomputed certificate is the one that was there:

    026E integral.primitive_orbits:
      hash: 71acd10a9086e12004375735a77f3c09cfa35d98687b9746995f994599b427c3

`certificates/f1.yaml` is byte-identical to the copy taken before the recomputation. `failures/f1.yaml`
records the entry as `resolved`, which is what a computation that now completes means.

## The regression, red first (7e206245be)

`tests/test_certify_reads.py` runs the command over a corpus of three cards with `genus.certify`
replaced by a recorder:

    test_a_tag_request_reads_only_that_tag_s_card          ['0012']          RED: all three
    test_a_two_tag_request_reads_the_two_cards             ['0012','0026']   RED: all three
    test_a_whole_corpus_request_still_reads_every_card     all three         green

On that commit, with the read unchanged: 2 failed, 1 passed. After the repair: 3 passed. The third test
keeps the repair from narrowing the corpus run, which still certifies, and reads, every card.
