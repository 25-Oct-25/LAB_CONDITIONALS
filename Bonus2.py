name = input("Enter your name: ")
email = input("Enter your email: ")

if len(name) > 2 and email.endswith("@gmail.com"):
    print(f"Welcome {name}, you registered with the email {email}!")

elif len(name) <= 2 and email.endswith("@gmail.com"):
    print("The name length must be more than 2 characters, please provide a valid name.")

elif not email.endswith("@gmail.com") and len(name) > 2:
    print("The email is not valid, please provide a valid email.")

else:
    print("The email and the name are not valid, please provide a valid email and name.")
