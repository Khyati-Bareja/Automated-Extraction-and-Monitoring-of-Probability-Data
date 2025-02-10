# Orchestrating the pipeline
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 9),
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}
dag = DAG(
    "kafka_airflow_pipeline",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False
)
def run_kafka_producer():
    subprocess.run(["python", "src/kafka-producer.py"])
