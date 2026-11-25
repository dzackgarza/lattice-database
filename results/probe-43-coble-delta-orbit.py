"""#43: is any symmetry's image of delta in the W_v-orbit of +-delta?  Bounded, and it does not settle it.

The withdrawn (4.3.9) row claimed two orbits on the ground that the Coble condition is decided on the diagram
symmetries, since the reflection subgroup fixes delta. The reflection subgroup does not fix delta, so the question is
whether some product ws (w in W_v, s a symmetry) preserves delta. That happens exactly when s(delta) lies in the
W_v-orbit of +-delta for some symmetry s, which is what this walks.

Measured: the orbit of +-delta under the fourteen wall reflections has 17,468 elements at depth 8, and none of the six
symmetries that do not preserve delta has s(delta) in it. That is evidence and not a proof — the orbit may be infinite,
and a step beyond depth 8 is not excluded — so the row stays withdrawn.

Original description follows.

#43: is any symmetry's image of delta in the W_v-orbit of +-delta?

If some s in S (a diagram symmetry not preserving delta) has s(delta) = w(+-delta) for w in W_v, then w^-1 s (or its
product) preserves delta and the Coble condition is NOT decided on the symmetries alone. Otherwise it is.
"""
from sage.all import matrix, ZZ, QQ, vector
import frontmatter

meta = frontmatter.load("/repo/lattices/029J.md").metadata
gram = matrix(QQ, [[QQ(e) for e in r] for r in meta["gram_tensor"]])
n = gram.nrows()
ch = meta["integral"]["cusp_chambers"]["gamma-en-2"][4]
walls = [vector(QQ, [QQ(e) for e in w["vector"]]) for w in ch["walls"]]
names = [w["name"] for w in ch["walls"]]
delta = vector(QQ, [1, -1] + [0] * (n - 2))

def pair(a, b): return (matrix(QQ, 1, n, list(a)) * gram * matrix(QQ, n, 1, list(b)))[0, 0]

def reflect(w, x):
    return x - (2 * pair(x, w) / pair(w, w)) * w

# W_v-orbit of +-delta, breadth first
frontier = [delta, -delta]
seen = {tuple(delta), tuple(-delta)}
depth = 0
while frontier and depth < 8:
    nxt = []
    for x in frontier:
        for w in walls:
            y = reflect(w, x)
            key = tuple(y)
            if key not in seen:
                seen.add(key); nxt.append(y)
    frontier = nxt
    depth += 1
    print(f"depth {depth}: orbit size {len(seen)}", flush=True)

# the eight symmetries as permutations of the walls, and their image of delta on the span
sq = [pair(w, w) for w in walls]
perms = []
def ext(p):
    if len(p) == len(walls): perms.append(dict(p)); return
    i = len(p)
    for j in range(len(walls)):
        if j in p.values() or sq[j] != sq[i]: continue
        if all(pair(walls[i], walls[k]) == pair(walls[j], walls[p[k]]) for k in p):
            p[i] = j; ext(p); del p[i]
ext({})
independent, chosen = [], []
for i, w in enumerate(walls):
    if matrix(QQ, independent + [list(w)]).rank() > len(independent):
        independent.append(list(w)); chosen.append(i)
B = matrix(QQ, independent)
co = (B * B.transpose()).inverse() * B * matrix(QQ, n, 1, list(delta))
for p in perms:
    img = vector(QQ, [sum((co[i, 0] * walls[p[chosen[i]]][r] for i in range(len(independent))), QQ(0)) for r in range(n)])
    tag = "delta" if img == delta else "-delta" if img == -delta else ("in the orbit" if tuple(img) in seen else "not in the orbit reached")
    print("  symmetry:", {names[k]: names[v] for k, v in p.items() if k != v} or "identity", "->", tag, flush=True)
