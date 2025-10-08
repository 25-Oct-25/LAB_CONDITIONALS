name = input("Enter your name :").strip()
email = input("Enter you email :").strip()
allowed_domains = ("@gmail.com", "@yahoo.com", "@hotmail.com")


if not name:
    print("Name cannot be empty.")

elif len(name) <= 2 :
    print("The name length must be more than 2 characters .")

elif not name[0].isalpha():
    print("The name must start with a letter.")

elif  "*" in name or "&" in name or "%" in name or "#" in name or "@"  in name:
    print("The name cannot contain *, &, % , @ ,or # characters.")

elif not email:
    print("Email cannot be empty.")

elif " " in email:
    print("Email cannot contain spaces.")

elif email.endswith(allowed_domains):
    print(f"Welcome {name}, you registered with the email {email}")

else :
    print("The email is not valid .")