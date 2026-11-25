# Issue #2, acceptance item by item

Issue: `dzackgarza/lattice-database#2`, *External catalogue cards: Nebe–Sloane and Elkies values cited on cards*.
Labels at the time of writing: `enhancement`, `epic`, `deferred`. No sub-issues (`sub_issues_summary.total` = 0),
which its own body makes the condition of being "opened for work".

The contract is the body. It asks, in one sentence, for three things:

1. a card for each lattice of the named catalogues — the Nebe–Sloane root and weight lattices and their duals,
   the Barnes–Wall series, the table of densest packings, the table of modular lattices, the individual entry
   pages, and Elkies' MW128 data;
2. the invariants those sources publish — Gram tensor, determinant, minimal norm, kissing number,
   automorphism group order — **as cited values**;
3. **a test per catalogue table** that the cards agree with the table.

## The recorded blocker

The issue's one comment (id 6633128418, 2026-07-10) is a hard dependency:
"**Blocked by dzackgarza/research#5 (sign convention).** Do not begin mining named-lattice Gram matrices /
invariant fixtures until dzackgarza/research#5 lands the AG negative-definite default."

That repository is outside this connector's single connected repository, and `github_issue` refuses an issue
that is not in the connected repository (`github_invalid_reference`), so **whether #5 has landed is not
verifiable from here**. Nothing in this turn mines a Gram matrix or an invariant fixture into a card: the
45 stored transcriptions under `sources/nebe_sloane/` and all 302,504 cards are unchanged, and the code change
is a parser completion whose effect is visible only on the next seeding pass (§"What changed").

## Item 1 — a card for each lattice of the named sources

The decisive test is the Gram tensor, not the name, for two recorded reasons: a dual lattice is never a second
record, it is `dual_gram_tensor` on the card of its primal (`README.md:210`), and the corpus names a lattice by
its form, so the root lattice A1 is the card named `<1>` with alias `I_{1,0}` (`lattices/0001.md:3-5`), and A2
is `lattices/0012.md` with its dual at `lattices/0012.md:34`. `gram-index.json` maps a Gram tensor to the tags
that state it (302,430 tags; the corpus holds 302,504 cards).

Probe: `results/probe-2-catalogue-coverage.py` (run in the research image; ~19 s).

### 1f — the individual entry pages (the standard-format archive, 823 rows)

| measure | value |
| --- | --- |
| rows | 823 |
| distinct names stating a `GRAM` section | 782 |
| names whose `GRAM` this intake cannot read | 50 |
| readable names whose Gram a card states | **731 of 732** |
| readable names with no card | 1 — `Shimada_86` |

`Shimada_86` is not a gap of ignorance: `tests/source_intake/test_nebe_sloane_source.py:172` reads its
86 × 86 matrix and asserts its determinant, minimal norm and kissing number (196608, 8, 109421928), and no
card was authored from it.

The 50 unreadable Gram sections are the exact failure of this item, with its line:

- 23 names print a **rational** Gram and are refused by `integer()`'s integrality assert
  (`src/latticedb/nebe_sloane.py:72-73`), because `Entry.gram_tensor` is typed
  `tuple[tuple[int, ...], ...]` (`src/latticedb/nebe_sloane.py:54`): `D2*`, `D3*` … `D24*`, `Bring8`.
  This is the whole of "the root lattices **and their duals**" for D_n: the catalogue's dual Gram entries are
  half-integral (`.500000000000E+00`), while a card's `gram_tensor` does admit a rational component
  (`README.md:207`), so the restriction is the intake's, not the schema's.
- 9 print a matrix program rather than components (`B45`, `P60q`, `dim52min5`, `dim56min6`, `dim68min6`,
  `mcc`, `((5+sqrt(5))/2)*P48n`, `(4+sqrt(5))*P48n`, `Z2P48n`): `components` reads those rows at
  `src/latticedb/nebe_sloane.py:124-131` and only `GRAM_MATRIX` gets the Maple reader
  (`src/latticedb/nebe_sloane.py:198`).
- 16 sections hold a token `Decimal` refuses (`KAPPA10`, `36MIN3`, `dim11kis308.std` … `dim15kis1872.std`).
- 2 fit neither layout (`E7*`, `OBW16*`): the count assert at `src/latticedb/nebe_sloane.py:130`.

### 1a–1c — root, weight and dual lattices

Of the 24 `A_n`, 24 `A_n*`, 25 `D_n` (the catalogue has `D25`) and 22 `D_n*` rows (`D9*` is not a row), every
readable one has a card by Gram. The `D_n*` family is the 1c failure above and only that: **all 22 `D_n*` rows**
are refused, so no dual of a D lattice can be seeded from this archive at all.

### 1d — the Barnes–Wall series

