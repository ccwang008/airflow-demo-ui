from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="demo_web_ui",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    BashOperator(
        task_id="hello",
        bash_command="echo Airflow Web UI Demo",
    )
