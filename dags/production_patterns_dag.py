import os
import pandas as pd
from datetime import datetime, timedelta

from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator

DATA_DIR = os.path.abspath("./data/daily_transactions")
TARGET_DIR = os.path.abspath("./data/processed_transactions")
REQUIRED_COLUMNS = {"order_id", "date", "amount", "status"}

default_args = {
    'owner': 'data_engineering',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def validate_file_quality(**context):
    ds = context['ds']
    file_path = os.path.join(DATA_DIR, f"transactions_{ds}.csv")

    if not os.path.exists(file_path):
        return 'flag_invalid_file'

    try:
        df = pd.read_csv(file_path)
        if df.empty or (REQUIRED_COLUMNS - set(df.columns)):
            return 'flag_invalid_file'
        return 'process_daily_file'
    except Exception:
        return 'flag_invalid_file'

def process_and_write_partition(**context):
    ds = context['ds']
    file_path = os.path.join(DATA_DIR, f"transactions_{ds}.csv")
    partition_dir = os.path.join(TARGET_DIR, f"date={ds}")

    df = pd.read_csv(file_path)
    df['processed_at'] = datetime.now().isoformat()
    df['amount'] = df['amount'].astype(float)

    os.makedirs(partition_dir, exist_ok=True)
    target_file = os.path.join(partition_dir, "data.csv")
    df.to_csv(target_file, index=False)

def log_invalid_file_alert(**context):
    ds = context['ds']
    print(f"🚨 ALERT: Daily file for {ds} was empty or missing required columns.")

with DAG(
    dag_id='production_patterns_demo',
    default_args=default_args,
    description='Demonstrates Sensors, Branching, Idempotency, and Backfill',
    schedule='0 6 * * *',
    start_date=datetime(2026, 6, 1),
    catchup=False,
    tags=['production_patterns', 'task_10_3'],
) as dag:

    wait_for_daily_file = FileSensor(
        task_id='wait_for_daily_file',
        filepath=f"{DATA_DIR}/transactions_"+ "{{ ds }}.csv",
        poke_interval=5,
        timeout=30,
        mode='poke'
    )

    check_file_quality = BranchPythonOperator(
        task_id='check_file_quality',
        python_callable=validate_file_quality,
    )

    process_daily_file = PythonOperator(
        task_id='process_daily_file',
        python_callable=process_and_write_partition,
    )

    flag_invalid_file = PythonOperator(
        task_id='flag_invalid_file',
        python_callable=log_invalid_file_alert,
    )

    pipeline_completion = EmptyOperator(
        task_id='pipeline_completion',
        trigger_rule='none_failed_min_one_success'
    )

    wait_for_daily_file >> check_file_quality
    check_file_quality >> [process_daily_file, flag_invalid_file]
    process_daily_file >> pipeline_completion
    flag_invalid_file >> pipeline_completion
