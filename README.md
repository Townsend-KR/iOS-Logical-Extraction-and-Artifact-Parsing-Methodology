# iOS Logical Extraction and Artifact Parsing Methodology

A digital-forensics portfolio project documenting the preservation, recovery, examination, parsing, and correlation of authorized Apple/iOS artifacts spanning approximately 2017 to the present.

**Focus:** SQLite • WAL/SHM • Apple Messages • synchronization/CloudKit artifacts • secondary-storage recovery • artifact correlation • hashing • reproducible Python/SQL workflows

> This repository publishes methodology and sanitized or synthetic examples. Original private evidence, communications, identifiers, forensic images, recovered databases, and evidentiary hashes are intentionally excluded.

## Project Scope

The examination drew from multiple authorized sources, including iOS backup-derived logical data, recovered SQLite databases, historical database copies, SQLite WAL/SHM companions, synchronization-related artifacts, attachments, filesystem artifacts, and files recovered from secondary storage.

Not every artifact was produced by a logical extraction. Acquisition and recovery are documented separately from subsequent parsing and analysis so that provenance is not blurred simply because two artifacts can be queried with the same tools.

The work was performed without relying on interactive access to the originating devices, device passcodes, or application interfaces. No commercial mobile-forensics suite was used for the artifact analysis documented here. Examination instead relied on direct inspection of underlying data with SQLite/SQL, filesystem analysis, cryptographic hashing, command-line/open-source tools, and purpose-built scripts.

## Featured Case Studies

### Messages WAL State Comparison

A controlled comparison of `chat.db` before and after incorporation of the captured WAL documented a change from **53,072 to 53,073 message rows**, together with corresponding changes in attachment and relationship tables.

[Read the case study](docs/case-studies/messages-wal-state-comparison.md)

### Synchronization-Assisted Messages Reconstruction

The associated `Sync/sync.db` synchronization database was examined as a separate evidence source. Its WAL-applied state contained five additional `ZREMOTERECORD` entries relative to the base-file state. Those records are not assumed to map directly to local Messages changes without record-level validation.

[Read the case study](docs/case-studies/synchronization-assisted-messages-reconstruction.md)

### Unallocated-Space Messages Database Recovery

A separate 64 GB secondary-storage source was preserved as a forensic image and examined for allocated and unallocated data. Historical examination records document hashing, filesystem-layout review, file carving with PhotoRec, and subsequent SQLite analysis. A Messages-related SQLite database recovered during that work was examined by schema and relational content rather than by filename alone.

The public case study documents the recovery and analytical method while deliberately withholding the private database, communications, identifiers, source image, and evidentiary hash values.

[Read the case study](docs/case-studies/unallocated-space-sqlite-recovery.md)

## Analytical Questions Demonstrated

The project goes beyond simply opening `chat.db`. The documented SQL workflow addresses several recurring forensic problems:

- **Identity resolution:** correlating service/identifier representations through `handle.rowid` and `message.handle_id`.
- **Directionality:** interpreting `is_from_me` in conjunction with participant relationships rather than treating a handle as the sender by default.
- **Content representation:** testing `text`, `attributedBody`, attachments, and message-item metadata before concluding that a NULL text field represents an empty message.
- **Deletion and recovery:** examining `deleted_messages`, `unsynced_removed_recoverable_messages`, GUID relationships, and recovered database material.
- **Timestamp interpretation:** distinguishing stored Apple timestamp values from normalized UTC or local-time presentation.

## Forensic Workflow

```text
Acquisition / Recovery
        |
        v
Preservation & Hashing
        |
        v
Filesystem / Artifact Inventory
        |
        v
Validation & Schema Discovery
        |
        v
Parsing & Timestamp Normalization
        |
        v
Relational & Cross-Artifact Correlation
        |
        v
Reconstruction & Validation
        |
        v
Sanitized Reporting
```

The workflow is evidence-first. Original artifacts are preserved, analysis is performed against working copies where practical, and directly observed facts are distinguished from analytical inference.

## Repository Layout

| Path | Purpose |
| --- | --- |
| `docs/` | Scope, evidence handling, methodology, limitations, and case studies |
| `scripts/` | Conservative utilities for hashing, inventory, SQLite metadata, and timestamp handling |
| `queries/` | Schema discovery and sanitized analytical SQL |
| `samples/` | Synthetic or sanitized demonstration material only |
| `research/` | Technical references and schema/version research |

For a short technical-review path, start with the [Portfolio Review Guide](docs/portfolio-guide.md).

## Evidence Protection

This is a portfolio, not an evidence dump. Original databases, forensic images, private communications, attachments, credentials, account/device identifiers, phone numbers, email addresses, identifying local paths, and evidentiary hash values are not published.

Where historical examination records establish that hashing was performed, the methodology records that fact without exposing a persistent identifier for the private source artifact.

## Methodological Caution

The presence of a record or recovered file does not automatically establish authorship, ownership, user interaction, original path, or intent. A successful parse is not itself a forensic conclusion.

SQLite schemas and timestamp representations also change across Apple software generations. Queries are therefore documented with their assumptions rather than presented as universally valid across every iOS release.

## Repository Status

This repository is a sanitized professional representation of completed and ongoing authorized forensic work. It contains repeatable methodology, conservative analysis utilities, schema-discovery queries, and case studies derived from actual examination workflows while maintaining a strict boundary around private evidence.

Start with [Forensic Methodology](docs/methodology.md), [Evidence Handling](docs/evidence-handling.md), [Limitations](docs/limitations.md), and the [Portfolio Review Guide](docs/portfolio-guide.md).
