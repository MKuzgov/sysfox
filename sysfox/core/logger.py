from rich.console import Console

console = Console()

def show_log():
    try:
        with open("logs/sysfox_network.log", "r") as f:
            logs = f.read()
        console.print(f"[bold yellow]Logs:[/bold yellow]\n{logs}")
    except FileNotFoundError:
        console.print("[red]Log file not found.")
