-- Schema discovery for an Apple Messages database.
-- Run against a working copy/read-only connection.
-- This file intentionally avoids assuming a particular iOS schema version.

SELECT type, name, tbl_name, sql
FROM sqlite_master
WHERE type IN ('table', 'index', 'trigger', 'view')
ORDER BY type, name;

-- Inspect candidate tables only after confirming they exist:
-- PRAGMA table_info(message);
-- PRAGMA table_info(handle);
-- PRAGMA table_info(chat);
-- PRAGMA table_info(attachment);
--
-- Join queries belong in version-specific files after the schema has been
-- validated. Do not assume historical chat.db copies share identical columns.
