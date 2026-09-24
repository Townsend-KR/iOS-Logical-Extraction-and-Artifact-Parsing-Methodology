-- Database scope and timestamp-boundary checks.
-- Run against a working copy. Apple timestamp representation varies by schema/version.

SELECT COUNT(*) AS message_count
FROM message;

SELECT
    MIN(datetime(date / 1000000000 + 978307200, 'unixepoch')) AS earliest_utc,
    MAX(datetime(date / 1000000000 + 978307200, 'unixepoch')) AS latest_utc
FROM message;

SELECT
    ROWID,
    guid,
    datetime(date / 1000000000 + 978307200, 'unixepoch') AS time_utc,
    is_from_me,
    handle_id,
    text
FROM message
WHERE text IS NOT NULL
ORDER BY date DESC
LIMIT 50;
