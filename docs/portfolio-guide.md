# Portfolio Review Guide

This repository is designed to demonstrate digital-forensics methodology rather than publish case evidence.

## Start Here

A reviewer evaluating technical approach can begin with:

1. [Forensic Methodology](methodology.md)
2. [Evidence Handling](evidence-handling.md)
3. [Messages WAL State Comparison](case-studies/messages-wal-state-comparison.md)
4. [Synchronization-Assisted Messages Reconstruction](case-studies/synchronization-assisted-messages-reconstruction.md)
5. [Limitations and Interpretation Boundaries](limitations.md)

The [Unallocated-Space SQLite Recovery](case-studies/unallocated-space-sqlite-recovery.md) note is intentionally marked unresolved. It demonstrates documentation of uncertainty rather than conversion of a working hypothesis into a finding.

## Skills Demonstrated

The repository is intended to show practical experience with:

- preservation and SHA-256 inventory of forensic artifacts;
- SQLite database, WAL, and SHM handling;
- schema discovery before substantive querying;
- comparison of base-file and WAL-applied logical states;
- Apple Messages artifact analysis;
- synchronization and CloudKit-related artifact examination;
- timestamp normalization with explicit unit assumptions;
- cross-artifact correlation and reconstruction;
- secondary-storage recovery limitations;
- reproducible command-line/Python workflows; and
- reporting that separates observations, inference, hypotheses, and unresolved questions.

## Reproducibility

Utilities under `scripts/` use Python's standard library where practical. SQL under `queries/` begins with schema discovery rather than assuming one Apple schema applies universally.

No original evidentiary databases or private communications are required to review the methodology.

## Evidence Safety

Public examples must be synthetic, sanitized, or aggregate. The repository excludes original communications, credentials, account identifiers, device identifiers, private attachment content, and original evidence databases.

The goal is to make the technical reasoning reviewable without making the underlying private evidence public.
