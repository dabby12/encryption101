# symmetric_encryption.py

from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt function
def encrypt(message: str) -> bytes:
    encrypted = cipher.encrypt(message.encode())
    return encrypted

# Decrypt function
def decrypt(encrypted_message: bytes) -> str:
    decrypted = cipher.decrypt(encrypted_message).decode()
    return decrypted

if __name__ == "__main__":
    msg = "Hello, World!"
    encrypted_msg = encrypt(msg)
    print(f"Encrypted: {encrypted_msg}")
    print(f"Decrypted: {decrypt(encrypted_msg)}")
