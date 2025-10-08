name = input("Enter your name: ")
email = input("Enter your email: ")

if len(name) <= 2 :
    print("the name length must be more than 2 characters, please provide a valid name.")
else :
    if email.endswith("@gmail.com") :
        print(f"welcome {name}, you registered with the email {email} !")
    else:
        print("the email is not valid , please provide a valid email .")

# Abdulrahman Al-Qahtani

