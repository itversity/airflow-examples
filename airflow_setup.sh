export AIRFLOW_HOME=`pwd`/airflow

cat airflow/airflow-webserver*.pid|xargs kill -9
rm airflow/airflow-webserver*.pid
cat airflow/airflow-scheduler*.pid|xargs kill -9
rm airflow/airflow-scheduler*.pid


airflow webserver -D --stdout airflow/airflow-webserver.log
airflow scheduler -D --stdout airflow/airflow-scheduler.log

airflow users create \
  --username admin \
  --firstname Student \
  --lastname ITVersity \
  --role Admin \
  --email support@itversity.com
