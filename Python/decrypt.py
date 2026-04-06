from cryptography.fernet import Fernet
import hashlib
import base64

def generate_key(password):
    return base64.urlsafe_b64encode(
        hashlib.sha256(password.encode()).digest()
    )

# 🔴 PASTE YOUR GENERATED VALUE HERE
encrypted_flag = b'PASTE_HERE'

user_input = input("Enter final password: ")

key = generate_key(user_input)
cipher = Fernet(key)

try:
    print("\n🎉 FLAG:", cipher.decrypt(encrypted_flag).decode())
except:
    print("❌ Wrong password")