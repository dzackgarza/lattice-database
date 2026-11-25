"""#49, #43: the image S of the Gamma_Co,2 cusp stabilizer in the symmetries of the cusp face's Coxeter diagram.

At each of the four Gamma_{Co,2}-cusps v of T_Co (card 6JRR) the chamber is the face C cap delta^perp of Sterk's
chamber at the T_En cusp of v. It is the chamber of W_perp, with walls the walls of C orthogonal to delta and
beta_u = alpha_u + delta (`results/issue-49-transporters-and-coble-cusp5.md`). This program assumes no lifting
statement. For each Gram-preserving permutation sigma of the face walls it:

1. builds the rational isometry g0 of T_Co with g0(v) = v and g0(w_b) = w_sigma(b) on nine independent walls. It then
   checks that g0 carries every wall to the image wall mod Qv.
2. computes the lattice Lambda = {a in v^perp (x) Q : E(v, a) integral} of Eichler transvections
   E(v, a)(x) = x - (a, x) v + (v, x) a - (a, a)/2 (v, x) v
   (Gritsenko-Hulek-Sankaran, arXiv:0810.1614, Sect. 3.1, eq. (4)). These make up the kernel of Stab_{O(T_Co)}(v) on
   v^perp/Zv, so the lifts of sigma to Stab_{O(T_Co)}(v) are the integral E(v, a) g0.
3. finds an integral lift g if one exists. It then decides whether some lift lies in Gamma_{Co,2} = rho^{-1}(P_0),
   P_0 = Stab(A_U(2)) (sage-extensions `results/issue607-gamma-co-2-rows-by-the-polar-space.md`). That is: does the
   coset rho(g) rho(E(v, Lambda)) meet P_0? Here A_{T_Co} = (1/2)T_Co/T_Co, so rho(h) is h mod 2, and P_0 is the
   stabilizer of span(e1, f1) mod 2.

sigma is in S exactly when step 3 finds such a lift. The probe prints the order of S, its generators as permutations
of the face walls in the printed order, the face chamber (walls, Gram, diagram) and the root-class orbits under S.

    sage-docker-python results/probe-49-gamma-co-2-chamber-symmetries.py
"""

import itertools
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import yaml
from sage.all import GF, QQ, ZZ, matrix, vector

ROOT = Path(__file__).resolve().parent.parent
START = time.time()


def front(tag):
    return yaml.safe_load((ROOT / "lattices" / f"{tag}.md").read_text().split("---")[1])


co, en = front("6JRR"), front("029J")
G = matrix(QQ, co["gram_tensor"])
GEN = matrix(QQ, en["gram_tensor"])
n = 11
DELTA = vector(QQ, [1, -1] + [0] * 10)


def to_co(x):
    assert x[0] == x[1]
    return vector(QQ, [x[0]] + list(x[2:]))


def b(x, y):
    return (x * G * y)


def edge_order(x, y):
    g = b(x, y)
    if g == 0:
        return None
    r = g * g / (b(x, x) * b(y, y))
    return {QQ(1) / 4: 3, QQ(1) / 2: 4, QQ(3) / 4: 6}.get(r, "inf")


def eichler(v, a):
    cols = []
    for j in range(n):
        e = vector(QQ, [1 if i == j else 0 for i in range(n)])
        cols.append(e - b(a, e) * v + b(v, e) * a - b(a, a) / 2 * b(v, e) * v)
    return matrix(QQ, cols).transpose()


def integral(m):
    return all(x.denominator() == 1 for x in m.list())


def in_p0(m2):
    return all(m2[i, j] == 0 for j in (1, 2) for i in range(n) if i not in (1, 2))


