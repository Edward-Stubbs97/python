
def password_manager():
    
    passwords = {
        "instagram": "stubbsy901",
        "facebook": "stubbsy901!",
    }
    
    while True:
        
        requirement = input("Please type add, require or quit: ").lower()
        
        if requirement == "add":
            
            site = input("What site is the password for? ").lower()
            password = input("What is the password? ")
            passwords[site] = password
            print(f"Your passwords object has ben updated {passwords}")
            
        elif requirement == "require":
            
            required = input("What site do you need? ").lower()
            
            if required in passwords:
                print(f"Your password for {required} is {passwords[required]}")
        
            else:
                print("Site not found")
        
        elif requirement == "quit":
            print("Exiting password manager.")
            break
        
        else:
            print("That is not a recognised command.")

        
password_manager()