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
