import csv
from datetime import datetime
import os

def task_logger(task_name, duration_minutes, status="completed"):
    """
    Logs task information to a CSV file.
    
    Args:
        task_name (str): Name of the task that was performed
        duration_minutes (int): Duration of the task in minutes
        status (str): Status of the task (completed/cancelled)
    """
    log_file = "tasklog.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create file with headers if it doesn't exist
    if not os.path.exists(log_file):
        with open(log_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Task', 'Duration (mins)', 'Status'])
    
    # Append the task log
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, task_name, duration_minutes, status])
