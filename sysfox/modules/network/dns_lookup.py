import socket
from rich import print
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

def dns_lookup(domain):
    print_logo()
    print_header("DNS Lookup")
    logger.info(f"[DNS] Поиск IP для домена: {domain}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"[bold cyan]{domain}[/bold cyan] resolved to [bold green]{ip}[/bold green]")
        logger.info(f"[DNS] Результат: {domain} -> {ip}")
    except socket.gaierror as e:
        print(f"[bold red]Unable to resolve domain: {domain}[/bold red]")
        logger.error(f"[DNS] Ошибка: {e}")
