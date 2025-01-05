from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator # type: ignore
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import sql_statements

# AWS_KEY = os.environ.get('AWS_KEY')
# AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
    'owner': 'udacity',
    'depends_on_past': False,
    'start_date': datetime(2019, 7, 26),    
    #'end_date': datetime(2018, 11, 12),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'catchup': False,
}

dag = DAG('Sparkify_Data_Pipeline_dag',
          default_args=default_args,
          description='Load and transform data in SQLite with Airflow',          
          schedule_interval='0 0 * * *'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

create_staging_events_table = SQLExecuteQueryOperator (
    task_id="create_staging_events_table",
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.CREATE_staging_events_TABLE_SQL
)

stage_events_to_sqlite = SQLExecuteQueryOperator (
    task_id="Stage_events_from_s3_to_sqlite",
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.STAGE_events_SQL
)

create_staging_songs_table = SQLExecuteQueryOperator (
    task_id="create_staging_songs_table",
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.CREATE_staging_songs_TABLE_SQL
)

stage_songs_to_sqlite = SQLExecuteQueryOperator (
    task_id="Stage_songs_from_s3_to_sqlite",
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.STAGE_songs_SQL
)

load_songplays_table = SQLExecuteQueryOperator (
    task_id='Load_songplays_fact_table',
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.LOAD_songplays_SQL
)

load_user_dimension_table = SQLExecuteQueryOperator (
    task_id='Load_user_dim_table',
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.user_table_insert
)

load_song_dimension_table = SQLExecuteQueryOperator (
    task_id='Load_song_dim_table',
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.song_table_insert
)

load_artist_dimension_table = SQLExecuteQueryOperator (
    task_id='Load_artist_dim_table',
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.artist_table_insert
)

load_time_dimension_table = SQLExecuteQueryOperator (
    task_id='Load_time_dim_table',
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.time_table_insert
)

run_quality_checks = SQLExecuteQueryOperator (
    task_id='Run_data_quality_checks',
    dag=dag,
    sqlite_conn_id="sqlite_default",
    sql=sql_statements.DATA_quality_check_SQL
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> create_staging_events_table
start_operator >> create_staging_songs_table

create_staging_events_table >> stage_events_to_sqlite
create_staging_songs_table >> stage_songs_to_sqlite

stage_events_to_sqlite >> load_songplays_table
stage_songs_to_sqlite >> load_songplays_table

load_songplays_table >> load_user_dimension_table
load_songplays_table >> load_song_dimension_table
load_songplays_table >> load_artist_dimension_table
load_songplays_table >> load_time_dimension_table

load_user_dimension_table >> run_quality_checks
load_song_dimension_table >> run_quality_checks
load_artist_dimension_table >> run_quality_checks
load_time_dimension_table >> run_quality_checks

run_quality_checks >> end_operator