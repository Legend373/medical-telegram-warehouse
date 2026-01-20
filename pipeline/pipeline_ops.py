from dagster import op
import scripts.run_scraper as scraper
import scripts.load_telegram_data as loader
import scripts.run_yolo_detect as yolo


@op
def scrape_telegram_data():
    """Scrape Telegram messages and save raw data."""
    scraper.main()  # Call the main function of the scraper
    return "Scraping completed"

@op
def load_raw_to_postgres():
    """Load raw JSON data into PostgreSQL."""
    loader.main()  # Call the main function of the loader
    return "Raw data loaded"

@op
def run_dbt_transformations():
    """Run dbt models to transform raw data into analytics-ready tables."""
    dbt_runner.run_dbt()  # Call a wrapper to run dbt models
    return "DBT transformations completed"

@op
def run_yolo_enrichment():
    """Run YOLO-based object detection on images."""
    yolo.main()  # Call YOLO detection script
    return "YOLO enrichment completed"
