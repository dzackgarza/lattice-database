#!/usr/bin/env python3
"""Store lifts that generate H <= G_e on card 0125 (lattice-database#40).

Sterk's group is $G_e = \\rho_L^{-1}(P)$, where $L = U(2) \\oplus E_8(-2)$, $\\rho_L \\colon O(L) \\to O(A_L)$ is
the reduction of the discriminant representation and $P \\le O(A_L)$ is the stabilizer of $A_{U(2)}$
(H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991),
(4.3.5), p. 19). sage-extensions#354 (closed at `7ef38d52cf`) supplies the two calls that make $G_e$
expressible:

* `L.Aut().discriminant_point_stabilizer(A_{U(2)}).group_generators()` is the Schreier family of the
  $O(L)$-orbit of $A_{U(2)}$ (Seress, *Permutation Group Algorithms*, Lemma 4.2.1, p. 57). It
  generates $G_e$ and has `15 * 67456 - 67455 = 944385` members, which no card holds.
* `L.Aut().discriminant_point_stabilizer_image_generators(A_{U(2)})` returns the subfamily of it
  selected so that its images in $O(A_L)$ generate $P$. It does not return on this machine: three
  runs, at 845 s, 2600 s and 15 min, each ended inside the selection loop with no traceback, no
  value and exit status 0 (results/evidence-40-ge-generators.md records them).

The route stored here is the owner's other one, and it is the same mathematical content in fewer
members. $\\rho_L$ is onto $O(A_L)$, so every element of $P$ has a lift in $G_e$, and
`L.Aut().discriminant_lift(h)` returns one: it factors $h$ as a word in the images of $O(L)$'s own
selected generators and evaluates that word in $O(L)$. Lifting $P$'s three engine generators gives
three isometries of $L$ whose images generate $P$, so they generate a subgroup $H \\le G_e$ with
$\\rho_L(H) = P$. They do not generate $G_e$, whose remaining part is $\\ker \\rho_L = \\widetilde O(L)$,
for which no generating set exists (sage-extensions#597). So they are stored as generators of $H$,
never as generators of $G_e$, and $H$'s card states $\\rho_L(H) = P$.

What this program checks before writing, from the card's stored Gram tensor alone:

* each stored matrix is integral, unimodular and preserves the form, $M^t G M = G$;
* every lift induces an element of $P$ -- `discriminant_lift` checks each against $\\rho_L$ itself
  and raises instead of returning a wrong element -- and every image preserves $A_{U(2)}$;
* the images of the lifts generate a subgroup of $O(A_L)$ whose order is $P$'s, computed three ways:
  the engine's own stabilizer order, $|O(A_L)| / |\\mathrm{orbit}(A_{U(2)})|$ by the index--stabilizer
  identity, and the product of the two summands' isometry-group orders read from the two diagonal
  blocks of the card's Gram. A wrong point or a truncated lift breaks one of the three.
"""

from __future__ import annotations

import faulthandler
import json
import os
import resource
import threading
import time
from pathlib import Path

from latticedb import certificates, corpus, genus, records, storage
from latticedb.certificates import Certificate
from latticedb.model import Lattice
from latticedb.sage_genus import _matrix_rows
from sage_extensions.all import ZZ
from sage_extensions.categories.lattices import Lattices

ROOT = Path(__file__).resolve().parent.parent
TAG = "0125"
SLUG = "h-e"
SAGE_EXTENSIONS_REVISION = "2fb37d5a717fac890e9cbf239f63d3a97f487040"
"""The owner revision this ran at: `origin/main` of sage-extensions as fetched on 2026-11-17."""

ORDER = 46998591897600
"""$|O(A_L)|$ of the card's discriminant form, as the owner returns it."""

ORBIT = 67456
"""The cardinality of the orbit of $A_{U(2)}$ under $O(A_L)$, which is $[O(A_L) : P]$."""

TARGET = 696729600
"""The order of the subgroup the stored generators generate: 2 * 348364800 = |O(A_L)| / |orbit(A_U(2))| = 696729600."""

