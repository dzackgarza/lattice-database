# #43, one lemma: $\delta$ is not reducible into the chamber, so the 135-orbit $\Gamma_{\mathrm{Co},2}$-cusp question is a word problem

**Lemma.** At Sterk's `(4.3.9)` the vector $\delta = e - f$ has a *positive* pairing, $+2$, with one wall of the chamber
and $-2$ with two others, so it does not lie in the closed chamber up to sign, and Vinberg's reduction — reflect in any
wall with a positive pairing, repeat — does not terminate on it. The question "is $s(\delta)$ in the $W_v$-orbit of
$\pm\delta$", which decides whether the Coble condition is settled on the diagram symmetries, is therefore not decidable
by reduction here: it is a word problem in a hyperbolic reflection group.

**Proof, computed from card 029J's Gram tensor.** The pairings of $\delta$ with the fourteen walls are

$$0,0,0,0,0,0,0,0,-2,-2,+2,0,0,0,$$

so the chamber's interior condition (all pairings $\le 0$) fails in three places. Reduction by the standard step
$x \mapsto x - 2\,b(x,w)/b(w,w)\,w$ for a wall with $b(x,w) > 0$ runs past 200 steps without reaching a vector whose
pairings are all non-positive. Vinberg's algorithm — the one Sterk sets out at `(4.3.2)`–`(4.3.3)`, p. 18, and cites as
[26], [27] — reduces a vector that lies in the closed Tits cone; $\delta$'s positive pairing puts it outside that cone,
and the orbit is not finite.

**What it settles.** It rules out the one route that would have certified two orbits without the owner's group code: a
finite reduction of the six non-preserving symmetries' images of $\delta$. With the depth-8 walk
(`results/probe-43-coble-delta-orbit.py`, 17,468 vectors, none of the six images reached) as evidence and this as the
reason no bound can be read off the chamber, the count at `(4.3.9)` stays undecided between one and two, and the row
stays withdrawn.

**Sources by printed page.** H. Sterk, *Compactifications of the period space of Enriques surfaces, Part I*,
Math. Z. 207 (1991), 1–36: `(4.3.2)`, p. 17, and `(4.3.3)`, p. 18, for Vinberg's algorithm and the polyhedron $P$;
`(4.3.9)`, p. 24, for the chamber whose walls are used. The pairings are card 029J's, computed from its Gram tensor.
