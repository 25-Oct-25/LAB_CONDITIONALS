name = input("Enter your name:")
email = input("Enter your email:")
if len(name) <= 2 :
    print("Name must be more than 2 characters.")
else :
   if "@" in email and email.endswith("@gmail.com") :
       print(f"welcome {name}, you registered with the email {email} !")
   else:
        print( "the email is not valid , please provide a valid email .")