export AIRFLOW_HOME=`pwd`/airflow

cat airflow/*.pid|xargs kill
rm airflow/*.pid

sleep 5s
airflow webserver -D --stdout airflow/airflow-webserver.log
airflow scheduler -D --stdout airflow/airflow-scheduler.log

