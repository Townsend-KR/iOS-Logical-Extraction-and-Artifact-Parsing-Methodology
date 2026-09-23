# iOS Logical Extraction and Artifact Parsing Methodology

A digital-forensics portfolio project documenting the preservation, examination, parsing, and correlation of authorized Apple/iOS artifacts spanning approximately 2017 to the present.

**Focus:** SQLite • WAL/SHM • Apple Messages • synchronization/CloudKit artifacts • artifact correlation • hashing • recovery methodology • reproducible Python/SQL workflows

> This repository publishes methodology, aggregate results, and sanitized or synthetic examples. It does not publish original private evidence.

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

## Featured Case Studies

### Messages WAL State Comparison

A controlled comparison of `chat.db` before and after incorporation of the captured WAL documented a change from **53,072 to 53,073 message rows**, along with corresponding changes in attachment and relationship tables.

[Read the case study](docs/case-studies/messages-wal-state-comparison.md)

### Synchronization-Assisted Messages Reconstruction

The associated `Sync/sync.db` synchronization database was examined as a separate evidence source. Its WAL-applied state contained five additional `ZREMOTERECORD` entries relative to the base-file state. The methodology deliberately avoids assuming those records map directly to the local Messages changes without record-level validation.

[Read the case study](docs/case-studies/synchronization-assisted-messages-reconstruction.md)

### Unallocated-Space SQLite Recovery

A secondary-storage observation involving Messages-related SQLite material recovered from unallocated space is documented as **unresolved** while the original recovery records are being located. The working hypothesis is explicitly separated from established findings.

[Read the unresolved recovery note](docs/case-studies/unallocated-space-sqlite-recovery.md)

## Primary Artifact Families

Analysis includes:

- Apple Messages `chat.db`
- Apple Notes `NoteStore.sqlite`
- SQLite `-wal` and `-shm` files
- Messages attachments and relational records
- Notes/Core Data structures
- `Sync/sync.db` and CloudKit-related structures
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

For a short technical-review path through the project, see the [Portfolio Review Guide](docs/portfolio-guide.md).

## Evidence Protection

Original evidentiary databases, private communications, credentials, account identifiers, device identifiers, phone numbers, email addresses, identifying local paths, and other personally identifying information are not published.

Examples in this repository must be synthetic, sanitized, aggregate, or structurally representative.

## Methodological Caution

The presence of a record or recovered file does not automatically establish authorship, ownership, user interaction, original path, or intent. Conclusions are limited to what the available artifacts and provenance support.

Likewise, SQLite schemas and timestamp representations can change between application and operating-system versions. Queries are documented with their assumptions rather than presented as universally valid across every iOS release.

## Repository Status

The repository contains a reviewable methodology foundation, conservative analysis utilities, schema-discovery queries, and initial case studies. Additional record-level correlation examples will be added only when they can be published without exposing private source evidence and when the underlying relationship is independently supported.

Start with the [Portfolio Review Guide](docs/portfolio-guide.md), then see [Forensic Methodology](docs/methodology.md), [Evidence Handling](docs/evidence-handling.md), and [Limitations](docs/limitations.md).
