name:str = input("Enter your name: ")
main_email:str = input("Enter your email: ").strip()

email:str = main_email.lower()

if len(name) <= 2 :
    print("the name length must be more than 2 characters, please provide a valid name.")
else :
    if email.endswith("@gmail.com") and email.count("@") == 1 and email.count(".com") == 1 and " " not in email and email[0].isalpha :
        print(f"welcome {name}, you registered with the email {main_email} !")
    else:
        print("the email is not valid , please provide a valid email .")

# Abdulrahman Al-Qahtani

