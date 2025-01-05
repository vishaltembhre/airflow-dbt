#!/bin/bash
source airflowVenv/bin/activate

# Kill Airflow webserver and scheduler processes in parallel
pkill -f "airflow webserver" &  # Run in the background
pkill -f "airflow scheduler" &  # Run in the background

echo "Stopping webserver and scheduler..."
wait  # Wait for both background processes to finish
echo "Both webserver and scheduler stopped."
