# Unallocated-Space Messages SQLite Recovery

## Scope

This case study documents an authorized examination of a 64 GB secondary-storage device that contained allocated and unallocated data relevant to a broader historical Apple/iOS artifact examination.

The purpose of the public case study is to demonstrate recovery methodology, SQLite identification, and artifact correlation. The original source image, recovered database, private communications, personal identifiers, and evidentiary hash values are not published.

## Preservation and Source Layout

The source device was unmounted before imaging. Historical examination notes document creation of a raw forensic image with `dd`, verification of the resulting image, cryptographic hashing as part of the preservation workflow, and subsequent examination of the image rather than continued content analysis against the physical source.

A preserved `mmls` report records a DOS partition table with a primary NTFS/exFAT-type partition beginning at sector 32,768 and extending through sector 124,735,487, with unallocated sectors before and after the partition. At 512 bytes per sector, the reported geometry is consistent with a nominal 64 GB device.

The public repository records the structure and methodology without publishing the source image or its evidentiary digest.

## Recovery Workflow

Historical examination records document the following sequence:

```text
Physical secondary-storage source
        |
        v
Unmount source media
        |
        v
Create raw forensic image
        |
        v
Verify / hash image
        |
        v
Inspect filesystem and unallocated space
        |
        v
Carve recoverable files with PhotoRec
        |
        v
Identify SQLite artifacts
        |
        v
Examine schema and relational content
        |
        v
Correlate against other authorized historical artifacts
```

PhotoRec was used during recovery from the forensic image. Because carved filenames and extensions are not reliable provenance, SQLite material was evaluated by file structure and database schema rather than by filename alone.

## Messages Artifact Analysis

The recovered Messages-related database was examined directly with SQLite/SQL. Historical query output documents examination of the `message`, `handle`, `chat`, attachment-related, and deletion/recovery structures.

The analytical process included:

- establishing database scope and message-date ranges;
- resolving identifier representations through `handle` records and `message.handle_id`;
- checking duplicate handle representations rather than assuming a single identifier mapped to a single row;
- interpreting `is_from_me` as message direction while retaining the participant relationship supplied by the handle;
- testing NULL `message.text` records for content in `attributedBody`, attachments, and other message-item metadata;
- examining `deleted_messages` and `unsynced_removed_recoverable_messages`; and
- correlating GUIDs and relational records when evaluating deleted or recoverable material.

This progression matters because a zero-row query, a NULL text field, or a duplicate identifier is not by itself a forensic conclusion. Each result changes the next question.

## Timestamp Handling

Historical queries converted Apple message timestamps using the 2001 Apple epoch and nanosecond scaling used by the examined schema. Some exploratory output was presented as UTC while later targeted queries used SQLite's `localtime` modifier.

Those representations are intentionally distinguished. Presentation timezone is not treated as part of the stored timestamp value.

## Validation

The recovered database was not interpreted in isolation. Its records were compared with other authorized historical database copies and related artifacts available during the broader examination. Correlation relied on structural relationships such as identifiers, GUIDs, timestamps, attachments, and chronology rather than on filename similarity alone.

Cryptographic hashing was performed during the historical workflow. The actual digest is intentionally withheld from this public portfolio because publishing a persistent identifier for private evidence is unnecessary to demonstrate the method.

## Evidentiary Limits

Carving can establish that recoverable byte sequences consistent with a file existed in the examined source. Without supporting filesystem metadata, a carved artifact does not by itself establish its original filename, path, owner, acquisition mechanism, or whether a user opened it.

Likewise, successful SQLite parsing establishes that a structure can be interpreted. Authorship, intent, and user action require separate evidentiary support.

## Portfolio Boundary

This case study intentionally stops where public demonstration should stop. It documents the acquisition/recovery sequence, preservation practice, filesystem examination, carving method, database-analysis strategy, and validation logic while keeping the actual evidence private.

That boundary is part of the methodology, not a missing step.
