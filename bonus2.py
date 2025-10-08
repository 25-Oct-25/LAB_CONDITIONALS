name = input("Enter your Name: ")
email =  input("Enter your Email: ")

if len(name) <= 2 and (not "@gmail" in email or not email.endswith(".com") or " " in email):
    print("Both name and email are invalid, please provide valid information.")

elif len(name) <= 2 :
    print("The name length must be more than 2 characters, please provide a valid name.")

elif not "@gmail" in email or not email.endswith(".com") or " " in email :
    print("The email is not valid , please provide a valid email .")

else:
     print(f"Welcome {name}, you registered with the email {email} !")