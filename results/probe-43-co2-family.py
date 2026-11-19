"""#43: the restricted family of the stabilizer of T_Co, and the order of its discriminant image.

The card the cusp-5 row waits on states `[O(T_Co) : Gamma_Co,2]`, which the acceptance record derives as
93997183795200 * |O(A_T_Co, q)|. This asks the owner for the objects that derivation rests on, in one bounded run:
`Stab_{O(T_En)}(delta).group_generators()`, the restriction of each generator to `delta^perp = T_Co`, and the order of
the subgroup their discriminant images generate. The owner's own record measures 330 generators in 352 s, 40 s to
restrict and 25 s for `rho` on them; the last line here is the number the card must reproduce.

    .scratch/wt43r-run.sh -u results/probe-43-co2-family.py
"""

import time
from fractions import Fraction
from pathlib import Path

from latticedb import corpus
from sage.all import ZZ as SageZZ, matrix
from sage_extensions.all import ZZ, NamedLattices  # noqa: F401,F403

start = time.time()


def stamp(label):
    print(f"[{time.time() - start:7.1f}s] {label}", flush=True)


enriques = NamedLattices.TEn
labels = tuple(enriques.module_generating_set())
rank = int(enriques.module_rank())
gram = matrix(SageZZ, [[int(enriques.b(enriques.module_generator(a), enriques.module_generator(b))) for b in labels] for a in labels])
delta = enriques.linear_combination({labels[0]: enriques.base_ring()(1), labels[1]: enriques.base_ring()(-1)})
perpendicular = delta.orthogonal_complement()
perpendicular_labels = tuple(perpendicular.module_generating_set())
inclusion = perpendicular.inclusion()
basis = matrix(
    SageZZ,
    [[int(entry) for entry in inclusion(perpendicular.module_generator(label)).to_vector()] for label in perpendicular_labels],
).transpose()
stamp(f"T_Co basis in T_En coordinates: {basis.nrows()} x {basis.ncols()}, det of its Gram {int((basis.transpose() * gram * basis).det())}")

stabilizer = enriques.O().stabilizer(delta, action="setwise")
stamp(f"stabilizer of delta: {type(stabilizer).__name__}")
family = tuple(stabilizer.group_generators())
stamp(f"its generator family: {len(family)} generators")

inverse = (basis.transpose() * basis).inverse()
restricted = []
for position, generator in enumerate(family):
    # The generator as a matrix in T_En's own basis, from the images of the basis vectors.
    image_rows = []
    for label in labels:
        coordinates = [int(entry) for entry in generator(enriques.module_generator(label)).to_vector()]
        image_rows.append(coordinates)
    as_matrix = matrix(SageZZ, image_rows).transpose()
    # The restriction: each basis vector of T_Co, carried, and written in T_Co's coordinates.
    columns = []
    for column in range(basis.ncols()):
        vector = matrix(SageZZ, 1, rank, list(basis.column(column)))
        image = vector * as_matrix
        coordinates = (image * basis) * inverse
        assert all(entry.denominator() == 1 for entry in coordinates.list()), (position, coordinates)
        columns.append([int(entry) for entry in coordinates.list()])
    restricted.append(matrix(SageZZ, columns).transpose())
stamp(f"restricted {len(restricted)} generators to T_Co")

rho = enriques.discriminant_representation()
images = [rho(generator) for generator in family]
stamp(f"rho on the family: {len(images)} images")
image_order = rho.codomain().subgroup(tuple(images)).cardinality()
stamp(f"|<rho(g)>| = {image_order}")

card = corpus.front_matter(corpus.read_card(Path("/repo/lattices/6JRR.md")))
print(f"RESULT: {len(family)} generators, {len(restricted)} restrictions, |<rho(g)>| = {image_order}", flush=True)
print("RESULT: card 6JRR determinant", card["determinant"], "and |O(A,q)| expected 46998591897600", flush=True)
print(f"RESULT: [O(T_Co) : Gamma_Co,2] = 93997183795200 * {int(image_order)} = {93997183795200 * int(image_order)}", flush=True)
