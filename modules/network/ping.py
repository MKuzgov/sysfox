import subprocess
from rich import print
from modules.network.utils import print_header, print_logo

def ping_host(target, count):
    print_logo()
    print_header("Ping")
    try:
        result = subprocess.run(["ping", "-c", str(count), target], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
