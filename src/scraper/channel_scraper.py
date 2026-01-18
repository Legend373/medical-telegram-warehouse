import json
from datetime import datetime
from src.scraper.media_downloader import download_image
from src.scraper.logger import logger
from src.scraper.paths import DATA_DIR

async def scrape_channel(client, channel_url):
    channel_name = channel_url.split("/")[-1]
    today = datetime.utcnow().strftime("%Y-%m-%d")

    output_dir = DATA_DIR / "telegram_messages" / today
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{channel_name}.json"
    messages_data = []

    logger.info(f"Scraping channel: {channel_name}")

    async for message in client.iter_messages(channel_url):
        try:
            image_path = await download_image(message, client, channel_name)

            messages_data.append({
                "message_id": message.id,
                "date": message.date.isoformat() if message.date else None,
                "text": message.text,
                "views": message.views,
                "forwards": message.forwards,
                "media": {
                    "has_photo": bool(message.photo),
                    "image_path": image_path,
                },
            })

        except Exception as e:
            logger.error(f"{channel_name} | msg {message.id}: {e}")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(messages_data, f, ensure_ascii=False, indent=2)

    logger.info(f"Saved {len(messages_data)} messages → {output_file}")
