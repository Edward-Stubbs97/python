def password_manager(requirement):
    
    passwords = {
        "instagram": "Rollo1997!",
        "facebook": "Rollo7991!",
    }
    
    if requirement == "add":
        
        site = input("What site is the password for? ").lower()
        password = input("What is the password? ")
        passwords[site] = password
        print(f"Your passwords object has ben updated {passwords}")
        
    elif requirement == "require":
        
        required = input("What site do you need? ").lower()
        print(f"Your password for {required} is {passwords[required]}")
    
    else:
        
        print("That is not a recognised command:")
        
        
requirement = input("Please type add or require ").lower()
password_manager(requirement)