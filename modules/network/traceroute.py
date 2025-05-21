import subprocess


def traceroute(host):
    try:
        result = subprocess.check_output(["traceroute", host], text=True)
        return result
    except Exception as e:
        return f"[red]Ошибка traceroute:[/red] {e}"
