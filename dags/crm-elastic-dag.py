from plugins.includes.helper import print_hello

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'Fernando Pérez',
    'start_date': days_ago(1)
}

dag = DAG(
    dag_id='crm-elastic-dag',
    default_args=args,
    schedule_interval='@daily'
)

with dag:
    hello_world = PythonOperator(
        task_id='hello',
        python_callable=print_hello
    )