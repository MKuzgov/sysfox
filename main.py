import click
from cli.monitor import monitor
from cli.autopostinstall import autopostinstall
from cli.audit import audit


@click.group()
def cli():
    """🦊 SysFox — Многофункциональный инструмент для Linux админов"""
    pass


cli.add_command(monitor)
cli.add_command(autopostinstall)
cli.add_command(audit)

if __name__ == "__main__":
    cli()
