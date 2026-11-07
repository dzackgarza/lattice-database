#!/usr/bin/env bash
# Verify the recovery of run 42326648686 as values, not as an incident.
# Inside the published image with supported PYTHONPATH, exact usual command:
set -euo pipefail
export PYTHONPATH="${GITHUB_WORKSPACE}/research/src:${GITHUB_WORKSPACE}/src"
pythonbin=/sage/.venv/bin/python

echo "1. Every artifact recovers to a valid card and validates its computed fields' certificates"
"$pythonbin" results/recover-42326648686.py attachments/you-work-the-github-s6pa/extracted/openmath-certify-42326648686

echo "2. Store counts and recomputed hashes with the real preamble"
"$pythonbin" results/verify-recovered-values.py attachments/you-work-the-github-s6pa/extracted/openmath-certify-42326648686

echo "3. Persistence by the workflow's selection (a commit, no remote push; inspect before accepting)"
"$pythonbin" results/persist-recovered-changes.py
