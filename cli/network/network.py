import click
from modules.network.scan import net_scan
from modules.network.ping import ping_host
from modules.network.interface import show_interfaces
from modules.network.traceroute import trace_route
from modules.network.dns_lookup import dns_lookup
from modules.network.whois_lookup import whois_lookup
from modules.network.mac_lookup import mac_lookup
from modules.network.live_hosts import scan_live_hosts

from modules.network.traceroute import traceroute
from modules.network.dns_lookup import dns_lookup
from modules.network.whois_lookup import whois_lookup
from modules.network.mac_lookup import mac_lookup
from modules.network.live_hosts import live_hosts

from modules.network.ping import ping_host
from modules.network.interface import list_interfaces



from modules.network.report import generate_report

import click
import subprocess
import json
from rich import print
from rich.table import Table
from rich.console import Console



@click.group()
def network():
    """🧠 Сетевые инструменты SysFox"""
    pass


@network.command()
@click.option("--target", "-t", prompt="Введите IP/хост", help="Целевой IP или хост")
def scan(target):
    """🔍 Сканирование хоста"""
    net_scan(target)


@network.command()
def interface():
    """🖧 Показать сетевые интерфейсы"""
    show_interfaces()


@network.command()
@click.option("--target", "-t", prompt="Введите IP/хост", help="Целевой хост")
def ping(target):
    """📡 Проверка доступности хоста"""
    ping_host(target)


@network.command()
@click.option("--target", "-t", prompt="Введите IP/хост", help="Целевой хост")
def traceroute(target):
    """📍 Маршрут до хоста"""
    trace_route(target)


@network.command()
@click.argument("domain")
def dns(domain):
    """🌐 DNS-запрос"""
    dns_lookup(domain)


@network.command()
@click.argument("domain")
def whois(domain):
    """🔍 WHOIS-информация о домене"""
    whois_lookup(domain)


@network.command()
@click.argument("mac")
def mac(mac):
    """🔧 Производитель MAC-адреса"""
    mac_lookup(mac)


@network.command()
@click.argument("subnet")
def live(subnet):
    """🌐 Поиск активных хостов в подсети"""
    scan_live_hosts(subnet)


@network.command()
@click.option('--target', prompt='Введите IP/домен для ping', help='Целевой хост')
@click.option('--count', default=4, help='Количество запросов (по умолчанию 4)')
def ping(target, count):
    """Ping до целевого хоста"""
    ping_host(target, count)

@network.command()
def interface():
    """Показать информацию о сетевых интерфейсах"""
    show_interfaces()

