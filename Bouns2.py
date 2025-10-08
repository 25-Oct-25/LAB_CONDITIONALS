username=input("Enter your username: ")
email=input("Enter your email: ")
checkEmail=email.partition("@gmail")

if len(username)<=2: 
    print("the name length must be more than 2 characters, please provide a valid name.") 
elif len(checkEmail[0])>2 and checkEmail[0].isidentifier() and checkEmail[1]=="@gmail" and checkEmail[2]==".com":
        print(f"welcome {username}, you registered with the email {email}!")
elif len(checkEmail[0])<=2 or checkEmail[0].isidentifier()==False or checkEmail[1]!="@gmail" or checkEmail[2]==".com":
    print(" the email is not valid , please provide a valid email .")
   
