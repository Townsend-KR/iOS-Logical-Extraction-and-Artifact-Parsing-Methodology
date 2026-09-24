-- Resolve identifier representations through handle.rowid -> message.handle_id.
-- Replace the placeholder with a sanitized target identifier.

SELECT rowid, id, service, country, uncanonicalized_id
FROM handle
WHERE id LIKE '%<TARGET_IDENTIFIER>%';

-- Determine which matching handle representation is actually related to messages.
SELECT
    h.rowid AS handle_rowid,
    h.id,
    h.service,
    COUNT(m.ROWID) AS message_count
FROM handle h
LEFT JOIN message m ON m.handle_id = h.rowid
WHERE h.id LIKE '%<TARGET_IDENTIFIER>%'
GROUP BY h.rowid, h.id, h.service
ORDER BY message_count DESC;

-- Direction belongs to the message record. The handle remains the associated participant.
SELECT
    m.ROWID,
    h.id AS associated_handle,
    CASE WHEN m.is_from_me = 1 THEN 'ME' ELSE 'THEM' END AS direction,
    m.text
FROM message m
LEFT JOIN handle h ON m.handle_id = h.rowid
WHERE h.id LIKE '%<TARGET_IDENTIFIER>%';
