import streamlit as st
import sqlite3
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from io import BytesIO

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    iv = encrypted_data[:16]  # Extract the IV from the encrypted data
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted_data

# Connect to the SQLite database
conn = sqlite3.connect('encrypted_files.db')
cursor = conn.cursor()

# Retrieve the encrypted data from the database
cursor.execute('SELECT data FROM encrypted_files WHERE filename=?', ('video.enc',))
encrypted_data = cursor.fetchone()[0]

# Close the database connection
conn.close()

# Main Streamlit app
def main():
    st.title("Encrypted Video Viewer")

    encryption_key = st.text_input("Enter decryption key:")
    if encryption_key:
        key = encryption_key.encode('utf-8')
        decrypted_data = decrypt_data(encrypted_data, key)
        st.video(BytesIO(decrypted_data))
    else:
        st.warning("Please enter a decryption key.")

if __name__ == "__main__":
    main()
