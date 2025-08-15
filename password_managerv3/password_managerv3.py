import sqlite3

def add_passwords(site ,passwords):
    
    # Step 1: Connect to the database
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    
    # Step 2: Insert or replace the password
    cursor.execute(
        "INSERT OR REPLACE INTO passwords (site, password) VALUES (?, ?)",
        (site, password)
    )
    
    # Step 3: Save changes and close    
    conn.commit()
    conn.close()
    
    print(f"Password for {site} as been saved.")
    
    
def get_password(site):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT password FROM passwords WHERE site = ?",
        (site,)
    )
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        print(f"Your password for {site} is {result[0]}")
    else:
        print(f"No resulut for {site}")

while True:
    requirement = input("Please type 'add' to store a password, 'require' to get one or 'quit' to exit: ").lower()
    
    if requirement == "add":
        site = input("What site is the password for? ").lower()
        password = input("What is the password? ")
        add_passwords(site, password)
        
    elif requirement == "require":
        site = input("What site do you need? ").lower()
        get_password(site)
    
    elif requirement == "quit":
        print("Goodbye!")
        break
    
    else:
        print("That is not a recognised command please try again")
        