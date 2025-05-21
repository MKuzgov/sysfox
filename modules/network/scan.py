# modules/network/scan.py
import subprocess
import json
import os
from datetime import datetime


def net_scan(target):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = "reports/network"
    os.makedirs(report_dir, exist_ok=True)
    report_path = f"{report_dir}/scan_{timestamp}.json"

    try:
        result = subprocess.run(
            ["nmap", "-sn", target], capture_output=True, text=True, check=True
        )
        lines = result.stdout.splitlines()
        hosts = []

        current_host = {}
        for line in lines:
            if line.startswith("Nmap scan report for"):
                current_host = {"ip": line.split()[-1]}
            elif "MAC Address" in line:
                current_host["mac"] = line.split(" ")[2]
                hosts.append(current_host)

        with open(report_path, "w") as f:
            json.dump(hosts, f, indent=4)

        print(f"[+] Scan complete. {len(hosts)} host(s) found.")
        for host in hosts:
            print(f"IP: {host['ip']} | MAC: {host.get('mac', 'N/A')}")

    except subprocess.CalledProcessError as e:
        print("[!] Scan failed:", e)
