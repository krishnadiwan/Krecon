import socket

def is_telnet(host, port):
    try:
        s = socket.create_connection((host, port), timeout=2)
        s.sendall(b"\r\n")  # Send basic Telnet handshake
        response = s.recv(1024)
        if b"\xff" in response:  # Telnet IAC byte
            return True
        s.close()
    except:
        return False
    return False

# Example use
host = "example.com"
for port in range(1, 1025):
    if is_telnet(host, port):
        print(f"[TELNET DETECTED] {host}:{port}")
