from sage.all import matrix, ZZ, QQ, vector
import frontmatter
meta = frontmatter.load("/repo/lattices/029J.md").metadata
gram = matrix(QQ, [[QQ(e) for e in r] for r in meta["gram_tensor"]])
n = gram.nrows()
ch = meta["integral"]["cusp_chambers"]["gamma-en-2"][4]
walls = [vector(QQ, [QQ(e) for e in w["vector"]]) for w in ch["walls"]]
names = [w["name"] for w in ch["walls"]]
delta = vector(QQ, [1, -1] + [0]*(n-2))
def pair(a, b): return (matrix(QQ,1,n,list(a))*gram*matrix(QQ,n,1,list(b)))[0,0]
print("pairings of delta with the walls:", [str(pair(delta, w)) for w in walls])
def reflect(w, x): return x - (2*pair(x,w)/pair(w,w))*w
def reduce_vector(x, limit=200):
    for step in range(limit):
        moved = False
        for w in walls:
            c = pair(x, w)
            if c > 0:
                x = reflect(w, x); moved = True; break
        if not moved:
            return x, step
    return None, limit
red, steps = reduce_vector(delta)
print("delta reduces in", steps, "steps; equals delta:", red == delta, " equals -delta:", red == -delta if red is not None else None)
if red is not None:
    print("reduced delta:", list(red)[:6], "...")
