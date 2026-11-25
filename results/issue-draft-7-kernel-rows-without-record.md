# Draft issue: the kernel plane rows have no computation route on the card's own worker

**Not filed.** This connection cannot create issues on `dzackgarza/lattice-database`; this is the
issue to file, and `lattices/6JRR.md` and `results/evidence-7-plane-rows.md` name it.

## The item

The kernel plane counts on `lattices/6JRR.md` — `Otilde`, `Otilde+`, `SOtilde`, `SOtilde+`, all
189720 — are **stored and certified**, carried from sage-extensions' record
(`results/issue286-the-stage-1-call.md:275`, `:285`, `:372`, `:373` at
`47865446a7c37c85d873f91ac9d74cea472e208c`) and the two transport lemmas proved on this card
(`results/verify-7-plane-sign-witnesses.py`, `results/verify-7-kernel-plane-transport.py`). No value is
missing.

What is missing is the ability of this database's own worker to compute those rows, which matters
because a certified computation is the repository's preferred provenance and a citation is the
fallback:

| row | what a computation would need |
| --- | --- |
| `Otilde` | one parabolic walk, 1813–2171 s of cusps at 3.3–3.5 GiB, on a host with ~4 GiB free |
| `SOtilde` | the same; its route is available (index 93997183795200, determinant kernel only) |
| `Otilde+` | already computed here once (2000 s, 3.3 GiB, 2026-11-19) — the route works |
| `SOtilde+` | no route: its finite character quotient is killed on this host (594 s alone, 676 s as the fourth of one process), and `_plane_orbit_from_parabolic_stabilizer` refuses a two-sign-kernel subgroup by name (`orthogonal_quotients.py:4237`) |

## What would close it

- A runner of the certify workflow's size (16 GiB) running
  `certify --tag 6JRR --field 'primitive_orbits[Otilde].planes' --field 'primitive_orbits[SOtilde].planes' --phase fields`:
  the two rows are ~2000 s each at 3.3 GiB, inside one job's budget.
- For `SOtilde+`: sage-extensions admitting a two-sign-kernel subgroup to the plane route, or a
  record of that subgroup's own row.

## Why it is long tail and not an acceptance

A full-scale plane row is long tail and never an acceptance (AGENTS.md, 2026-11-19). Every row of
`integral.primitive_orbits` on this card states its plane count and each is either computed here or
carried from a record with a proof; what remains is a route this host does not have.
