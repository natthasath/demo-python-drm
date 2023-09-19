from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a random encryption key (you should securely store this key in a real DRM system)
encryption_key = get_random_bytes(16)  # 16 bytes for AES-128

# Function to pad the data to be encrypted to a multiple of 16 bytes
def pad(data):
    return data + b'\0' * (16 - len(data) % 16)

# Function to encrypt a file
def encrypt_file(input_file, output_file, encryption_key):
    cipher = AES.new(encryption_key, AES.MODE_ECB)
    
    with open(input_file, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(16)
                if not chunk:
                    break
                encrypted_chunk = cipher.encrypt(pad(chunk))
                outfile.write(encrypted_chunk)

# Function to decrypt a file
def decrypt_file(input_file, output_file, encryption_key):
    cipher = AES.new(encryption_key, AES.MODE_ECB)
    
    with open(input_file, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(16)
                if not chunk:
                    break
                decrypted_chunk = cipher.decrypt(chunk)
                outfile.write(decrypted_chunk.rstrip(b'\0'))

# Example usage
input_file = 'main.py'
encrypted_file = 'encrypted.py'
decrypted_file = 'decrypted.py'

# Encrypt the file
encrypt_file(input_file, encrypted_file, encryption_key)

# Decrypt the file
decrypt_file(encrypted_file, decrypted_file, encryption_key)
