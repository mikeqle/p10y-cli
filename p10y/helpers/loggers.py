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
    log_file = f"/Users/{os.environ['USER']}/git-projects/2024/p10y/tasklog.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create file with headers if it doesn't exist
    if not os.path.exists(log_file):
        with open(log_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Timestamp', 'Task', 'Duration (mins)', 'Status'])
            next_id = 1
    else:
        # Read the last row to get the next ID
        with open(log_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            last_id = 0
            for row in reader:
                if row:  # Check if row is not empty
                    last_id = int(row[0])
            next_id = last_id + 1
    
    # Append the task log
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([next_id, timestamp, task_name, duration_minutes, status])
