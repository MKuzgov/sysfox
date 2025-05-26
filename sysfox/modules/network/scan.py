import socket
from rich import print
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

def port_scan(host, ports):
    print_logo()
    print_header("Port Scan")
    print(f"[bold]Scanning host:[/bold] {host}")
    logger.info(f"[SCAN] Сканирование порта для {host}, порты: {ports}")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[bold green]Port {port} is open[/bold green]")
                logger.info(f"[SCAN] Port {port} открыт")
            else:
                print(f"[grey]Port {port} is closed[/grey]")
