# The 190 values #50 restored: each one's certificate, and the owner's answer at `dcf5e18`

The repair (`results/repair-50-regularity.py`, commit `2e19fbae7e`) wrote no value of its own: for each card it
read the value out of the certificate the card's shard already held, over that card's Gram tensor, and restored the
citation of that same certificate. This file re-derives every repaired card the way `sage_genus._compute` does —
`records.derive`, `Lattice.model_validate`, `Lattices(ZZ or QQ)(gram_tensor)` — at
`sage-extensions dcf5e18655ef976e63accaf1bad09e3d99c3ec0b` (2026-11-19 23:14 UTC), and asks the owner for
`is_regular()` and `is_spinor_regular()`. **190 of 190 values are reproduced by the owner**, 38 `regular` true and
65 false, 37 `spinor_regular` true and 50 false, on 103 cards.

The hash is the whole identifying data: a certificate commits to (computation name, Gram tensor, result), so a hash
that matches one of `{true, false}` and not the other fixes the value. Nothing was re-minted — `certificates/` is
untouched by the repair — and the probe below is an independent computation by the owner, not a re-hash.

| field | values | true | false |
| --- | ---: | ---: | ---: |
| `definite.regular` | 103 | 38 | 65 |
| `definite.spinor_regular` | 87 | 37 | 50 |

