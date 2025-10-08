name = input("Enter your name:")
email = input("Enter your email:")

if len(name) <= 2 and (" " in email 
or not email[0].isalnum() 
or email.count("@") != 1 
or not email.endswith("@gmail.com") 
or ".." in email
or email.sartswith("gmail.com")):
    print("Both the name and email are invalid. Please provide valid inputs.")
elif len(name) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif " " in email or not email[0].isalnum() or email.count("@") != 1 or not email.endswith("@gmail.com") or ".." in email or email.startswith(".") or email.startswith("@"):
    print("the email is not valid , please provide a valid emailز")
else:
    print(f"Welcome{name}, you registered with the email {email}!")
