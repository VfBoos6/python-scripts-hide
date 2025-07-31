#scan-port-at-an-IP

import socket
from datetime import datetime

target = "45.33.32.156" #put aici any IP
start_port = 1
end_port = 1024

print(f"[+] Scanning {target} from port {start_port} to {end_port}")
print(f"[+] Started at: {datetime.now()}\n")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("[-] Hostname could not be resolved.")
    exit()

try:
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                print(f"[OPEN] Port {port} ({service})")
            s.close()
        except Exception as e:
            print(f"[-] Error on port {port}: {e}")
except KeyboardInterrupt:
    print("\n[!] Scan aborted by user.")

print(f"\n[+] Scan complete at: {datetime.now()}")
