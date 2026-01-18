from src.scraper.paths import DATA_DIR

async def download_image(message, client, channel_name):
    if not message.photo:
        return None

    image_dir = DATA_DIR / "images" / channel_name
    image_dir.mkdir(parents=True, exist_ok=True)

    file_path = image_dir / f"{message.id}.jpg"

    await client.download_media(message.photo, file_path)

    return str(file_path)
