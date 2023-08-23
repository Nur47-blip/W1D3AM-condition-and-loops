isValid = False

while not isValid:
    password = input("Enter a password: ")

    if not any(i.islower() for i in password):
        print("Password must contain at least one lowercase letter.")
    elif not any(i.isupper() for i in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(i in ['$', '#', '@'] for i in password):
        print("Password must contain at least one of the characters $, #, @.")
    elif (len(password) < 6 or len(password) > 16):
        print("Password must be between 6 and 16 characters (inclusive).")
    else:
        isValid = True
        print("Password is valid.")