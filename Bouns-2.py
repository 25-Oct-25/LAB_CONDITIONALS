checkName = 0
checkEmail = 0



#Create a username

while len(input("Enter your username : ")) < 3:
    
    print('the name length must be more than 2 characters,' \
    'please provide a valid name.')
    
else:
    print("The username added successfully")
    checkName = 1
#Create an email
#email = 
emailType = "@gmail.com"

while input("Enter your email: ").find(emailType) == -1:
    print("the email you entered not valid, try other email.")
else:
    print("Your email added successfuly")
    checkEmail = 1

   

#print("the email you entered not valid, try other email.")

if checkName == 1 and checkEmail==1:
    print(f"Welcome , you are registered with email  !")
else: print("The username and email both of them are wrong")