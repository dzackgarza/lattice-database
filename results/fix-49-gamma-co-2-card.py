"""#49, #43, #7: one Gamma_Co,2 on every card. Its index in O(T_Co) is 67456, and its parent is O(T_Co).

Gamma_Co,2 := R_{Gamma_En,2}, the image in O(T_Co) of Stab_{Gamma_En,2}(delta). sage-extensions
`results/issue286-gamma-co-2-is-the-discriminant-preimage.md` proves that this equals rho^{-1}(P_0), with
P_0 = Stab_{O(q)}(A_U(2)). The proof uses prop:gamma-co-images(3), and its one hypothesis is |A_U(2)| = 4 != 256 =
|A_E8(2)|. That is the group of issue607's counts 4, 7, 13 and of the cusp rows on card 6JRR. Hence:

- Gamma_Co,2 contains ker rho = Otilde(T_Co), so it is not a subgroup of Otilde+(T_Co). Its card states no
  parent_group, which makes O(T_Co) the group its index is taken in.
- rho: O(T_Co) -> O(q) is onto (Nikulin, Math. USSR-Izv. 14 (1980), Thm. 3.6.3), so
  [O(T_Co) : Gamma_Co,2] = [O(q) : P_0]. P_0 is the stabilizer of the hyperbolic line A_U(2) of w^perp = F_2^10, and
  O(q) = O(w^perp) is transitive on hyperbolic lines. This program checks that directly: the orbit of A_U(2) under the
  orthogonal transvections x -> x + B(x, u) u, for the nonsingular u of w^perp, is every hyperbolic line. So the
  index is the number of hyperbolic lines of w^perp, counted on card 6JRR's Gram tensor: each such line holds exactly
  two singular points x, y with B(x, y) = 1.

The earlier value 93997183795200 * 46998591897600 multiplied the index of Otilde+(T_Co) by |O(q)|. A group that
contains ker rho cannot have that index.

    sage-docker-python results/fix-49-gamma-co-2-card.py --write
"""

import itertools
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / "src")]

from latticedb import card_serialization, certificates, corpus, records, storage  # noqa: E402
from latticedb.catalogues import ArithmeticGroup  # noqa: E402
from latticedb.model import Lattice  # noqa: E402

TAG, SLUG = "6JRR", "gamma-co-2"
FIELD = f"arithmetic-group.{SLUG}.index_in_orthogonal_group"
LATTICE_CARD = ROOT / "lattices" / f"{TAG}.md"
GROUP_CARD = ROOT / "arithmetic-groups" / f"{SLUG}.md"

