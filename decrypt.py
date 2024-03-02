from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt_file(input_file, output_file, key):
    chunk_size = 64 * 1024  # 64 KB

    # Read the IV from the encrypted file
    with open(input_file, 'rb') as in_file:
        iv = in_file.read(16)

        # Create AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Determine file size to handle padding correctly
        file_size = os.path.getsize(input_file)

        # Decrypt the file chunk by chunk
        with open(output_file, 'wb') as out_file:
            while True:
                chunk = in_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                decrypted_chunk = cipher.decrypt(chunk)
                out_file.write(decrypted_chunk)

            # Remove padding at the end of the decrypted file
            padding_length = decrypted_chunk[-1]  # Get the last byte, which indicates padding length
            out_file.seek(-padding_length, os.SEEK_END)  # Move the file pointer back by the padding length
            out_file.truncate()  # Truncate the file to remove padding

    print(f"Decryption complete. Decrypted file saved as {output_file}")

# Example usage
input_file = 'encrypted_video.enc'
output_file = 'decrypted_video.mp4'  # You can change the output filename
key = b'ThisIsASecretKey'  # Use the same key used for encryption

decrypt_file(input_file, output_file, key)
