# block_and_stream_cipher.py

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# AES Block Cipher Encryption
def aes_encrypt(text: str) -> dict:
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(text.encode()) + encryptor.finalize()
    return {'encrypted': encrypted, 'key': key, 'iv': iv}

# AES Decrypt
def aes_decrypt(data: dict) -> str:
    cipher = Cipher(algorithms.AES(data['key']), modes.CFB(data['iv']))
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(data['encrypted']) + decryptor.finalize()
    return decrypted.decode()

if __name__ == "__main__":
    msg = "Hello, World!"
    encrypted_data = aes_encrypt(msg)
    print(f"Encrypted (AES): {encrypted_data}")
    print(f"Decrypted (AES): {aes_decrypt(encrypted_data)}")
