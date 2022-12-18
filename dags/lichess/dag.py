import datetime
import requests
from functools import partial

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from dags.lichess.utils import get_games_for_user

default_args = {
    "owner": "me",
    "start_date": datetime.datetime(2022, 1, 1),
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=5),
}

dag = DAG(
    "get_request_dag",
    default_args=default_args,
    schedule_interval=datetime.timedelta(days=1),
)

MAGNUS_CARLSEN_USERNAME = "DrNykterstein"
get_games_for_magnus_carlsen = partial(get_games_for_user(MAGNUS_CARLSEN_USERNAME))

get_request_task = PythonOperator(
    task_id="send_get_request",
    python_callable=get_games_for_magnus_carlsen,
    dag=dag,
)

# Set the task to run once a day
get_request_task >> dag
