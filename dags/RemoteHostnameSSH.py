
"""Example DAG demonstrating the usage of the SSHOperator."""

from datetime import timedelta

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.ssh.hooks.ssh import SSHHook
from airflow.utils.dates import days_ago


args = {
    'owner': 'airflow',
}

sshHook = SSHHook(ssh_conn_id='ITVersity Gateway')

with DAG(
    dag_id='hostname_ssh',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
) as dag:


    # [START airflow_dag]
    run_this = SSHOperator(
        task_id='get_host_name',
        command='hostname -f',
        ssh_hook=sshHook
    )
    # [END airflow_dag]

run_this

if __name__ == "__main__":
    dag.cli()
