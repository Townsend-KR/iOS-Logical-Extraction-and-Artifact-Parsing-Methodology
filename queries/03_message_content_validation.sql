-- A NULL message.text value does not establish absence of meaningful content.

SELECT
    ROWID,
    guid,
    text,
    length(attributedBody) AS attributed_body_bytes,
    item_type,
    associated_message_type,
    associated_message_guid
FROM message
WHERE text IS NULL
LIMIT 100;

-- Check attachment relationships for messages whose text field is NULL.
SELECT
    m.ROWID AS message_rowid,
    m.guid,
    a.ROWID AS attachment_rowid,
    a.filename,
    a.transfer_name,
    a.mime_type
FROM message m
JOIN message_attachment_join maj ON maj.message_id = m.ROWID
JOIN attachment a ON a.ROWID = maj.attachment_id
WHERE m.text IS NULL
LIMIT 100;
