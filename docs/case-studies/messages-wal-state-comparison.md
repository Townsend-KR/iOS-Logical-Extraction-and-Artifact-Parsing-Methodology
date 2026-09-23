# Messages WAL State Comparison

## Purpose

This case study documents a controlled comparison between two logical states of an authorized Apple Messages dataset:

1. the main `chat.db` database examined without applying the captured WAL; and
2. a reconstructed state in which committed transactions represented by the captured `chat.db-wal` were incorporated.

The purpose is not to treat WAL content as automatically equivalent to a deleted message or to infer user intent from database state. The comparison demonstrates why an examiner should preserve and evaluate SQLite sidecar files alongside the primary database.

## Evidence States

The export workflow retained the database states separately rather than collapsing them into a single result:

- **base_file_only** — examination of the main SQLite database without applying the captured WAL;
- **wal_applied** — a derived working state in which the captured committed WAL state was incorporated.

These are two representations of the same underlying evidence at different logical states. Rows appearing in both states are not separate messages and must not be double-counted.

## Observed Differences

The exported inventories documented the following changes after incorporation of the captured WAL:

| Artifact | Base-file state | WAL-applied state | Difference |
| --- | ---: | ---: | ---: |
| `message` | 53,072 | 53,073 | +1 |
| `attachment` | 3,552 | 3,553 | +1 |
| `chat_message_join` | 23,280 | 23,281 | +1 |
| `message_attachment_join` | 3,521 | 3,522 | +1 |
| Edited/retracted/associated export rows | 3,102 | 3,103 | +1 |

The result demonstrates that examination of the main database alone did not represent the complete committed logical state available in the captured SQLite stack.

These count differences do **not**, by themselves, establish that every added row represents an independent event. Relationships among the added message, attachment, join records, and lifecycle-related export must be established at record level before drawing that conclusion.

## Synchronization Artifact Context

Messages examination also included the associated synchronization database, `Sync/sync.db` (labeled `Sync__sync` in the examination export). This database was analyzed separately from `chat.db` and was used as an additional source during reconstruction.

The synchronization database contained CloudKit-related record types including:

- `MessageEncryptedV3`
- `attachment`
- `chatEncryptedv2`
- `messageUpdateV1`
- `recoverableMessage`

Its own base-file and WAL-applied states differed:

| Synchronization artifact | Base-file state | WAL-applied state | Difference |
| --- | ---: | ---: | ---: |
| `ZREMOTERECORD` | 225,698 | 225,703 | +5 |
| `MessageEncryptedV3` | 185,666 | 185,667 | +1 |
| `messageUpdateV1` | 1,138 | 1,142 | +4 |

The five additional synchronization records must not be assumed to map one-to-one to the additional `chat.db` message. Establishing such a relationship requires record-level correlation using supported identifiers, timestamps, record types, and other available relationships.

A separate root-level `sync.db` present in the export was empty in its base-file state and is not the synchronization database discussed above. Maintaining this distinction prevents similarly named artifacts from being conflated during reporting.

## Reconstruction Approach

The examination treated the local Messages database and synchronization artifacts as complementary evidence sources rather than interchangeable copies.

The reconstruction process was:

1. preserve the original database and available sidecars;
2. hash and inventory the preserved source material;
3. examine the main database state independently;
4. derive a separate WAL-applied working state;
5. export complete table inventories before applying keyword filters;
6. compare row counts and relevant structures between states;
7. retain lifecycle, tombstone, recovery, and raw-region material with provenance;
8. examine `Sync/sync.db` and its captured WAL as a separate synchronization evidence stack;
9. correlate records only where the underlying fields support the relationship; and
10. document limitations rather than treating ambiguous records as reconstructed facts.

## Interpretation

The comparison supports a narrow but important forensic conclusion:

> Applying the captured WAL changed the reconstructed logical state of the Messages database. The WAL-applied state contained one additional message row, one additional attachment row, one additional message-to-chat relationship, and one additional message-to-attachment relationship relative to the main database examined alone.

It does not establish, solely from aggregate counts, why those changes occurred, whether the additional records all concern the same message event, or whether synchronization-database changes correspond directly to those local-database changes.

That distinction is central to the methodology: **database recovery produces evidence for interpretation, not interpretation by itself.**

## Public-Portfolio Handling

No original message content, private communications, account identifiers, device identifiers, attachment contents, or original evidentiary databases are included in this repository.

Any future record-level examples published here will use sanitized or synthetic data while preserving enough structure to demonstrate the correlation methodology. Original evidence hashes and identifying local filesystem paths are also excluded from the public-facing case study unless disclosure is independently determined to be appropriate.

## Next Validation Step

The next stage for this case study is record-level comparison of the changed local Messages records with relevant synchronization records. That work should document the exact fields used for correlation and distinguish:

- direct identifier matches;
- timestamp-supported relationships;
- structural relationships;
- lifecycle/update evidence; and
- associations that remain uncertain.

No cross-database relationship should be represented as established until the underlying records support it.
