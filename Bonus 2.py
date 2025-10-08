name = input("Enter your name :")
email = input("Enter your email")


if len(name) <= 2 : 
    print("the name length must be more than 2 characters, please provide a valid name.")

if "@gmail.com" in email : 
    print("valid email")
else :
    print("the email is not valid , please provide a valid email.")


if len(name) > 2 and "@gmail.com"in email : 
    print(f"Welcome {name},you registered with the email {email}!O")