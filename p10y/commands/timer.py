# p10y/p10y/commands/timer.py
import click
import time
import sys
import platform
from p10y.helpers.loggers import task_logger

@click.command()
@click.argument('minutes', type=int)
@click.option('-n', '--name', type=str, default="null", help="Name of the task being timed")
def timer(minutes, name):
    """
    Runs a timer for MINUTES minutes and beeps 3 times when finished.
    """
    total_seconds = minutes * 60
    start_time = time.time()
    click.echo(f"Timer started for {minutes} minute(s).")
    try:
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            click.echo(f"\rTime Remaining: {time_format}", nl=False)
            time.sleep(1)
        click.echo("\nTime's up!")
        beep_times = 3
        for _ in range(beep_times):
            beep()
            # time.sleep(0.5)  # Short pause between beeps
        task_logger(name, minutes, "completed")
    except KeyboardInterrupt:
        elapsed_seconds = int(time.time() - start_time)
        elapsed_minutes = elapsed_seconds // 60  # Round down to nearest minute
        click.echo("\nTimer interrupted.")
        task_logger(name, elapsed_minutes, "completed")
        sys.exit(0)

def beep():
    """
    Produces a beep sound. Uses system-specific commands.
    """
    system = platform.system()
    if system == "Darwin":  # macOS
        import subprocess
        subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
    elif system == "Windows":
        import winsound
        frequency = 1000  # Set Frequency To 1000 Hertz
        duration = 500    # Set Duration To 500 ms
        winsound.Beep(frequency, duration)
    else:
        # For Linux or other OS, print the ASCII bell character
        print('\a', end='', flush=True)
