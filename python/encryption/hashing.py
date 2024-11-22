# hashing.py

import hashlib

# SHA-256 Hash function
def hash_sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

# MD5 Hash function (not recommended for sensitive data)
def hash_md5(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

if __name__ == "__main__":
    msg = "Hello, World!"
    print(f"SHA-256: {hash_sha256(msg)}")
    print(f"MD5: {hash_md5(msg)}")
