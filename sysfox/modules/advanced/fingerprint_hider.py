# modules/advanced/fingerprint_hider.py
import os
import subprocess
from rich import print
from modules.network.utils import print_header, print_logo
from sysfox.core.logger import setup_logger

logger = setup_logger()

# Предустановленные шаблоны маскировки (можно расширять)
PROFILES = {
    "win11": {
        "ttl": 128,
        "window": 65535,
        "ssh_banner": "SSH-2.0-OpenSSH_7.9 Win32",
        "http_server": "IIS/10.0"
    },
    "debian": {
        "ttl": 64,
        "window": 29200,
        "ssh_banner": "SSH-2.0-OpenSSH_8.3p1 Debian",
        "http_server": "Apache/2.4.41 (Debian)"
    }
}

def apply_mask(profile):
    print_logo()
    print_header("Fingerprint Masking")

    if profile not in PROFILES:
        print(f"[bold red]Профиль '{profile}' не найден[/bold red]")
        return

    settings = PROFILES[profile]
    print(f"[bold green]Применяем маску под: {profile}[/bold green]")
    logger.info(f"[MASK] Применение профиля {profile}")

    try:
        subprocess.run(["sudo", "sysctl", f"net.ipv4.ip_default_ttl={settings['ttl']}"], check=True)
        print(f"[cyan]✔ TTL установлен: {settings['ttl']}[/cyan]")
    except Exception as e:
        logger.error(f"[MASK] Ошибка TTL: {e}")

    try:
        subprocess.run(["sudo", "iptables", "-t", "mangle", "-A", "POSTROUTING", "-p", "tcp", "--tcp-flags", "SYN,RST", "SYN", "-j", "TCPMSS", "--set-mss", str(settings['window'])], check=True)
        print(f"[cyan]✔ TCP Window Size: {settings['window']}[/cyan]")
    except Exception as e:
        logger.warning(f"[MASK] iptables ошибка: {e}")

    ssh_file = "/etc/ssh/sshd_config"
    if os.geteuid() == 0:
        try:
            with open(ssh_file, "a") as f:
                f.write(f"\nBanner /etc/ssh_banner\n")
            with open("/etc/ssh_banner", "w") as b:
                b.write(settings['ssh_banner'] + "\n")
            subprocess.run(["sudo", "systemctl", "restart", "ssh"], check=True)
            print(f"[cyan]✔ SSH баннер изменён[/cyan]")
        except Exception as e:
            logger.warning(f"[MASK] SSH banner: {e}")

    apache_conf = "/etc/apache2/conf-enabled/security.conf"
    if os.path.exists(apache_conf):
        try:
            with open(apache_conf, "a") as f:
                f.write(f"\nServerTokens Full\nServerSignature On\nHeader set Server \"{settings['http_server']}\"\n")
            subprocess.run(["sudo", "systemctl", "restart", "apache2"], check=True)
            print(f"[cyan]✔ HTTP-заголовок подменён[/cyan]")
        except Exception as e:
            logger.warning(f"[MASK] Apache ServerHeader: {e}")

    print(f"[bold green]\n✅ Маска '{profile}' применена успешно![/bold green]")
    logger.info("[MASK] Маскировка завершена")

def revert_mask():
    print_logo()
    print_header("Revert Fingerprint Mask")
    logger.info("[MASK] Откат маскировки")

    try:
        subprocess.run(["sudo", "sysctl", "net.ipv4.ip_default_ttl=64"], check=True)
        print("[green]✔ TTL сброшен до 64[/green]")
    except Exception as e:
        logger.warning(f"[REVERT] TTL: {e}")

    try:
        subprocess.run(["sudo", "iptables", "-t", "mangle", "-F"], check=True)
        print("[green]✔ iptables очищен[/green]")
    except Exception as e:
        logger.warning(f"[REVERT] iptables: {e}")

    try:
        subprocess.run(["sudo", "sed", "-i", "/Banner \/etc\/ssh_banner/d", "/etc/ssh/sshd_config"], check=True)
        subprocess.run(["sudo", "rm", "-f", "/etc/ssh_banner"], check=True)
        subprocess.run(["sudo", "systemctl", "restart", "ssh"], check=True)
        print("[green]✔ SSH баннер удалён[/green]")
    except Exception as e:
        logger.warning(f"[REVERT] SSH: {e}")

    apache_conf = "/etc/apache2/conf-enabled/security.conf"
    if os.path.exists(apache_conf):
        try:
            subprocess.run(["sudo", "sed", "-i", "/ServerTokens/d", apache_conf], check=True)
            subprocess.run(["sudo", "sed", "-i", "/ServerSignature/d", apache_conf], check=True)
            subprocess.run(["sudo", "sed", "-i", "/Header set Server/d", apache_conf], check=True)
            subprocess.run(["sudo", "systemctl", "restart", "apache2"], check=True)
            print("[green]✔ Apache ServerHeader очищен[/green]")
        except Exception as e:
            logger.warning(f"[REVERT] Apache: {e}")

    print("[bold green]\n✅ Маска успешно удалена и всё восстановлено[/bold green]")
    logger.info("[MASK] Маска удалена")
