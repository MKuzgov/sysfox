import psutil
from rich import print
from modules.network.utils import print_header, print_logo

def show_interfaces():
    print_logo()
    print_header("Network Interfaces")
    interfaces = psutil.net_if_addrs()
    for interface, addrs in interfaces.items():
        print(f"[bold blue]{interface}[/bold blue]")
        for addr in addrs:
            print(f"  - {addr.family.name}: {addr.address}")
