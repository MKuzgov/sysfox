import subprocess
from rich import print
from modules.network.utils import print_header, print_logo

def traceroute(target):
    print_logo()
    print_header("Traceroute")
    try:
        result = subprocess.run(["traceroute", target], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
