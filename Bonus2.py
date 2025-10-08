name:str = input("Enter your name: ")
email:str = input("Enter your email: ")

if len(name) > 2 and "@gmail" in email:
    print(f"Welcome {name}, your registred email is {email}")
elif len(name) <= 2 and "@gmail" in email:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif "@gmail" not in email and len(name) > 2:
    print(" the email is not valid , please provide a valid email .")
elif len(name) <= 2 and "@gmail" not in email:
    print("the email and the name are not valid , please provide a valid email and name .")