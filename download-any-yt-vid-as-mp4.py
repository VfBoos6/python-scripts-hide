import os
import subprocess

def download_youtube_video():
    url = input("🔗 Introdu link-ul YouTube: ").strip()
    if not url.startswith("http"):
        print("[-] Link invalid. Încearcă din nou.")
        return

    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    print("⬇️ Se descarcă videoclipul...")
    try:
        subprocess.run([
            "yt-dlp.exe",  # executabil local, trebuie să fie în același folder cu scriptul, install yt-dlp
            "-f", "bestvideo+bestaudio/best",
            "-o", os.path.join(output_dir, "%(title)s.%(ext)s"),
            url
        ], check=True)
        print("[+] Descărcare completă! Vezi folderul 'downloads/'.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Eroare la descărcare: {e}")

if __name__ == "__main__":
    download_youtube_video()
