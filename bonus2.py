name:str = input("Enter your name: ").strip()
email:str = input("Enter your email: ").strip()


if len(name) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
else:
    if email.count("@") != 1:
        print(" the email is not valid , please provide a valid email .")

    elif "@gmail" not in email:
        print("the email is not valid , please provide a valid email .")

    elif " " in email:
            print(" the email is not valid , please provide a valid email .")
    else:
        print(f"welcome {name}, you registered with the email {email} !")