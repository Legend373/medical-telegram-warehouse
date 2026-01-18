import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

import asyncio
from src.scraper.telegram_client import get_client
from src.scraper.channel_scraper import scrape_channel
from src.scraper.logger import logger

CHANNELS = [
    # "https://t.me/lobelia4cosmetics",
    # "https://t.me/tikvahpharma",
    "https://t.me/CheMed123",
]

async def main():
    client = get_client()
    await client.start()

    for channel in CHANNELS:
        try:
            await scrape_channel(client, channel)
        except Exception as e:
            logger.error(f"Failed scraping {channel}: {e}")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
