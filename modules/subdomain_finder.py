import requests

def run(target):
    print("\n[*] Running Subdomain Finder...")
    subdomains = []
    try:
        with open("wordlists/subdomains.txt", "r") as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print("[!] Wordlist file 'wordlists/subdomains.txt' not found!")
        return

    found_subdomains = []

    for subdomain in subdomains:
        url = f"http://{subdomain}.{target}"
        try:
            res = requests.get(url, timeout=5)  # Timeout increased to 5 seconds
            if res.status_code == 200:
                print(f"  Found: {url}")
                found_subdomains.append(url)
        except requests.exceptions.Timeout:
            print(f"  [!] Timeout occurred for {url}")
        except requests.exceptions.ConnectionError:
            # Connection error, usually means subdomain doesn't exist or no response
            pass
        except requests.exceptions.RequestException as e:
            print(f"  [!] Request failed for {url}: {e}")

    if not found_subdomains:
        print("  No subdomains found.")
