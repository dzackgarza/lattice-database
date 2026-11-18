#!/usr/bin/env python3
"""Store the nine members that generate H <= G_e, from the call that returns them (lattice-database#40).

Sterk's group is $G_e = \\rho_L^{-1}(P)$, where $L = U(2) \\oplus E_8(-2)$, $\\rho_L \\colon O(L) \\to O(A_L)$ is
the reduction of the discriminant representation and $P \\le O(A_L)$ is the stabilizer of $A_{U(2)}$
(H. Sterk, "Compactifications of the period space of Enriques surfaces, Part I", Math. Z. 207 (1991),
(4.3.5), p. 19). The call this program makes is the one sage-extensions#354 delivered and the issue
names: `L.Aut().discriminant_point_stabilizer_image_generators(A_{U(2)})`, the subfamily of the Schreier
family of the orbit of $A_{U(2)}$ whose images in $O(A_L)$ generate $P$. It returns nine members here.

The call did not return at sage-extensions `2fb37d5a717`: seven runs ended inside it, recorded in
`results/evidence-40-ge-generators.md`. sage-extensions#459 closed that, at `b501886b`, by making the
family lazy — `_discriminant_point_orbit_and_section` records the orbit and its transversal words and
no transition table, and `_discriminant_point_stabilizer_members` evaluates a member's letter image when
the member asks for it. This program runs at `b501886b` and the call returns in about 93 s at a 1.0 GiB
peak.

The nine lie in $G_e$, so each is one self-isometry $L \\to L$, and they generate $H \\le G_e$ with
$\\rho_L(H) = P$; they do not generate $G_e$, whose remaining part is $\\ker \\rho_L = \\widetilde O(L)$,
for which no generating set exists (sage-extensions#597). So they are stored as generators of $H$,
never as generators of $G_e$, and $H$'s card states $\\rho_L(H) = P$.

What this program checks before writing, from the card's stored Gram tensor alone:

* each returned matrix is integral, unimodular and preserves the form, $M^t G M = G$;
* every member lies in the preimage and preserves the point under the preimage's own morphism;
* the images of the nine generate a subgroup of $O(A_L)$ of order $2 \\cdot 348364800 = 696729600$,
  which is $|O(A_L)| / |\\mathrm{orbit}| = 46998591897600 / 67456$, the stabilizer's order by the
  index--stabilizer identity, read from the orbit's cardinality and not from a typed constant;
* that order is also the product of the two summands' isometry-group orders, computed from the two
  diagonal blocks of the card's Gram, so $P = O(q_{U(2)}) \\times O(q_{E_8(-2)})$ is what is generated.
"""

from __future__ import annotations

import json
import os
import resource
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
SAGE_EXTENSIONS_REVISION = "b501886bcbda94699dde0213adbca5d97d77163a"
"""The owner revision this ran at: `origin/main` after sage-extensions#459 closed."""

ORDER = 46998591897600
"""$|O(A_L)|$ of the card's discriminant form, as the owner returns it."""

ORBIT = 67456
"""The cardinality of the orbit of $A_{U(2)}$ under $O(A_L)$, which is $[O(A_L) : P]$."""

TARGET = 696729600
"""The order of the subgroup the nine members' images generate: 2 * 348364800 = |O(A_L)| / |orbit|."""

START = time.time()


def stamp(label: str) -> None:
    print(f"[{time.time() - START:7.1f}s] {label} peak={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024} MiB", flush=True)


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


