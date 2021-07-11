# Getting Started with Airflow Dags

As part of this topic we will get into the basics of Airflow Dags.
* Deploying first Airflow Dag using BashOperator
* Running first Airflow Dag using BashOperator
* Checking Airflow Dag Runs  
* Managing Airflow Dag using CLI
* Understanding Airflow Dag Object
* Develop Airflow Dag with Variables
* Configure Airflow Dag Variables using Web UI
* Deploy and run Airflow Dag with Variables
* Managing Airflow Dag Variables using CLI

## Deploying first Airflow Dag

Let us get into Airflow DAGS using **Hello World** as example.
* Right click on `airflow-examples/dags` folder.
* Click on **New** -> **Python File**.
* Give the name as **HelloWorldDAG**.
* Paste the below code in the script. Make sure to save it.

```python

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
```
* Now copy this script to `$AIRFLOW_HOME/dags` folder and see if the DAG is available in UI.
* You can also run `airflow dags list` to review whether DAG is visible or not.
* Make sure to run `airflow dags -h` to understand what other commands available to manage DAGs using command line.

## Running first Airflow Dag
As our Hello World DAG is deployed let us run and validate.
* Go to Airflow UI and unpause the DAG by using **Pause/Unpause DAG** toggle.
* You can also trigger the Dag manually.

## Checking Airflow Dag Runs 
Let us get into the details of Dag Runs using UI.
* You will see 2 DAG Runs as start_date is set to 2 days ago.
* You can click on **Runs** to list the runs.
* You can click on **Dag Id** or **Run Id** to get into more details. You can click on the specific task to get more details at task level.
* Clicking on **Log** will give all the details related to the specific task.

## Managing Airflow Dag using CLI
Here is how you can leverage command line to pause, unpause, run as well as get the details about the run.
```shell
airflow dags list # Lists all the Dags. Check for paused to see if a Dag is paused or unpaused.
airflow dags -h
airflow dags pause -h # Get the syntax for pause. It primarily takes dag_id as argument.
airflow dags pause helloworld_bash # Validate by using list or by going to Web UI
airflow dags list|grep helloworld_bash
airflow dags unpause -h # Get the syntax for unpause. It primarily takes dag_id as argument.
airflow dags unpause helloworld_bash # Validate by using list or by going to Web UI

airflow dags -h
airflow dags trigger -h
airflow dags trigger helloworld_bash

airflow dags list-runs -h
airflow dags list-runs -d helloworld_bash # Gives the details of all the runs. You can pick the run_id and deep dive further.
```

## Understanding Dag Object

Let us understand the Dag Object. It is part of `airflow` module.
* We can import it by saying `from airflow import DAG`.
* We can construct the object by using several key word arguments. Here is an example.

```python
DAG(
    dag_id='helloworld_bash',
    default_args={'owner': 'airflow'},
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
)
```

* Make sure `dag_id` is unique.
* We can pass the default arguments using `default_args`.
* `schedule_interval` follows cron style syntax. You can configure the frequency to as low as 1 minute.
* You can also specify when the job should be started as well as timeout.

## Develop Airflow Dag with Variables
Let us understand how to pass variables to Airflow Dags.
* The variables can be set via UI and can be accessed from Dags.
* The defined variables can be accessed using `airflow.models.Variable`
* `airflow.models.Variable` have methods such as `set`, `get` etc.

Here are the steps involved to deploy the Dag with Variables.
* Create a file by name **DownloadGHArchiveArgBash.py** with below code. Use **airflow-examples/dags** folder to place the script under development.
```python

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
    run_this = BashOperator(
        task_id='download_file',
        bash_command=f'{scripts_dir}/download_gharchive_arg.sh {data_dir} {file_hour}',
    )
    # [END airflow_dag]

run_this

if __name__ == "__main__":
    dag.cli()
```
* Create a shell script with below code under **airflow-examples/scripts** with name **download_gharchive_arg.sh**.
```shell
DATA_DIR=${1}
FILE_HOUR=${2}
echo "Downloading the file for ${FILE_HOUR}"
cd ${DATA_DIR} && curl -O https://data.gharchive.org/${FILE_HOUR}.json.gz
```
* When we invoke this script from Airflow Dag **DownloadGHArchiveArgBash.py**, we need to pass 2 arguments.

## Configure Airflow Dag Variables using Web UI

Before deploying, make sure to create following 3 Variables using Aiflow UI.
* `SCRIPTS_DIR` - Folder in which the shell scripts will be deployed.
* `DATA_DIR` - Folder in which the data shall be downloaded.
* `gh_file_hour` - The hour using which the file shall be downloaded.

## Deploy and run Airflow Dag with Variables

Let us deploy and run Airflow Dag with Variables.
* Copy the **DownloadGHArchiveArgBash.py** to $AIRFLOW_HOME/dags.
* Copy the script to the folder pointed by the variable `SCRIPTS_DIR`.
* Make sure the data folder pointed by the variable `DATA_DIR` is ready.
* Now go to Web UI and run the script.

## Managing Airflow Dag Variables using CLI

Let us understand how we can manage Airflow Dag variables using Airflow CLI. We will also run the Dag using CLI.
```shell
airflow variables -h
airflow variables set -h
airflow variables set gh_file_hour 2021-01-13-5
airflow dags trigger download_ghactivity_arg_bash
```

