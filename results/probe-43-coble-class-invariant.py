"""#43: the class of delta in K_I separates the symmetries that move delta — and settles cusp 5.

The Coble condition at (4.3.9) is whether a product ws (w in W_v, s a diagram symmetry) can fix delta. Every element of
W_v fixes the cusp v, so it acts on K_I = v^perp / Zv and preserves the *class* of a vector of v^perp. Hence if the class
of s(delta) differs from the class of +-delta, then s(delta) is not in the W_v-orbit of +-delta, and no such product
preserves delta.

This computes, from card 029J's Gram tensor, the class of delta and of every symmetry's image of it. Two of the eight
preserve delta itself — the identity and the symmetry exchanging alpha_13 with alpha_14 — and all six others land in a
different class. So the delta-preserving part of G_v is <W_v, sigma>, and the Coble cusp of three classes is two orbits.

Original script follows.
"""
from sage.all import matrix, ZZ, QQ, vector
import frontmatter
meta = frontmatter.load("/repo/lattices/029J.md").metadata
gram = matrix(QQ, [[QQ(e) for e in r] for r in meta["gram_tensor"]])
n = gram.nrows()
ch = meta["integral"]["cusp_chambers"]["gamma-en-2"][4]
walls = [vector(QQ, [QQ(e) for e in w["vector"]]) for w in ch["walls"]]
names = [w["name"] for w in ch["walls"]]
v = vector(QQ, [QQ(e) for e in ch["cusp"]])
delta = vector(QQ, [1, -1] + [0]*(n-2))
def pair(a,b): return (matrix(QQ,1,n,list(a))*gram*matrix(QQ,n,1,list(b)))[0,0]
print("b(delta, v) =", pair(delta, v))
sq = [pair(w,w) for w in walls]
perms=[]
def ext(p):
    if len(p)==len(walls): perms.append(dict(p)); return
    i=len(p)
    for j in range(len(walls)):
        if j in p.values() or sq[j]!=sq[i]: continue
        if all(pair(walls[i],walls[k])==pair(walls[j],walls[p[k]]) for k in p):
            p[i]=j; ext(p); del p[i]
ext({})
ind, chos = [], []
for i,w in enumerate(walls):
    if matrix(QQ, ind+[list(w)]).rank() > len(ind):
        ind.append(list(w)); chos.append(i)
B = matrix(QQ, ind)
co = (B*B.transpose()).inverse()*B
coeff = co * matrix(QQ, n, 1, list(delta))
def is_multiple_of_cusp(x):
    """Whether x is a rational multiple of the (isotropic) cusp vector."""
    index = next(i for i in range(n) if v[i] != 0)
    t = x[index] / v[index]
    return x == t * v
print("delta is not a multiple of the cusp:", not is_multiple_of_cusp(delta))
for p in perms:
    img = sum((coeff[i,0]*walls[p[chos[i]]] for i in range(len(ind))), vector(QQ, [0]*n))
    tag = ("delta" if img == delta else "-delta" if img == -delta else
           "same class" if (is_multiple_of_cusp(img - delta) or is_multiple_of_cusp(img + delta)) else "DIFFERENT class")
    print("  ", {names[k]: names[v_] for k, v_ in p.items() if k != v_} or "identity", "->", tag)
