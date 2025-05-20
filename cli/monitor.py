import click
import psutil
import time
import json
import os
from rich.console import Console
from rich.table import Table


def get_stats():
    return {
        "uptime_h": round((time.time() - psutil.boot_time()) / 3600, 1),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": {
            "used_mb": psutil.virtual_memory().used // (1024**2),
            "total_mb": psutil.virtual_memory().total // (1024**2),
        },
        "disk": {
            "used_gb": psutil.disk_usage("/").used // (1024**3),
            "total_gb": psutil.disk_usage("/").total // (1024**3),
        },
    }


@click.command()
@click.option("--json", "as_json", is_flag=True, help="Вывести в JSON")
@click.option("--save", is_flag=True, help="Сохранить в data/report_TIMESTAMP.json")
@click.option("--interval", default=0, help="Интервал в секундах между обновлениями")
def monitor(as_json, save, interval):
    """Расширенный мониторинг системы с флагами"""
    console = Console()

    def show(stats):
        if as_json:
            console.print_json(data=stats)
        else:
            table = Table(title="🦊 SysFox: Мониторинг системы")
            table.add_column("Метрика", style="cyan")
            table.add_column("Значение", style="magenta")
            table.add_row("Uptime", f"{stats['uptime_h']} ч")
            table.add_row("CPU", f"{stats['cpu_percent']}%")
            table.add_row(
                "RAM",
                f"{stats['memory']['used_mb']}MB / {stats['memory']['total_mb']}MB",
            )
            table.add_row(
                "Диск", f"{stats['disk']['used_gb']}GB / {stats['disk']['total_gb']}GB"
            )
            console.print(table)

        if save:
            from utils.reporter import generate_report

            generate_report(stats)

            os.makedirs("data", exist_ok=True)
            timestamp = int(time.time())
            with open(f"data/report_{timestamp}.json", "w") as f:
                json.dump(stats, f, indent=2)

    if interval > 0:
        while True:
            stats = get_stats()
            os.system("clear")
            show(stats)
            time.sleep(interval)
    else:
        stats = get_stats()
        show(stats)
