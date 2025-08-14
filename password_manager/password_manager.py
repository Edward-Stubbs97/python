

def password_manager(site_required):
    passwords = {
        "facebook": "Stubbsy901",
        "instagram": "Stubbsy1997!",
    }
    
    site_required = site_required.lower()
    
    if site_required in passwords:
        print(passwords[site_required])
    else:
        print("Site not found")
    
site = input("What site do you require a password for? ")
password_manager(site)