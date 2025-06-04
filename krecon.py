from colorama import init, Fore, Style
import argparse
import socket
import subprocess

# Import your existing modules
from modules import whois_lookup, subdomain_finder, port_scanner, dns_info, headers_grabber, reverse_ip, waf_detect

init(autoreset=True)

def banner():
    try:
        with open("banner.txt", "r") as f:
            print(Fore.MAGENTA + Style.BRIGHT + f.read())
    except FileNotFoundError:
        print(Fore.RED + "[!] Banner file not found. Skipping banner.\n")

def task(message, number):
    print(Fore.CYAN + Style.BRIGHT + f"[{number}] {message}")

def run_nmap(target):
    print(Fore.YELLOW + "    [*] Running Nmap Scan...")
    try:
        result = subprocess.run(["nmap", "-sV", target], capture_output=True, text=True)
        print(Fore.WHITE + result.stdout)
    except Exception as e:
        print(Fore.RED + f"    [!] Nmap scan failed: {e}")

def find_ip(target):
    print(Fore.YELLOW + "    [*] Finding IPv4 and IPv6 addresses...")
    try:
        ipv4 = socket.gethostbyname(target)
        print(Fore.GREEN + f"    IPv4 Address: {ipv4}")
    except Exception as e:
        print(Fore.RED + f"    Could not find IPv4: {e}")

    try:
        infos = socket.getaddrinfo(target, None, socket.AF_INET6)
        ipv6s = set()
        for info in infos:
            ipv6s.add(info[4][0])
        if ipv6s:
            print(Fore.GREEN + "    IPv6 Addresses:")
            for ip6 in ipv6s:
                print(Fore.GREEN + f"      - {ip6}")
        else:
            print(Fore.RED + "    No IPv6 addresses found.")
    except Exception as e:
        print(Fore.RED + f"    Could not find IPv6: {e}")

def telnet_check(target, ports=[23, 2323, 992]):
    print(Fore.YELLOW + f"    [*] Checking Telnet ports on {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(Fore.GREEN + f"    Telnet port {port} is OPEN")
            else:
                print(Fore.RED + f"    Telnet port {port} is CLOSED")
            sock.close()
        except Exception as e:
            print(Fore.RED + f"    Telnet check on port {port} failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="KRecon - Complete Recon Tool")
    parser.add_argument("-t", "--target", required=True, help="Target domain or IP")
    args = parser.parse_args()
    target = args.target

    banner()
    print(Fore.GREEN + Style.BRIGHT + f"[+] Starting Recon on: {target}\n")

    try:
        task("Running WHOIS Lookup...", 1)
        whois_lookup.run(target)
        print()

        task("Finding Subdomains...", 2)
        subdomain_finder.run(target)
        print()

        task("Running Port Scanner...", 3)
        port_scanner.run(target)
        print()

        task("Running DNS Info...", 4)
        dns_info.run(target)
        print()

        task("Grabbing HTTP Headers...", 5)
        headers_grabber.run(target)
        print()

        task("Performing Reverse IP Lookup...", 6)
        reverse_ip.run(target)
        print()

        task("Running Nmap Scan...", 7)
        run_nmap(target)
        print()

        task("Finding IP Addresses (IPv4 & IPv6)...", 8)
        find_ip(target)
        print()

        task("Checking Telnet Port (23)...", 9)
        telnet_check(target)
        print()

        task("Running WAF Detection...", 10)
        waf_detect.detect_waf(target)
        print()

        print(Fore.GREEN + Style.BRIGHT + "[+] Recon Completed Successfully!")

    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "[!] Error: " + str(e))

if __name__ == "__main__":
    main()