The catalogue defines `BW4 = D4`, `BW4' = D4*`, `BW8 = E8`, `BW8' = E8_code`, `BW16 = LAMBDA16`,
`BW32 = KV32RM` (index page, `NAME="BW"` and 16-dimensional entries). Five of the six are on cards under their
catalogue names — `BW4` is the `D4` card, `BW8` the `E8` card, `BW8'` the card named `E8 (coding theory
version)`, `BW16` the `LAMBDA16` card and `BW32` the card named `2^1+10.O10^+(2) = BW32`; `BW4' = D4*` is the
rational row §1f refuses and is represented, by `README.md:210`, as `D4`'s `dual_gram_tensor`. But **no
Barnes–Wall family tag exists**: `families.yaml:8` is the only Nebe–Sloane family, `nebe-sloane-catalogue`, and
`rg -i barnes families.yaml` is empty. So the series is carded and unlabelled; a `where: families: barnes-wall`
page cannot be built from the corpus as it stands.

### 1e — the table of densest packings

36 entries linked from <density.html>; **30 have a card by Gram**; 0 lack one; **6 are not archive rows**
(`LAMBDA22`, `LAMBDA23`, `CQ48a`, `P48p`, `P48q`, `CQ64b`) — that table is decided only by fetching those pages.
The table's own numbers are centre densities, which are not one of the five invariants the epic names and have
no field on a card; the last row is `MW_128` (§1g).

### 1e — the table of modular lattices

76 entries linked from <modular.html>; **25 have a card by Gram**; 0 of the archive rows lack one;
**51 are not archive rows** (`QQF.4.h`, `H4`, `F8.6`, `O10_mod`, `A12_mod`…`G26_mod`, `Beis13`, `Bhurw8`,
`P24.2`, `oddBW16`, …). The archive is not the whole catalogue, so those 51 are undecided by the Gram test and
need their entry pages.

### 1g — Elkies' MW128 data

`https://people.math.harvard.edu/~elkies/mv128.txt` was fetched on 2026-11-18. It states, for the
Mordell–Weil lattice `M` of `y² + y = x³ + t⁶⁵ + a₆` over `F₄₀₉₆`:

- kissing number `218044170240 = 2^17 · 3 · 5 · 13 · 19 · 449`;
- group order `76677120 = 2¹² · 65 · 24 · 12`;
- `2940` minimal-vector orbits with their stabiliser orders, and `Σ 1/S = 8531/3`.

That sum is consistent with the kissing number (`76677120 × 8531/3 = 218044170240`), so the file is a
citable source for two of the five invariants. **It publishes no Gram tensor and no determinant**: its vectors
are polynomial solutions of degree 22 and 33, and the lattice is defined by the curve, not by a Gram matrix.
A card is required to state `gram_tensor` as its defining datum (`README.md:206`), so this source cannot
produce a card of the kind the epic asks for; it can only supply `definite.kissing_number` and
`definite.automorphism_group_order` on a card whose Gram comes from somewhere else. No card named `MW128`,
`MW_128` or `MW80` exists.

## Item 2 — the published invariants as cited values

| invariant | where the intake puts it | state |
| --- | --- | --- |
| Gram tensor | `record()` → `gram_tensor` (`src/latticedb/nebe_sloane.py:220`) | read for 732 of 782 archive names; the 50 in §1f are the gap |
| determinant | `record()` → `determinant` (`src/latticedb/nebe_sloane.py:225-226`) | read from `DET` **or** `DETERMINANT` since this turn (`src/latticedb/nebe_sloane.py:186`); before, the 31 entries that name it `DETERMINANT` (`E7*`, `N(12A2)`, `HZ40`, …) were silently read as absent |
| minimal norm | `record()` → `definite.minimum` (`src/latticedb/nebe_sloane.py:227-230`) | read; but see below — `derive` discards it |
| kissing number | `record()` → `definite.kissing_number` (`src/latticedb/nebe_sloane.py:231-232`) | read; discarded by `derive` |
| automorphism group order | `record()` → `definite.automorphism_group_order` (`src/latticedb/nebe_sloane.py:233-234`, new) | the archive states it for **405 of 823 rows**; the intake read none of them before this turn |

The obstruction to "as cited values" is not the intake but `derive`: `_definite` rebuilds `minimum` from
`computation_lattice.minimum()` (`src/latticedb/records.py:216-226`) and `kissing_number` from
`computation_lattice.kissing_number()` (`src/latticedb/records.py:227`), and the loop that preserves authored
fields skips any field already in that block (`src/latticedb/records.py:244-246`). So a catalogue-cited
`definite.minimum` or `definite.kissing_number` is **replaced by the computed value** the first time `derive`
runs, and the citation survives only in the card's `references`, not in the value. That is the repo's own
contract, stated at `README.md:231`: "A completed computation replaces any disagreeing authored value in the
scope it computes and then certifies the resulting card value." Reconciling the epic's "cited values" with it
is a decision, not a defect: for a definite card the computed value is the stronger claim, and the catalogue's
number is then checked against it rather than asserted.

