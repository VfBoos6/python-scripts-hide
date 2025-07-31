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


