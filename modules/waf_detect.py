import requests
from colorama import Fore, Style

def detect_waf(target):
    print(Fore.CYAN + "[WAF Detection Started]")
    try:
        url = f"https://{target}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " 
                          "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        resp_headers = {k.lower(): v.lower() for k, v in response.headers.items()}

        # Common WAF headers map
        waf_signatures = {
            "cloudflare": "Cloudflare WAF",
            "sucuri": "Sucuri WAF",
            "akamai": "Akamai WAF",
            "incapsula": "Imperva Incapsula WAF",
            "barracuda": "Barracuda WAF",
            "f5-big-ip": "F5 BIG-IP WAF",
            "mod_security": "ModSecurity WAF",
            "aws": "AWS WAF",
            "gws": "Google Web Server (May have protection)",
        }

        # Instagram/Meta specific headers
        meta_headers = ["x-fb-request-id", "x-fb-trace-id", "x-fb-debug"]

        waf_found = False

        # Check for common WAF headers
        for header, val in resp_headers.items():
            for key in waf_signatures:
                if key in header or key in val:
                    print(Fore.RED + f"[!] WAF Header Detected: {header} → {val}")
                    print(Fore.YELLOW + f"    → Possibly: {waf_signatures[key]}")
                    waf_found = True

        # Check for Instagram/Meta stealth WAF headers
        meta_found = []
        for meta_h in meta_headers:
            if meta_h in resp_headers:
                meta_found.append(f"{meta_h} → {resp_headers[meta_h]}")

        if meta_found:
            print(Fore.YELLOW + "[+] Suspicious Meta headers found:")
            for mh in meta_found:
                print(Fore.YELLOW + "    " + mh)
            print(Fore.RED + "[!] Stealth WAF Possibly Present (Meta/Facebook style)")
            waf_found = True

        # Check for common blocking status codes
        if response.status_code in [403, 406, 429]:
            print(Fore.RED + f"[!] Suspicious response status: {response.status_code} - Possible WAF block")
            waf_found = True

        if not waf_found:
            print(Fore.GREEN + "[-] No obvious WAF detected.")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Request error during WAF detection: {e}")
