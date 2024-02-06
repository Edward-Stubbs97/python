question = input("What can I help you with? Please answer with the following, 'username' or 'password' ")
if question == "username":
    question_two = input("What site do you require your username for? ")
    if question_two == "instagram":
        print("Your instagram account username is 'Stubbsy901'")
    elif question_two == "facebook":
        print("Your facebook account username is 'edward.stubbs'")
    elif question_two == "twitter":
        print("Your twitter account username is 'eddy'")
    else:
        print("Sorry that does not match any site we have for you please try again!")
elif question == "password":
    question_two = input("What site do you require your password for? ")
    if question_two == "instagram":
        print("Your Instagram password is 'Rollo1997'")
    elif question_two == "facebook":
        print("Your Facebook password is 'Rollo7991!'")
    elif question_two == "twitter":
        print("Your Twitter password is 'Willow7991!'")
    else:
        print("Sorry that does not match any site we have for you please try again!")
else:
    print("your input does not match, please try again")

user_pass = {
    "Instagram": "Rollo1997",
    "facebook": "Rollo7991!",
    "twitter": "Willow7991!"
}

user_name = {
    "Instagram": "Stubbsy901",
    "facebook": "edward.stubbs",
    "twitter": "eddy"
}
