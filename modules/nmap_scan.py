from colorama import Fore, Style
import nmap

def run(target):
    print(Fore.CYAN + Style.BRIGHT + f"[+] Starting Nmap scan on {target} ...\n")
    nm = nmap.PortScanner()
    try:
        nm.scan(target, arguments='-sS -Pn -T4')
        for host in nm.all_hosts():
            print(Fore.YELLOW + f"Host: {host} ({nm[host].hostname()})")
            print(Fore.YELLOW + f"State: {nm[host].state()}")
            for proto in nm[host].all_protocols():
                print(Fore.MAGENTA + f"Protocol: {proto}")
                ports = nm[host][proto].keys()
                for port in sorted(ports):
                    state = nm[host][proto][port]['state']
                    print(Fore.GREEN + f"  Port {port}: {state}")
            print()
    except Exception as e:
        print(Fore.RED + f"[!] Nmap scan error: {e}")
