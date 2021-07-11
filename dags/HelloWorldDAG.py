
"""Example DAG demonstrating the usage of the BashOperator."""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='helloworld_bash',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
) as dag:


    # [START airflow_dag]
    run_this = BashOperator(
        task_id='say_hello_world',
        bash_command='echo "Hello World"',
    )
    # [END airflow_dag]

run_this

if __name__ == "__main__":
    dag.cli()
