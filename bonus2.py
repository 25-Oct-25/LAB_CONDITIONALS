

name = input("Enter your name: ")
email = input("Enter your email: ")

#email = email.replace(" ", "")

if len(name) > 2:
    if (
        " " not in email and
        ";" not in email and
        "," not in email and
        ":" not in email and
        "!" not in email and
        "?" not in email and
        email[0]  != '.' and
        email[-1] != '.' and
        email.count('@') == 1 and
        email.endswith('@gmail.com')
    ):
        print(f"welcome {name}, you registered with the email {email} !")
    else:
        print(f"{email} is not valid , please provide a valid email")
else:
    print(f"{name} length must be more than 2 characters, please provide a valid name")
