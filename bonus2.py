Name = input("write your name: ")
Email = input("write your email: ")

# Check Name:
if len(Name) > 2:
    print("Valid name")
else:
    print("the name length must be more than 2 characters, please provide a valid name.")

# Check Email:
if Email.count("@") == 1 and Email.endswith("@gmail.com") and Email.index("@") > 0:
    print("welcome" , Name , "you registered with the" , Email )
else:
    print("the email is not valid , please provide a valid email.")
