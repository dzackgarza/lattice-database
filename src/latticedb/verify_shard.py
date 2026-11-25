"""Verify one shard of the cards in a process of its own.

`latticedb verify` starts one of these for each shard of the corpus, so that one
process holds one shard's worth of the structures the preamble memoizes and then
ends (#6). The process reads its shard on standard input, writes one JSON problem
per line, and reports the peak memory it needed, which the caller leaves attached
so that a run's log records it.
"""

import json
import resource
import sys
from pathlib import Path

from latticedb import checks


def main() -> None:
    """Verify the shard named on standard input and report the memory it needed."""
    request = json.loads(sys.stdin.readline())
    index, count = int(request["index"]), int(request["count"])
    verified, problems = checks.run(Path(request["root"]), (index, count))
    for problem in problems:
        print(json.dumps(problem), flush=True)
    print(json.dumps({"verified": verified}), flush=True)
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20
    print(f"memory: {peak:.1f} GiB peak for {verified} cards in shard {index}/{count}", file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()
