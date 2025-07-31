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



#ai assistant simple
#install openai

import openai
import pyttsx3

openai.api_key = "" #add your openai API

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
question = input(" Ask the ai something: ")

response = openai.ChatCompletition.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": question}]
)

reply = response['choices'][0][message]['content']
print(f"AI: {reply}")
speak(reply)



#basic security camera
#grab a free account from twilio.com

import cv2
import time
from twilio.rest import Client

# Twilio your credentials
TWILIO_SID = 'enter your twilio sid here'
TWILIO_AUTH_TOKEN = 'enter your auth token here'
FROM_PHONE = 'your twilio phone number'
TO_PHONE = 'your phone number'
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_sms():
    try:
        message = client.messages.create(
            body="[!] MOTION DETECTED [!]",
            from_=FROM_PHONE,
            to=TO_PHONE
        )
        print(f"[SMS SENT] SID: {message.sid}")
    except Exception as e:
        print(f"[ERROR SENDING SMS]: {e}")

video = cv2.VideoCapture(0)
time.sleep(2)

first_frame = None
motion_detected = False
motion_timer = 0

while True:
    check, frame = video.read()
    if not check:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_in_frame = False
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        motion_in_frame = True
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Check if enough time has passed since last alert
    if motion_in_frame:
        if not motion_detected or time.time() - motion_timer > 60:
            send_sms()
            motion_detected = True
            motion_timer = time.time()
        status_text = "Motion Detected"
    else:
        status_text = "No Motion"

    cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Motion Detector", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

if key == ord('q'):
    break
video.release()
cv2.destroyAllWindows()
