
"""Example DAG demonstrating invoking script with Arguments using BashOperator."""

from datetime import timedelta

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.ssh.hooks.ssh import SSHHook
from airflow.utils.dates import days_ago
from airflow.models import Variable


args = {
    'owner': 'airflow',
}

sshHook = SSHHook(ssh_conn_id='ITVersity Gateway')

with DAG(
    dag_id='download_ghactivity_python_bash_ssh',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
) as dag:

    # [START airflow_dag]
    python_loc = Variable.get('ITV_PYTHON_VENV_DIR')
    apps_dir = Variable.get('ITV_APPS_DIR')
    download_file = SSHOperator(
        task_id='download_file',
        command=f'{python_loc}/python {apps_dir}/gharchive/app.py lab /home/itversity/airflow-examples/apps/gharchive/conf.yml',
        ssh_hook=sshHook,
    )

    # [END airflow_dag]

download_file

if __name__ == "__main__":
    dag.cli()
