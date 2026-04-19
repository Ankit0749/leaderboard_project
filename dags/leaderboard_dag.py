from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def generate_data():
    os.system("python /mnt/c/Users/KIIT0001/Desktop/leaderboard_project/scripts/generate_data.py")

def ingest_data():
    os.system("python /mnt/c/Users/KIIT0001/Desktop/leaderboard_project/scripts/ingestion.py")

def process_data():
    os.system("python /mnt/c/Users/KIIT0001/Desktop/leaderboard_project/scripts/processing.py")

with DAG(
    dag_id='leaderboard_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule='*/2 * * * *',   # runs every 2 minutes,
    catchup=False
) as dag:

    t1 = PythonOperator(task_id='generate_data', python_callable=generate_data)
    t2 = PythonOperator(task_id='ingestion', python_callable=ingest_data)
    t3 = PythonOperator(task_id='processing', python_callable=process_data)

    t1 >> t2 >> t3