import dns.resolver

def run(target):
    print("\n[*] Fetching DNS Records...")
    try:
        for record_type in ['A', 'MX', 'NS', 'TXT']:
            answers = dns.resolver.resolve(target, record_type)
            print(f"  {record_type} Records:")
            for rdata in answers:
                print(f"    {rdata.to_text()}")
    except Exception as e:
        print("  [!] Error fetching DNS records:", e)
