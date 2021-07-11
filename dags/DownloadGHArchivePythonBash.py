
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
    dag_id='download_ghactivity_python_bash',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
) as dag:

    # [START airflow_dag]
    python_loc = Variable.get('PYTHON_VENV_DIR')
    apps_dir = Variable.get('APPS_DIR')
    environ = Variable.get('ENVIRON')
    conf_file_name = Variable.get('CONF_FILE_NAME')
    run_this = BashOperator(
        task_id='download_file',
        bash_command=f'{python_loc}/python {apps_dir}/gharchive/app.py',
        env={'ENVIRON': '{{ environ }}', 'CONF_FILE_NAME': '{{ conf_file_name }}'},
    )
    # [END airflow_dag]

run_this

if __name__ == "__main__":
    dag.cli()
