# #43: the twenty lines the gate reported, and the values their certificates already held

`latticedb verify` reported twenty contradictions on three of the four 1/64 slices run last turn, and they were one
kind: a completed certificate whose card states no value. Eight definite cards — `02LP`, `3ICA`, `02BW`, `02O9`,
`02YE`, `0353`, `03UB`, `04R0` — carried `definite.regular` or `definite.spinor_regular` in `certificates/` with the
provenance `research preamble`, and stated neither the value nor a citation for either.

The value is not a judgement call. These are the only fields the gate reported that are
`bool | "true under GRH"`, so `certificates.certification_hash` over the three candidates commits to the card's Gram
tensor and the computation's name and decides which one the computation returned. `results/probe-43-regular-certificate.py`
found exactly one match per certificate, and `results/store-43-regular-values.py` wrote it:

| card | `regular` | `spinor_regular` |
| --- | --- | --- |
| 02LP | true | true |
| 3ICA | false | true (already stated and cited) |
| 02BW | true | true |
| 02O9 | false | false |
| 02YE | true | true |
| 0353 | false | false |
| 03UB | false | false |
| 04R0 | false | false |

Fifteen fields were written; `3ICA definite.spinor_regular` already stated its value and cited its certificate, which
is why the gate reported it nowhere. Each written card states the value and cites the certificate's hash under the same
field name. Nothing in `certificates/` was written, no hash changed, and `regular` and `spinor_regular` are not part of
`records.derived_projection`, so no `<tag> derive` certificate moved — the tagged probe below is what confirms that:
`checks.records.problems` on the eight cards with their certificates went from 20 problems to **0**.

## Why this is the repair and not a withdrawal of the certificates

A certificate is a computation's record: it says what was computed from the card's Gram tensor. Where the card lost the
value, the card is what is incomplete, and the certificate is what says which value to put back. Withdrawing the
certificate would delete the only evidence the value was ever computed, and re-minting would need the computation to
run again. Writing the value the certificate commits to is the one repair that adds nothing: the hash is unchanged and
the card now agrees with it.

## What this does not touch

The three `T_Co` rows of #43 (cusps 3–5) remain empty, and the reason recorded in
`results/evidence-43-coble-okj-complement.md` stands: `integral.cusp_root_orbits` is keyed by the eight standard
subgroups or by an arithmetic-group card of the same lattice, and 6JRR lists only `otilde-t-co` and
`otilde-plus-t-co` — there is no `gamma-co-2` card, and the person's standing decision is that the group's own draft
is not a citation, so such a card would have to be certified by computation. The eight cards above are unrelated to
that.
