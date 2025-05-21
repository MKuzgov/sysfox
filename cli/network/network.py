from modules.network.traceroute import traceroute
from modules.network.dns_lookup import dns_lookup
from modules.network.whois_lookup import whois_lookup
from modules.network.mac_lookup import mac_lookup
from modules.network.live_hosts import live_hosts

import click
import subprocess
import json
from rich import print
from rich.table import Table
from rich.console import Console
from modules.network.scan import net_scan

console = Console()


@click.group()
def network():
    """🕸️ Сетевой модуль: сканирование, маршруты, соединения"""
    pass


@network.command()
@click.option("--target", prompt="Введите IP/хост", help="Цель для сканирования")
def scan(target):
    """Сканирование сети"""
    console.rule("[bold green]Сканирование сети")
    net_scan(target)


@network.command()
@click.argument("host")
def trace(host):
    """Маршрут до хоста"""
    console.rule(f"[bold green]Traceroute до {host}")
    print(traceroute(host))


@network.command()
@click.argument("domain")
def dns(domain):
    """DNS-записи домена"""
    console.rule(f"[bold green]DNS-записи для {domain}")
    print(dns_lookup(domain))


@network.command()
@click.argument("domain")
def whois(domain):
    """Информация о домене"""
    console.rule(f"[bold green]WHOIS {domain}")
    print(whois_lookup(domain))


@network.command()
@click.argument("mac")
def mac(mac):
    """Производитель устройства по MAC"""
    console.rule(f"[bold green]Производитель MAC {mac}")
    print(mac_lookup(mac))


@network.command()
@click.argument("subnet")
def sweep(subnet):
    """Поиск активных хостов"""
    console.rule(f"[bold green]Сканирование хостов в {subnet}")
    print(live_hosts(subnet))
