r"""#43, the T_Co side: the O(K_I)-invariant of the root classes at cusps 3--5, from the cards alone.

The issue's third item asks the T_Co card for "the same row at its cusps 3--5".  $T_{Co} = \delta^\perp$ inside
$T_{En}$ with $\delta = e - f$, so a vector of the card's coordinates lies in $T_{Co}$ exactly when it is orthogonal
to $\delta$, and at Sterk's cusps 3--5 the printed cusp vector has equal $e$ and $f$ coefficients, so it lies there.
$K_I = \eta^\perp/\mathbb{Z}\eta$ inside $T_{Co}$ has rank 9, and the roots of $K_I$ are the classes of the chamber's
walls that lie in $T_{Co}$, are orthogonal to the cusp, and have square $-2$.

The invariant is the one the `T_{En}` side uses, for the same reason: for a primitive root $r$ of $K_I$,
$K_I = \langle r\rangle \perp r^\perp$ orthogonally, so two root classes are $O(K_I)$-equivalent iff their complements
are isometric; each complement is an even 2-elementary lattice of rank 8 and determinant $\pm 2^{10}$, and Sage's
`representatives()` counts the classes in its genus.

    sage results/probe-43-coble-okj-invariant.py

Sage only: no preamble import, so it does not need the pinned image.
"""

from math import gcd

import yaml
from sage.all import ZZ, IntegralLattice, matrix, vector

CARD = "lattices/029J.md"

metadata = yaml.safe_load(open(CARD).read().split("---")[1])
card_gram = matrix(ZZ, metadata["gram_tensor"])
rows = metadata["integral"]["cusp_chambers"]["gamma-en-2"]
delta = vector(ZZ, [1, -1] + [0] * 10)


def square(ambient, x) -> int:
    return int(vector(ZZ, x) * ambient * vector(ZZ, x))


def product(ambient, x, y) -> int:
    return int(vector(ZZ, x) * ambient * vector(ZZ, y))


def orthogonal_basis(ambient, vector_of):
    """A Z-basis of the vectors of `ambient`'s lattice orthogonal to `vector_of`, and its Gram matrix."""
    kernel = matrix(ZZ, [ambient * vector(ZZ, vector_of)]).right_kernel_matrix()
    return kernel, kernel * ambient * kernel.transpose()


def coordinates(basis, gram_basis, ambient, target):
    """Coordinates of `target` in the lattice spanned by `basis`, checked against the square of `target`."""
    rhs = vector(ZZ, [product(ambient, row, target) for row in basis.rows()])
    a = vector(ZZ, [ZZ(entry) for entry in gram_basis.solve_right(rhs)])
    assert a * gram_basis * a == square(ambient, target), "the coordinates do not reproduce the square"
    return a


def quotient_basis(basis, ambient, representative):
    """A Z-basis of `basis`-span / Z `representative` and its Gram matrix, the representative being primitive.

    The rows of `basis` are primitive in the coordinate lattice, so the representative's coordinates are read off
    with the identity form on that lattice; the Gram of `basis` is singular, the representative spanning its radical.
    """
    c = vector(ZZ, [ZZ(entry) for entry in vector(ZZ, representative) * basis.transpose() * (basis * basis.transpose()).inverse()])
    assert c * basis == vector(ZZ, representative)
    assert gcd(*[abs(int(entry)) for entry in c]) == 1, "the class's representative is not primitive"
    smith = matrix(ZZ, [c]).transpose().smith_form()[1]
    unimodular = smith.inverse().transpose()
    assert vector(ZZ, list(unimodular[0])) in (c, -c)
    quotient = (unimodular * basis)[1:]
    return quotient, quotient * ambient * quotient.transpose()


def complement_invariant(gram_k, root):
    kernel = matrix(ZZ, [vector(ZZ, root) * gram_k]).right_kernel_matrix()
    lattice = kernel * gram_k * kernel.transpose()
    inverse = lattice.inverse()
    delta_of_lattice = 0 if all(entry in ZZ for entry in inverse.diagonal()) and all(2 * entry in ZZ for entry in inverse.list()) else 1
    return lattice, delta_of_lattice


coble, gram_coble = orthogonal_basis(card_gram, delta)
print(f"T_Co: rank {coble.nrows()}, det {int(gram_coble.det())}, signature {IntegralLattice(gram_coble).signature_pair()}", flush=True)

for row in rows[2:5]:
    eta_coble = coordinates(coble, gram_coble, card_gram, vector(ZZ, row["cusp"]))
    eta = eta_coble * coble
    assert product(card_gram, eta, delta) == 0, "the cusp is not in T_Co"
    inside, gram_inside = orthogonal_basis(gram_coble, eta_coble)
    k_i, gram_i = quotient_basis(inside, gram_coble, eta_coble)
    assert k_i.nrows() == 9
    roots = []
    for wall in row["walls"]:
        entry = tuple(wall["vector"])
        if product(card_gram, entry, delta) != 0:
            continue
        in_coble = coordinates(coble, gram_coble, card_gram, vector(ZZ, entry))
        if product(gram_coble, in_coble, eta_coble) != 0 or square(gram_coble, in_coble) != -2:
            continue
        root = coordinates(k_i, gram_i, gram_coble, in_coble)
        if all(root != seen for seen in roots):
            roots.append(root)
    walls_in_coble = sum(1 for wall in row["walls"] if product(card_gram, tuple(wall["vector"]), delta) == 0)
    if not roots:
        print(f"{row['statement']:>7} p.{row['printed_page']:>2}  {walls_in_coble} walls in T_Co  K_I rank {k_i.nrows()}, "
              f"det {int(gram_i.det())}  no root class", flush=True)
        continue
    lattices = []
    deltas = []
    for root in roots:
        lattice, delta_of_lattice = complement_invariant(gram_i, root)
        lattices.append(lattice)
        deltas.append(delta_of_lattice)
    genera = [IntegralLattice(lattice).genus() for lattice in lattices]
    classes = [len(genus.representatives()) for genus in genera]
    distinct = 1 + sum(1 for index in range(1, len(genera)) if all(genera[index] != genera[earlier] for earlier in range(index)))
    symbols = [(genus.signature(), genus.determinant(), genus.local_symbol(2)) for genus in genera]
    print(
        f"{row['statement']:>7} p.{row['printed_page']:>2}  {walls_in_coble} walls in T_Co  K_I rank {k_i.nrows()}, "
        f"det {int(gram_i.det())}, signature {IntegralLattice(gram_i).signature_pair()}  root classes {len(roots)}  "
        f"complement det {int(lattices[0].det())}\n"
        f"        deltas {deltas}  genus of each complement {symbols}\n"
        f"        classes in each genus {classes}  distinct genera {distinct}"
        f"  -> O(K_I)-orbits on the row: {'one, all ' + str(len(roots)) + ' classes O(K_I)-equivalent' if distinct == 1 and all(count == 1 for count in classes) else str(distinct)}",
        flush=True,
    )
