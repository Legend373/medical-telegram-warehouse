select *
from "medical_dw"."analytics"."stg_telegram_messages"
where message_timestamp > now()