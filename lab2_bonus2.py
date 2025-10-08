name = input("Enter your name: ")
email = input("Enter your email: ")

if len(name) <= 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
elif "@gmail.com" not in email or email.count("@") != 1 or not email.endswith("@gmail.com"):
    print("The email is not valid, please provide a valid email.")
else:
    print(f"Welcome {name}, you registered with the email {email}!")
