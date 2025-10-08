name = input("Enter your name:")
email = input("Enter your email:")
if len(name) <= 2 :
    print("Name must be more than 2 characters.")
else:
       
    if  "@" not in email :
        print("the email is not valid , please provide a valid email .")           
    else:
        username, domain = email.split("@", 1) 
   
        if " " in username :
            print("the email is not valid , please provide a valid email .") 
        elif username[0] in ".-" :
            print("the email is not valid , please provide a valid email .") 
        elif username[-1] in ".-" :
            print("the email is not valid , please provide a valid email .") 
        elif ".." in username :
            print("the email is not valid , please provide a valid email .") 
        elif domain != "gmail.com" :
            print("the email is not valid , please provide a valid email .")
        else:
            print(f"Welcome {name}, you registered with the email {email}")
