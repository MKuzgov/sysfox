import requests
from rich import print
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

def mac_lookup(mac):
    print_logo()
    print_header("MAC Address Lookup")
    logger.info(f"[MAC] Получен запрос на MAC-адрес: {mac}")
    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url)
        if response.status_code == 200:
            vendor = response.text
            print(f"[bold green]Vendor:[/bold green] {vendor}")
            logger.info(f"[MAC] Производитель найден: {vendor}")
        else:
            print("[bold red]MAC address not found[/bold red]")
            logger.warning(f"[MAC] Производитель не найден для: {mac}")
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.error(f"[MAC] Ошибка запроса: {e}")
