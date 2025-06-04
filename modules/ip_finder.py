from colorama import Fore, Style
import socket

def run(target):
    print(Fore.CYAN + Style.BRIGHT + f"[+] Finding IP addresses (IPv4 & IPv6) for {target} ...\n")
    try:
        addr_info = socket.getaddrinfo(target, None)
        ipv4 = set()
        ipv6 = set()
        for info in addr_info:
            family = info[0]
            ip = info[4][0]
            if family == socket.AF_INET:
                ipv4.add(ip)
            elif family == socket.AF_INET6:
                ipv6.add(ip)
        if ipv4:
            print(Fore.YELLOW + "IPv4 Addresses:")
            for ip in ipv4:
                print(Fore.GREEN + f"  {ip}")
        else:
            print(Fore.RED + "No IPv4 address found.")
        if ipv6:
            print(Fore.YELLOW + "\nIPv6 Addresses:")
            for ip in ipv6:
                print(Fore.GREEN + f"  {ip}")
        else:
            print(Fore.RED + "No IPv6 address found.")
    except socket.gaierror:
        print(Fore.RED + "[!] Could not resolve IP addresses.")
    print()
