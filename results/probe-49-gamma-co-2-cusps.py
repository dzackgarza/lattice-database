"""#49, #43: the Gamma_Co,2-cusp of each T_Co root-orbit row, and the root-class orbits at all four Gamma_Co,2-cusps.

Part A certifies which Gamma_{Co,2}-cusp (0-cusp of F_Co) each row of card 6JRR's `cusp_root_orbits['gamma-co-2']`
sits at. Gamma_{Co,2} = rho^{-1}(P_0) with P_0 = Stab_{O(q)}(A_{U(2)}) = O(A_{U(2)}) x O(A_{E8(2)})
(sage-extensions `results/issue607-gamma-co-2-rows-by-the-polar-space.md`, "The reduction" and "Lines: 4"), and
Gamma_{Co,2} contains ker rho, so the Gamma_{Co,2}-orbit of a primitive isotropic v is decided by the P_0-orbit of
p = [v/2] among the 527 singular points of w^perp = A_{U(2)} + A_{E8(2)}. In card 6JRR's basis (e0 | e1, f1 | E8(-2)
roots) the Gram tensor is 2M with M integral, w = [e0/2], and w^perp is coordinates 1..10 of v mod 2, with
q(x) = x^T M x / 2 mod 2 and polar form x^T M y mod 2. The probe generates a subgroup of P_0 (the swap e1 <-> f1 of
A_{U(2)} and the 120 transvections x -> x + B(x, u) u in the nonsingular u of A_{E8(2)}), computes its orbits on the
singular points, and checks they have sizes 135, 2, 270, 120. P_0 preserves the type of the decomposition p = a + b
(a in A_{U(2)}, b in A_{E8(2)}: a zero, singular or nonsingular; b zero or not), and these four types have exactly
these sizes, so the subgroup's orbits are P_0's orbits.

Part B computes, at each of the four cusps, the root classes and their orbits the way the (4.3.9) row was computed
(`results/issue-49-transporters-and-coble-cusp5.md`): each cusp of T_Co is a cusp vector of card 029J lying in
delta^perp, delta = e - f, at which delta is a wall of Sterk's chamber with only order-4 edges. Then
C_{W_v}(s_delta) = <s_delta> x W_perp (Allcock, arXiv:1106.3822v2, Thm. 5, Cor. 6), W_perp has simple roots the walls
orthogonal to delta and beta_u = alpha_u + delta for the order-4 neighbours u, the root classes are W_perp's simple
roots of square -2 up to odd paths, and the diagram symmetries fixing delta (realized in Gamma_v by Sterk (4.3.7)-(4.3.9),
pp. 22-24; trivial at (4.3.6)) join classes. A 6JRR vector is a 029J vector of delta^perp with its first coordinate
dropped.

    sage-docker-python results/probe-49-gamma-co-2-cusps.py
"""

import itertools
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def front(tag):
    return yaml.safe_load((ROOT / "lattices" / f"{tag}.md").read_text().split("---")[1])


co, en = front("6JRR"), front("029J")
GCO, GEN = co["gram_tensor"], en["gram_tensor"]


def pair(gram, a, b):
    return sum(Fraction(a[i]) * gram[i][j] * Fraction(b[j]) for i in range(len(gram)) for j in range(len(gram)))


