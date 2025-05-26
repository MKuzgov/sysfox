from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from datetime import datetime
import os
import json
from scapy.all import sniff, ARP, ICMPv6ND_NS, IPv6
from sysfox.core.logger import setup_logger

console = Console()
logger = setup_logger()

found_hosts = []

# Логика анализа
mac_table = {}


def log_ndp_event(ip, mac, status):
    found_hosts.append({"ip": ip, "mac": mac, "status": status})


def save_ndp_report():
    folder = "reports"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(folder, f"ndp_{timestamp}.txt")

    lines = []
    lines.append("\n╭──── Сеть ARP/NDP Обнаружение ────╮")
    for host in found_hosts:
        ip = host["ip"]
        mac = host["mac"]
        status = host["status"]

        if status == "active":
            lines.append(f"│ 🟢 {ip} → MAC: {mac}")
        elif status == "suspicious":
            lines.append(f"│ 🔶 {ip} → ⚠️ Подозрение на подмену! MAC: {mac}")
        elif status == "lost":
            lines.append(f"│ 🔴 {ip} → ❌ Нет ответа")
        else:
            lines.append(f"│ ⚪ {ip} → MAC: {mac}")

    lines.append("╰────────────────────────────────╯\n")

    with open(filename, "w") as f:
        f.write("\n".join(lines))

    return filename


def display_network_map():
    console.print("\n📊 [bold cyan]Сводка:[/bold cyan]\n")
    print("\n╭──── Сеть ARP/NDP Обнаружение ────╮")
    for host in found_hosts:
        ip = host["ip"]
        mac = host["mac"]
        status = host["status"]

        if status == "active":
            print(f"│ 🟢 {ip} → MAC: {mac}")
        elif status == "suspicious":
            print(f"│ 🔶 {ip} → ⚠️ Подозрение на подмену! MAC: {mac}")
        elif status == "lost":
            print(f"│ 🔴 {ip} → ❌ Нет ответа")
        else:
            print(f"│ ⚪ {ip} → MAC: {mac}")
    print("╰────────────────────────────────╯\n")
    return save_ndp_report()


def start_ndp_scan(timeout):
    logger.info("[NDP] Запущен анализ сети")
    console.print("[bold blue]📡 Захват трафика в течение[/bold blue]", timeout, "[bold blue]секунд...[/bold blue]")

    def handle_packet(packet):
        if ARP in packet and packet[ARP].op == 2:
            ip = packet[ARP].psrc
            mac = packet[ARP].hwsrc
            logger.info(f"[ARP] Обнаружен {ip} -> {mac}")

            if ip in mac_table:
                if mac_table[ip] != mac:
                    status = "suspicious"
                else:
                    status = "active"
            else:
                status = "active"
            mac_table[ip] = mac
            log_ndp_event(ip, mac, status)

        elif IPv6 in packet and ICMPv6ND_NS in packet:
            ip = packet[IPv6].src
            logger.info(f"[NDP] Обнаружено IPv6 устройство: {ip}")
            log_ndp_event(ip, "IPv6", "active")

    sniff(prn=handle_packet, store=False, timeout=timeout)
    report_path = display_network_map()
    console.print(f"✔ Отчёт сохранён в: [green]{report_path}[/green]")
    logger.info(f"[NDP] Отчёт создан: {report_path}")
    logger.info("[NDP] Анализ завершён")
