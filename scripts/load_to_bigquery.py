from google.cloud import bigquery

client = bigquery.Client.from_service_account_json(
    "credentials/airflow-key.json"
)

table_id = "banking-etl-project1.banking_dataset.customer_transactions"

job = client.load_table_from_file(
    open(
        "data/banking_data.csv",
        "rb"
    ),
    table_id,
    job_config=bigquery.LoadJobConfig(
        source_format=
        bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=
        "WRITE_TRUNCATE"
    )
)

job.result()

print("Loaded to BigQuery")