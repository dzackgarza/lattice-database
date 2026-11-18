r"""#43: the O(K_J)-invariant of a cusp's root classes, from the card's Gram tensor and the cusp.

For a primitive root $r$ of $K_J$ the root spans a primitive sublattice and $K_J = \langle r\rangle \perp r^\perp$
orthogonally, so an isometry $r_1^\perp \to r_2^\perp$ extends to an isometry of $K_J$ carrying $r_1$ to $r_2$:
two root classes are $O(K_J)$-equivalent **iff** their complements are isometric.  The complete invariant is
therefore the isometry class of $r^\perp$, and for an even 2-elementary lattice of rank 9 and determinant
$\pm 2^9$ its genus is $(9, \text{signature}, 9, \delta)$ --- every entry fixed here, so the genus is one symbol and
Sage's `representatives()` says how many classes it has.  One class means the complements are isometric, hence
the roots are one $O(K_J)$-orbit, and no $O(K_J)$-invariant whatsoever separates them.

$K_J$ is built from the card alone.  $\Lambda = \eta^\perp \subset \mathbb{Z}^{12}$ is the kernel of
$x \mapsto b(x, \eta)$, the image of $\eta$ in $\Lambda \cong \mathbb{Z}^{11}$ is a primitive row $c$, and the rows
$2, \ldots, 11$ of a unimodular $W$ whose first row is $c$, applied to a basis of $\Lambda$, give a
$\mathbb{Z}$-basis of $\Lambda/\mathbb{Z}\eta$.  A wall of the card's chamber then has a class in $K_J$ exactly when
it is orthogonal to $\eta$, and the roots are the walls of square $-2$.

    sage results/probe-43-okj-complement-invariant.py

Sage only: no preamble import, so it does not need the pinned image.
"""

from math import gcd

import yaml
from sage.all import ZZ, IntegralLattice, matrix, vector

CARD = "lattices/029J.md"

metadata = yaml.safe_load(open(CARD).read().split("---")[1])
gram = matrix(ZZ, metadata["gram_tensor"])
rows = metadata["integral"]["cusp_chambers"]["gamma-en-2"]


def square(x) -> int:
    return int(vector(ZZ, x) * gram * vector(ZZ, x))


def product(x, y) -> int:
    return int(vector(ZZ, x) * gram * vector(ZZ, y))


def boundary_lattice(cusp):
    """A Z-basis of K_J = cusp^perp / Z cusp in the card's coordinates, and its Gram matrix."""
    eta = vector(ZZ, cusp)
    assert square(eta) == 0
    kernel = matrix(ZZ, [gram * eta]).right_kernel_matrix()
    assert kernel.nrows() == 12 - 1
    assert all(product(row, eta) == 0 for row in kernel.rows())
    c = vector(ZZ, [ZZ(entry) for entry in eta * kernel.transpose() * (kernel * kernel.transpose()).inverse()])
    assert c * kernel == eta, "the cusp is not in its own orthogonal lattice"
    assert gcd(*[abs(int(entry)) for entry in c]) == 1, "the cusp is not primitive"
    smith, left, _right = matrix(ZZ, [c]).transpose().smith_form()
    assert [smith[i, 0] for i in range(smith.nrows())] == [1] + [0] * (kernel.nrows() - 1)
    # left * c^T = +-e_1, so the first row of left^-T is +-c and the rows after it are a basis of a complement.
    unimodular = left.inverse().transpose()
    assert vector(ZZ, list(unimodular[0])) in (c, -c)
    basis = (unimodular * kernel)[1:]
    return eta, basis, basis * gram * basis.transpose()


def coordinates(basis, gram_k, x):
    """The coordinates in that basis of the class of `x`, checked against the square of `x`."""
    x = vector(ZZ, x)
    solved = gram_k.solve_right(vector(ZZ, [product(row, x) for row in basis.rows()]))
    a = vector(ZZ, [ZZ(entry) for entry in solved])
    assert a * gram_k * a == square(x), "the coordinates do not reproduce the square"
    return a


def root_classes(gram_k, eta, basis, chamber):
    """The root classes of K_J among the chamber's walls, one per class."""
    roots = []
    for wall in chamber:
        entry = tuple(wall["vector"])
        if product(entry, eta) != 0 or square(entry) != -2:
            continue
        root = coordinates(basis, gram_k, entry)
        if all(root != seen for seen in roots):
            roots.append(root)
    return roots


def complement(gram_k, root):
    """The rank-9 orthogonal complement of a root in K_J."""
    kernel = matrix(ZZ, [vector(ZZ, root) * gram_k]).right_kernel_matrix()
    assert kernel.nrows() == gram_k.nrows() - 1
    return kernel * gram_k * kernel.transpose()


def delta(gram_9) -> int:
    """$0$ when $b(x, x)$ is an integer on the dual lattice, $1$ otherwise: the diagonal of the inverse Gram decides."""
    inverse = gram_9.inverse()
    integral_diagonal = all(entry in ZZ for entry in inverse.diagonal())
    half_integral_off_diagonal = all(2 * entry in ZZ for entry in inverse.list())
    return 0 if integral_diagonal and half_integral_off_diagonal else 1


for row in rows:
    eta, basis, gram_k = boundary_lattice(row["cusp"])
    roots = root_classes(gram_k, eta, basis, row["walls"])
    if not roots:
        print(f"{row['statement']:>7} p.{row['printed_page']:>2}  det K_J {int(gram_k.det()):>5}  no root class: no row", flush=True)
        continue
    complements = [complement(gram_k, root) for root in roots]
    genera = [IntegralLattice(lattice).genus() for lattice in complements]
    # A genus printed carries a representative's Gram matrix, which is no isometry invariant; the symbols and the
    # comparison of the genus objects are, and a genus with one class is that class.
    symbols = [(genus.signature(), genus.determinant(), [genus.local_symbol(prime) for prime in (2,)]) for genus in genera]
    classes = [len(genus.representatives()) for genus in genera]
    distinct = 1 + sum(1 for index in range(1, len(genera)) if all(genera[index] != genera[earlier] for earlier in range(index)))
    print(
        f"{row['statement']:>7} p.{row['printed_page']:>2}  det K_J {int(gram_k.det()):>5}  "
        f"root classes {len(roots)}  complement det {int(complements[0].det())}  deltas {[delta(lattice) for lattice in complements]}\n"
        f"        genus of each complement: {symbols}\n"
        f"        classes in each genus {classes}  distinct genera {distinct}"
        f"  -> O(K_J)-orbits on the row: {'one, all ' + str(len(roots)) + ' classes O(K_J)-equivalent' if distinct == 1 and all(count == 1 for count in classes) else str(distinct)}",
        flush=True,
    )
