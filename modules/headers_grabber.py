import requests

def run(target):
    print("\n[*] Fetching HTTP Headers...")
    url = f"http://{target}"
    try:
        res = requests.get(url, timeout=2)
        print("  Headers:")
        for k, v in res.headers.items():
            print(f"    {k}: {v}")
    except Exception as e:
        print("  [!] Error fetching headers:", e)
