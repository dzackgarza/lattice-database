"""Run the command line, or one of Git's merge drivers, without importing the Sage stack.

Git calls `merge-keyed-map` and `card_merge` as merge drivers of `certificates/`, `exceeded.yaml`
and `lattices/` (`.gitattributes`). Both are pure Python over YAML and Markdown, but the command
line imports the corpus, which imports the research preamble: routed through it, a merge driver
therefore needs a working Sage session, and a driver that cannot import is a merge Git reports as
a conflict with no side to it (#47). The driver names are dispatched here, before the import.
"""

import sys
from pathlib import Path

DRIVERS = ("merge-keyed-map", "card_merge")


def main(argv: list[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if arguments and arguments[0] in DRIVERS:
        if len(arguments) != 4:
            print(f"usage: python -m latticedb {arguments[0]} BASE OURS THEIRS", file=sys.stderr)
            return 2
        base, ours, theirs = (Path(argument) for argument in arguments[1:])
        if arguments[0] == "merge-keyed-map":
            from latticedb.keyed_merge import merge_files
        else:
            from latticedb.card_merge import merge_files
        merge_files(base, ours, theirs)
        return 0
    from latticedb.cli import main as command_line

    command_line()
    return 0


if __name__ == "__main__":
    sys.exit(main())
