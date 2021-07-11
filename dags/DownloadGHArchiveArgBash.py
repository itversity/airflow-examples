
"""Example DAG demonstrating invoking script with Arguments using BashOperator."""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable


args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='download_ghactivity_arg_bash',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
) as dag:

    # [START airflow_dag]
    file_hour = Variable.get('gh_file_hour')
    scripts_dir = Variable.get('SCRIPTS_DIR')
    data_dir = Variable.get('DATA_DIR')
    download_file = BashOperator(
        task_id='download_file',
        bash_command=f'{scripts_dir}/download_gharchive_arg.sh {data_dir} {file_hour}',
    )
    # [END airflow_dag]

download_file

if __name__ == "__main__":
    dag.cli()
