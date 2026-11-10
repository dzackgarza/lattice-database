# #26 and #6: verify run 42844490886, and the contradictions its shards report

Dispatcher: 188412a150 (the landed #26 swap patch). Read from the Actions API at 18:35Z and 18:50Z.

## #26's acceptance: the swap step passes on every shard

| | |
| --- | --- |
| shards whose step "Give this shard its swap and state its memory ceiling" succeeded | **16 of 16** |
| shards whose step "Verify lattice cards and certificate hashes" ran | 16 of 16 (none skipped) |

That is the whole of #26: the step turns the runner's own swap off, allocates its own, enables it and
states the ceiling; a runner that refused would have failed the step, and none did. Before the patch
(run 42823977953) 14 of 16 shards died at that step and the verification never started.

**The peak lines are not readable from here.** `latticedb verify --shard i/16` prints
`memory: <x> GiB peak for this process` on stderr, which lands in the job log; downloading a job log
needs repository-admin rights (`403 Must have admin rights to Repository`), and the shard check runs
carry no `output.summary`/`output.text` (checked: 0 of 18). So the peaks are recorded — in the run's
logs — but this connection cannot quote them. What it can quote is the conclusion of every step, above,
and each shard's own problem count, reproduced below.

## #6: every shard completes over its cards and reports

The verify step exits nonzero on 15 of the 16 shards, and shard 3 had not finished when this was read.
It is not a memory kill and not a cancellation: each shard read its cards and reported the
contradictions it found — which is what #6 asks the workflow to do. The report is the failure.

Reproduced here per shard, with the verifier's own guard, on this tree before the repairs below
(`results/evidence-6-verify-run.log` has the raw output): 265 contradictions over 16 shards.

| class | fields | what it is |
| --- | --- | --- |
| `unstated` | 220 on 120 cards | a certificate in `certificates/` and no value on the card — **#23**, deferred by the owner |
| `uncited` | 16 on 6 cards | value and certificate agree, the card cites nothing — **#21's class, recurring** |
| `uncarded` | 26 on 8 cards | the card cites a hash `certificates/` does not hold — a certification run wrote the card and lost the entry |
| `mismatch` | 0 | — |

## What this turn repairs, and what it leaves

**`uncited`, 16 fields on 0269, 026A, 02AI, 028L, 02A4, 02A9.** These cards were certified by a run
that pushed before the card merge driver landed, so the same defect #21 closed: the stored value
hashes to its shard's entry and the card cites nothing. `results/repair-21-citations.py`, extended to
these six, restores the references and refuses to write a card whose value does not hash to the entry.

**`uncarded`, 26 of the 29 missing entries.** `results/evidence-6-verify-run.log`'s companion run
certified the eight affected cards in a corpus of their own, and each recomputed certificate was
restored to `certificates/` **only where the card's own stored value hashes to it** — so the card and
the ledger agree, and no entry was minted for a value the card does not state. Three were skipped for
exactly that reason (58S6's `automorphisms.automorphism_group_generator_morphisms` and
`integral.local_densities`, 5989's `automorphisms…`): the card states no value for them and a full
recomputation would have to write one.

**Still open, and not this turn's:**

- the 220 `unstated` regularity fields: #23, "deferred behind the current stage-1 mathematical
  results", whose acceptance is the owner's decision between recomputing the values and retracting the
  orphaned certificates;
- 5989's `integral.modular_scale`, `anisotropic_primes` and `local_representations`, because its
  certification cannot finish — see the owner defect below.

After the repairs, the same scan reports **220 `unstated` and 3 `uncarded`**, with no `uncited` and no
`mismatch`: **223** contradictions, all of them the two open items.

## The owner defect that blocks 5989 and 58S6

`sage_extensions.categories.isotropic_orbits._isotropic_orbit_representatives` imports a module that
does not exist, so `integral.primitive_orbits` dies for every indefinite card that reaches it:

    $ PYTHONPATH=/sage-ext/src:... python -c "
        from sage.all import ZZ; from sage_extensions.categories.lattices import Lattices
        print(Lattices(ZZ)([[-1,0,0,0],[0,2,0,0],[0,0,-4,2],[0,0,2,-4]]).primitive_orbit_series())"
    ...
    File "/sage-ext/src/sage_extensions/categories/lattice_orbit_invariants.py", line 143, in _primitive_isotropic_line_series
        "constant": subgroup.isotropic_orbit_representatives(1).cardinality(),
    File "/sage-ext/src/sage_extensions/categories/lattice_morphisms.py", line 4378, in isotropic_orbit_representatives
    File "/sage-ext/src/sage_extensions/categories/isotropic_orbits.py", line 1308, in _isotropic_orbit_representatives
        from sage_indefinite_port.indefinite.witt_one_hilbert import isotropic_line_representative
    ModuleNotFoundError: No module named 'sage_indefinite_port.indefinite.witt_one_hilbert'

Measured against sage-extensions main (`38f8109`) and `sage-indefinite-port` main, whose
`indefinite/` package holds `edgewalk*.py`, `eichler.py`, `exact_isotropic.py`, `isotropic_induction.py`,
`lorentzian_cells.py`, `pointwise_shell.py`, `recursive.py`, `scaled_shells.py` — no
`witt_one_hilbert`. The module was renamed or removed upstream and sage-extensions still names it.
That is not this repository's to repair and no issue can be filed from this connection; the
reproduction above is for the orchestrator to file against sage-extensions.
