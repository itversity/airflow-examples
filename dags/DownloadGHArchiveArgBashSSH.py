
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
    dag_id='download_ghactivity_arg_bash_ssh',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
) as dag:

    # [START airflow_dag]
    file_hour = Variable.get('gh_file_hour')
    scripts_dir = Variable.get('ITV_SCRIPTS_DIR')
    data_dir = Variable.get('ITV_DATA_DIR')
    download_file = SSHOperator(
        task_id='download_file',
        command=f'{scripts_dir}/download_gharchive_arg.sh {data_dir} {file_hour}',
        ssh_hook=sshHook
    )
    # [END airflow_dag]

download_file

if __name__ == "__main__":
    dag.cli()
