import json
import os
import psycopg2
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

# Load environment variables
load_dotenv()

DATA_DIR = Path("../data/raw/telegram_messages")

# Read DB config from environment
DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST"),
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "port": os.getenv("POSTGRES_PORT"),
}

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

cur.execute("""
CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.telegram_messages (
    message_id BIGINT,
    channel_name TEXT,
    message_date TIMESTAMP,
    text TEXT,
    views INTEGER,
    forwards INTEGER,
    has_photo BOOLEAN,
    image_path TEXT,
    load_timestamp TIMESTAMP
);
""")
conn.commit()

for date_dir in DATA_DIR.iterdir():
    if not date_dir.is_dir():
        continue

    for file in date_dir.glob("*.json"):
        channel_name = file.stem

        with open(file, "r", encoding="utf-8") as f:
            messages = json.load(f)

        for msg in messages:
            cur.execute("""
                INSERT INTO raw.telegram_messages (
                    message_id,
                    channel_name,
                    message_date,
                    text,
                    views,
                    forwards,
                    has_photo,
                    image_path,
                    load_timestamp
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                msg.get("message_id"),
                channel_name,
                msg.get("date"),
                msg.get("text"),
                msg.get("views"),
                msg.get("forwards"),
                msg.get("media", {}).get("has_photo"),
                msg.get("media", {}).get("image_path"),
                datetime.utcnow()
            ))

conn.commit()
cur.close()
conn.close()

print("✅ Raw Telegram messages loaded successfully")
