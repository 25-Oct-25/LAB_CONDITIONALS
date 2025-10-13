name = input("Enter your name: ")
email = input("Enter you email: ")

if len(name) <= 2 and email.count("@") == 1 and email.endswith("@gmail.com") and email.index("@")>0:
    print(f"Wellcom {name}, you registered with the email {email}!")
elif len(name)<=2:
    print("The name length must be mora than 2 characters, please provide a valid name.")
else:
    print("The email is not valid, please provide a vaild email.")