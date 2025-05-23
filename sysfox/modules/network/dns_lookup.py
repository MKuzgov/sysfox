import socket
from rich import print
from modules.network.utils import print_header, print_logo

def dns_lookup(domain):
    print_logo()
    print_header("DNS Lookup")
    try:
        ip = socket.gethostbyname(domain)
        print(f"[bold cyan]{domain}[/bold cyan] resolved to [bold green]{ip}[/bold green]")
    except socket.gaierror:
        print(f"[bold red]Unable to resolve domain: {domain}[/bold red]")
