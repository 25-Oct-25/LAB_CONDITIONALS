##نواف البريكان
## الكود يلخبط
name = input("Enter your name: ")
email = input("Enter your email: ")
flag = False

if len(name)> 2:
    flag = True
at = email.find("@")
gmail = email[at+1:at+6]
if (len(email)>10) and (not email.startswith("@")) and (not email.endswith("@")) and ("@" in email) and (email.count("@")==1) and (email.endswith(".com")) and (gmail == "gmail"):
    flag = True
else:
    flag = False

if flag:
    print(f"Welcome {name}, you registered with the email {email} !")

else:
    print("the email is not valid , please provide a valid email .")

print(gmail)