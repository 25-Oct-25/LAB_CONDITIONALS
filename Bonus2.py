name:str= input("Please enter your name= ")
email:str= input("Please enter your email= ")


if len(name) >=2 and email.endswith("@gmail.com") and " " not in email and email.count("@")==1 and email.count(".com")==1 and not email.startswith("@gmail.com"):
    print(f"Welcome {name}, you registered with the email {email}")

elif len(name) >=2 and not email.endswith("@gmail.com") or " " in email or not email.count("@")==1 or not email.count(".com")==1 or email.startswith("@gmail.com"):
    print("the email is not valid, please provide a valid email")

elif len(name)<2 and email.endswith("@gmail.com") and " " not in email and email.count("@")==1 and email.count(".com")==1 and not email.startswith("@gmail.com"):
    print("the name length must be more than 2 characters, please provide a valid name.")
    
else:
    len(name) <2 and not email.endswith("@gmail.com") or " " in email or not email.count("@")==1 or not email.count(".com")==1 or email.startswith("@gmail.com")
    print("The name and the email you provided are not valid. Please enter a valid name and email.")