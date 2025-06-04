import socket

def run(target):
    print("\n[*] Running Port Scanner on common ports...")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"  Port {port}: Open")
        sock.close()