metadata = corpus.front_matter(corpus.read_card(LATTICE_CARD))
gram = metadata["gram_tensor"]
assert gram[0] == [2] + [0] * 10 and all(x % 2 == 0 for r in gram for x in r)
M = [[gram[i][j] // 2 for j in range(1, 11)] for i in range(1, 11)]


def B(x, y):
    return sum(x[i] * M[i][j] * y[j] for i in range(10) for j in range(10)) % 2


def q(x):
    return sum(x[i] * M[i][j] * x[j] for i in range(10) for j in range(10)) // 2 % 2


singular = [x for x in itertools.product((0, 1), repeat=10) if any(x) and q(x) == 0]
assert len(singular) == 527
pairs = sum(1 for x in singular for y in singular if B(x, y) == 1)
assert pairs % 2 == 0
INDEX = pairs // 2
order = metadata["integral"]["discriminant_form"]["orthogonal_group_order"]
assert order % INDEX == 0
print(f"hyperbolic lines of w^perp: {INDEX}; |O(q)| / {INDEX} = {order // INDEX} = |P_0|")
# transitivity: bit-encoded vectors, B by a precomputed table of M y
enc = lambda x: sum(c << i for i, c in enumerate(x))
dec = lambda k: tuple((k >> i) & 1 for i in range(10))
My = {k: enc(tuple(sum(M[i][j] * dec(k)[j] for j in range(10)) % 2 for i in range(10))) for k in range(1024)}
Bi = lambda a, b: bin(a & My[b]).count("1") & 1
nonsingular = [enc(x) for x in itertools.product((0, 1), repeat=10) if any(x) and q(x) == 1]
start = frozenset({enc((1,) + (0,) * 9), enc((0, 1) + (0,) * 8), enc((1, 1) + (0,) * 8)})
seen, frontier = {start}, [start]
while frontier:
    line = frontier.pop()
    for u in nonsingular:
        image = frozenset(z ^ (u if Bi(z, u) else 0) for z in line)
        if image not in seen:
            seen.add(image)
            frontier.append(image)
assert len(seen) == INDEX, (len(seen), INDEX)
print(f"the orbit of A_U(2) under the transvections of w^perp has {len(seen)} lines: O(q) is transitive on them")
assert (q((0, 1, 1) + (0,) * 7), q((0, 1) + (0,) * 8), q((1,) + (0,) * 9)) == (1, 0, 0), "A_U(2) is a hyperbolic line"

group = corpus.front_matter(corpus.read_card(GROUP_CARD))
group.pop("parent_group", None)
group["data"]["index_in_orthogonal_group"] = INDEX
group["data"]["abstract_structure"] = (
    "R_{Gamma_En,2}, the image in O(T_Co) of the isometries of T_En that lie in Gamma_En,2 and fix delta, "
    "T_Co = delta^perp, delta = e - f; equal to rho^{-1}(P_0) with P_0 = Stab_{O(q)}(A_U(2)), the preimage of the "
    "stabilizer of the hyperbolic line A_U(2) of [h/2]^perp; it contains ker rho = Otilde(T_Co)"
)
group["data"]["reference"]["citation"] = (
    "the construction, and not a definition in print: research def:gamma-co-groups(5) defines Gamma_Co,2 = R_{Gamma_En,2}; "
    "sage-extensions results/issue286-gamma-co-2-is-the-discriminant-preimage.md proves R_{Gamma_En,2} = rho^{-1}(P_0) "
    "from prop:gamma-co-images(3) (the summands A_U(2) and A_E8(2) have orders 4 and 256, so no isometry swaps them). "
    "The index is [O(q) : P_0], because rho is onto (Nikulin 1980, Thm. 3.6.3); by the transitivity of O(q) on them, which the program checks, it is the number of "
    "hyperbolic lines of [h/2]^perp, 67456, which results/fix-49-gamma-co-2-card.py counts on card 6JRR. The three orbit "
    "counts are carried from sage-extensions results/issue607-gamma-co-2-rows-by-the-polar-space.md at commit "
    "47865446a7c37c85d873f91ac9d74cea472e208c, which proves 4 line, 7 plane and 13 flag orbits of this group "
    "(GAP log results/issue607-the-levi-candidate.log), in agreement with sage-extensions#391's image run 43556671111. "
    "Nothing here identifies this group with the Coble period group"
)
record = ArithmeticGroup.model_validate(group)
lattice = Lattice.model_validate(metadata)
digest = certificates.certification_hash(f"{TAG} {FIELD}", lattice, INDEX)
print(f"{TAG} {FIELD} = {digest}")
if "--write" not in sys.argv[1:]:
    raise SystemExit("dry run")
document = corpus.read_card(GROUP_CARD)
storage.write_text(GROUP_CARD, card_serialization.catalogue_text(group, document.content))
document = corpus.read_card(LATTICE_CARD)
stored = corpus.front_matter(document)
stored["certifications"] = {**stored["certifications"], FIELD: digest}
storage.write_text(LATTICE_CARD, records.record_text(stored, document.content))
held = certificates.load(ROOT, tags=(TAG,))
held[f"{TAG} {FIELD}"] = certificates.Certificate(
    hash=digest,
    by=(
        "results/fix-49-gamma-co-2-card.py: [O(T_Co) : Gamma_Co,2] = [O(q) : Stab(A_U(2))] = 67456, the number of "
        "hyperbolic lines of [h/2]^perp counted on this card's Gram tensor; Gamma_Co,2 = R_{Gamma_En,2} = rho^{-1}(P_0) by "
        "sage-extensions results/issue286-gamma-co-2-is-the-discriminant-preimage.md, rho onto by Nikulin 1980 Thm. 3.6.3, "
        "O(q) transitive on hyperbolic lines, checked by the orbit of A_U(2) under the transvections of [h/2]^perp"
    ),
)
certificates.save(ROOT, held, tags=(TAG,))
print("written")
