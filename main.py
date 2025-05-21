import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import click
from cli.monitor import monitor
from cli.autopostinstall import autopostinstall
from cli.audit import audit
from cli.network.network import network


@click.group()
def cli():
    """🦊 SysFox — Многофункциональный инструмент для Linux админов"""
    pass


cli.add_command(monitor)
cli.add_command(autopostinstall)
cli.add_command(audit)
cli.add_command(network)

if __name__ == "__main__":
    cli()