MEASURED_RUNS = (
    "The greedy subfamily call the issue names was run six times on this machine and none returned: four runs "
    "ended inside its selection loop over the 944385-member Schreier family with no value and no traceback, at "
    "845 s, 1075 s, 1404 s and 2600 s, one was still running at a 900 s cap, and a sixth had not finished "
    "building that family after 2662 s at 2.51 GiB"
)
"""What the call the issue names did on the machine this was computed on, in results/evidence-40-ge-generators.md."""


def provenance() -> str:
    """The certificate's account of this computation: what was asked of the owner, and at which revision."""
    return (
        "the owner's lifts along rho_L: P = Stab_{O(A_L)}(A_U(2)) from O(A_L).stabilizer_of_classes, and "
        "L.Aut().discriminant_lift of each of its generators (a word in O(L)'s selected generators, checked "
        f"against rho_L), at sage-extensions {SAGE_EXTENSIONS_REVISION}. |P| = {TARGET} is the engine "
        f"stabilizer's order, |O(A_L)|/|orbit| = {ORDER}/{ORBIT}, and 2 * 348364800 from the two summands; "
        "the images of the stored matrices generate P, so they generate H <= G_e with rho_L(H) = P. They do "
        "not generate G_e: G_e = Otilde(L) . H and no generating set of Otilde(L) exists (sage-extensions#597). "
        f"{MEASURED_RUNS} (results/evidence-40-ge-generators.md). results/generators-40-ge.py computed the "
        "matrices and these checks."
    )

START = time.time()


def stamp(label: str) -> None:
    print(f"[{time.time() - START:7.1f}s] {label} peak={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024} MiB", flush=True)


def watch(period: float = 60.0) -> None:
    """Report the resident size while an owner call runs, so a run that ends has a cost on record."""
    while True:
        time.sleep(period)
        stamp("running")


def preserves(matrix: list[list[int]], gram: list[list[int]]) -> bool:
    """Whether `matrix` is an isometry of the integral form `gram`: $M^t G M = G$."""
    size = len(gram)
    product = [[sum(matrix[k][i] * gram[k][l] * matrix[l][j] for k in range(size) for l in range(size)) for j in range(size)] for i in range(size)]
    return product == gram


def determinant(matrix: list[list[int]]) -> int:
    """The determinant of an integer matrix, by elimination over the rationals."""
    from fractions import Fraction

    rows = [[Fraction(entry) for entry in row] for row in matrix]
    size = len(rows)
    value = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if rows[row][column] != 0), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        value *= rows[column][column]
        scale = rows[column][column]
        rows[column] = [entry / scale for entry in rows[column]]
        for row in range(column + 1, size):
            if rows[row][column] != 0:
                factor = rows[row][column]
                rows[row] = [a - factor * b for a, b in zip(rows[row], rows[column], strict=True)]
    return int(value)


