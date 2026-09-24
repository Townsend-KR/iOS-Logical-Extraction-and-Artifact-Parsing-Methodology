# Sanitized Messages Analysis Example

This example demonstrates the reasoning pattern used during examination without reproducing private source records.

## Scenario

A target identifier resolves to more than one row in the `handle` table. A direct query against one handle ID returns zero messages.

A zero-row result is not treated as proof that no communication exists.

## Resolution

1. Query all `handle` rows matching the normalized identifier.
2. LEFT JOIN each candidate `handle.rowid` to `message.handle_id`.
3. Compare message counts for each representation.
4. Query the handle IDs that actually participate in message relationships.
5. Interpret `is_from_me` as direction while retaining the associated participant separately.

## NULL Text Example

If `message.text` is NULL, examine `attributedBody`, attachment relationships, `item_type`, `associated_message_type`, and `associated_message_guid` before characterizing the record as empty.

## Deleted-Record Example

Where supported by the examined schema, inspect `deleted_messages` and `unsynced_removed_recoverable_messages`, then correlate GUIDs back to the primary message table or other available artifacts.

## Reporting

The public example intentionally contains no real identifiers, message content, attachment paths, evidentiary hashes, or private database material.
