name = input("Enter your name: ")
email = input("Enter your email: ")
flag = False
if len(name)> 2:
    flag = True
if "@gmail" in email and "." in email:
    flag = True
if flag:
    print(f"Welcome {name}, you registered with the email {email} !")

else:
    print("the email is not valid , please provide a valid email .")