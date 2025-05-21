import subprocess


def whois_lookup(domain):
    try:
        result = subprocess.check_output(["whois", domain], text=True)
        return result
    except Exception as e:
        return f"[red]Ошибка WHOIS:[/red] {e}"
