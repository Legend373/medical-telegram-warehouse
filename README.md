# Medical Telegram Analytics Pipeline

## Overview
This project provides an end-to-end analytics pipeline for Telegram channels in the Ethiopian medical domain. It automates data collection, storage, transformation, image analysis, and exposes insights via a RESTful API. The pipeline is fully orchestrated using **Dagster**, making it robust, observable, and schedulable for production use.

## Features
- **Telegram Data Scraping**: Collect messages and media from target channels.
- **Data Warehouse Integration**: Store raw and transformed data in PostgreSQL.
- **DBT Transformations**: Convert raw messages into analytics-ready fact and dimension tables.
- **YOLO Image Enrichment**: Detect objects in images and classify them (promotional, product display, lifestyle, other).
- **Analytical API**: FastAPI endpoints for querying messages, channel activity, top products, and visual content statistics.
- **Pipeline Orchestration**: Dagster manages execution, scheduling, and observability.

## Architecture
1. **Data Collection** (`src/scraper/channel_scraper.py`)  
2. **Load to PostgreSQL** (`scripts/load_telegram_data.py`)  
3. **DBT Transformations** (`medical_warehouse/`)  
4. **Image Enrichment** (`scripts/run_yolo_detect.py`)  
5. **Analytical API** (`api/`)  
6. **Pipeline Orchestration** (`pipeline/`) using Dagster  

## Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL
- Dagster: `pip install dagster dagster-webserver`
- DBT (if running transformations): `pip install dbt-core dbt-postgres`
- YOLOv8 dependencies: `pip install ultralytics`

### Setup
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd medical-telegram-warehouse
2. Install Python dependencies:

```pip install -r requirements.txt```

3. Configure database in .env:

```DATABASE_URL=postgresql://<user>:<password>@localhost:5432/medical_dw ```

4. Run Pipeline
```dagster dev -f pipeline/pipeline.py```


5. Access Dagster UI at http://localhost:3000

Run the pipeline manually or monitor scheduled executions.

6. API Access

Start FastAPI server:

```uvicorn api.main:app --reload```


Interactive docs: http://localhost:8000/docs

Key endpoints:

/api/reports/top-products

/api/channels/{channel_name}/activity

/api/search/messages

/api/reports/visual-content


7. Outcomes

Fully automated, observable, and schedulable analytics pipeline.

Enriched data warehouse with textual and visual content metrics.

Accessible RESTful API for real-time insights on Telegram activity.
