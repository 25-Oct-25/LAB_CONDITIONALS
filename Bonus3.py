while True:
    # Ask for name and email
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    # Check if name is valid
    if len(name) <= 2:
        print("The name length must be more than 2 characters, please provide a valid name.\n")
        continue  # Go back to the beginning of the loop

    # Check if email is valid
    if "@" not in email or not email.endswith("@gmail.com"):
        print("The email is not valid, please provide a valid email.\n")
        continue  # Go back to the beginning of the loop

    # If both are valid, welcome the user and break the loop
    print(f"Welcome {name}, you registered with the email {email}!")
    break
