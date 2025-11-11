import re

def validate_email(email):
    pattern = r'^^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

user_email = input("Enter your email: ")

if validate_email(user_email):
    print("Valid Email")
else:
    print("Invalid Email")