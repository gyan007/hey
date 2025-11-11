import re

def validate_pan_card(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(pattern, pan):
        return True
    else:
        return False

user_pan = input("Enter your PAN card number: ")

if validate_pan_card(user_pan):
    print("Valid PAN Card Number")
else:
    print("Invalid PAN Card Number")