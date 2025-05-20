import click
import os
import subprocess
from rich.console import Console

console = Console()


@click.command()
def audit():
    """Базовый аудит системы безопасности"""
    console.print("[bold magenta]🦊 SysFox: Аудит безопасности[/bold magenta]")

    checks = {
        "Открытые порты (ss)": "ss -tuln",
        "Список пользователей": "cut -d: -f1 /etc/passwd",
        "Проверка sudo пользователей": "getent group sudo",
        "Активные процессы": "ps aux --sort=-%mem | head -n 10",
    }

    for title, cmd in checks.items():
        console.print(f"\n[green]{title}[/green]")
        console.print("[italic]" + cmd + "[/italic]")
        console.print(os.popen(cmd).read())