def main() -> None:
    path = ROOT / "lattices" / f"{TAG}.md"
    card = Lattice.model_validate(corpus.front_matter(corpus.read_card(path)))
    assert card.gram_tensor is not None
    gram = [[int(entry) for entry in row] for row in card.gram_tensor]
    lattice = Lattices(ZZ)(gram)
    stamp("lattice")

    form = lattice.discriminant_group()
    basis = tuple(lattice.module_generators())
    # The point is the two-class discriminant group of the U(2) summand, spanned by the classes of the
    # primitive duals of its two basis vectors; the remaining eight basis vectors span E8(-2) on the card.
    first = lattice.discriminant_class(lattice.primitive_dual(basis[0]))
    second = lattice.discriminant_class(lattice.primitive_dual(basis[1]))
    point = frozenset({form.zero(), first, second, first + second})
    assert len(point) == 4, "the classes of A_{U(2)} are two and their span is four"

    group = lattice.Aut()
    orthogonal = form.orthogonal_group()
    order = int(orthogonal.cardinality())
    stabilizer = orthogonal.stabilizer_of_classes(point)
    target = int(stabilizer.cardinality())
    assert (order, target) == (ORDER, TARGET), f"the owner returns |O(A_L)| = {order} and |P| = {target}, not the measured {ORDER} and {TARGET}"
    generators = tuple(stabilizer.group_generators())
    print(f"|O(A_L)| = {order}, |P| = {target}, P generated by {len(generators)}", flush=True)
    stamp("P and its generators")

    lifts = tuple(group.discriminant_lift(generator) for generator in generators)
    assert all(lift is not None for lift in lifts), "an element of P is not induced by an isometry of L, but rho_L is onto"
    stamp("lifts")

    matrices = [_matrix_rows(lift) for lift in lifts]
    dump = os.environ.get("GE_DUMP")
    if dump:
        Path(dump).write_text(json.dumps({"size": len(matrices), "matrices": matrices}, indent=1))
    for matrix in matrices:
        assert len(matrix) == card.rank and all(len(row) == card.rank for row in matrix)
        assert preserves(matrix, gram), "a lift's matrix is not an isometry of the card's form"
        assert abs(determinant(matrix)) == 1, "a lift's matrix is not unimodular"
    stamp("matrices preserve the form")

    # rho_L(H) = P, from the images themselves and from two further routes to |P|.
    images = tuple(lift.discriminant_morphism() for lift in lifts)
    for image in images:
        assert frozenset(image(class_) for class_ in point) == point, "a lift does not preserve the point under rho_L"
    generated = orthogonal.subgroup(images)
    assert int(generated.cardinality()) == target, f"the images generate {int(generated.cardinality())}, not P's {target}"
    orbit = int(group.discriminant_point_orbit(point).cardinality())
    assert orbit == ORBIT, f"the orbit of A_U(2) has {orbit} points, not the measured {ORBIT}"
    assert order % orbit == 0 and order // orbit == target, f"|O(A_L)|/|orbit| is {order // orbit}, not |P| = {target}"
    # A_L = A_{U(2)} + A_{E8(-2)} is an orthogonal decomposition into nondegenerate summands, so its
    # isometry group is the product of theirs. Both blocks are the card's own.
    product = 1
    for summand in (Lattices(ZZ)([row[:2] for row in gram[:2]]), Lattices(ZZ)([row[2:] for row in gram[2:]])):
        product *= int(summand.discriminant_group().orthogonal_group().cardinality())
    assert product == target, f"the two summands' isometry groups have order {product}, not {target}"
    print(f"|orbit| = {orbit}, {order}/{orbit} = {order // orbit} = {product}", flush=True)
    stamp("rho_L(H) = P")

    by = provenance()

    stored = genus.store_arithmetic_group(ROOT, TAG, SLUG, {"generator_morphisms": matrices})
    stamp("stored")
    held = certificates.load(ROOT, tags=[TAG])
    metadata = corpus.front_matter(corpus.read_card(path))
    stored_card = Lattice.model_validate(metadata)
    cited = dict(stored_card.certifications)
    for field, committed in stored:
        computation = genus.name(TAG, f"{genus.ARITHMETIC_PREFIX}{SLUG}.{field}", stored_card.definiteness)
        certificate_hash = certificates.certification_hash(computation, stored_card, committed)
        cited[f"{genus.ARITHMETIC_PREFIX}{SLUG}.{field}"] = certificate_hash
        held[computation] = Certificate(hash=certificate_hash, by=by)
        print(computation, certificate_hash, flush=True)
    metadata["certifications"] = cited
    storage.write_text(path, records.record_text(metadata, corpus.read_card(path).content))
    certificates.save(ROOT, held, tags=[TAG])
    stamp("certified")

    names = corpus.front_matter(corpus.read_card(ROOT / "arithmetic-groups" / f"{SLUG}.md"))["data"]["generator_morphisms"]
    print("generators:", names, flush=True)
    print("certifications:", {key: value for key, value in corpus.front_matter(corpus.read_card(path))["certifications"].items() if key.startswith("arithmetic-group.")}, flush=True)


if __name__ == "__main__":
    faulthandler.enable()
    threading.Thread(target=watch, daemon=True).start()
    main()
