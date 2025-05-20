import click
import os
import subprocess
from rich.console import Console
from rich.prompt import Confirm

console = Console()


@click.command()
def autopostinstall():
    """Автоматическая настройка и установка ПО"""
    console.print("[bold cyan]🦊 SysFox: Автоматическая настройка системы[/bold cyan]")

    steps = [
        (
            "Обновление системы",
            ["sudo", "apt", "update", "&&", "sudo", "apt", "upgrade", "-y"],
        ),
        (
            "Установка полезных утилит",
            [
                "sudo",
                "apt",
                "install",
                "-y",
                "curl",
                "wget",
                "git",
                "htop",
                "net-tools",
            ],
        ),
        (
            "Установка fail2ban (базовая защита)",
            ["sudo", "apt", "install", "-y", "fail2ban"],
        ),
        ("Создание пользователя sysfoxadmin", ["sudo", "adduser", "sysfoxadmin"]),
    ]

    for label, cmd in steps:
        if Confirm.ask(f"▶ {label}?"):
            console.print(f"[green]Выполняется:[/green] {label}")
            subprocess.run(" ".join(cmd), shell=True)
        else:
            console.print(f"[yellow]Пропущено:[/yellow] {label}")
