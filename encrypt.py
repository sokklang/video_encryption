from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

from Crypto.Util.Padding import pad

def encrypt_file(input_file, output_file, key):
    chunk_size = 64 * 1024  # 64 KB
    iv = get_random_bytes(16)  # Generate a random IV (Initialization Vector)

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Get the size of the input file
    file_size = os.path.getsize(input_file)

    # Write the IV to the output file (to be used during decryption)
    with open(output_file, 'wb') as out_file:
        out_file.write(iv)

        # Encrypt the file chunk by chunk
        with open(input_file, 'rb') as in_file:
            while True:
                chunk = in_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                else:
                    # Pad the chunk if its length is not a multiple of 16
                    chunk = pad(chunk, AES.block_size)
                out_file.write(cipher.encrypt(chunk))

    print(f"Encryption complete. Encrypted file saved as {output_file}")

# Example usage
input_file = 'video.mp4'
output_file = 'encrypted_video.enc'
key = b'ThisIsASecretKey'  # 16, 24, or 32 bytes AES key

encrypt_file(input_file, output_file, key)
