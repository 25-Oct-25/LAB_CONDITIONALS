while True:
    name = input("Enter your name: ").strip()
    if len(name) > 2:
        break
    print("Name must be more than 2 characters.\n")

while True:
    email = input("Enter your email: ").strip()

    if any(ch.isspace() for ch in email):
        print("Email must not contain spaces or whitespace.\n")
        continue

    
    if email.count("@") != 1:
        print("Email must contain exactly one '@'.\n")
        continue

    local, domain = email.rsplit("@", 1)

    
    if domain.lower() != "gmail.com":
        print("Domain must be gmail.com.\n")
        continue

    
    if not local:
        print("Email must have characters before '@'.\n")
        continue

   
    s = local.lower()

    
    valid_chars = True
    for c in s:
        if c == '.':
            continue
        if not (c.isascii() and c.isalnum()): # isascii for : ASCII   isalnum for : A–Z/a–z/0–9
            valid_chars = False
            break

    if not valid_chars:
        print("Username may contain only letters, digits, and dots.\n")
        continue

    if s[0] == '.' or s[-1] == '.':
        print("Username cannot start or end with a dot.\n")
        continue

    if '..' in s:
        print("Username cannot contain consecutive dots.\n")
        continue

   
    break

print(f"Welcome {name}, you registered with the email {email}!")
