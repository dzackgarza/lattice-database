# #27: the three modules, each alone in the image, against sage-extensions main

Run for the issue's acceptance: *"the three modules pass in the image, or each remaining failure has a
sage-extensions issue with a reproduction and a blocked-by edge to it."*

| | |
| --- | --- |
| sage-extensions | `5fc4e0119b21c4b0aecb4fa26a24b99d84d8f40d` (`Merge remote-tracking branch 'refs/remotes/omm/main'`), main, imported from `/sage-ext/src` |
| image | `ghcr.io/dzackgarza/sage:develop`, config digest `sha256:2d6a4754b6f1518af356dd28ac6ec2e7678c7fe4ab0d70c2e7c9ecbc2c605eca`, through `~/sage-image/run.sh` |
| lattice-database | `587d56febe` |
| interpreter | `/sage/.venv/bin/python` (3.14), `PYTHONPATH=/sage-ext/src:/repo/research/src:/repo/src`, started with `import sage.all` as the workflow does |

Each module was run alone, in a process of its own:

    $ pytest -q tests/source_intake/test_nebe_sloane_source.py
    sage_extensions: /sage-ext/src/sage_extensions/__init__.py
    ....                                                                     [100%]
    4 passed in 10.32s

    $ pytest -q tests/test_construction_corpus.py
    sage_extensions: /sage-ext/src/sage_extensions/__init__.py
    ......                                                                   [100%]
    6 passed in 38.65s

    $ pytest -q tests/validation/test_construction.py
    sage_extensions: /sage-ext/src/sage_extensions/__init__.py
    ============================= slowest 4 durations ==============================
    1679.94s call     tests/validation/test_construction.py::test_stored_lattice_morphisms_construct_in_the_preamble
    353.82s call     tests/validation/test_construction.py::test_integral_root_span_sum_embeddings_construct_in_the_preamble
    4.61s setup    tests/validation/test_construction.py::test_stored_lattice_morphisms_construct_in_the_preamble
    3 passed in 2039.93s (0:33:59)

Three of three pass, so nothing is left for a sage-extensions issue under this acceptance.

What each module's earlier failure was, and where it was repaired:

| module | failure at `fa05071d75` | repaired by |
| --- | --- | --- |
| `test_nebe_sloane_source.py` | `int(formed.determinant())` on the owner's rational element | `d62dc45f00` — read through the element's `numerator()`/`denominator()`, as `records.derive` reads it |
| `test_construction_corpus.py` | `surjectivity_premise` refused by `TensorProductModuleMorphismMethods.__init__` | nothing here: the owner's main accepts it (`7b222e8621` refuses, `main` accepts); no assertion touched |
| `test_validation/test_construction.py` | exit 137, killed for memory | `69e16ad530` — one card at a time, and the morphism check in eight chunks of two concurrent processes |

The 33 min 59 s is the construction of the stored morphisms of 302,504 cards — 1,679.94 s of it in
that one test — with the preamble's own `Mor` and image evaluation; it is bounded and it completes,
which is what this acceptance asks.