def provenance() -> str:
    """The certificate's account of this computation: what was asked of the owner, and at which revision."""
    return (
        "the owner's own selection: L.Aut().discriminant_point_stabilizer_image_generators(A_U(2)) at "
        f"sage-extensions {SAGE_EXTENSIONS_REVISION}, the subfamily of the Schreier family of the orbit of "
        "A_U(2) whose images generate P = Stab_{O(A_L)}(A_U(2)). "
        f"|O(A_L)| = {ORDER}, |orbit| = {ORBIT}, |P| = {TARGET} = {ORDER}/{ORBIT} = 2 * 348364800; each member "
        "was checked to lie in rho_L^-1(P) and to preserve the classes of A_U(2) under the preimage's own "
        "morphism. The result is H <= G_e with rho_L(H) = P, not G_e: G_e = Otilde(L) . H and no generating "
        "set of Otilde(L) exists (sage-extensions#597). The call returns after sage-extensions#459 made the "
        "family lazy (results/evidence-40-ge-generators.md). results/generators-40-ge.py computed the "
        "matrices and these checks."
    )


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
    subfamily = group.discriminant_point_stabilizer_image_generators(point)
    members = tuple(subfamily)
    matrices = [_matrix_rows(member) for member in members]
    print("subfamily size", len(members), flush=True)
    dump = os.environ.get("GE_DUMP")
    if dump:
        # Keep the result if a later stage of this run falls over.
        Path(dump).write_text(json.dumps({"size": len(members), "matrices": matrices}, indent=1))
    stamp("subfamily")

    orthogonal = form.orthogonal_group()
    order = int(orthogonal.cardinality())
    orbit = int(group.discriminant_point_orbit(point).cardinality())
    target = order // orbit
    assert (order, orbit, target) == (ORDER, ORBIT, TARGET), f"the owner returns |O(A_L)| = {order}, |orbit| = {orbit}, |P| = {target}"
    preimage = group.discriminant_point_stabilizer(point)
    rho = preimage.preimage_morphism()
    stamp("preimage")

    for matrix, member in zip(matrices, members, strict=True):
        assert len(matrix) == card.rank and all(len(row) == card.rank for row in matrix)
        assert preserves(matrix, gram), "a returned matrix is not an isometry of the card's form"
        assert abs(determinant(matrix)) == 1, "a returned matrix is not unimodular"
        assert member in preimage, "a returned member is not in rho_L^-1(P)"
        assert frozenset(rho(member)(class_) for class_ in point) == point, "a returned member does not preserve the point"
    images = tuple(rho(member) for member in members)
    assert int(orthogonal.subgroup(images).cardinality()) == target, "the images do not generate P"
    # The same order from the two summands, whose blocks are the card's own.
    product = 1
    for summand in (Lattices(ZZ)([row[:2] for row in gram[:2]]), Lattices(ZZ)([row[2:] for row in gram[2:]])):
        product *= int(summand.discriminant_group().orthogonal_group().cardinality())
    assert product == target, f"the two summands' isometry groups have order {product}, not {target}"
    stamp("checks")

    stored = genus.store_arithmetic_group(ROOT, TAG, SLUG, {"generator_morphisms": matrices})
    stamp("stored")

    # A name this program created for a matrix the nine do not use would claim a generator it is not.
    document = corpus.read_card(path)
    metadata = corpus.front_matter(document)
    names = set(corpus.front_matter(corpus.read_card(ROOT / "arithmetic-groups" / f"{SLUG}.md"))["data"]["generator_morphisms"])
    before = list(metadata["morphisms"])
    kept = [m for m in before if not (str(m.get("name", "")).startswith("H_e generator") and m["name"] not in names)]
    if len(kept) != len(before):
        metadata["morphisms"] = kept
        storage.write_text(path, records.record_text(metadata, document.content))
        stamp(f"dropped {len(before) - len(kept)} H_e entries the nine do not use")

    held = certificates.load(ROOT, tags=[TAG])
    metadata = corpus.front_matter(corpus.read_card(path))
    stored_card = Lattice.model_validate(metadata)
    cited = dict(stored_card.certifications)
    for field, committed in stored:
        computation = genus.name(TAG, f"{genus.ARITHMETIC_PREFIX}{SLUG}.{field}", stored_card.definiteness)
        certificate_hash = certificates.certification_hash(computation, stored_card, committed)
        cited[f"{genus.ARITHMETIC_PREFIX}{SLUG}.{field}"] = certificate_hash
        held[computation] = Certificate(hash=certificate_hash, by=provenance())
        print(computation, certificate_hash, flush=True)
    metadata["certifications"] = cited
    storage.write_text(path, records.record_text(metadata, corpus.read_card(path).content))
    certificates.save(ROOT, held, tags=[TAG])
    print("generators:", corpus.front_matter(corpus.read_card(ROOT / "arithmetic-groups" / f"{SLUG}.md"))["data"]["generator_morphisms"], flush=True)
    stamp("certified")


if __name__ == "__main__":
    main()