| card | field | restored | certificate (group:hash) | owner at `dcf5e18` |
| --- | --- | --- | --- | --- |
| 0035 | definite.regular | true | `a5.yaml:59d14b4792b22c7d…` | true |
| 0035 | definite.spinor_regular | true | `a5.yaml:4fa9847cafd2cfd1…` | true |
| 02BR | definite.regular | true | `b4.yaml:fc135994fa701e88…` | true |
| 02BZ | definite.regular | true | `9c.yaml:7cc37e8aab6d6650…` | true |
| 02BZ | definite.spinor_regular | true | `9c.yaml:dbf2d7c446800f26…` | true |
| 02C0 | definite.regular | true | `c9.yaml:46c013a87a8da1a4…` | true |
| 02C0 | definite.spinor_regular | true | `c9.yaml:c9f2faad7ab55d14…` | true |
| 02C2 | definite.regular | true | `f7.yaml:ac06fbb644e3f7db…` | true |
| 02C2 | definite.spinor_regular | true | `f7.yaml:631b69c6aeb637e7…` | true |
| 02C3 | definite.regular | true | `54.yaml:ca63e90b87ced2d1…` | true |
| 02C3 | definite.spinor_regular | true | `54.yaml:4a5314165fb218d7…` | true |
| 02C4 | definite.regular | true | `f2.yaml:185fd222a186de71…` | true |
| 02C4 | definite.spinor_regular | true | `f2.yaml:9268ffea95b0870e…` | true |
| 02CB | definite.regular | true | `07.yaml:863a5c568a27ccff…` | true |
| 02CB | definite.spinor_regular | true | `07.yaml:cbdfb8f093a436da…` | true |
| 02CF | definite.regular | true | `e6.yaml:0656aab05c4734a4…` | true |
| 02CF | definite.spinor_regular | true | `e6.yaml:6f3137e3b3771ecb…` | true |
| 02DC | definite.regular | true | `c4.yaml:170877546fe99c30…` | true |
| 02DC | definite.spinor_regular | true | `c4.yaml:50b947e6aeebe3fe…` | true |
| 02DI | definite.regular | true | `13.yaml:dddccded99dcccd7…` | true |
| 02DI | definite.spinor_regular | true | `13.yaml:cfdb1be8f9054217…` | true |
| 02EF | definite.regular | true | `38.yaml:e38c28db2a7a68e1…` | true |
| 02EF | definite.spinor_regular | true | `38.yaml:c75eaa15d45c0e7b…` | true |
| 02EI | definite.regular | true | `c4.yaml:a28a311b10ca677a…` | true |
| 02EI | definite.spinor_regular | true | `c4.yaml:1eca1174fc2327a5…` | true |
| 02EL | definite.regular | true | `a9.yaml:2e5d1df7a4c3ce64…` | true |
| 02EL | definite.spinor_regular | true | `a9.yaml:981939d8dd9e6669…` | true |
| 02FR | definite.regular | true | `56.yaml:37e7320b684c577a…` | true |
| 02FR | definite.spinor_regular | true | `56.yaml:cd35406750a5a7ba…` | true |
| 02FV | definite.regular | true | `ea.yaml:cf1c49305d435994…` | true |
| 02FV | definite.spinor_regular | true | `ea.yaml:44d76215e516b541…` | true |
| 02HK | definite.regular | true | `fd.yaml:7576ea827ba10258…` | true |
| 02HK | definite.spinor_regular | true | `fd.yaml:43c4bd5eedd5c82b…` | true |
| 02JT | definite.regular | true | `1e.yaml:113b83823b77ac50…` | true |
| 02JT | definite.spinor_regular | true | `1e.yaml:8636c0822ab6da33…` | true |
| 02LQ | definite.regular | true | `ee.yaml:385f18d8eccaf3bc…` | true |
| 02LQ | definite.spinor_regular | true | `ee.yaml:1ab2c59f0b067028…` | true |
| 02LX | definite.regular | true | `fc.yaml:a7fa9e06b417be5f…` | true |
| 02LX | definite.spinor_regular | true | `fc.yaml:af60d2f8e8493aba…` | true |
| 02LZ | definite.regular | true | `6d.yaml:a326a07b7882be46…` | true |
| 02LZ | definite.spinor_regular | true | `6d.yaml:17c87d56f8d5c531…` | true |
| 02M1 | definite.regular | true | `4a.yaml:03d72ef2bfadf783…` | true |
| 02M1 | definite.spinor_regular | true | `4a.yaml:cefd958ad327bd01…` | true |
| 02M2 | definite.regular | true | `fd.yaml:fe5f35debf2591b6…` | true |
| 02M2 | definite.spinor_regular | true | `fd.yaml:05041814e0240cda…` | true |
| 02O8 | definite.regular | false | `0c.yaml:1519f9087e18b7b6…` | false |
| 02O8 | definite.spinor_regular | false | `0c.yaml:96cfd8af99e76c6c…` | false |
| 02OA | definite.regular | true | `d8.yaml:132565a198d1cdc8…` | true |
| 02OA | definite.spinor_regular | true | `d8.yaml:ab8f6e9e51587a3d…` | true |
| 02OD | definite.regular | true | `d5.yaml:686d4eb6e69ce56f…` | true |
| 02OD | definite.spinor_regular | true | `d5.yaml:85bc19b45685e83d…` | true |
| 02OM | definite.regular | true | `cb.yaml:6aecf9f3ee4239fb…` | true |
| 02OM | definite.spinor_regular | true | `cb.yaml:e10578e926c64e94…` | true |
| 02QT | definite.regular | false | `f6.yaml:0c2891d5ea1c56f3…` | false |
| 02QT | definite.spinor_regular | false | `f6.yaml:181ea48ebc729fe5…` | false |
| 02TP | definite.regular | false | `13.yaml:b80df29ed0bfaabd…` | false |
| 02TP | definite.spinor_regular | false | `13.yaml:f1e1a249e4b87e11…` | false |
| 02U9 | definite.regular | false | `10.yaml:14e9c2517213df39…` | false |
| 02U9 | definite.spinor_regular | false | `10.yaml:1d9bbdbd982d9eec…` | false |
| 02XC | definite.regular | false | `63.yaml:67c11866aef51fd7…` | false |
| 02XC | definite.spinor_regular | false | `63.yaml:a6e4ac8ce20f2f8a…` | false |
| 02XD | definite.regular | false | `83.yaml:399aa133b72401b2…` | false |
| 02XD | definite.spinor_regular | false | `83.yaml:2dcafbdc48791139…` | false |
| 02XN | definite.regular | true | `f1.yaml:249cab4237a486ac…` | true |
| 02XN | definite.spinor_regular | true | `f1.yaml:c6bebc2cfc9eaaa5…` | true |
| 02XV | definite.regular | true | `12.yaml:578c08a0dd08d6e6…` | true |
| 02XV | definite.spinor_regular | true | `12.yaml:f0b10c30c0000b07…` | true |
| 02Y4 | definite.regular | true | `73.yaml:4969154f0325dc22…` | true |
| 02Y4 | definite.spinor_regular | true | `73.yaml:4723ad1bfc2a359c…` | true |
| 02Y9 | definite.regular | true | `7a.yaml:49d0845e67416778…` | true |
| 02Y9 | definite.spinor_regular | true | `7a.yaml:feb81ecd901408f6…` | true |
| 02YD | definite.regular | true | `55.yaml:ef160b60bab7d73f…` | true |
| 02YD | definite.spinor_regular | true | `55.yaml:03b9cdbdb2085876…` | true |
| 031Q | definite.regular | false | `56.yaml:36ffdd1930b543e2…` | false |
| 031Q | definite.spinor_regular | false | `56.yaml:125ccb0346ce462c…` | false |
| 0360 | definite.regular | false | `b3.yaml:fcde80233ab9f768…` | false |
| 0360 | definite.spinor_regular | false | `b3.yaml:4982511cb082263b…` | false |
| 0394 | definite.regular | false | `94.yaml:ec55d1fdab26701e…` | false |
| 0394 | definite.spinor_regular | false | `94.yaml:3559d156774a7d35…` | false |
| 0395 | definite.regular | false | `b4.yaml:11a1ab1cb1dad6ec…` | false |
| 0395 | definite.spinor_regular | false | `b4.yaml:9f9d03bc4125bf1f…` | false |
| 0396 | definite.regular | false | `b5.yaml:a0be264a0f7796c8…` | false |
| 0396 | definite.spinor_regular | false | `b5.yaml:5a123a97ac7da152…` | false |
| 03A9 | definite.regular | false | `f7.yaml:5a1e5c1639849a20…` | false |
| 03A9 | definite.spinor_regular | false | `f7.yaml:ec688ef7709736e9…` | false |
| 03EC | definite.regular | false | `33.yaml:3d7840f61a8b2783…` | false |
| 03EC | definite.spinor_regular | false | `33.yaml:bffc7c29fbe5e523…` | false |
| 03EK | definite.regular | false | `6b.yaml:81f0eeb3d6a9cfc3…` | false |
| 03EK | definite.spinor_regular | false | `6b.yaml:8998a8630e575289…` | false |
| 03EN | definite.regular | true | `46.yaml:d8e54f036f79f7df…` | true |
| 03EN | definite.spinor_regular | true | `46.yaml:d3d88921ef91d191…` | true |
| 03EP | definite.regular | true | `51.yaml:f860ba2a2b36d4f2…` | true |
| 03EP | definite.spinor_regular | true | `51.yaml:a4fd81d1eb34d3ab…` | true |
| 03ER | definite.regular | true | `54.yaml:46a3ac3731fb1b6f…` | true |
| 03ER | definite.spinor_regular | true | `54.yaml:fb9b2f9377909d45…` | true |
| 03ES | definite.regular | true | `6c.yaml:5a7c4418bb2e3c81…` | true |
| 03ES | definite.spinor_regular | true | `6c.yaml:271715d7ed6a0d90…` | true |
| 03IL | definite.regular | false | `d3.yaml:425c3fd3959c735e…` | false |
| 03IL | definite.spinor_regular | false | `d3.yaml:c7c1199f43032db9…` | false |
| 03IN | definite.regular | false | `05.yaml:f107546cdb9ec3c3…` | false |
| 03IN | definite.spinor_regular | false | `05.yaml:3151b20616543147…` | false |
| 03NT | definite.regular | false | `5b.yaml:18f4fc9d4323be95…` | false |
| 03NT | definite.spinor_regular | false | `5b.yaml:e27bea3592514918…` | false |
| 03OU | definite.regular | false | `e6.yaml:7b496d6c65463541…` | false |
| 03OU | definite.spinor_regular | false | `e6.yaml:865386dbc26a1dcc…` | false |
| 03TK | definite.regular | false | `b2.yaml:3b0440bc8184033e…` | false |
| 03TK | definite.spinor_regular | false | `b2.yaml:f55deed0b1d92d3f…` | false |
| 03TL | definite.regular | false | `2b.yaml:6002cb9c1f65de70…` | false |
| 03TL | definite.spinor_regular | false | `2b.yaml:bb0fd1db3a9867e2…` | false |
| 03UC | definite.regular | false | `8e.yaml:58fbd8289fd9e986…` | false |
| 03UC | definite.spinor_regular | false | `8e.yaml:698881fa0bf8cc4c…` | false |
| 03ZY | definite.regular | false | `a4.yaml:8e5e66f242d471a7…` | false |
| 03ZY | definite.spinor_regular | false | `a4.yaml:ec179c0524554050…` | false |
| 0407 | definite.regular | false | `54.yaml:148f7582f299f4ea…` | false |
| 0407 | definite.spinor_regular | false | `54.yaml:dd1b3e1e9f19d56b…` | false |
| 0458 | definite.regular | false | `ea.yaml:d283e329a1dba5ee…` | false |
| 0458 | definite.spinor_regular | false | `ea.yaml:f5ecaa8896f573ee…` | false |
| 0459 | definite.regular | false | `92.yaml:a5290c4d092f49e5…` | false |
| 0459 | definite.spinor_regular | false | `92.yaml:a3d32d0d9e2132af…` | false |
| 045N | definite.regular | false | `35.yaml:014fa8eab4b6fdd4…` | false |
| 045N | definite.spinor_regular | false | `35.yaml:d2fb95a66a49efa6…` | false |
| 045O | definite.regular | false | `f7.yaml:d989c716b385b885…` | false |
| 045O | definite.spinor_regular | false | `f7.yaml:ad891d7eb28675e7…` | false |
| 045P | definite.regular | false | `d6.yaml:8202019aaa141a24…` | false |
| 045P | definite.spinor_regular | false | `d6.yaml:cd4310319149b8e6…` | false |
| 0464 | definite.regular | false | `1c.yaml:0ae62c6c5cbe2c2d…` | false |
| 0464 | definite.spinor_regular | false | `1c.yaml:895a2df9aae330b9…` | false |
| 0465 | definite.regular | false | `cb.yaml:ce58644505a3f04a…` | false |
| 0465 | definite.spinor_regular | false | `cb.yaml:74576e3dcfacb77b…` | false |
| 046V | definite.regular | false | `8e.yaml:2caae5a49649457d…` | false |
| 046V | definite.spinor_regular | false | `8e.yaml:bbc4bc1e7cd52362…` | false |
| 046W | definite.regular | false | `62.yaml:8ecff20411144a35…` | false |
| 046W | definite.spinor_regular | false | `62.yaml:093875f702e18c06…` | false |
| 04IE | definite.regular | false | `7c.yaml:7d8924bc68da14b7…` | false |
| 04IE | definite.spinor_regular | false | `7c.yaml:ab2864b736e03f99…` | false |
| 04II | definite.regular | false | `94.yaml:368700f6b96cc001…` | false |
| 04II | definite.spinor_regular | false | `94.yaml:a4d58d79dd742103…` | false |
| 04JO | definite.regular | false | `fb.yaml:8bcdbdfda74f1906…` | false |
| 04JO | definite.spinor_regular | false | `fb.yaml:231f60512e3b6df0…` | false |
| 04PB | definite.regular | false | `a6.yaml:33cc4027ae539179…` | false |
| 04PB | definite.spinor_regular | false | `a6.yaml:6787cbdb23d5e062…` | false |
| 04Q6 | definite.regular | false | `d5.yaml:3223034629ebbf8c…` | false |
| 04Q6 | definite.spinor_regular | false | `d5.yaml:110d80530099360a…` | false |
| 04Q7 | definite.regular | false | `04.yaml:15e7fc7d2efe4218…` | false |
| 04Q7 | definite.spinor_regular | false | `04.yaml:f09923b930feba5a…` | false |
| 04Q9 | definite.regular | false | `c6.yaml:66a8f9fb4d3f8511…` | false |
| 04Q9 | definite.spinor_regular | false | `c6.yaml:0d7f7760e31f558c…` | false |
| 04QO | definite.regular | false | `9a.yaml:1731c5e3b0ac50fc…` | false |
| 04QO | definite.spinor_regular | false | `9a.yaml:510ca373216eff27…` | false |
| 04XM | definite.regular | false | `da.yaml:43404c409d964f36…` | false |
| 04XM | definite.spinor_regular | false | `da.yaml:be80c330b8ad8fa9…` | false |
| 04Y8 | definite.regular | false | `34.yaml:a403d73aed021a9b…` | false |
| 04Y8 | definite.spinor_regular | false | `34.yaml:c87cde601b4df0cd…` | false |
| 04Y9 | definite.regular | false | `d4.yaml:2733229805d77ead…` | false |
| 04Y9 | definite.spinor_regular | false | `d4.yaml:5f1afc58f81e01ea…` | false |
| 04YM | definite.regular | true | `ee.yaml:fdeb54774172af09…` | true |
| 04YM | definite.spinor_regular | true | `ee.yaml:c5ef2b843b5cbfe7…` | true |
| 054R | definite.regular | false | `64.yaml:9ad8de1ca8094531…` | false |
| 054R | definite.spinor_regular | false | `64.yaml:b90f51ebeb9d086e…` | false |
| 054U | definite.regular | false | `dc.yaml:e236aa27c8ec4dfa…` | false |
| 054U | definite.spinor_regular | false | `dc.yaml:e241029caaf95cad…` | false |
| 0557 | definite.regular | false | `fe.yaml:5ce8b75cd93ab7de…` | false |
| 0557 | definite.spinor_regular | false | `fe.yaml:f29af5c3261f22f6…` | false |
| 05CW | definite.regular | false | `3e.yaml:683c5f22e2fcf0b0…` | false |
| 05CW | definite.spinor_regular | false | `3e.yaml:9492dcd8f2c9c556…` | false |
| 05VD | definite.regular | false | `31.yaml:7b51e2a9890f4ba4…` | false |
| 05VD | definite.spinor_regular | false | `31.yaml:91112fcab97e0ca8…` | false |
| 063G | definite.regular | false | `f4.yaml:2d988bd40af8aa3c…` | false |
| 063G | definite.spinor_regular | false | `f4.yaml:93dccb1715d40e45…` | false |
| 064C | definite.regular | false | `44.yaml:92faa2ae025709ca…` | false |
| 064C | definite.spinor_regular | false | `44.yaml:ca945f7a939556a3…` | false |
| 06NV | definite.regular | true | `51.yaml:8969581fd1d2bc09…` | true |
| 06NV | definite.spinor_regular | true | `51.yaml:2d1a898905988609…` | true |
| 06O4 | definite.regular | true | `71.yaml:25894399eaaf5dff…` | true |
| 06O4 | definite.spinor_regular | true | `71.yaml:be8267ea739ddc83…` | true |
| 3ICB | definite.regular | false | `1c.yaml:e877232fc32c24ec…` | false |
| 3ICC | definite.regular | false | `73.yaml:a6f621bde144d8b9…` | false |
| 3ICD | definite.regular | false | `d6.yaml:c84d5904c8a3fe63…` | false |
| 3ICE | definite.regular | false | `de.yaml:5546b04ebf5fc14e…` | false |
| 3ICF | definite.regular | false | `0e.yaml:6c976e68d4a0a795…` | false |
| 3ICI | definite.regular | false | `e8.yaml:c36c1f4c29c41806…` | false |
| 3ICJ | definite.regular | false | `f1.yaml:1299e7b9ccdbce8e…` | false |
| 3ICK | definite.regular | false | `60.yaml:3ee5857d22a22931…` | false |
| 3ICL | definite.regular | false | `54.yaml:1686d77a0367a844…` | false |
| 3ICM | definite.regular | false | `15.yaml:0217d66955237327…` | false |
| 3ICN | definite.regular | false | `36.yaml:269bf1024d08f223…` | false |
| 3ICO | definite.regular | false | `f7.yaml:f6a6b65317e00a2b…` | false |
| 3ICP | definite.regular | false | `16.yaml:809b85df1d243f1d…` | false |
| 3ICQ | definite.regular | false | `a4.yaml:12154018727473fe…` | false |
| 3ICR | definite.regular | false | `a1.yaml:dee3f493ae23c551…` | false |

## The gate

`verify` has run 54 times. The newest is `44624851354` (`workflow_dispatch`, head `ff3a497ebf`): its `plan` job
produced the two jobs the tags name, `shard 0/16` and `shard 1/16`, and both failed the step `Verify lattice cards
and certificate hashes` (22:36:48 and 22:46:07 on 2026-11-19). **No `verify` run exists on `2e19fbae7e` or
`4457a42676`**: the runs API listed at 2026-11-20T00:41Z has that failure as its newest, and the workflow's schedule
is `17 3 * * *`, so the next scheduled run is 03:17 UTC. Shards 0 and 1 therefore cannot be confirmed from CI here —
the missing input is a `verify` dispatch with `tags: 6JRR 029J`, which needs workflow write; this connection has
none. What is measured locally, at `c7d741a0ef`: `checks.records.problems` over the 103 cards in one process reports 0
problems, and `tests/test_stored_records.py::test_a_search_certificate_is_stated_by_the_card_it_names` passes
(1 passed in 48.0 s). A later shard run that changes only `exceeded.yaml` or `failures/` moves the tip without
touching a card.
