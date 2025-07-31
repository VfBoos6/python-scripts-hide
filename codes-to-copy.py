#python-script-into-exe

#pip install pyinstaller

import subprocess
import os
import sys

script_path = "your_script.py"  # Replace with your script

def build_exe(script_path):
    if not os.path.exists(script_path):
        print("[-] File not found:", script_path)
        return

    try:
        print("[|] Building executable...")
        subprocess.run([
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--noconsole",
            script_path
        ], check=True)

        exe_name = os.path.splitext(os.path.basename(script_path))[0] + ".exe"
        dist_path = os.path.join("dist", exe_name)

        if os.path.exists(dist_path):
            print("[+] Executable created at:", dist_path)
        else:
            print("⚠ Build finished, but .exe not found in /dist")

    except subprocess.CalledProcessError:
        print("[-] Build failed. Is PyInstaller installed?")
    except Exception as e:
        print("[-] Error:", str(e))

if __name__ == "__main__":
    build_exe(script_path)




#code-in-png

#replace "image.png" with the desired image
#replace "code" with your code as bytes

with open("image.png", "rb") as file:
    data = file.read()

hidden_code = b"This is hidden malware code..."

with open("image.png", "ab") as file:
    file.write(hidden_code)

with open("image.png", "rb") as file:
    content = file.read()
    if hidden_code in content:
        print("Hidden malware detected inside the image!")
    else:
        print("No hidden payload found.")




#code-in-png-v2

with open("image.png", "rb") as image_file:
    original_data = image_file.read()

payload = b"This is hidden malware code..."

with open("image.png", "ab") as image_file:
    image_file.write(payload)

with open("image.png", "rb") as image_file:
    content = image_file.read()

if payload in content:
    print("Hidden payload detected inside the image!")
else:
    print("No hidden payload found.")



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



#password-current-wifi-linux

import os
import glob
import re
import glob
import re

wifi_files = glob.glob('/etc/NetworkManager/system-connections/*')

for file in wifi_files:
    try:
        with open(file, 'r') as f:
            content = f.read()
        
        ssid = re.search(r'ssid=(.*)', content)
        psk = re.search(r'psk=(.*)', content)

        if ssid:
            print(f"SSID: {ssid.group(1)}")
        if psk:
            print(f"Password: {psk.group(1)}")
        print('-' * 30)

    except PermissionError:
        print(f"Permission denied for: {file}")
    except Exception as e:
        print(f"Error reading {file}: {e}")

#/etc/NetworkManager/system-connections/
#sudo python3 script.py
#sudo python3 script_wifi_linux.py 



#password-current-wifi-windows


data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profile = []
for i in data:
    if "All User Profile" in i:
        profile.append(i.split(":")[1][1:-1])

for i in profile:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        result = []

        for b in results:
            if "Key Content" in b:
                result.append(b.split(":")[1][1:-1])
        
        try:
            print("{:<30}| {:<}".format(i, result[0]))
        except Exception as e:
            print("{:<30}| {:<}".format(i, ""))
    except Exception as e:
        print("{:<30}| {:<}".format(i, "ERROR OCCURED"))


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


#Face blur script

import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 5)

for (x, y, w, h) in faces:
    face_roi = frame[y:y+h, x:x+w]
    face_roi = cv2.GaussianBlur(face_roi, (99, 99), 30)
    frame[y:y+h, x:x+w] = face_roi
    cv2.imshow("Live Face Blur", frame)
    
    #press q to stop
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cap.release()
    cv2.destroyAllWindows()
