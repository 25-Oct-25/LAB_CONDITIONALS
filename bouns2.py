
name=input("Please enter your name: ")

email =input("Please enter your email: ")

if len(name)>2:
    if email.find("@gmail.com") != -1 or email.find("outlook.com") != -1 or email.find("hotmail.com") != -1:
        if email.find(" ") == -1 and email.find("@@") == -1:
            print(f"Welcome {name}, you registered with the email {email} !")

          
if len(name)<= 2:
    print("The name length must be more than 2 characters, please provide a valid name")
if email.find("@gmail.com") == -1 or email.find("@outlook") == -1 or email.find("@hotmail.com") == -1 or email.find(" ")!= -1 or email.find("@@") != -1:
    print("The email is not valid , please provide a valid email .")

  
