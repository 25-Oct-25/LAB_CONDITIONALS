
# Create a function to check if user name is correct or not 
# If not he will stack intel he put it right 
# Then the function return a user name to ' welcomeUser ' function

def checkUserName():
    
    userName = input("Enter your name : ")  
    lengthName = len(userName)
    
    if lengthName <= 2 :
        print("the name length must be more than 2 characters, please provide a valid name.")
        checkUserName() # if user doesn't put a name correct he will stack  
        
    print("Your user name is vaild")
    return userName

# Create a anuther function cheacks for user email 
# If the function found a '@gmail' in the email thats a correct email 
# then return user email into ' welcomeUser ' function 

def checkUserEmail():
    
    userEmail = input("Enter your email ( Only email exsptied is \'Gmail\'!) :")

    # To git a @ in user email 
    checkEmail = userEmail.find("@")

    # To git @ and 'gmail'
    # userEmail[checkEmail:checkEmail+]

    if userEmail[checkEmail:checkEmail+6] != "@gmail" :
        print("the email is not valid , please provide a valid email .")
        checkUserEmail() # if user doesn't put a email correct he will stack 

    print("Your email is vaild")
    return userEmail

# This function to print 'userName' and 'userEmail' , then it will print welcome masseg

def walcomeUser():
    
    # call the two function :
    userName = checkUserName()
    userEmail = checkUserEmail()

    print(f'welcome {userName}, you registered with the email {userEmail} !')

# To call the main function
walcomeUser()