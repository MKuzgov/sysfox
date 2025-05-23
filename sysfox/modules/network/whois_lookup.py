import whois
from rich import print
from modules.network.utils import print_header, print_logo

def whois_lookup(domain):
    print_logo()
    print_header("Whois Lookup")
    try:
        result = whois.whois(domain)
        print(result)
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
