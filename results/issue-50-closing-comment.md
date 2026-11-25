Closing #50: the nine cards state the regularity their own certificates name, and the 94 other cards the
same defect left in the ledger do too. Unposted: this connector cannot comment on issues, so this is the
text of the comment with the tree's own line numbers.

**1. Reproduced on one card.** `02U9` reports two problems, both `contradicts its completed computation
certificate`: `definite.regular` and `definite.spinor_regular` (`lattices/02U9.md:113`, `:114`), whose
certificates are at `certificates/10.yaml:136` and `:142`. `latticedb verify` takes `--shard
i/n`, not `--tags`, so the one-card form of the shard's check is `checks.records.problems` over
`corpus.cards(['02U9'])`: 2 problems before the repair, 0 after, and 21 of the card's 21 certificates
then match.

**2. The stored value changed; the certifying program did not.** `git log -S "definite.regular" --
lattices/02U9.md` names the add (`7b1e287c99`, 2026-10-21 15:53) and the delete (`7626a33202`, 21:40);
the seven shard-1 cards are `7b7402ed2e` → `5017c44c2b`. That is #23's defect: the second run of each
shard derived the card from a queue-time record whose `definite` block holds no search result and wrote
it over the card, while `certificates/`, which merges key by key, kept the entry.
`genus.keep_other_computations` (`7bc8daefb9`) stops a recurrence but restores nothing. On the
certifier's side nothing moved: `certification_hash`, `certified_value`, `genus.name` and the `regular`
entry of `genus.BLOCKS` are unchanged since `287b70c979` (2026-10-15), and `_regular` in
`sage_genus.py` since `cbddc33946` (2026-10-16) — all before the certificates were minted. The owner
agrees, computed at sage-extensions `dcf5e18`: 02XN/03EP/06NV/06O4 true/true, 05VD false/false,
3ICJ/3ICR/3ICK false/true, 02U9 false/false.

**3. The nine are a subset.** A certificate commits to (computation, Gram tensor, result), so the value
is readable from it without re-hashing: of `{true, false}` exactly one reproduces each stored hash.
Scanning every group for the five search fields (`genus.SEMI_DECISIONS`) found 190 such certificates
whose card states no value, on 103 cards, at the base this landed on (205 on 111 when first measured at
`c6d3411`; `3790c656c3` has since repaired eight of those). The 2026-10-21 shard runs hit all sixteen
shards, and #50's nine are the shards 0 and 1 subset that a tag-scoped verify reports. All 190
name exactly one value and all agree with today's decision structure: `regular` true exactly when the
genus has one class, `spinor_regular` true exactly when its spinor genus does.

**4. The repair is at the owner of the value.** `results/repair-50-regularity.py:56` writes each value
its own certificate names, with that certificate's citation, and refuses a card where no candidate or
more than one matches (`:31`); 0 refused. 380 lines added to 103 cards, none removed, each in the
model's own field order; `02U9`'s blob is again `948ff6b4c5`, the blob `7b1e287c99` left.
`certificates/` is untouched and no definition changed. Landed as `2e19fbae7e`.

**5. Red test first.** `tests/test_stored_records.py:140` scans the ledger for the fields a job may stop
inside (`:125`) and holds each card to the value its certificate commits to: red on the base with 190
problems, green after, 1 passed in 48.4 s. It still passes on `0a2a0e5198`, the shard 0/1 run that
landed after the push — that run changed only `exceeded.yaml`.

**6. What CI carries.** The sixteen-shard `verify` gate. A tag-scoped dispatch reports only the shards of its
tags, so run 44624851354's scope was shards 0 and 1; the other 94 cards were outside it and were red all
the same, and they are repaired here. No value was re-hashed and no
field was introduced; `definite.regular` and `definite.spinor_regular` are the published fields, and
every restored value is the one its existing certificate commits to over the card's Gram tensor.
