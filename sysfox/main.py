# main.py
import argparse
import sys
import traceback
from sysfox.core import error_handler
from sysfox.core.logger import setup_logger
from sysfox.modules.network import (
    dns_lookup, geolocation, interface, ipinfo, live_hosts,
    mac_lookup, ping, scan, traceroute, whois_lookup, report
)
from sysfox.modules.advanced import fingerprint_hider

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="SysFox Network Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    parser_dns = subparsers.add_parser("dns")
    parser_dns.add_argument("domain")

    parser_geo = subparsers.add_parser("geo")
    parser_geo.add_argument("ip")

    parser_iface = subparsers.add_parser("ifaces")

    parser_ipinfo = subparsers.add_parser("ipinfo")
    parser_ipinfo.add_argument("domain")

    parser_live = subparsers.add_parser("live")
    parser_live.add_argument("subnet")

    parser_mac = subparsers.add_parser("mac")
    parser_mac.add_argument("mac")

    parser_ping = subparsers.add_parser("ping")
    parser_ping.add_argument("target")
    parser_ping.add_argument("-c", "--count", type=int, default=4)

    parser_scan = subparsers.add_parser("scan")
    parser_scan.add_argument("host")
    parser_scan.add_argument("ports", nargs="*", type=int)

    parser_trace = subparsers.add_parser("trace")
    parser_trace.add_argument("target")

    parser_whois = subparsers.add_parser("whois")
    parser_whois.add_argument("domain")

    parser_mask = subparsers.add_parser("x-mask")
    parser_mask.add_argument("--profile", help="Маска для подмены fingerprint (например: win11)")
    parser_mask.add_argument("--revert", action="store_true", help="Сброс маскировки")

    parser_report = subparsers.add_parser("report")

    args = parser.parse_args()
    logger.info(f"Команда получена: {args.command}")

    try:
        if args.command == "dns":
            report.log_command(f"dns {args.domain}")
            dns_lookup.dns_lookup(args.domain)
        elif args.command == "geo":
            report.log_command(f"geo {args.ip}")
            geolocation.get_ip_info(args.ip)
        elif args.command == "ifaces":
            report.log_command("ifaces")
            interface.show_interfaces()
        elif args.command == "ipinfo":
            report.log_command(f"ipinfo {args.domain}")
            ipinfo.get_ip_info(args.domain)
        elif args.command == "live":
            report.log_command(f"live {args.subnet}")
            live_hosts.find_live_hosts(args.subnet)
        elif args.command == "mac":
            report.log_command(f"mac {args.mac}")
            mac_lookup.mac_lookup(args.mac)
        elif args.command == "ping":
            report.log_command(f"ping {args.target} -c {args.count}")
            ping.ping_host(args.target, args.count)
        elif args.command == "scan":
            report.log_command(f"scan {args.host} {args.ports}")
            scan.port_scan(args.host, args.ports)
        elif args.command == "trace":
            report.log_command(f"trace {args.target}")
            traceroute.traceroute(args.target)
        elif args.command == "whois":
            report.log_command(f"whois {args.domain}")
            whois_lookup.whois_lookup(args.domain)
        elif args.command == "report":
            report.create_auto_report()
        elif args.command == "x-mask":
            if args.revert:
                fingerprint_hider.revert_mask()
            elif args.profile:
                fingerprint_hider.apply_mask(args.profile)
            else:
                print("[bold red]❗ Укажите --profile или --revert[/bold red]")
        else:
            parser.print_help()
    except Exception as e:
        logger.error(f"[!] Глобальная ошибка: {e}")
        logger.debug(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
