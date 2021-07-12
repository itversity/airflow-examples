# Airflow Dags using SSH Operator

Let us go through running Airflow Dags using SSH Operator.
* Installing Airflow SSH Provider 
* Create SSH Connection using Airflow UI
* Sample Airflow Dag using SSH Provider
* Pass Environment Variables using SSH Provider

## Installing Airflow SSH Provider

Let us go ahead and install Airflow SSH Provider, so that we can establish SSH connections to the remote servers and run the jobs using SSH Connections.
* You can go to Airflow UI and confirm if SSH is available as one of the connection types.
* You can install Airflow SSH Provider using `pip`.

```shell
pip install apache-airflow-providers-ssh
```

* Make sure to restart Airflow Webserver and Scheduler to see SSH as one of the connection types.

## Create SSH Connection using Airflow UI

Let us go ahead and create SSH Connection using Airflow UI. 
* We need to have details of remote host, username and password to create the SSH Connection.
* Choose **SSH** as connection type and enter the information to create the connection.
* Make sure to give meaningful name. We will use this name as part of the Dag program to run commands on remote servers via SSH.

## Sample Airflow Dag using SSH Provider

Let us see how to develop, deploy and run a sample Airflow Dag using SSH Operator.
* Here is the code for the program. The name of the program is **RemoteHostnameSSH.py**.
```python

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
```
* Make sure to copy the program to `$AIRFLOW_HOME/dags` and run it from Web UI. If you could not find the Dag, restart Airflow Webserver and Scheduler.
* Check the logs to see the remote hostname as we are trying to run `hostname -f` command.

