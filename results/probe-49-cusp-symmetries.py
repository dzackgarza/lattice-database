"""#49: the diagram symmetries at Sterk's cusps of card 029J, and the root classes at the Coble cusp (4.3.9).

Part (a). For each stored chamber of `integral.cusp_chambers['gamma-en-2']`, the symmetries of its Coxeter diagram with
the wall squares kept are the permutations of the walls that preserve their Gram matrix. Each is tested for being an
isometry of the boundary lattice K_J = v^perp / Z v: the walls span K_J (x) Q, so a permutation defines at most one
linear map, and the script reports whether that map is integral and unimodular on K_J. It prints the group the
realized symmetries induce on each orbit of the root walls (the walls of square -2), and the order of that group.

Part (b). At (4.3.9), delta = e - f is minus the wall alpha_11 (T_Co = delta^perp). The script prints the Coxeter
edges at alpha_11 (an odd edge is the only way a simple reflection is conjugate to another), the symmetries fixing
alpha_11, the chamber of the reflection subgroup W_perp on delta^perp (the walls orthogonal to alpha_11 and, for each
even edge alpha_11 - alpha_k, the root of span{alpha_11, alpha_k} orthogonal to alpha_11), its diagram, the classes
of its root walls under odd paths, and the orbits of those classes under the symmetries fixing alpha_11.

    sage-docker-python results/probe-49-cusp-symmetries.py
"""

import sys
from pathlib import Path

import yaml
from sage.all import QQ, ZZ, PermutationGroup, matrix, vector

card = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "lattices" / "029J.md")
meta = yaml.safe_load(card.read_text().split("---")[1])
gram = matrix(ZZ, meta["gram_tensor"])
rows = meta["integral"]["cusp_chambers"]["gamma-en-2"]


def boundary(cusp):
    """A Z-basis of K_J = v^perp / Z v as rows, and the coordinate map of v^perp into it."""
    perp = matrix(ZZ, [list(gram * cusp)]).right_kernel_matrix()
    c = perp.solve_left(cusp)
    _, _, change = matrix(ZZ, [list(c)]).smith_form()
    basis = change.inverse()  # first row is +-c
    assert abs(basis[0] * perp * gram * cusp) == 0 and vector(ZZ, basis[0]) in (c, -c)
    quotient = basis[1:] * perp
    def coords(x):
        return vector(ZZ, (perp.solve_left(x) * change)[1:])
    return quotient * gram * quotient.transpose(), coords


def symmetries(g):
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


def order(a, b, g):
    c = QQ(g[a, b] ** 2) / (g[a, a] * g[b, b])
    return {QQ(0): 2, QQ(1) / 4: 3, QQ(1) / 2: 4, QQ(3) / 4: 6}.get(c, "inf")


