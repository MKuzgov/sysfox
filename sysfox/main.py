
### main.py
import argparse
from modules.network import (
    dns_lookup, geolocation, interface, ipinfo, live_hosts,
    mac_lookup, ping, scan, traceroute, whois_lookup
)

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

    args = parser.parse_args()

    if args.command == "dns":
        dns_lookup.dns_lookup(args.domain)
    elif args.command == "geo":
        geolocation.get_ip_info(args.ip)
    elif args.command == "ifaces":
        interface.show_interfaces()
    elif args.command == "ipinfo":
        ipinfo.get_ip_info(args.domain)
    elif args.command == "live":
        live_hosts.find_live_hosts(args.subnet)
    elif args.command == "mac":
        mac_lookup.mac_lookup(args.mac)
    elif args.command == "ping":
        ping.ping_host(args.target, args.count)
    elif args.command == "scan":
        scan.port_scan(args.host, args.ports)
    elif args.command == "trace":
        traceroute.traceroute(args.target)
    elif args.command == "whois":
        whois_lookup.whois_lookup(args.domain)
    else:
        parser.print_help()