# Part A ---------------------------------------------------------------------------------------------------------
M = [[GCO[i][j] // 2 for j in range(1, 11)] for i in range(1, 11)]
assert all(GCO[i][j] % 2 == 0 for i in range(11) for j in range(11))
assert GCO[0] == [2] + [0] * 10, "e0 spans the <2> summand"


def B(x, y):
    return sum(x[i] * M[i][j] * y[j] for i in range(10) for j in range(10)) % 2


def q(x):
    value = sum(x[i] * M[i][j] * x[j] for i in range(10) for j in range(10))
    assert value % 2 == 0
    return (value // 2) % 2


points = [x for x in itertools.product((0, 1), repeat=10) if any(x)]
singular = [x for x in points if q(x) == 0]
assert len(singular) == 527, len(singular)
nonsingular_w = [x for x in points if x[0] == x[1] == 0 and q(x) == 1]
assert len(nonsingular_w) == 120


def swap(x):
    return (x[1], x[0]) + x[2:]


def transvection(u):
    return lambda x: tuple((x[i] + B(x, u) * u[i]) % 2 for i in range(10))


generators = [swap] + [transvection(u) for u in nonsingular_w]
for g in generators:
    for x in points[:64]:
        assert q(g(x)) == q(x)
orbit_of = {}
orbits = []
for x in singular:
    if x in orbit_of:
        continue
    orbit, frontier = {x}, [x]
    while frontier:
        y = frontier.pop()
        for g in generators:
            z = g(y)
            if z not in orbit:
                orbit.add(z)
                frontier.append(z)
    for y in orbit:
        orbit_of[y] = len(orbits)
    orbits.append(orbit)


def kind(x):
    a, b = x[:2], x[2:]
    a_kind = "0" if not any(a) else ("singular" if q(a + (0,) * 8) == 0 else "nonsingular")
    return a_kind, ("0" if not any(b) else ("singular" if q((0, 0) + b) == 0 else "nonsingular"))


sizes = sorted(len(o) for o in orbits)
print("A. P_0-orbits on the 527 singular points:", sizes)
assert sizes == [2, 120, 135, 270]
for o in orbits:
    print(f"   size {len(o):3d}: types {sorted({kind(x) for x in o})}")


def cusp_orbit(v):
    assert pair(GCO, v, v) == 0, "not isotropic"
    assert v[0] % 2 == 0, "[v/2] lies in w^perp"
    p = tuple(c % 2 for c in v[1:])
    assert any(p), "v is primitive, so v/2 is not in T_Co"
    return len(orbits[orbit_of[p]]), kind(p)


for row in co["integral"]["cusp_root_orbits"]["gamma-co-2"]:
    size, k = cusp_orbit(row["cusp"])
    print(f"   stored row {row['cusp']} (labelled {row.get('statement')}): Gamma_Co,2-cusp of orbit size {size}, (a, b) = {k}")

# Part B ---------------------------------------------------------------------------------------------------------
DELTA = [1, -1] + [0] * 10


def to_co(x):
    assert x[0] == x[1], x
    return [x[0]] + list(x[2:])


def closure(gens, n):
    group, frontier = {tuple(range(n))}, [tuple(range(n))]
    while frontier:
        g = frontier.pop()
        for h in gens:
            k = tuple(h[g[i]] for i in range(n))
            if k not in group:
                group.add(k)
                frontier.append(k)
    return group


symmetries = {r["statement"]: r["chamber_symmetries"]["generators"] for r in en["integral"]["cusp_root_orbits"]["gamma-en-2"]}
print("B. root-class orbits at the four Gamma_Co,2-cusps")
for chamber in en["integral"]["cusp_chambers"]["gamma-en-2"]:
    statement, v = chamber["statement"], chamber["cusp"]
    if pair(GEN, v, DELTA) != 0:
        print(f"   ({statement}): cusp not in delta^perp")
        continue
    walls = [w["vector"] for w in chamber["walls"]]
    names = [w["name"] for w in chamber["walls"]]
    n = len(walls)
    (s,) = [i for i, w in enumerate(walls) if w in (DELTA, [-c for c in DELTA])]
    alpha_s = walls[s]
    edges = {j: pair(GEN, alpha_s, walls[j]) for j in range(n) if j != s and pair(GEN, alpha_s, walls[j]) != 0}
    for j, g in edges.items():
        assert g * g / (pair(GEN, alpha_s, alpha_s) * pair(GEN, walls[j], walls[j])) == Fraction(1, 2), "only order-4 edges"
    simple = {("wall", j): walls[j] for j in range(n) if j != s and j not in edges}
    for u in edges:
        beta = [walls[u][i] + alpha_s[i] for i in range(12)]
        assert pair(GEN, beta, alpha_s) == 0
        simple[("beta", u)] = beta
    roots = [key for key, x in simple.items() if pair(GEN, x, x) == -2 and pair(GEN, x, v) == 0]
    parent = {key: key for key in roots}

    def find(key):
        while parent[key] != key:
            key = parent[key]
        return key

    for a, b in itertools.combinations(roots, 2):
        g = pair(GEN, simple[a], simple[b])
        if g * g / (pair(GEN, simple[a], simple[a]) * pair(GEN, simple[b], simple[b])) == Fraction(1, 4):
            parent[find(a)] = find(b)  # an edge of order 3: conjugate reflections
    fixing = [g for g in closure(symmetries[statement], n) if g[s] == s] if symmetries[statement] else [tuple(range(n))]
    for g in fixing:
        for key in roots:
            image = (key[0], g[key[1]])
            assert image in parent, (statement, key, image)
            parent[find(key)] = find(image)
    classes = {}
    for key in roots:
        classes.setdefault(find(key), []).append(key)
    co_v = to_co(v)
    size, k = cusp_orbit(co_v)
    label = lambda key: names[key[1]] if key[0] == "wall" else f"beta({names[key[1]]})"
    print(f"   chamber ({statement}) -> T_Co cusp {co_v}: Gamma_Co,2-cusp of orbit size {size} {k};"
          f" {len(fixing)} symmetries fix delta; {len(roots)} root walls of W_perp, {len(classes)} orbits")
    for members in classes.values():
        print("      orbit:", [(label(key), to_co(simple[key])) for key in members])
