from dagster import job
from pipeline_ops import scrape_telegram_data, load_raw_to_postgres, run_dbt_transformations, run_yolo_enrichment

@job
def telegram_pipeline():
    # Define the sequence of execution
    scrape = scrape_telegram_data()
    load = load_raw_to_postgres()
    dbt = run_dbt_transformations()
    yolo_op = run_yolo_enrichment()

    # Execution order: scrape → load → dbt → yolo
    load.after(scrape)
    dbt.after(load)
    yolo_op.after(dbt)
