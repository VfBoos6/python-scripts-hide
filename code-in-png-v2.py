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
