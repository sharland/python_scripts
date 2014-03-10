import re

#postcode rule is 'letter, letter, number, number, space, number, letter, letter'
postcodeRule = "[A-Z][A-Z][0-9][0-9] [0-9][A-Z][A-Z]"

userInput = input("Enter a postcode: ")
if re.search(postcodeRule,userInput):
    print("Valid postcode!")
else:
    print("Invalid postcode!")
