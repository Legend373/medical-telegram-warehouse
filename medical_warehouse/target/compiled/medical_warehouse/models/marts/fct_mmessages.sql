select
    m.message_id,
    c.channel_key,
    d.date_key,
    m.message_text,
    m.message_length,
    m.view_count,
    m.forward_count,
    m.has_image
from "medical_dw"."analytics"."stg_telegram_messages" m
join "medical_dw"."analytics"."dim_channels" c
  on m.channel_name = c.channel_name
join "medical_dw"."analytics"."dim_dates" d
  on date(m.message_timestamp) = d.full_date