import socket
from rich import print
from modules.network.utils import print_header, print_logo

def get_ip_info(domain):
    print_logo()
    print_header("IP Info")
    try:
        print(f"[bold]Domain:[/bold] {domain}")
        print(f"[bold]IP Address:[/bold] {socket.gethostbyname(domain)}")
    except socket.gaierror:
        print(f"[bold red]Unable to resolve domain: {domain}[/bold red]")
