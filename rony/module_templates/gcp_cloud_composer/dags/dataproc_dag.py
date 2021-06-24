import os
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocSubmitJobOperator,
    DataprocDeleteClusterOperator
)
from airflow.utils.trigger_rule import TriggerRule

PROJECT_ID = ""
CLUSTER_NAME = ""
REGION = ""
DATALAKE = ""

DEFAULT_ARGS = {
    'owner': 'Rony',
    "depends_on_past": False,
    "start_date": datetime(2021, 6, 21),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0
}

CLUSTER_CONFIG = {
    "master_config": {
        "num_instances": 1,
        "machine_type_uri": "n1-standard-2",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 1024},
    },
    "worker_config": {
        "num_instances": 2,
        "machine_type_uri": "n1-standard-2",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 1024},
    },
}

PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": "gs://"}
}

dag = DAG(
    dag_id="dataproc_dag",
    default_args=DEFAULT_ARGS,
    catchup=False
)

dataproc_create_cluster = DataprocCreateClusterOperator(
    task_id="dataproc_create_cluster",
    project_id=PROJECT_ID,
    cluster_name=CLUSTER_NAME,
    region=REGION,
    cluster_config=CLUSTER_CONFIG,
    dag=dag
)

dataproc_submit_job = DataprocSubmitJobOperator(
    task_id="dataproc_submit_job",
    project_id=PROJECT_ID,
    location=REGION,
    job=PYSPARK_JOB,
    dag=dag
)

dataproc_delete_cluster = DataprocDeleteClusterOperator(
    task_id="dataproc_delete_cluster",
    project_id=PROJECT_ID,
    cluster_name=CLUSTER_NAME,
    region=REGION,
    trigger_rule=TriggerRule.ALL_DONE,
    dag=dag
)

dataproc_create_cluster >> dataproc_submit_job >> dataproc_delete_cluster
