# main.py

from encryption.symmetric_encryption import encrypt as encrypt_symmetric, decrypt as decrypt_symmetric
from encryption.asymmetric_encryption import encrypt as encrypt_asymmetric, decrypt as decrypt_asymmetric
from encryption.hashing import hash_sha256, hash_md5
from encryption.hybrid_encryption import encrypt as encrypt_hybrid, decrypt as decrypt_hybrid
from encryption.steganography import encode_message, decode_message
from encryption.block_and_stream_cipher import aes_encrypt, aes_decrypt
from encryption.homomorphic_encryption import encrypt as encrypt_homomorphic, decrypt as decrypt_homomorphic, add_encrypted_numbers, multiply_encrypted_by_scalar

# Symmetric Encryption Example
def symmetric_encryption_example():
    message = "Hello, Symmetric World!"
    encrypted_msg = encrypt_symmetric(message)
    print(f"Encrypted (Symmetric): {encrypted_msg}")
    decrypted_msg = decrypt_symmetric(encrypted_msg)
    print(f"Decrypted (Symmetric): {decrypted_msg}")

# Asymmetric Encryption Example
def asymmetric_encryption_example():
    message = "Hello, Asymmetric World!"
    encrypted_msg = encrypt_asymmetric(message)
    print(f"Encrypted (Asymmetric): {encrypted_msg}")
    decrypted_msg = decrypt_asymmetric(encrypted_msg)
    print(f"Decrypted (Asymmetric): {decrypted_msg}")

# Hashing Example
def hashing_example():
    message = "Hello, Hashing World!"
    print(f"SHA-256: {hash_sha256(message)}")
    print(f"MD5: {hash_md5(message)}")

# Hybrid Encryption Example
def hybrid_encryption_example():
    message = "Hello, Hybrid World!"
    encrypted_data = encrypt_hybrid(message)
    print(f"Encrypted (Hybrid): {encrypted_data}")
    decrypted_msg = decrypt_hybrid(encrypted_data)
    print(f"Decrypted (Hybrid): {decrypted_msg}")

# Steganography Example
def steganography_example():
    input_image = 'input.png'  # Replace with your image path
    output_image = 'output.png'
    message = "Secret Message!"
    encode_message(input_image, output_image, message)
    print(f"Message Encoded in {output_image}")
    decoded_message = decode_message(output_image)
    print(f"Decoded Message: {decoded_message}")

# Block Cipher (AES) Example
def block_cipher_example():
    message = "Hello, AES World!"
    encrypted_data = aes_encrypt(message)
    print(f"Encrypted (AES): {encrypted_data}")
    decrypted_msg = aes_decrypt(encrypted_data)
    print(f"Decrypted (AES): {decrypted_msg}")

# Homomorphic Encryption Example
def homomorphic_encryption_example():
    number1 = 10
    number2 = 20
    encrypted_num1 = encrypt_homomorphic(number1)
    encrypted_num2 = encrypt_homomorphic(number2)
    print(f"Encrypted Number 1: {encrypted_num1}")
    print(f"Encrypted Number 2: {encrypted_num2}")
    
    encrypted_sum = add_encrypted_numbers(encrypted_num1, encrypted_num2)
    decrypted_sum = decrypt_homomorphic(encrypted_sum)
    print(f"Decrypted Sum (10 + 20): {decrypted_sum}")
    
    encrypted_product = multiply_encrypted_by_scalar(encrypted_num1, 5)
    decrypted_product = decrypt_homomorphic(encrypted_product)
    print(f"Decrypted Product (10 * 5): {decrypted_product}")

if __name__ == "__main__":
    print("Symmetric Encryption Example")
    symmetric_encryption_example()
    
    print("\nAsymmetric Encryption Example")
    asymmetric_encryption_example()
    
    print("\nHashing Example")
    hashing_example()
    
    print("\nHybrid Encryption Example")
    hybrid_encryption_example()
    
    print("\nSteganography Example")
    steganography_example()
    
    print("\nBlock Cipher Example (AES)")
    block_cipher_example()
    
    print("\nHomomorphic Encryption Example")
    homomorphic_encryption_example()
