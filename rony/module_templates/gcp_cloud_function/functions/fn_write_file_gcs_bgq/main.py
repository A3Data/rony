import os
from google.cloud import bigquery

dataset_name = os.getenv("dataset_name")
table_name = os.getenv("table_name")


def fn_write_file_gcs_bgq(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
    Args:
        event (dict):  The dictionary with data specific to this type of event.
        context (google.cloud.functions.Context): Metadata of triggering event.
    """
    try:
        # Bigquery instance
        bigquery_client = bigquery.Client()

        if event["name"].split("/")[0] == "public_dataset":
            uri = f"gs://{event['bucket']}/{event['name']}"

            table_ref = bigquery_client.get_dataset(dataset_ref=dataset_name).table(table_id=table_name)
            table = bigquery_client.get_table(table=table_ref)

            job_config = bigquery.job.LoadJobConfig(
                schema=table.schema,
                source_format=bigquery.SourceFormat.CSV,
                field_delimiter=","
            )
            load_job = bigquery_client.load_table_from_uri(source_uris=uri, destination=table, job_config=job_config)
            load_job.result()

    except Exception as err:
        print(err)
