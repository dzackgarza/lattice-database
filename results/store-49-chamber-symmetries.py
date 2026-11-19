"""#49: store the chamber symmetries at Sterk's cusps on card 029J, and drop `transporter_order` from 029J and 6JRR.

For each row of `integral.cusp_root_orbits['gamma-en-2']` on card 029J this computes, from the card's Gram tensor,
the permutations of the chamber's walls (`integral.cusp_chambers`, same statement) that keep the wall Gram matrix,
checks that each is an isometry of K_J = v^perp / Z v, and stores the group they form as the row's
`chamber_symmetries`: its order and a small generating set as permutations of the walls. That group is the image S
of Gamma_v in the symmetry group of the Coxeter diagram (Sterk 1991, (4.3.2), p. 17, and (4.3.3), p. 18), because
Sterk states that every symmetry is realized in Gamma_v at (4.3.7), p. 22, (4.3.8), p. 23, and (4.3.9), p. 24, and
(4.3.6), p. 21, has none. The (4.3.7) order is compared with Sterk's printed G_v = {+-1} W_v x| Z/2.

    sage-docker-python results/store-49-chamber-symmetries.py            # check, write nothing
    sage-docker-python results/store-49-chamber-symmetries.py --write    # write both cards and their certificates
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / "src"), "/repos/research/src", "/repos/sage-extensions/src"]

from sage.all import ZZ, PermutationGroup, matrix, vector  # noqa: E402

from latticedb import certificates, corpus, genus, records, storage  # noqa: E402
from latticedb.model import Lattice  # noqa: E402

WRITE = "--write" in sys.argv[1:]
STERK_PRINTED_ORDER = {"4.3.7": 2}  # (4.3.7), p. 22: G_v = {+-1} W_v x| Z/2


def boundary(gram, cusp):
    """A Z-basis of K_J = v^perp / Z v as rows, and the coordinate map of v^perp into it."""
    perp = matrix(ZZ, [list(gram * cusp)]).right_kernel_matrix()
    c = perp.solve_left(cusp)
    _, _, change = matrix(ZZ, [list(c)]).smith_form()
    basis = change.inverse()
    assert vector(ZZ, basis[0]) in (c, -c)
    quotient = basis[1:] * perp

    def coords(x):
        return vector(ZZ, (perp.solve_left(x) * change)[1:])

    return quotient * gram * quotient.transpose(), coords


def wall_symmetries(g):
    """Every permutation of the walls that keeps their Gram matrix g."""
    n = g.nrows()
    found = []

    def extend(partial):
        i = len(partial)
        if i == n:
            found.append(list(partial))
            return
        for j in range(n):
            if j in partial or g[j, j] != g[i, i]:
                continue
            if all(g[i, k] == g[j, partial[k]] for k in range(i)):
                partial.append(j)
                extend(partial)
                partial.pop()

    extend([])
    return found


def is_isometry_of_boundary(gram, cusp, walls, permutation):
    """The linear map of K_J (x) Q that the permutation defines is integral, unimodular and keeps the form."""
    form, coords = boundary(gram, cusp)
    source = matrix([coords(w) for w in walls])
    target = matrix([coords(walls[j]) for j in permutation])
    assert source.rank() == form.nrows(), "the walls span K_J (x) Q"
    image = source.solve_right(target)  # rows are coordinates in K_J, so wall i goes to wall p(i) under x -> x * image
    if source * image != target:
        return False
    return all(x in ZZ for x in image.list()) and abs(image.det()) == 1 and image * form * image.transpose() == form


card = ROOT / "lattices" / "029J.md"
document = corpus.read_card(card)
metadata = corpus.front_matter(document)
gram = matrix(ZZ, metadata["gram_tensor"])
block = dict(metadata["integral"])
chambers = {row["statement"]: row for row in block["cusp_chambers"]["gamma-en-2"]}
rows = dict(block["cusp_root_orbits"])
en = []
for row in rows["gamma-en-2"]:
    row = dict(row)
    chamber = chambers[row["statement"]]
    cusp = vector(ZZ, row["cusp"])
    walls = [vector(ZZ, wall["vector"]) for wall in chamber["walls"]]
    g = matrix(ZZ, [[w * gram * u for u in walls] for w in walls])
    found = wall_symmetries(g)
    assert all(is_isometry_of_boundary(gram, cusp, walls, p) for p in found), row["statement"]
    group = PermutationGroup([[i + 1 for i in p] for p in found], domain=list(range(1, len(walls) + 1)))
    assert group.order() == len(found), "the Gram-preserving permutations form a group"
    generators = [tuple(gen(i + 1) - 1 for i in range(len(walls))) for gen in group.gens_small() if not gen.is_one()]
    printed = STERK_PRINTED_ORDER.get(row["statement"])
    assert printed is None or printed == group.order(), (row["statement"], group.order(), printed)
    row["orbits"] = [{k: v for k, v in dict(orbit).items() if k != "transporter_order"} for orbit in row["orbits"]]
    row["chamber_symmetries"] = {"order": int(group.order()), "generators": [list(map(int, gen)) for gen in generators]}
    print(f"029J ({row['statement']}): {len(walls)} walls, S of order {group.order()}, generators {generators}")
    en.append(row)
rows["gamma-en-2"] = en
block["cusp_root_orbits"] = rows
metadata["integral"] = block
lattice = Lattice.model_validate(metadata)
computation = genus.name("029J", "cusp_root_orbits", lattice.definiteness)
digest = certificates.certification_hash(computation, lattice, genus.certified_value("cusp_root_orbits", rows, lattice))
print(f"029J: {computation} = {digest}")
BY_EN = (
    'H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991), 1-36: '
    "(4.3.6), p. 21, has one root wall; (4.3.7), p. 22, (4.3.8), p. 23, and (4.3.9), p. 24, state that the diagram "
    "symmetries are realized in Gamma_v, so each orbit is one orbit. chamber_symmetries is the image S of Gamma_v in "
    "the symmetry group of the chamber's Coxeter diagram ((4.3.2), p. 17, G = W(G) x| S; (4.3.3), p. 18): "
    "results/store-49-chamber-symmetries.py computes the Gram-preserving permutations of each chamber's walls from this "
    "card, checks each is an isometry of K_J = v^perp/Zv, and finds orders 1, 2, 2, 8, the (4.3.7) order agreeing with "
    "Sterk's printed G_v = {+-1} W_v x| Z/2"
)

TAG = "6JRR"
co_card = ROOT / "lattices" / f"{TAG}.md"
co_document = corpus.read_card(co_card)
co_metadata = corpus.front_matter(co_document)
co_block = dict(co_metadata["integral"])
co_rows = {
    key: [
        {**dict(row), "orbits": [{k: v for k, v in dict(o).items() if k != "transporter_order"} for o in row["orbits"]]}
        for row in value
    ]
    for key, value in dict(co_block["cusp_root_orbits"]).items()
}
co_block["cusp_root_orbits"] = co_rows
co_metadata["integral"] = co_block
co_lattice = Lattice.model_validate(co_metadata)
co_computation = genus.name(TAG, "cusp_root_orbits", co_lattice.definiteness)
co_digest = certificates.certification_hash(
    co_computation, co_lattice, genus.certified_value("cusp_root_orbits", co_rows, co_lattice)
)
print(f"{TAG}: {co_computation} = {co_digest}")

if WRITE:
    for tag, path, doc, meta, blk, lat, comp, dig, by in (
        ("029J", card, document, metadata, block, lattice, computation, digest, BY_EN),
        (TAG, co_card, co_document, co_metadata, co_block, co_lattice, co_computation, co_digest, None),
    ):
        meta["certifications"] = {**lat.certifications, "integral.cusp_root_orbits": dig}
        storage.write_text(path, records.record_text({k: v for k, v in meta.items() if k != "integral"} | {"integral": blk}, doc.content))
        held = certificates.load(ROOT, tags=(tag,))
        held[comp] = certificates.Certificate(hash=dig, by=by if by is not None else held[comp].by)
        certificates.save(ROOT, held, tags=(tag,))
    print("written")
else:
    print("dry run: nothing written")
