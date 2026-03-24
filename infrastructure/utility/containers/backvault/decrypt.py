# decrypt.py
import os
import sys
from getpass import getpass
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidTag

SALT_SIZE = 16
KEY_SIZE = 32
PBKDF2_ITERATIONS = 600000

def decrypt_data(encrypted_data: bytes, password: str) -> bytes:
    salt = encrypted_data[:SALT_SIZE]
    nonce = encrypted_data[SALT_SIZE:SALT_SIZE+12]
    ciphertext_with_tag = encrypted_data[SALT_SIZE+12:]
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=PBKDF2_ITERATIONS
    )
    key = kdf.derive(password.encode("utf-8"))
    
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext_with_tag, None)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <encrypted_file> [password]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    password = sys.argv[2] if len(sys.argv) > 2 else getpass("Enter backup password: ")
    
    if file_path.endswith('.enc'):
        output_path = file_path[:-4] + '.json'
    else:
        output_path = file_path + '.json'
    
    try:
        with open(file_path, "rb") as f:
            encrypted_contents = f.read()
        
        decrypted_json = decrypt_data(encrypted_contents, password)
        
        with open(output_path, "wb") as f:
            f.write(decrypted_json)
        
        print(f"Decryption successful. Output saved to: {output_path}", file=sys.stderr)
    except InvalidTag:
        print("Decryption failed: Invalid password or corrupted file.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

