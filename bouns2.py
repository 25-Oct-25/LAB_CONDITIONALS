name = input("Please enter your name: ")
email = input(" Please enter your email: ")
if len(name) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name")
elif "@" not in email or ".com" not in email or not email.endswith("@gmail.com"):
    print("the email is not vaild, plaese provid a vaild email.")
else:
    print("welcome Ahmed, you registered with the email ahmed@gmail.com !") 