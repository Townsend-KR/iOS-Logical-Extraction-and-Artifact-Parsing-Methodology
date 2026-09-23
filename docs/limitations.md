# Limitations and Interpretation Boundaries

Forensic artifact analysis is constrained by what survived, how it was acquired or recovered, and what provenance remains available.

## Acquisition Limits

The datasets in this project came from multiple authorized sources. They should not be represented as though they were all produced by one logical extraction or one device acquisition.

## Historical Copies

A historical database copy represents the state captured by that copy. Its absence of a later record does not prove that the record never existed elsewhere or at another time.

## SQLite Recovery

WAL content, freelist pages, carved records, and other remnants require careful interpretation. Recoverability does not automatically establish when a record became inactive or why it is no longer represented in the active database.

## File Carving

Files recovered from unallocated space may lack original filesystem metadata. Unless independently established, carving alone does not prove original filename, original directory, ownership, who created or downloaded the file, whether a user opened it, or why it existed on the source media.

## Timestamps

Apple artifacts use multiple timestamp representations. A numeric value should not be converted until its epoch, units, and field semantics are supported by the artifact being examined.

## Attribution

Correlation can strengthen an interpretation, but temporal proximity or shared identifiers alone may not establish identity, authorship, intent, or device use. Findings should state the strength and limits of the available evidence.
