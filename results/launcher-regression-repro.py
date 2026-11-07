"""Controlled guest for results/launcher-regression.sh: prints, or fails, in a known way.

    launcher-regression-repro.py normal|incomplete|short|raise|segv

`normal` prints two per-item result lines and the anchored summary; `incomplete` prints both result
lines but no summary; `short` prints one of two; `raise` exits 1 after the results; `segv` kills
itself with SIGSEGV, which the image wrapper reports to its caller as exit 0.
"""
import os
import signal
import sys

MODE = sys.argv[1] if len(sys.argv) > 1 else "normal"

print("4ec0a9d032: 509 cards, 0 problems")
if MODE != "short":
    print("b29b4ba832: 674 cards, 0 problems")
if MODE in {"normal"}:
    print("\n0 problems in 1183 recovered cards over 2 commits")
if MODE == "raise":
    raise SystemExit(1)
if MODE == "segv":
    os.kill(os.getpid(), signal.SIGSEGV)
