#!/bin/bash
source airflowVenv/bin/activate

# Set Airflow Home directory
export AIRFLOW_HOME=~/Projects/airflow+DBT  # Change this path as needed

# Start Airflow scheduler
echo "Starting Airflow scheduler..."
airflow scheduler
