
name=input("Please enter your name: ")

email =input("Please enter your email: ")

if len(name)>2 and email.find("@gmail.com") != -1 :
    print(f"Welcome {name}, you registered with the email {email} !")
elif len(name)<= 2:
    print("The name length must be more than 2 characters, please provide a valid name")
elif email.find("@gmail.com") == -1 :
    print("The email is not valid , please provide a valid email .")

  
