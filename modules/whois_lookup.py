import whois
from datetime import datetime

def run(target):
    print("[*] Running WHOIS lookup...\n")
    try:
        w = whois.whois(target)

        # Format domain name(s)
        domain_names = w.domain_name
        if isinstance(domain_names, list):
            domain_names = ', '.join(domain_names)
        print(f"Domain Name: {domain_names}")

        # Registrar
        registrar = w.registrar if w.registrar else "N/A"
        print(f"Registrar: {registrar}")

        # Format dates nicely
        def format_date(d):
            if isinstance(d, list):
                d = d[0]
            if isinstance(d, datetime):
                return d.strftime("%d %b %Y")
            return str(d)

        creation_date = format_date(w.creation_date)
        expiry_date = format_date(w.expiration_date)

        print(f"Creation Date: {creation_date}")
        print(f"Expiry Date: {expiry_date}")

    except Exception as e:
        print(f"[!] Error fetching WHOIS data: {e}")
