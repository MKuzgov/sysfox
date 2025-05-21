import subprocess


def dns_lookup(domain):
    try:
        result = subprocess.check_output(
            ["dig", domain, "+noall", "+answer"], text=True
        )
        return result
    except Exception as e:
        return f"[red]Ошибка DNS:[/red] {e}"