for row in rows:
    if "walls" not in row or row["statement"] == "4.3.5":
        continue
    cusp = vector(ZZ, row["cusp"])
    names = [w["name"] for w in row["walls"]]
    walls = [vector(ZZ, w["vector"]) for w in row["walls"]]
    gk, coords = boundary(cusp)
    k = [coords(w) for w in walls]
    wg = matrix(ZZ, [[a * gram * b for b in walls] for a in walls])
    assert wg == matrix(ZZ, [[QQ(x) for x in r] for r in row["gram"]]), "stored wall Gram differs"
    chosen = []
    for i, x in enumerate(k):
        if matrix(QQ, [k[j] for j in chosen] + [x]).rank() > len(chosen):
            chosen.append(i)
    assert len(chosen) == gk.nrows(), "the walls do not span K_J (x) Q"
    sub = matrix(QQ, [k[i] for i in chosen])
    realized = []
    print(f"== ({row['statement']}) cusp {list(cusp)}: {len(walls)} walls, K_J rank {gk.nrows()}, det {gk.det()}")
    for perm in symmetries(wg):
        a = sub.inverse() * matrix(QQ, [k[perm[i]] for i in chosen])
        linear = all(k[i] * a == k[perm[i]] for i in range(len(walls)))
        integral = linear and all(x in ZZ for x in a.list()) and abs(a.det()) == 1 and a * gk * a.transpose() == gk
        moved = {names[i]: names[perm[i]] for i in range(len(walls)) if perm[i] != i}
        print(f"  symmetry {moved or 'identity'}: linear {linear}, an isometry of K_J {integral}")
        if integral:
            realized.append(perm)
    roots = [i for i in range(len(walls)) if wg[i, i] == -2]
    print(f"  realized symmetries: {len(realized)}; root walls: {[names[i] for i in roots]}")
    group = PermutationGroup([[p[i] + 1 for i in range(len(walls))] for p in realized], domain=list(range(1, len(walls) + 1)))
    for orbit in group.orbits():
        orbit = sorted(x - 1 for x in orbit)
        if orbit[0] not in roots:
            continue
        induced = {tuple(p[i] for i in orbit) for p in realized}
        print(f"  root-wall orbit {[names[i] for i in orbit]}: induced permutation group of order {len(induced)}")
    if row["statement"] != "4.3.9":
        continue

    print("== part (b): the Coble cusp, delta = -alpha_11")
    s = names.index("\\alpha_11")
    delta = vector(ZZ, [1, -1] + [0] * 10)
    assert walls[s] == -delta
    print("  edges at alpha_11:", {names[j]: order(s, j, wg) for j in range(len(walls)) if j != s and wg[s, j] != 0})
    fixing = [p for p in realized if p[s] == s]
    print("  realized symmetries fixing alpha_11:", [{names[i]: names[p[i]] for i in range(len(walls)) if p[i] != i} or "identity" for p in fixing])
    perp_walls, perp_names = [], []
    for j in range(len(walls)):
        if j == s:
            continue
        if wg[s, j] == 0:
            perp_walls.append(walls[j]); perp_names.append(names[j])
        elif order(s, j, wg) == 4:
            # the root of span{alpha_11, alpha_j} orthogonal to alpha_11: alpha_j + t alpha_11
            t = -QQ(wg[s, j]) / wg[s, s]
            beta = walls[j] + t * walls[s]
            assert beta in ZZ ** 12 and beta * gram * walls[s] == 0
            perp_walls.append(vector(ZZ, beta)); perp_names.append(f"beta({names[j]})")
        else:
            raise AssertionError(f"edge of order {order(s, j, wg)} at alpha_11")
    pg = matrix(ZZ, [[a * gram * b for b in perp_walls] for a in perp_walls])
    print("  W_perp chamber walls and squares:", [(perp_names[i], pg[i, i]) for i in range(len(perp_walls))])
    print("  off-diagonal pairings all >= 0 (a Coxeter chamber in this sign convention):", all(pg[i, j] >= 0 for i in range(pg.nrows()) for j in range(pg.nrows()) if i != j))
    edges = [(perp_names[i], perp_names[j], order(i, j, pg)) for i in range(pg.nrows()) for j in range(i + 1, pg.nrows()) if pg[i, j] != 0]
    print("  W_perp diagram edges:", edges)
    proots = [i for i in range(pg.nrows()) if pg[i, i] == -2]
    # classes of root walls under odd paths (edges of order 3 between root walls)
    parent = {i: i for i in proots}
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i in proots:
        for j in proots:
            if i < j and order(i, j, pg) == 3:
                parent[find(i)] = find(j)
    classes = {}
    for i in proots:
        classes.setdefault(find(i), []).append(perp_names[i])
    print("  W_perp-classes of root walls (odd paths):", list(classes.values()))
    # action of the alpha_11-fixing symmetries on the W_perp walls
    image_of = {}
    for p in fixing:
        a = sub.inverse() * matrix(QQ, [k[p[i]] for i in chosen])
        mapped = {}
        for i, w in enumerate(perp_walls):
            img = coords(w) * a
            hits = [perp_names[j] for j, x in enumerate(perp_walls) if coords(x) == img]
            assert len(hits) == 1
            mapped[perp_names[i]] = hits[0]
        image_of[tuple(p)] = mapped
    reps = [frozenset(c) for c in classes.values()]
    merged = {r: r for r in reps}
    for mapped in image_of.values():
        for r in reps:
            target = next(t for t in reps if mapped[next(iter(r))] in t)
            a, b = merged[r], merged[target]
            if a != b:
                for key in merged:
                    if merged[key] == b:
                        merged[key] = a
    orbits = {}
    for r in reps:
        orbits.setdefault(merged[r], []).append(sorted(r))
    print("  orbits of the root classes under (s_11 x W_perp) x <symmetries fixing alpha_11>:", list(orbits.values()))
    print("  count:", len(orbits))
