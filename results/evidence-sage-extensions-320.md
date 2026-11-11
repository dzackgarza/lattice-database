# Comment for dzackgarza/sage-extensions#320 (not postable from this connection)

The GitHub connection in this project is scoped to `dzackgarza/lattice-database` and offers no issue
comment operation, so the reproduction below is recorded here for the orchestrator to post on
`sage-extensions#320`. Everything in it was measured in the pinned image
(`ghcr.io/dzackgarza/sage:develop`, Sage 11.0.beta5), against `sage-extensions` main `32e116e`.

---

**Reproduction: one form value on a rank-19 subobject costs 156 s, and `gram_matrix()` raises**

Consumer: `dzackgarza/lattice-database`, `tests/source_intake/test_hoehn_mason_source.py`
(row 81 of Höhn–Mason; the record card is `02AQ`, rank 19, inside the Leech lattice of rank 24). The
call path is

    hoehn_mason.automorphisms(leech, entry, record)
      -> hoehn_mason._record_isometry
      -> hashimoto.basis_isometry
      -> FormModules(ZZ).Mor(source, target).preserves_forms(module_map)

where `target` is the subobject `A ⊂ leech[1]` returned by `framed.subobject_on(...)`.

Measured with `time.monotonic()` around each call, `sage-extensions` at `32e116e`:

| call | time |
| --- | --- |
| `_leech_lattice` (build the rank-24 formed module) | 0.2 s |
| `_sublattice` (the rank-19 subobject and its inclusion) | 1.2 s |
| `source = _formed(record.gram_tensor).twist(twist)` | 1.4 s |
| **one `b(x, x)` on the subobject** — `sublattice.b(left, left)` for `left = sublattice.module_generators()[0]` | **156.65 s** |
| the same `b(x, x)` on the ambient Leech lattice | 0.014 s |
| the same `b(x, x)` on `source` | 0.011 s |
| `preserves_forms` from `source` into the *ambient* (a second route I tried) | 249.17 s |

So one form value on a subobject costs about four orders of magnitude more than the same value on the
ambient lattice or on a twisted lattice. `preserves_forms` asks for `rank²` of them — 361 at rank 19 —
which is the whole of the 70 minutes
`test_row_81_source_generators_are_the_seeded_self_isometries` took.

What the consumer sees, minimally:

    from sage.all import ZZ
    from sage_extensions.categories.modules.framed.formed.form_modules import FormModules
    # ... build the Leech formed module and its subobject A on a stored basis ...
    A.b(A.module_generators()[0], A.module_generators()[0])   # 156.65 s at rank 19
    L.b(L.module_generators()[0], L.module_generators()[0])   # 0.014 s, L the ambient

Related, and blocking the obvious workaround: the subobject's form cannot be read as a matrix at all.

    A.gram_matrix()
    AttributeError: 'RestrictedScalarsModules.parent_class' object has no attribute 'matrix_space'

`A.gram_tensor()` does work (1.9 s at rank 19) and is the same form on the same generators, which is
why rebuilding the module from that tensor answers the same question in seconds — but a consumer
rebuilding the owner's object is a second code path for one decision, so
`dzackgarza/lattice-database` does not do it: it decides on `target` itself and waits on this issue
(lattice-database#29 is blocked by it).

Expected, for that repository's suite: the row-81 tests go from ~70 minutes to the time their other
work takes.
