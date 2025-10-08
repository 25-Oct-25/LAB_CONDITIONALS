
# Create a function to check if user name is correct or not 
# If not he will stack intel he put it right 
# Then the function return a user name to ' welcomeUser ' function

def check_user_name():
    
    user_name = input("Enter your name : ")  
    length_name = len(user_name)
    
    if length_name <= 2 :
        print("the name length must be more than 2 characters, please provide a valid name.")
        return check_user_name() # if user doesn't put a name correct he will stack  
        
    print("Your user name is vaild")
    return user_name

# Create a anuther function cheacks for user email 
# If the function found a '@gmail' in the email thats a correct email 
# then return user email into ' welcomeUser ' function 

def check_user_email():
    
    user_email = input("Enter your email ( Only email exsptied is \'Gmail\'!) :")

    # To git a @ in user email 
    check_email = user_email.find("@")

    # To git @ and 'gmail'
    # userEmail[checkEmail:checkEmail+]

    if user_email[check_email:] != "@gmail.com" :
        print("the email is not valid , please provide a valid email .")
        return check_user_email() # if user doesn't put a email correct he will stack 
    
    # cheack before the @ if thers any charcter before or not

    username_part = user_email.split("@")[0]
    if len(username_part.strip()) == 0: # Strip will remove any spaces in the word 
        print("Email must have text before '@', please provide a valid email.")
        return check_user_email()

    print("Your email is vaild")
    return user_email

# This function to print 'userName' and 'userEmail' , then it will print welcome masseg

def walcome_user():
    
    # call the two function :
    user_name = check_user_name()
    user_email = check_user_email()

    print(f'welcome {user_name}, you registered with the email {user_email} !')

# To call the main function
walcome_user()