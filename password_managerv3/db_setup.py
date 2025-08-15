import sqlite3

# connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("passwords.db")

# create a cursor to run SQL commands
cursor = conn.cursor()

# Create the passwords table
cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords (
    site TEXT PRIMARY KEY,
    password TEXT
)
""")

# Save and close
conn.commit()
conn.close()

print("Database setup complete.")