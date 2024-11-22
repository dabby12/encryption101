# homomorphic_encryption.py

from phe import paillier

# Generate a Paillier key pair
public_key, private_key = paillier.generate_paillier_keypair()

# Encrypt function
def encrypt(number: int) -> paillier.EncryptedNumber:
    return public_key.encrypt(number)

# Decrypt function
def decrypt(encrypted_number: paillier.EncryptedNumber) -> int:
    return private_key.decrypt(encrypted_number)

# Homomorphic operations
def add_encrypted_numbers(enc_num1: paillier.EncryptedNumber, enc_num2: paillier.EncryptedNumber) -> paillier.EncryptedNumber:
    return enc_num1 + enc_num2

def multiply_encrypted_by_scalar(enc_num: paillier.EncryptedNumber, scalar: int) -> paillier.EncryptedNumber:
    return enc_num * scalar

if __name__ == "__main__":
    # Example usage
    number1 = 10
    number2 = 20

    # Encrypt numbers
    encrypted_num1 = encrypt(number1)
    encrypted_num2 = encrypt(number2)
    print(f"Encrypted Number 1: {encrypted_num1}")
    print(f"Encrypted Number 2: {encrypted_num2}")

    # Perform homomorphic addition
    encrypted_sum = add_encrypted_numbers(encrypted_num1, encrypted_num2)
    decrypted_sum = decrypt(encrypted_sum)
    print(f"Decrypted Sum (10 + 20): {decrypted_sum}")

    # Perform homomorphic multiplication by scalar
    encrypted_product = multiply_encrypted_by_scalar(encrypted_num1, 5)
    decrypted_product = decrypt(encrypted_product)
    print(f"Decrypted Product (10 * 5): {decrypted_product}")
