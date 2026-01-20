WITH detections AS (
    SELECT
        ed.message_id,
        tm.channel_name,
        d.date_key,
        ed.detected_class,
        ed.confidence_score,
        ed.image_category
    FROM enrichment.image_detections ed
    JOIN raw.telegram_messages tm
      ON ed.message_id = tm.message_id
    JOIN analytics.dim_dates d
      ON DATE(tm.message_date) = d.full_date
)

SELECT *
FROM detections