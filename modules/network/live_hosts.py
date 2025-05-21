import subprocess


def live_hosts(subnet):
    try:
        result = subprocess.check_output(["fping", "-a", "-g", subnet], text=True)
        return result
    except Exception as e:
        return f"[red]Ошибка при поиске хостов:[/red] {e}"
