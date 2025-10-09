
name = input("Enter your name: ")
email = input("Enter your email: ")
allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"

if len(name) <= 2:
    print("The name length must be more than 2 characters")
else:
    if (
        " " in email or
        email.count("@") != 1 or
        not email.endswith("@gmail.com") or
        email.startswith("@")
    ):
        print("The email is not valid")
    else:
        firstName = email.split("@")[0]
        valid = all(ch in allowed_chars for ch in firstName)

        if not valid or firstName == "":
            print("The email is not valid")
        else:
            print(f"Welcome {name}, you registered with the email {email}!")
