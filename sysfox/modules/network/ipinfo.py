import socket
from rich import print
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

def get_ip_info(domain):
    print_logo()
    print_header("IP Info")
    logger.info(f"[IPINFO] Получен запрос IP информации для домена: {domain}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"[bold]Domain:[/bold] {domain}")
        print(f"[bold]IP Address:[/bold] {ip}")
        logger.info(f"[IPINFO] {domain} -> {ip}")
    except socket.gaierror as e:
        print(f"[bold red]Unable to resolve domain: {domain}[/bold red]")
        logger.error(f"[IPINFO] Ошибка разрешения: {e}")
