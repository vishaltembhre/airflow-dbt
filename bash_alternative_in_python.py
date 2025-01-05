import subprocess
import os
import time

def start_airflow_webserver():
    """
    Starts the Airflow webserver.
    """
    try:
        print("Starting Airflow Webserver...")
        webserver_process = subprocess.Popen(
            ["airflow", "webserver"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"Airflow Webserver started with PID: {webserver_process.pid}")
        return webserver_process
    except Exception as e:
        print(f"Error starting Airflow Webserver: {e}")
        return None

def start_airflow_scheduler():
    """
    Starts the Airflow scheduler.
    """
    try:
        print("Starting Airflow Scheduler...")
        scheduler_process = subprocess.Popen(
            ["airflow", "scheduler"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"Airflow Scheduler started with PID: {scheduler_process.pid}")
        return scheduler_process
    except Exception as e:
        print(f"Error starting Airflow Scheduler: {e}")
        return None

if __name__ == "__main__":
    # Ensure Airflow is initialized
    if not os.path.exists("airflow.db"):
        print("Initializing Airflow database...")
        subprocess.run(["airflow", "db", "init"])
    
    # Start Webserver
    webserver_process = start_airflow_webserver()
    
    # Give the webserver some time to initialize
    time.sleep(5)
    
    # Start Scheduler
    scheduler_process = start_airflow_scheduler()
    
    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down processes...")
        if webserver_process:
            webserver_process.terminate()
        if scheduler_process:
            scheduler_process.terminate()
        print("Processes terminated.")
