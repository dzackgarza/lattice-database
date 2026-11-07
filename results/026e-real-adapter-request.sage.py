"""Run issue #16's real adapter request in the published Sage image, on a checkout of this repository.

The probe of attachments/026e-real-image-probe.log confirms, for the 026E lattice built with the
adapter's owned ring, that `primitive_orbit_series()["O"]["constant"]` is an element of the class
`sage_extensions.categories.sets.cardinals.Cardinalities.parent_class`, whose `int(constant)` and
`constant.cardinality()` both return 1, `is_finite()` returns True, and whose unadapted `json.dumps`
raises the run's reported TypeError. This script performs the adapter's own request on the same card,
prints the emitted JSON, and asserts that its value is the exact numeric value the owner returned. It
changes no file: the card check afterwards reads the card written by `latticedb certify --tag 026E
--phase fields` and shows its stored value.

    docker exec -i --workdir "$GITHUB_WORKSPACE" \
        --env "PYTHONPATH=$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
        sage-env /sage/.venv/bin/python results/026e-real-adapter-request.sage.py

and, for the ordinary path with a certificate:

    docker exec -i --workdir "$GITHUB_WORKSPACE" \
        --env "PYTHONPATH=$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
        sage-env /sage/.venv/bin/python -m latticedb certify --tag 026E --phase fields \
            --minutes 30 --workers 1
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

from latticedb import sage_genus

card = yaml.safe_load((Path("lattices") / "026E.md").read_text().split("---")[1])
lattice = sage_genus.Lattices(sage_genus.OWNED_ZZ)(card["gram_tensor"])
series = lattice.primitive_orbit_series()
constant = series["O"]["constant"]
assert constant.is_finite(), f"expected a finite cardinality: {constant!r}"
expected = int(constant)
assert expected == constant.cardinality()

emitted = sage_genus.VALUES["primitive_orbits"](lattice)
sage_genus._emit("026E", {"primitive_orbits": emitted})
line = json.dumps({"tag": "026E", "by": "research preamble", "primitive_orbits": emitted})
print("EMITTED_JSON", line)
assert json.loads(line)["primitive_orbits"]["O"]["constant"] == expected

print("CONSTANT_IS_FINITE", expected)
print("NONFINITE_CONVERSION", sage_genus._orbit_count(
    type("Infinite", (), {"is_finite": lambda self: False, "aleph_index": lambda self: 0})()
), "(the owner's own API for an infinite cardinality; not a lattice assertion)")