The group order is the one invariant where that is already the shape on the cards: `lattices/0110.md:9` carries
a certificate for `definite.automorphism_group_order` and `lattices/0110.md:59` the value 10321920, from
`L.orthogonal_group()` (`README.md:227`), not from the catalogue. The field exists
(`src/latticedb/invariant_models.py:964`) and `certify` asks for it (`README.md:225`).

One more gap with a line: `stored()` writes a transcription from the archive when the archive is present and
from the network otherwise (`src/latticedb/nebe_sloane.py:202-210`); 41 of the 45 stored entries are page-sourced
(`url` ends `.html`), and `stored_problems` returns early for those (`src/latticedb/nebe_sloane.py:250`). So the
only source↔card agreement check in the module **never runs for the 41 entries transcribed from entry pages**, which
are exactly the Lambda, Kappa, Niemeier and BW16 cards this epic is about.

## Item 3 — a test per catalogue table

| table | test | verdict |
| --- | --- | --- |
| the standard-format archive | `tests/test_bulk_sources.py:48-53` — 823 rows, ordinals 1…823, repeated names retained | a test of the source's shape, not of the cards |
| one archived entry against its card | `tests/source_intake/test_nebe_sloane_source.py:135` — `stored_problems(root, …) == []` on a one-card corpus | the mechanism exists and is exercised once |
| that the check **fails** when a card disagrees | `tests/source_intake/test_nebe_sloane_source.py:93` (new) | added this turn: the check names the card, not only passes |
| root/weight/dual, Barnes–Wall, densest packings, modular lattices, Niemeier | none | **nothing asserts a card against any of these tables** |
| Elkies MW128 | none | no card exists to assert |

So item 3 is **not met**: the corpus has no per-table card-agreement test for any of the epic's tables, and the
one agreement mechanism it has is scoped to the four archive-sourced cards. An exact statement of the failure:
`src/latticedb/nebe_sloane.py:250` excludes 41 of the 45 stored entries, and no test reads a table page
(`density.html`, `modular.html`) at all.

## The backlog this names

1. 50 archive names whose Gram the intake cannot read: 23 rational `D_n*`/`Bring8` (type at
   `src/latticedb/nebe_sloane.py:44`), 9 matrix-program blocks, 16 decimal tokens, 2 layout mismatches.
2. `Shimada_86`, the only readable archive entry with no card.
3. 6 densest-packing entries and 51 modular-table entries outside the archive, undecided without their pages.
4. No `barnes-wall` family tag in `families.yaml`.
5. No card for `MW80`/`MW128`; the 128-dimensional source publishes no Gram tensor.
6. No per-table card-agreement test, and `stored_problems` does not cover page-sourced cards.

## What changed

`src/latticedb/nebe_sloane.py` (parser only; no card and no stored transcription touched):

- `order()` and `_product_of()` (`src/latticedb/nebe_sloane.py:89-117`) read `GROUP_ORDER` in each of the seven
  forms the archive prints — `48`, `2^18`, `2^13*3^2`, `2^17 3^7 5 7 11 = 110361968640`,
  `737280 = 2^14 * 3^2 * 5`, `<2 10> <3 4>`, `<2, 12>, <3, 4>`, `[ <2, 9>, <3, 1> ]`,
  `|Aut| = 336 * 24 = 2^7 * 3^2 * 7 = 8064`, and the `*/ >;` tail one section carries — and refuse one whose
  forms disagree. Measured: **405 of 405** sections parse.
- `Entry.group_order` (`src/latticedb/nebe_sloane.py:52`), read at `src/latticedb/nebe_sloane.py:196`, written to
  `definite.automorphism_group_order` at `src/latticedb/nebe_sloane.py:233-234`, and compared by
  `stored_problems` at `src/latticedb/nebe_sloane.py:266`.
- `archive_entry` reads `DETERMINANT` when `DET` is absent (`src/latticedb/nebe_sloane.py:186`), which `fetch`
  already did at `src/latticedb/nebe_sloane.py:154`; 465 of 823 rows now yield a determinant instead of 434.

Tests: `tests/source_intake/test_nebe_sloane_source.py:47-110` (12 printed forms, the disagreement refusal, one
synthetic archive read, and the negative `stored_problems` case). `pytest tests/source_intake/test_nebe_sloane_source.py`
→ 19 passed; `pytest tests/test_bulk_sources.py` → 8 passed, in the research image with a current
`sage-extensions` bound over `/repos/sage-extensions`.

Evidence script: `results/probe-2-catalogue-coverage.py`.
