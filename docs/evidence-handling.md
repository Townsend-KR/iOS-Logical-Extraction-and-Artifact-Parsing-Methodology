# Evidence Handling

## Evidence-First Approach

The project uses a non-destructive workflow intended to preserve the state of source artifacts while allowing repeatable analysis.

### Originals and Working Copies

Where an original source artifact is available:

1. Record source and provenance information that can be established.
2. Calculate a cryptographic hash.
3. Preserve the original artifact.
4. Create a working copy for examination.
5. Record hashes of working copies when useful for reproducibility.

### SQLite Considerations

SQLite databases may have associated `-wal` and `-shm` files. These files are treated as potentially relevant components of database state and should be collected and preserved together when present.

Opening a database with ordinary SQLite tooling can cause state changes in some circumstances. Examination procedures therefore favor copies and read-only access.

### Public Repository Boundary

No original evidentiary database or private communication belongs in this repository. Public examples must be synthetic or sanitized.

The repository may document hashes of deliberately created demonstration files. Hashes of sensitive source material should not be published merely to prove that hashing occurred.

### Chain of Custody vs. Provenance

This portfolio documents provenance and evidence-handling methodology. It does not claim a formal law-enforcement chain of custody for historical artifacts where such a chain was not established contemporaneously.
