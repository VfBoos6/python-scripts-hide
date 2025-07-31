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
