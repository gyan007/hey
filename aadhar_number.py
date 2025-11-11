import re

def validate_aadhaar(number):
    pattern = r'^[2-9]\d{3}[\s\-]?\d{4}[\s\-]?\d{4}$'
    if re.match(pattern, number):
        return True
    else:
        return False

user_aadhaar = input("Enter your Aadhaar number: ")

if validate_aadhaar(user_aadhaar):
    print("Valid Aadhaar Number")
else:
    print("Invalid Aadhaar Number")