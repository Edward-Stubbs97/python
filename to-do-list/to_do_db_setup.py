import sqlite3

# connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("to_do_list.db")

# create a cursor to run SQL commands
cursor = conn.cursor()

# Create the todolist table
cursor.execute("""
CREATE TABLE IF NOT EXISTS to_do_list (
    task TEXT PRIMARY KEY,
    due_Date TEXT,
    status INTEGER
)
""")

# Save and close
conn.commit()
conn.close()

print("Database setup complete.")