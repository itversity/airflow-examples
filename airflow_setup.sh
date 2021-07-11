export AIRFLOW_HOME=`pwd`/airflow


airflow db init
airflow users create \
  --username admin \
  --firstname Student \
  --lastname ITVersity \
  --role Admin \
  --email support@itversity.com

# You can update load_examples to False so that examples are not loaded.

airflow webserver -D --stdout airflow/airflow-webserver.log
airflow scheduler -D --stdout airflow/airflow-scheduler.log