out = []
for chamber in en["integral"]["cusp_chambers"]["gamma-en-2"]:
    v_en = vector(QQ, chamber["cusp"])
    if v_en * GEN * DELTA != 0:
        continue
    walls_en = [vector(QQ, w["vector"]) for w in chamber["walls"]]
    names_en = [w["name"] for w in chamber["walls"]]
    (s,) = [i for i, w in enumerate(walls_en) if w in (DELTA, -DELTA)]
    nbrs = [j for j in range(len(walls_en)) if j != s and walls_en[s] * GEN * walls_en[j] != 0]
    face = [(names_en[j], to_co(walls_en[j])) for j in range(len(walls_en)) if j != s and j not in nbrs]
    face += [(f"{names_en[j]} + {names_en[s]}", to_co(walls_en[j] + walls_en[s])) for j in nbrs]
    names = [f[0] for f in face]
    W = [f[1] for f in face]
    v = to_co(v_en)
    k = len(W)
    gram = [[b(W[i], W[j]) for j in range(k)] for i in range(k)]
    assert all(b(w, v) == 0 for w in W)

    sigmas = []

    def extend(p):
        i = len(p)
        if i == k:
            sigmas.append(tuple(p))
            return
        for t in range(k):
            if t in p or gram[t][t] != gram[i][i]:
                continue
            if all(gram[i][o] == gram[t][p[o]] for o in range(i)):
                p.append(t)
                extend(p)
                p.pop()

    extend([])

    # nine walls independent modulo v, and u with (u, v) != 0
    chosen = []
    for i in range(k):
        if matrix(QQ, [v] + [W[c] for c in chosen] + [W[i]]).rank() == len(chosen) + 2:
            chosen.append(i)
    assert len(chosen) == 9
    u = next(vector(QQ, [1 if i == j else 0 for i in range(n)]) for j in range(n) if b(vector(QQ, [1 if i == j else 0 for i in range(n)]), v) != 0)
    basis = matrix(QQ, [v] + [W[c] for c in chosen] + [u]).transpose()
    assert basis.rank() == n

    # Lambda: a = y/2 with y in v^perp cap T_Co mod 2 (the (v, x) a term forces 2a in T_Co + Qv, since (v, T_Co) = 2Z)
    vperp = matrix(ZZ, [list(v * G)]).right_kernel().basis_matrix()
    assert vperp.nrows() == 10
    assert all(x % 2 == 0 for x in (v * G).list()) and __import__("math").gcd(*[int(x) for x in (v * G).list()]) == 2
    lam_gens = [vector(QQ, r) for r in vperp.rows()]
    for y in itertools.product((0, 1), repeat=10):
        if any(y):
            a = sum((QQ(c) / 2 * r for c, r in zip(y, vperp.rows())), vector(QQ, [0] * n))
            if integral(eichler(v, a)):
                lam_gens.append(a)
    # rho(K_v) is generated by the rho(E(v, a)), a in lam_gens; a generator already in the group is skipped
    one = matrix(ZZ, n, n, 1)
    key = lambda m: tuple(m.change_ring(GF(2)).list())
    group = {key(one): one}
    for a in lam_gens:
        h = eichler(v, a).change_ring(ZZ)
        if key(h) in group:
            continue
        frontier = list(group.values())
        while frontier:
            x = frontier.pop()
            y = h * x
            if key(y) not in group:
                group[key(y)] = y
                frontier.append(y)
                for z in list(group.values()):
                    w = z * y
                    if key(w) not in group:
                        group[key(w)] = w
                        frontier.append(w)
    kernel_image = list(group.values())

    in_S, lifted, notlift, witnesses = [], 0, 0, {}
    for sigma in sigmas:
        images = matrix(QQ, [v] + [W[sigma[c]] for c in chosen] + [vector(QQ, [0] * n)]).transpose()
        # x = g0(u): (x, v) = (u, v), (x, W[sigma c]) = (u, W[c]), (x, x) = (u, u); x = x0 + t v
        A = matrix(QQ, [list(v * G)] + [list(W[sigma[c]] * G) for c in chosen])
        rhs = vector(QQ, [b(u, v)] + [b(u, W[c]) for c in chosen])
        x0 = A.solve_right(rhs)
        t = (b(u, u) - b(x0, x0)) / (2 * b(x0, v))
        x = x0 + t * v
        images[:, n - 1] = x
        g0 = images * basis.inverse()
        assert g0.transpose() * G * g0 == G
        for i in range(k):
            d = g0 * W[i] - W[sigma[i]]
            assert matrix(QQ, [v, d]).rank() <= 1, "g0 carries every wall to its image mod Qv"
        # an integral lift E(v, a) g0, with a in (1/4)(v^perp cap T_Co), searched modulo v^perp cap T_Co
        lift = None
        den = max(x.denominator() for x in g0.list())
        assert den <= 2, f"g0 has denominator {den}"
        for y in itertools.product(range(4), repeat=10) if den > 1 else [(0,) * 10]:
            a = sum((QQ(c) / 4 * r for c, r in zip(y, vperp.rows())), vector(QQ, [0] * n))
            m = eichler(v, a) * g0
            if integral(m):
                lift = m
                break
        if lift is None:
            notlift += 1
            continue
        lifted += 1
        member = next((h * lift.change_ring(ZZ) for h in kernel_image if in_p0((h * lift.change_ring(ZZ)).change_ring(GF(2)))), None)
        if member is not None:
            assert member.transpose() * G * member == G and member * v == v
            in_S.append(sigma)
            witnesses[sigma] = [[int(c) for c in r] for r in member.rows()]
    # generators of S
    gens, closure = [], {tuple(range(k))}
    for sigma in in_S:
        if sigma not in closure:
            gens.append(sigma)
            frontier = list(closure)
            closure = set(closure)
            changed = True
            while changed:
                changed = False
                for p in list(closure):
                    for h in gens:
                        q = tuple(h[p[i]] for i in range(k))
                        if q not in closure:
                            closure.add(q)
                            changed = True
    assert closure == set(in_S), "S is a group"
    roots = [i for i in range(k) if gram[i][i] == -2]
    orbits = sorted({tuple(sorted({sg[i] for sg in in_S})) for i in roots})
    diagram = [
        {"a": names[i], "b": names[j], "order": edge_order(W[i], W[j])}
        for i in range(k) for j in range(i + 1, k) if edge_order(W[i], W[j]) is not None
    ]
    row = {
        "cusp": [int(c) for c in v],
        "walls": [{"name": names[i], "vector": [int(c) for c in W[i]]} for i in range(k)],
        "wall_count": k,
        "gram": [[str(x) for x in r] for r in gram],
        "diagram": diagram,
        "symmetry_order": len(in_S),
        "symmetry_generators": [list(g) for g in gens],
        "symmetry_witnesses": [witnesses[g] for g in gens],
        "root_orbits": [[[int(c) for c in W[i]] for i in o] for o in orbits],
    }
    out.append(row)
    print(
        f"[{time.time() - START:6.1f}s] cusp {row['cusp']} (Sterk ({chamber['statement']})): {k} face walls, "
        f"{len(sigmas)} diagram symmetries, {lifted} lift to O(T_Co) fixing v, {notlift} do not, |rho(K_v)| = {len(kernel_image)}, "
        f"|S| = {len(in_S)}, generators {row['symmetry_generators']}, root-class orbits {[len(o) for o in orbits]}",
        flush=True,
    )
print("JSON " + json.dumps(out))
