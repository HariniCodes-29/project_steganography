import cv2
import os
# Load image
img = cv2.imread("fruits.jpg")  # Ensure "fruits.jpg" exists in the script directory
if img is None:
    print("Error: Image not found!")
    exit()
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create character-to-value and value-to-character mappings
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Variables for pixel traversal
n, m, z = 0, 0, 0

# Encode message in image
for char in msg:
    img[n, m, z] = d[char]  # Store ASCII value in pixel
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= img.shape[1]:  # Move to next row if column limit is reached
            m = 0
            n += 1
            if n >= img.shape[0]:  # Prevent out-of-bounds error
                print("Error: Message too long for the image size!")
                exit()

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Decryption
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for decryption: ")
if password == pas:
    for i in range(len(msg)):  # Extract only the stored message length
        message += c[int(img[n, m, z])]  # Convert np.uint8 to int before lookup
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1
                if n >= img.shape[0]:
                    break  # Stop reading if message exceeds image size
    print("Decrypted message:", message)
else:
    print("Authentication failed! Incorrect password.")
