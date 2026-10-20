"""Attempt a real certificate update under a process file-size limit."""

import errno
import resource
import sys
from pathlib import Path

from latticedb import certificates

root = Path(sys.argv[1])
held = certificates.load(root)
held.update({f"specimen-{index}": certificates.Certificate(hash="a" * 64, by="computed") for index in range(40)})
resource.setrlimit(resource.RLIMIT_FSIZE, (1024, 1024))
try:
    certificates.save(root, held)
except OSError as error:
    if error.errno != errno.EFBIG:
        raise
    sys.exit(errno.EFBIG)
raise AssertionError("the filesystem limit did not interrupt the write")
