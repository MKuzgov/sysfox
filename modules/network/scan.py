from core.logger import logger
import subprocess
import platform
import time

import sys
import os
import subprocess
from rich.console import Console
from core.logger import logger

console = Console()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


def scan_ports(target: str):
    console.rule("[bold green]Port Scanner")
    try:
        result = subprocess.check_output(["nmap", "-T4", "-F", target], text=True)
        console.print(f"[cyan]{result}[/cyan]")
        logger.info(f"Port scan completed for target: {target}")
    except Exception as e:
        console.print(f"[red]Ошибка:[/red] {e}")
        logger.error(f"Port scan failed for target {target}: {e}")


def show_interfaces():
    console.rule("[bold green]Интерфейсы")
    try:
        result = subprocess.check_output(["ip", "a"], text=True)
        console.print(f"[white]{result}[/white]")
        logger.info("Network interfaces displayed successfully")
    except Exception as e:
        console.print(f"[red]Ошибка интерфейсов:[/red] {e}")
        logger.error(f"Failed to show interfaces: {e}")


def show_routes():
    console.rule("[bold green]Маршруты")
    try:
        result = subprocess.check_output(["ip", "route"], text=True)
        console.print(f"[white]{result}[/white]")
        logger.info("Routing table displayed successfully")
    except Exception as e:
        console.print(f"[red]Ошибка маршрутов:[/red] {e}")
        logger.error(f"Failed to show routes: {e}")


def show_connections():
    console.rule("[bold green]Подключения")
    try:
        result = subprocess.check_output(["ss", "-tunap"], text=True)
        console.print(f"[white]{result}[/white]")
        logger.info("Active connections displayed successfully")
    except Exception as e:
        console.print(f"[red]Ошибка соединений:[/red] {e}")
        logger.error(f"Failed to show active connections: {e}")


def ping_host(host: str):
    console.rule(f"[bold green]Ping {host}")
    try:
        result = subprocess.check_output(["ping", "-c", "4", host], text=True)
        console.print(f"[cyan]{result}[/cyan]")
        logger.info(f"Ping to {host} successful")
    except Exception as e:
        console.print(f"[red]Ошибка ping:[/red] {e}")
        logger.error(f"Ping to {host} failed: {e}")


def net_scan(target="127.0.0.1"):
    """
    Выполняет базовое сканирование сети с логированием и выводом.
    Использует ping для проверки доступности.
    """

    logger.info(f"🔍 Начало сканирования IP-адреса: {target}")
    print(f"🔍 Сканирование {target}...\n")

    try:
        start_time = time.time()

        if platform.system().lower() == "linux":
            command = ["ping", "-c", "4", target]
        else:
            command = ["ping", target]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            logger.info(f"✅ Хост {target} доступен")
            print(result.stdout)
        else:
            logger.warning(f"⚠️ Хост {target} не отвечает")
            print(result.stderr)

        duration = time.time() - start_time
        logger.info(f"⏱️ Время выполнения: {duration:.2f} секунд")

    except Exception as e:
        logger.error(f"❌ Ошибка сканирования: {str(e)}")
