# p10y/p10y/cli.py
import click
from p10y.commands.timer import timer
from p10y.commands.log import log

@click.group()
def cli():
    """p10y: A versatile CLI tool with multiple utilities."""
    pass

# Register commands
cli.add_command(timer)
cli.add_command(log)

if __name__ == "__main__":
    cli()