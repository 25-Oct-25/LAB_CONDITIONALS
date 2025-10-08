# Bonus 2
# write a program that asks the user to provide his name and his email using input , then do the following:


name= input("Enter your name: ")
email= input("Enter your email: ").lower()


if len(name) <=2 and not email.endswith("@gmail.com") or email.count("@")!=1 or " " in email or email.startswith(".") or email.startswith("@"):
    print("Both name and email invalid, please try again.")
elif len(name) <=2 :
    print("the name length must be more than 2 characters, please provide a valid name.")
elif not email.endswith("@gmail.com") or email.count("@")!=1 or " " in email or email.startswith(".") or email.startswith("@"):
     print("the email is not valid , please provide a valid email.")
else:
    print(f"welcome {name}, you registered with the email {email}!")
    