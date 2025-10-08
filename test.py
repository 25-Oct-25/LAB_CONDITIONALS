email:str= input("Please enter your email= ")

if not email.endswith("@gmail.com") or " "  in email or email.count("@") ==1:
    print("1")

else:
    print("0")