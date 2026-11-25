r"""#43: store the one cusp row whose count a computation decides, certify it, and verify the card.

Sterk's (4.3.6), p. 21, is the cusp of $\Gamma_{\mathrm{En},2}$ whose chamber has exactly one root of
$K_J = \eta^\perp/\mathbb{Z}\eta$ among its walls: the other nine walls are of square $-4$.  The orbits of a family of
one class are one orbit whatever the group acting is --- a one-element set has one orbit --- so that row's count is
decided without any generating family of the cusp stabilizer, which is what `generation_obstruction()` withholds at a
primitive isotropic line (sage-extensions#312) and what stops the other three cusped rows.

The row is computed from the card's own Gram tensor and its own chamber: the walls orthogonal to the cusp, of square
$-2$, one per class modulo the cusp.  It is written by `genus.store_cusp_root_orbits`, whose certificate's provenance
names this program, and the shard entry is written beside it.  The last step asks `checks.records.problems` of the
card alone whether the card's reference, the value and the shard agree.

    run.sh -w /repos/lattice-database -b <repo>:/repos/lattice-database -b <clone>:/repos/sage-extensions \
        -- env PYTHONPATH=/repos/research/src:/repos/lattice-database/src python results/store-43-cusp-root-orbits.py
"""

from fractions import Fraction
from pathlib import Path

from sage.all import ZZ, matrix, vector

from latticedb import certificates, checks, corpus, genus
from latticedb.model import Lattice

ROOT = Path("/repos/lattice-database")
TAG = "029J"
GROUP = "gamma-en-2"
STATEMENT = "4.3.6"

path = ROOT / "lattices" / f"{TAG}.md"
document = corpus.read_card(path)
metadata = corpus.front_matter(document)
lattice = Lattice.model_validate(metadata)
gram = matrix(ZZ, metadata["gram_tensor"])
chamber = next(row for row in metadata["integral"]["cusp_chambers"][GROUP] if row["statement"] == STATEMENT)
cusp = vector(ZZ, chamber["cusp"])


def same_class(left, right) -> bool:
    """Whether two lifts differ by a rational multiple of the cusp, which is what one class in K_J means."""
    difference = [int(a) - int(b) for a, b in zip(left, right)]
    ratio = None
    for entry, coordinate in zip(difference, cusp):
        if coordinate == 0:
            if entry != 0:
                return False
            continue
        step = Fraction(int(entry), int(coordinate))
        if ratio is None:
            ratio = step
        elif ratio != step:
            return False
    return True


roots = []
for wall in chamber["walls"]:
    x = vector(ZZ, wall["vector"])
    if int(x * gram * cusp) != 0 or int(x * gram * x) != -2:
        continue
    if all(not same_class(x, seen) for seen in roots):
        roots.append(x)

assert len(roots) == 1, f"{STATEMENT}: {len(roots)} root classes, and this program stores only a decided count"
representative = [int(entry) for entry in roots[0]]
assert int(vector(ZZ, representative) * gram * cusp) == 0
assert int(vector(ZZ, representative) * gram * vector(ZZ, representative)) == -2

row = {
    "cusp": [int(entry) for entry in cusp],
    "statement": STATEMENT,
    "printed_page": chamber["printed_page"],
    "orbits": [{"representative": representative, "classes": [representative], "transporter_order": 1}],
    "orbit_count": 1,
}
by = (
    "results/store-43-cusp-root-orbits.py: the cusp's root family has one class, so one orbit under any group "
    f"(the walls of {STATEMENT} orthogonal to the cusp and of square -2, one per class modulo the cusp, computed from "
    "the card's Gram tensor)"
)

held = certificates.load(ROOT, tags=(TAG,))
genus.store_cusp_root_orbits(path, GROUP, [row], by, held)
certificates.save(ROOT, held, tags=(TAG,))
print("stored", f"{TAG} integral.cusp_root_orbits[{GROUP}] at {STATEMENT}", "hash", lattice.certifications.get("integral.cusp_root_orbits"))

reloaded = Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
assert reloaded.integral is not None and reloaded.integral.cusp_root_orbits is not None
stored = reloaded.integral.cusp_root_orbits[GROUP]
print("rows on the card", [(entry.statement, entry.orbit_count, len(entry.orbits)) for entry in stored])

entry = corpus.Entry(reloaded, corpus.read_card(path).content, path)
loaded = corpus.Corpus(
    entries=(entry,),
    families={},
    retired={},
    geometric=(),
    geometric_families=(),
    graphs=(),
    genera=(),
    polytopes=(),
    toric_varieties=(),
    geometric_maps=(),
    local_systems=(),
    operators=(),
    moduli_problems=(),
    lattice_families=(),
    lie_groups=(),
    arithmetic_groups=(),
)
held = certificates.load(ROOT, tags=(TAG,))
problems = [problem for problem in checks.records.problems(loaded, held, frozenset({TAG})) if "cusp_root_orbits" in problem]
print("problems naming the field:", problems)
assert problems == []
