import random
import string

# https://www.youtube.com/watch?v=XCIBOl3FTKo&list=PLzMcBGfZo4-kBvY2DaxdSvoN_jGpzbw5V youtube tutorial

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters 
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ''
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length: # while either of these are true we continue so if we do not meet the criteria or length is too short
        new_char = random.choice(characters) # randomly generate a new character 
        pwd += new_char # add that to password

        if new_char in digits: # then we determin if the character added is a number or special character and set to true for either case
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number # if we should include a number but we don't have one set meet criteria to false, if we need to include a number and we do it will stay true
        if special_characters: 
            meet_criteria = meet_criteria and has_special # " same as above for special character

    return pwd # when all criteria is met wwe return the password pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n) ? ").lower() == "y"
has_special = input ("Do you want to have special characters (y/n) ? ").lower() == "y"


pwd = generate_password(min_length, has_number, has_special)
print("The genertated password is: ", pwd) 