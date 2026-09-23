-- Schema discovery for Apple Notes / NoteStore.sqlite.
-- NoteStore is Core Data-backed and schemas vary across software generations.

SELECT type, name, tbl_name, sql
FROM sqlite_master
WHERE type IN ('table', 'index', 'trigger', 'view')
ORDER BY type, name;

-- Follow with targeted PRAGMA table_info(<confirmed_table>) statements.
-- Relationships and encoded content should be interpreted only after the
-- schema/version under examination has been documented.
