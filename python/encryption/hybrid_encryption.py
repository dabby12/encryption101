# hybrid_encryption.py

import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Generate RSA key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Encrypt function
def encrypt(message: str) -> dict:
    # Symmetric encryption (AES)
    aes_key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()

    # Encrypt AES key with RSA
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    return {
        'encrypted_message': encrypted_message,
        'encrypted_key': encrypted_key,
        'iv': iv
    }

# Decrypt function
def decrypt(encrypted_data: dict) -> str:
    encrypted_message = encrypted_data['encrypted_message']
    encrypted_key = encrypted_data['encrypted_key']
    iv = encrypted_data['iv']
    
    # Decrypt AES key with RSA
    aes_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Symmetric decryption
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
    
    return decrypted_message.decode()

if __name__ == "__main__":
    msg = "Hello, World!"
    encrypted_data = encrypt(msg)
    print(f"Encrypted: {encrypted_data}")
    print(f"Decrypted: {decrypt(encrypted_data)}")
