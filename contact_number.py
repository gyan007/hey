import re

def validate_contact_number(number):
    pattern = r'^(\+91[\-\s]?)?[0]?[6-9]\d{9}$'
    if re.match(pattern, number):
        return True
    else:
        return False

user_number = input("Enter your contact number: ")

if validate_contact_number(user_number):
    print("Valid Contact Number")
else:
    print("Invalid Contact Number")