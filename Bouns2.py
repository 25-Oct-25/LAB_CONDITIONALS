username=input("Enter your username: ")
email=input("Enter your email: ")

if len(username)>2 and email.find("@gmail")!=-1 :
    print(f"welcome {username}, you registered with the email {email}!")
elif email.find("@gmail")==-1:
    print(" the email is not valid , please provide a valid email .")
elif len(username)<=2: 
    print("the name length must be more than 2 characters, please provide a valid name.")    
else: 
    print("please provide a valid name and email.")