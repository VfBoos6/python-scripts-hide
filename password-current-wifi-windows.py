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
