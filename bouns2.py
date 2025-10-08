
name = input("Please enter your name: ")
email = input("Please enter your email: ")


if len(name) <= 2:
    print("The name length must be more than 2 characters, please provide a valid name")
elif "@" not in email or "." not in email.split("@")[-1]:
    print("The email is not valid, please provide a valid email.")
else:
    print(f"Welcome {name}, you registered with the email {email}!")
