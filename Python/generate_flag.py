from cryptography.fernet import Fernet
import hashlib
import base64

FLAG = "MohawkCTF{NO ONE TOLD ME MAKING THESE CTF’S WOULD BE THIS DIFFICULT}"
FINAL_PASSWORD = "final_key"

def generate_key(password):
    return base64.urlsafe_b64encode(
        hashlib.sha256(password.encode()).digest()
    )

key = generate_key(FINAL_PASSWORD)
cipher = Fernet(key)

encrypted = cipher.encrypt(FLAG.encode())
print("Encrypted flag:\n", encrypted)