# Where the image wrapper's parts are, without depending on HOME. Sourced by the launchers that run a
# check through `sage-image/run.sh` (`verify-launcher.sh` and its unrepaired counterpart), so both
# start a guest in the same environment and differ only in what they require of its result (#41).
#
# `sage-image/run.sh` expands `$HOME/sage-image/rootfs` and `$HOME/.udocker/bin/proot-x86_64` under
# `set -u`, and the image's own OCI environment (`env.oci`) carries no HOME. So a launcher run inside
# the image died at the wrapper's line 7 with `HOME: unbound variable`, before proot existed: no
# `PYEXIT=` line, no per-item result, and a report that said only `PYEXIT=absent, results=0`.
# Both parts sit beside the wrapper that SAGE_IMAGE names, so they are resolved from there and passed
# to the wrapper explicitly; SAGE_ROOTFS, SAGE_PROOT and SAGE_IMAGE override each.
#
# Sets IMAGE, ROOT and PROOT. The caller defines nothing first.
IMAGE=${SAGE_IMAGE:-/workspace/nucleus/work/home/sage-image/run.sh}
wrapper_dir=$(dirname "$IMAGE")
prefix_dir=$(cd "$wrapper_dir/.." 2>/dev/null && pwd || echo "$wrapper_dir/..")
ROOT=${SAGE_ROOTFS:-$wrapper_dir/rootfs}
PROOT=${SAGE_PROOT:-$prefix_dir/.udocker/bin/proot-x86_64}
# A wrapper kept away from the tree that holds its rootfs and proot: fall back to the wrapper's own
# defaults, which read HOME.
if [ ! -d "$ROOT" ] && [ -n "${HOME:-}" ] && [ -d "$HOME/sage-image/rootfs" ]; then
  ROOT=$HOME/sage-image/rootfs
fi
if [ ! -x "$PROOT" ] && [ -n "${HOME:-}" ] && [ -x "$HOME/.udocker/bin/proot-x86_64" ]; then
  PROOT=$HOME/.udocker/bin/proot-x86_64
fi
