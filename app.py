import click
from pythonping import ping
from tabulate import tabulate
from functions import Functions

func = Functions()

@click.group()
def cli():
    pass


cli.add_command(func.run_ping)
cli.add_command(func.view_status)

if __name__ == '__main__':
    cli()
