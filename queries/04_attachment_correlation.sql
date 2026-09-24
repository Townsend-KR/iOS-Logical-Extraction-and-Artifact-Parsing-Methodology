-- Correlate Messages records with attachment metadata.

SELECT
    m.ROWID AS message_rowid,
    m.guid AS message_guid,
    m.is_from_me,
    a.ROWID AS attachment_rowid,
    a.filename,
    a.transfer_name,
    a.mime_type
FROM message m
JOIN message_attachment_join maj ON maj.message_id = m.ROWID
JOIN attachment a ON a.ROWID = maj.attachment_id
ORDER BY m.ROWID DESC
LIMIT 100;
