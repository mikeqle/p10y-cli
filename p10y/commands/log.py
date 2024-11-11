import click
from p10y.helpers.loggers import task_logger

@click.command()
@click.argument('name', type=str)
def log(name):
    """
    Logs a task with 0 minutes to the tasklog.csv file.
    """
    task_logger(name, 0, "completed")
    click.echo(f"Logged task '{name}'.")
