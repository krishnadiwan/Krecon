# KRecon

**KRecon** is a Kali Linux-compatible reconnaissance tool developed by Krishna. It provides a set of modules to gather intelligence on target domains and IPs during penetration testing and security assessments.

## 🚀 Features

- **WHOIS Lookup** – Retrieve domain registration details  
- **DNS Records Fetch** – Get A, MX, NS, TXT, and other records  
- **Port Scanning** – Scan for open TCP ports  
- **Subdomain Finder** – Discover subdomains via brute-force or APIs  
- **HTTP Headers Grabber** – Fetch and display HTTP response headers  
- **Reverse IP Lookup** – Identify domains hosted on the same IP  
- **WAF Detection** – Detect Web Application Firewalls  
- **IP Finder** – Resolve domain names to IP addresses  
- **Nmap Integration** – Perform deep service enumeration  
- **Telnet Check** – Verify if Telnet is enabled on a host  

## ⚙ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/krishnadiwan/Krecon.git
   cd Krecon
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tool:**
   ```bash
   python3 krecon.py --target example.com
   ```

## 💡 Usage

```bash
python3 krecon.py --target example.com
```

> You can add more flags or options based on available modules.

## 🧩 Modules Overview

| Module                | Description                        |
|-----------------------|------------------------------------|
| `whois_lookup.py`     | Performs WHOIS lookups             |
| `dns_info.py`         | Fetches DNS records                |
| `port_scanner.py`     | Scans ports on the target          |
| `subdomain_finder.py` | Discovers subdomains               |
| `headers_grabber.py`  | Retrieves HTTP response headers    |
| `reverse_ip.py`       | Performs reverse IP lookups        |
| `waf_detect.py`       | Detects Web Application Firewalls  |
| `ip_finder.py`        | Resolves domain to IP address      |
| `nmap_scan.py`        | Integrates Nmap scans              |
| `telnet_check.py`     | Checks for Telnet access           |

## ⚠ Notes

- Requires **Python 3.x**
- Some features (e.g., Nmap) may require **root privileges**
- Use responsibly: **Only scan targets you have permission for**

