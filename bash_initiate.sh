#!/bin/bash
source airflowVenv/bin/activate

export AIRFLOW_HOME=~/Projects/airflow+DBT  # Change this path as needed

# Initialize Airflow database if not already initialized
if [ ! -d "$AIRFLOW_HOME" ]; then
  echo "Initializing Airflow project at $AIRFLOW_HOME..."
  mkdir -p "$AIRFLOW_HOME"
  airflow db init
else
  echo "Airflow project already exists at $AIRFLOW_HOME."
fi

# Start Airflow webserver
echo "Starting Airflow webserver on port 8080..."
airflow webserver -p 8080

# Path to the script to run in a new terminal
script="./bash_scheduler.sh"

# Execute the first script in a new terminal
echo "Starting Airflow scheduler in a new terminal..."
gnome-terminal -- bash -c "$script; exec bash"

echo "Both scripts have been launched in new terminals."
