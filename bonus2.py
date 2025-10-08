# Bonus 2
# write a program that asks the user to provide his name and his email using input , then do the following:

while True:
    name= input("Enter your name: ")
    email= input("Enter your email: ").lower()

    # both name and email invalid
    if (len(name) <=2) and (not email.endswith("@gmail.com") or email.count("@")!=1 or " " in email or email.startswith(".") or email.startswith("@")):
        print("Both name and email invalid, Please try again..\n")
        continue
    
    # name invalid only
    elif len(name) <=2 :
        print("The name length must be more than 2 characters, Please provide a valid name. Try again..\n")
        continue
    
    # email invalid only
    elif not email.endswith("@gmail.com") or email.count("@")!=1 or " " in email or email.startswith(".") or email.startswith("@"):
        print("The email is not valid , Please provide a valid email. Try again..\n")
        continue
    
    # if everything valid
    else:
        print(f"Welcome {name}, You registered with the email {email}!")
        break