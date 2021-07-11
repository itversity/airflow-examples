# Airflow Examples

This will contain all the details about Airflow Examples related to our course.

## Setup Instructions
Here are the instructions you need to follow.
* Clone this repository.
* Create required folders.

```shell
cd airflow-examples
mkdir -p data bookmark
```

## Set up local Airflow
Here are the instructions to set up Airflow locally on Linux or Mac. For Windows, some of the commands might not work.
* Create virtual environment. Make sure to use Python 3.6 or later.
* Install Airflow.
* Refer to `airflow_setup.sh` and run the commands. Make sure to change `AIRFLOW_HOME` as per your environment.
* In my case, I have created airflow enviroment as part of sub-directory of airflow-examples.
```shell
python3 -m venv af-venv
pip install airflow
pip install -r requirements .txt
# Now refer to airflow_setup.sh and run the commands. 
# Make sure to change AIRFLOW_HOME to right value.
```
* Validate by going through the browser and by entering http://localhost:8080
* At any point, if you want to restart, you can run the commands from `airflow_restart.sh` script.

## Restarting local Airflow
Let us understand how to restart local airflow.
* We need to kill the sessions related to airflow webserver and scheduler.
* Start webserver and scheduler.

If we make any changes to the Airflow configuration, then we need to restart the Airflow server.
* Let us disable Airflow DAGs examples and restart.
* Go to `$AIRFLOW_HOME/airflow.cfg` and search for `load_examples`. If the value is `True` change it to `False`.
* Now refer to `airflow_restart.sh` and run the commands to restart both Airflow Webserver and Scheduler.

## Development Process

Here is the development process.
* We develop dags using `dags` folder under our project directory `airflow-examples`.
* Once the development is done, we need to copy to `airflow/dags` folder.
* Make sure the browser is started and validate if the DAG is visible with out any issues.

## DAG 1: Deploying Hello World

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

## DAG 1: Running Hello World
As our Hello World DAG is deployed let us run and validate.
* Go to Airflow UI and unpause the DAG by using **Pause/Unpause DAG** toggle.
* You will see 2 DAG Runs as start_date is set to 2 days ago.
* You can click on **Runs** to list the runs.
* You can click on **Dag Id** or **Run Id** to get into more details. You can click on the specific task to get more details at task level.
* Clicking on **Log** will give all the details related to the specific task.

## Managing Airflow DAG using CLI
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

## Understanding DAG Object

Let us understand the DAG Object. It is part of `airflow` module.
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
