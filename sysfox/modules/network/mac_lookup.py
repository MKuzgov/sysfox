import requests
from rich import print
from modules.network.utils import print_header, print_logo

def mac_lookup(mac):
    print_logo()
    print_header("MAC Address Lookup")
    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[bold green]Vendor:[/bold green] {response.text}")
        else:
            print("[bold red]MAC address not found[/bold red]")
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")

