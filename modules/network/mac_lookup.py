import requests


def mac_lookup(mac):
    try:
        r = requests.get(f"https://api.macvendors.com/{mac}")
        if r.status_code == 200:
            return r.text
        else:
            return f"[yellow]Производитель не найден[/yellow]"
    except Exception as e:
        return f"[red]Ошибка MAC Lookup:[/red] {e}"
