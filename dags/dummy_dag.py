from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'example_dag_with_10_tasks',
    default_args=default_args,
    description='An Airflow DAG with more than 10 tasks',
    schedule_interval=None,  # This is a one-time run. You can adjust the schedule_interval
    catchup=False,
)

# Task 1: Start Task
start = DummyOperator(
    task_id='start',
    dag=dag,
)

# Task 2: Task A
task_a = DummyOperator(
    task_id='task_a',
    dag=dag,
)

# Task 3: Task B
task_b = DummyOperator(
    task_id='task_b',
    dag=dag,
)

# Task 4: Task C
task_c = DummyOperator(
    task_id='task_c',
    dag=dag,
)

# Task 5: Task D
task_d = DummyOperator(
    task_id='task_d',
    dag=dag,
)

# Task 6: Task E
task_e = DummyOperator(
    task_id='task_e',
    dag=dag,
)

# Task 7: Task F
task_f = DummyOperator(
    task_id='task_f',
    dag=dag,
)

# Task 8: Task G
task_g = DummyOperator(
    task_id='task_g',
    dag=dag,
)

# Task 9: Task H
task_h = DummyOperator(
    task_id='task_h',
    dag=dag,
)

# Task 10: Task I
task_i = DummyOperator(
    task_id='task_i',
    dag=dag,
)

# Task 11: Task J
task_j = DummyOperator(
    task_id='task_j',
    dag=dag,
)

# Task 12: Task K
task_k = DummyOperator(
    task_id='task_k',
    dag=dag,
)

# Task 13: End Task
end = DummyOperator(
    task_id='end',
    dag=dag,
)

# Set up task dependencies
start >> [task_a, task_b]  # Task A and Task B start after 'start'
task_a >> [task_c, task_d]  # Task C and Task D start after Task A
task_b >> [task_e, task_f]  # Task E and Task F start after Task B
task_c >> [task_g, task_h]  # Task G and Task H start after Task C
task_d >> [task_i, task_j]  # Task I and Task J start after Task D
task_e >> task_k  # Task K starts after Task E
task_f >> task_k  # Task K starts after Task F
task_g >> task_k  # Task K starts after Task G
task_h >> task_k  # Task K starts after Task H
task_i >> task_k  # Task K starts after Task I
task_j >> task_k  # Task K starts after Task J
task_k >> end  # End task after Task K completes
