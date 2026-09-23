# Forensic Methodology

## Purpose

This project documents a repeatable approach to examining Apple/iOS artifacts obtained through more than one authorized acquisition or recovery path. The methodology separates how an artifact was obtained from how it was subsequently preserved, parsed, correlated, and interpreted.

## Workflow

### 1. Acquisition or Recovery Classification

Each dataset is classified according to the source information actually available. Useful classifications include backup-derived logical data, recovered SQLite databases, historical database copies, recovered filesystem artifacts, synchronization-related artifacts, secondary-storage recovery, and legacy artifacts with incomplete provenance.

A classification is not upgraded merely because the artifact can be parsed successfully.

### 2. Preservation

Original artifacts are retained separately from analysis output. Cryptographic hashes are calculated where source files are available, and analysis should occur against working copies whenever practical.

SQLite companion files such as `-wal` and `-shm` are preserved with the database rather than discarded as incidental files.

### 3. Inventory

Artifacts are inventoried before content-driven searching. Relevant metadata can include filename, relative source location when safe and known, byte size, cryptographic hash, detected file type, SQLite metadata, WAL/SHM presence, acquisition/recovery classification, and provenance notes.

### 4. Validation and Schema Discovery

SQLite databases are examined structurally before substantive queries are applied. Table and column names, relationships, indexes, triggers, and relevant metadata are documented. Integrity checks may be performed against working copies.

Queries are treated as schema-dependent. A query validated against one database generation is not assumed to work against another.

### 5. Parsing and Normalization

Records are parsed from relevant tables and relationships. Timestamp values are interpreted according to the artifact and schema being examined, then normalized for comparison while retaining the original value where useful.

### 6. Correlation

Correlation may involve relationships within one database, associated attachments, companion databases, or independent historical copies. Temporal agreement is supporting evidence, not automatic proof that two records represent the same event.

### 7. Reconstruction and Validation

Reconstructed activity should be traceable back to the underlying artifact. Where possible, findings are validated through multiple fields, relationships, or independent artifacts.

### 8. Reporting

Reporting distinguishes directly observed values, decoded or normalized values, relationships established by database structure, analytical inferences, and unresolved questions.

## Core Principle

A successful parse is not itself a forensic conclusion. Provenance, structure, context, and limitations remain part of the finding.
