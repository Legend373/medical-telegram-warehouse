with source as (

    select
        message_id,
        channel_name,
        cast(message_date as timestamp) as message_timestamp,
        text as message_text,
        cast(views as integer) as view_count,
        cast(forwards as integer) as forward_count,
        has_photo as has_image,
        load_timestamp
    from raw.telegram_messages
    where message_id is not null
      and text is not null
      and text <> ''

),

deduplicated as (

    select *,
           row_number() over (
               partition by channel_name, message_id
               order by load_timestamp desc
           ) as rn
    from source

)

select
    message_id,
    channel_name,
    message_timestamp,
    message_text,
    length(message_text) as message_length,
    coalesce(view_count, 0) as view_count,
    coalesce(forward_count, 0) as forward_count,
    has_image
from deduplicated
where rn = 1
