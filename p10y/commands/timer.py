# p10y/p10y/commands/timer.py
import click
import time
import sys
import platform

@click.command()
@click.argument('minutes', type=int)
def timer(minutes):
    """
    Runs a timer for MINUTES minutes and beeps 3 times when finished.
    """
    total_seconds = minutes * 60
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
    except KeyboardInterrupt:
        click.echo("\nTimer cancelled.")
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
