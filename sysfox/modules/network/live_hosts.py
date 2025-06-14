import subprocess
from rich import print
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

def find_live_hosts(subnet):
    print_logo()
    print_header("Live Hosts Scan")
    logger.info(f"[LIVE] Сканирование подсети: {subnet}")
    print(f"Scanning subnet: {subnet}")
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"[bold green]Host alive:[/bold green] {ip}")
            logger.info(f"[LIVE] Найден активный хост: {ip}")
