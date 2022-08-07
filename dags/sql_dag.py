from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG('sql_dag_test',
    start_date=datetime(2022, 8 ,1), 
    schedule_interval=timedelta(minutes=120),
    catchup=False) as dag:

        @task
        def extract():
            return 'my_Data'

        @task
        def process(data):
            print(data)

        clean_xcoms = PostgresOperator(
            task_id='clean_xcoms',
            postgres_conn_id='postgres heroku',
            sql='select * from xcom'
        )

        process(extract())