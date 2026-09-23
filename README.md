# iOS Logical Extraction and Artifact Parsing Methodology

A digital-forensics portfolio project documenting the preservation, examination, parsing, and correlation of authorized Apple/iOS artifacts spanning approximately 2017 to the present.

## Project Scope

The source material examined in this project originated from multiple authorized sources, including:

- iOS backup-derived logical data
- recovered SQLite databases and historical database copies
- SQLite write-ahead log (WAL) and shared-memory (SHM) companions
- synchronization and CloudKit-related artifacts
- attachments and associated filesystem artifacts
- files recovered from secondary storage

Not every artifact in this project was produced by a logical extraction. Acquisition or recovery method is documented separately from subsequent artifact parsing and analysis.

The examination was performed without relying on interactive access to the originating devices, device passcodes, or application interfaces. This created constraints similar to those encountered when an examiner receives historical, backup-derived, or independently recovered evidence rather than a functioning unlocked device.

No commercial mobile-forensics suite was used for the artifact analysis documented here. The methodology emphasizes direct examination of underlying data with SQLite/SQL, filesystem analysis, cryptographic hashing, command-line/open-source tools, and purpose-built scripts where appropriate.

## Primary Artifact Families

Initial analysis focuses on:

- Apple Messages `chat.db`
- Apple Notes `NoteStore.sqlite`
- SQLite `-wal` and `-shm` files
- Messages attachments and relational records
- Notes/Core Data structures
- synchronization and CloudKit-related artifacts
- relevant metadata and property-list artifacts
- historical database instances spanning multiple Apple software generations

## Forensic Workflow

```text
Acquisition / Recovery
        |
        v
Preservation & Hashing
        |
        v
Artifact Inventory
        |
        v
Validation & Schema Discovery
        |
        v
Parsing & Timestamp Normalization
        |
        v
Cross-Artifact Correlation
        |
        v
Reconstruction & Validation
        |
        v
Documented Findings
```

The workflow is deliberately evidence-first. Source artifacts are preserved, analysis is performed against working copies where practical, and directly observed facts are distinguished from analytical inference.

## Repository Layout

| Path | Purpose |
| --- | --- |
| `docs/` | Scope, evidence handling, artifact methodology, limitations, and case studies |
| `scripts/` | Conservative utilities for hashing, inventory, SQLite metadata, and timestamp handling |
| `queries/` | Version-aware SQL examples for Messages, Notes, and SQLite examination |
| `samples/` | Synthetic or sanitized demonstration material only |
| `research/` | Technical references and schema/version research |

## Evidence Protection

This repository is intended to become public. Original evidentiary databases, private communications, credentials, account identifiers, device identifiers, phone numbers, email addresses, and other personally identifying information are not published.

Examples in this repository must be synthetic, sanitized, or structurally representative.

## Methodological Caution

The presence of a record or recovered file does not automatically establish authorship, ownership, user interaction, original path, or intent. Conclusions are limited to what the available artifacts and provenance support.

Likewise, SQLite schemas and timestamp representations can change between application and operating-system versions. Queries are therefore documented with their assumptions rather than presented as universally valid across every iOS release.

## Current Status

This repository is under active construction. Documentation and utilities are being added only when the underlying procedure or claim can be substantiated.

See [docs/methodology.md](docs/methodology.md), [docs/evidence-handling.md](docs/evidence-handling.md), and [docs/limitations.md](docs/limitations.md) for the initial methodology.
