import sys
import base64
import hashlib
from cryptography.fernet import Fernet

usage_msg = "Usage: "+ sys.argv[0] +" (-e/-d) [file] [password]"

if len(sys.argv) < 3:
    print(usage_msg)
    sys.exit(1)

mode = sys.argv[1]
file = sys.argv[2]

if len(sys.argv) >= 4:
    password = sys.argv[3]
else:
    password = input("Enter password: ")

# SIMPLE FIX: always valid key
key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())
c = Fernet(key)

if mode == "-e":
    with open(file, "rb") as f:
        data = f.read()
    encrypted = c.encrypt(data)
    print(encrypted.decode())

elif mode == "-d":
    with open(file, "r") as f:
        data = f.read()
    decrypted = c.decrypt(data.encode())
    sys.stdout.buffer.write(decrypted)

else:
    print("Use -e or -d")