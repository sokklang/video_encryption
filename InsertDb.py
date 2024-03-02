import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('encrypted_files.db')
cursor = conn.cursor()

# Create a table to store encrypted files
cursor.execute('''CREATE TABLE IF NOT EXISTS encrypted_files
                (id INTEGER PRIMARY KEY, filename TEXT, data BLOB)''')

# Read the encrypted file as binary data
with open('encrypted_video.enc', 'rb') as file:
    encrypted_data = file.read()

# Insert the encrypted data into the database
cursor.execute('INSERT INTO encrypted_files (filename, data) VALUES (?, ?)', ('video.enc', sqlite3.Binary(encrypted_data)))
conn.commit()

# Close the database connection
conn.close()
