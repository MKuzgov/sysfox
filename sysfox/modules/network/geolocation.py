import requests
from rich import print
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

def get_ip_info(ip):
    print_logo()
    print_header("IP Geolocation")
    logger.info(f"[GEO] Получена геолокация для: {ip}")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            for key in ['query', 'country', 'regionName', 'city', 'zip', 'lat', 'lon', 'org', 'isp']:
                print(f"[bold]{key.capitalize()}:[/bold] {data[key]}")
            logger.info(f"[GEO] Геолокация получена успешно для {ip}")
        else:
            print("[bold red]Failed to retrieve geolocation data[/bold red]")
            logger.warning(f"[GEO] Не удалось получить данные для {ip}")
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.error(f"[GEO] Ошибка: {e}")
