-- Deleted-record correlation and artifact recovery.
-- Historical working title retained because forensic scripts are allowed one personality trait.

SELECT *
FROM deleted_messages
LIMIT 20;

SELECT *
FROM unsynced_removed_recoverable_messages
LIMIT 20;

-- Determine whether GUIDs represented in deleted_messages still correlate
-- to records visible in the examined message table.
SELECT
    m.ROWID,
    m.guid,
    datetime(m.date / 1000000000 + 978307200, 'unixepoch') AS time_utc,
    m.text
FROM message m
WHERE m.guid IN (
    SELECT guid
    FROM deleted_messages
)
ORDER BY m.date DESC
LIMIT 50;
