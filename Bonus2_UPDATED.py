name:str= input("Please enter your name= ")
email:str= input("Please enter your email= ")

if len(name)>= 2 and email.endswith("@gmail.com") and " " not in email and email.count("@") ==1 and not email.startswith("@gmail.com"):
    print(f"Welcome {name}! You registered with the email {email}")

elif len(name)<2:
    print("The name must be more than 2 characters. Please enter a valid name")

elif not email.endswith("@gmail.com") or " " in email or not email.count("@")==1 or email.startswith("@gmail.com"):
    print(f"The email is not valid, please enter a valid email.")