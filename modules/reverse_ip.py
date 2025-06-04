import requests

def run(target):
    print("\n[*] Running Reverse IP Lookup...")
    try:
        response = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={target}")
        if "No records" in response.text or response.status_code != 200:
            print("  [!] No domains found or lookup failed.")
        else:
            domains = response.text.strip().split('\n')
            for domain in domains:
                print(f"  Found: {domain}")
    except Exception as e:
        print(f"  [!] Error during reverse IP lookup: {e}")
