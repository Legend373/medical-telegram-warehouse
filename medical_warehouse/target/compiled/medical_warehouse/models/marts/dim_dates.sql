select distinct
    to_char(message_timestamp, 'YYYYMMDD')::int as date_key,
    date(message_timestamp) as full_date,
    extract(dow from message_timestamp) as day_of_week,
    to_char(message_timestamp, 'Day') as day_name,
    extract(week from message_timestamp) as week_of_year,
    extract(month from message_timestamp) as month,
    to_char(message_timestamp, 'Month') as month_name,
    extract(quarter from message_timestamp) as quarter,
    extract(year from message_timestamp) as year,
    case when extract(dow from message_timestamp) in (0,6) then true else false end as is_weekend
from "medical_dw"."analytics"."stg_telegram_messages"