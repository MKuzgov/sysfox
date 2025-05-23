import click
from rich import print
from rich.panel import Panel
from rich.console import Console

# Импорты функций (всего 12)
from modules.network.scan import scan_ports
from modules.network.dns_lookup import dns_lookup
from modules.network.whois_lookup import whois_lookup
from modules.network.mac_lookup import mac_lookup
from modules.network.live_hosts import find_live_hosts
from modules.network.utils import traceroute_host
from modules.network.ping import ping_host
from modules.network.interface import list_interfaces
from modules.network.ipinfo import get_ip_info
from modules.network.report import save_report

console = Console()

@click.group()
def network():
    """[bold cyan]SysFox Network Toolkit[/bold cyan] - Сетевые функции"""
    fox_logo = """
     /\_/\
    ( o.o )
     > ^ <   [bold orange3]SysFox[/bold orange3] Network Toolkit
    """
    print(Panel.fit(fox_logo, title="[bold yellow]Welcome to SysFox[/bold yellow]"))


@network.command()
@click.option('--target', prompt='Введите IP/домен', help='Целевой хост')
@click.option('--ports', default='22,80,443', help='Порты через запятую (пример: 22,80,443)')
def scan(target, ports):
    """Сканирование портов"""
    result = scan_ports(target, ports)
    path = save_report("scan", result)
    console.print(result)
    console.print(f"[green]Отчет сохранен:[/green] {path}")


@network.command()
@click.option('--domain', prompt='Введите домен', help='Домен для DNS-запроса')
def dns(domain):
    """DNS-запись домена"""
    result = dns_lookup(domain)
    path = save_report("dns", result)
    console.print(result)
    console.print(f"[green]Отчет сохранен:[/green] {path}")


@network.command()
@click.option('--domain', prompt='Введите домен', help='WHOIS информация о домене')
def whois(domain):
    """WHOIS информация"""
    result = whois_lookup(domain)
    path = save_report("whois", result)
    console.print(result)
    console.print(f"[green]Отчет сохранен:[/green] {path}")


@network.command()
@click.option('--mac', prompt='Введите MAC адрес', help='MAC адрес для поиска')
def maclookup(mac):
    """Поиск производителя MAC-адреса"""
    result = mac_lookup(mac)
    path = save_report("maclookup", result)
    console.print(result)
    console.print(f"[green]Отчет сохранен:[/green] {path}")


@network.command()
@click.option('--subnet', prompt='Введите подсеть (например 192.168.1.0/24)', help='Подсеть для сканирования')
def live(subnet):
    """Поиск активных хостов"""
    result = find_live_hosts(subnet)
    path = save_report("livehosts", result)
    console.print(result)
    console.print(f"[green]Отчет сохранен:[/green] {path}")


@network.command()
@click.option('--target', prompt='Введите IP/домен для traceroute', help='Целевой хост')
def traceroute(target):
    """Traceroute до хоста"""
    result = traceroute_host(target)
    path = save_report("traceroute", result)
    console.print(result)
    console.print(f"[green]Отчет сохранен:[/green] {path}")


@network.command()
@click.option('--target', prompt='Введите IP/домен для ping', help='Целевой хост')
@click.option('--count', default=4, help='Количество запросов (по умолчанию 4)')
def ping(target, count):
    """Ping до целевого хоста"""
    result = ping_host(target, count)
    path = save_report("ping", result)
    console.print(result)
    console.print(f"[green]Отчет сохранен:[/green] {path}")


@network.command()
def interface():
    """Сетевые интерфейсы устройства"""
    result = list_interfaces()
    path = save_report("interface", result)
    console.print(result)
    console.print(f"[green]Отчет сохранен:[/green] {path}")


@network.command()
@click.option('--ip', prompt='Введите IP для информации', help='IP адрес для поиска геолокации и провайдера')
def ipinfo(ip):
    """Информация об IP: страна, провайдер и т.д."""
    result = get_ip_info(ip)
    path = save_report("ipinfo", result)
    console.print(result)
    console.print(f"[green]Отчет сохранен:[/green] {path}")
