#website-traffic-on-wifi

#pip install scapy 
from scapy.all import sniff, TCP, Raw, IP
import re
from datetime import datetime

def extract_http_url(packet):
    if packet.haslayer(Raw) and packet.haslayer(TCP):
        payload = packet[Raw].load
        try:
            payload_str = payload.decode(errors="ignore")
            if "Host:" in payload_str and "GET" in payload_str:
                host = re.search(r"Host: (.*)", payload_str)
                path = re.search(r"GET (.*?) HTTP", payload_str)
                if host and path:
                    url = f"http://{host.group(1).strip()}{path.group(1).strip()}"

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    src_ip = packet[IP].src if packet.haslayer(IP) else "Unknown"
                    dst_ip = packet[IP].dst if packet.haslayer(IP) else "Unknown"

                    log_entry = f"[{timestamp}] {src_ip} -> {dst_ip} | {url}\n"
                    print(log_entry.strip())
                    with open("captured_urls.txt", "a") as f:
                        f.write(log_entry)
        except Exception:
            pass

sniff(filter="tcp port 80", prn=extract_http_url, store=False)

