import requests
from rich import print
from modules.network.utils import print_header, print_logo

def get_ip_info(ip):
    print_logo()
    print_header("IP Geolocation")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            for key in ['query', 'country', 'regionName', 'city', 'zip', 'lat', 'lon', 'org', 'isp']:
                print(f"[bold]{key.capitalize()}:[/bold] {data[key]}")
        else:
            print("[bold red]Failed to retrieve geolocation data[/bold red]")
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
