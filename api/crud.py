from sqlalchemy.orm import Session
from sqlalchemy import text

def get_top_products(db: Session, limit: int = 10):
    query = text("""
        SELECT word AS term, COUNT(*) AS count
        FROM (
            SELECT unnest(string_to_array(lower(message_text), ' ')) AS word
            FROM analytics.fct_mmessages
        ) t
        WHERE length(word) > 3
        GROUP BY word
        ORDER BY count DESC
        LIMIT :limit
    """)
    # .mappings() converts rows into dict-like objects
    result = db.execute(query, {"limit": limit}).mappings().all()
    return result


def get_channel_activity(db: Session, channel_name: str):
    query = text("""
        SELECT channel_name, message_date::date, COUNT(*) AS message_count
        FROM analytics.fct_mmessages
        WHERE channel_name = :channel_name
        GROUP BY channel_name, message_date::date
        ORDER BY message_date::date
    """)
    return db.execute(query, {"channel_name": channel_name}).fetchall()


def search_messages(db: Session, query_str: str, limit: int):
    query = text("""
        SELECT message_id, channel_name, message_date, text
        FROM analytics.fct_mmessages
        WHERE text ILIKE :query
        ORDER BY message_date DESC
        LIMIT :limit
    """)
    return db.execute(
        query, {"query": f"%{query_str}%", "limit": limit}
    ).fetchall()


def get_visual_content_stats(db: Session):
    query = text("""
        SELECT channel_name, image_category, COUNT(*) AS image_count
        FROM analytics.fct_image_detections
        GROUP BY channel_name, image_category
        ORDER BY channel_name, image_count DESC
    """)
    return db.execute(query).fetchall()
