
"""Example DAG demonstrating invocation of Python script using BashOperator."""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='helloworld_python_bash',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
) as dag:

    scripts_dir = Variable.get('SCRIPTS_DIR')
    # [START airflow_dag]
    run_this = BashOperator(
        task_id='run_hello_world_python',
        bash_command=f'python {scripts_dir}/hello_world.py',
    )
    # [END airflow_dag]

run_this

if __name__ == "__main__":
    dag.cli()
