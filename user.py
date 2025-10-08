name = input("Enter your name :")
email = input("Enter you email :")

if len(name) <= 2 :
    print("The name length must be more than 2 characters, please provide a valid name.")
elif email.endswith ("@gmail.com"):
    print(f"Welcome {name} , you registered with the email {email} ")
else :
    print("The email is not valid , please provide a valid email")