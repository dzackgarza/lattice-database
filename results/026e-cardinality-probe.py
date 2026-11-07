"""Run in the research image on a checkout of this repository, and paste back what it prints.

`latticedb certify --tag 026E --phase fields` died in the adapter's JSON emission with
`TypeError: Object of type Cardinalities.parent_class is not JSON serializable`, nested at
`primitive_orbits -> O -> constant` (job 128263401273 of run 42326648686). Issue #16's contract is that
the conversion is the returned object's own API, so this prints the object, its class, its public
attributes, and the candidates a conversion could use. The construction is the adapter's own
(`sage_genus._compute`): the owned integer ring, `Lattices(ring)(gram)`, then the owner's operation.

    docker exec -i --workdir "$GITHUB_WORKSPACE" \
        --env "PYTHONPATH=$GITHUB_WORKSPACE/research/src:$GITHUB_WORKSPACE/src" \
        sage-env /sage/.venv/bin/python results/026e-cardinality-probe.py
"""
import json
from pathlib import Path

import yaml

from sage_extensions.categories.lattices import Lattices
from sage_extensions.rings import session_ring_objects

ring = session_ring_objects()["ZZ"]
card = Path("lattices") / "026E.md"
gram = yaml.safe_load(card.read_text().split("---")[1])["gram_tensor"]
lattice = Lattices(ring)(gram)
series = lattice.primitive_orbit_series()
constant = series["O"]["constant"]

print("series groups:", sorted(series))
print("groups[O] keys:", sorted(series["O"]))
print("constant class:", type(constant).__name__, "| module:", type(constant).__module__)
print("constant mro:", [cls.__name__ for cls in type(constant).__mro__])
print("constant public attributes:", sorted(name for name in dir(constant) if not name.startswith("_")))
for name in ("is_finite", "is_infinite", "cardinality", "n", "value", "is_integer"):
    print(f"  {name}: {getattr(constant, name, '<absent>')!r}")
for expression in ("int(constant)", "constant.cardinality()", "constant.is_finite()"):
    try:
        print(f"  {expression} -> {eval(expression)!r}")
    except Exception as error:
        print(f"  {expression} raises {type(error).__name__}: {str(error)[:160]}")
try:
    print("json.dumps(series):", json.dumps(series)[:200])
except TypeError as error:
    print("json.dumps(series) raises TypeError:", error)
print("the whole value:", series)
print("its repr:", repr(series))
