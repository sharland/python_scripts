#! /usr/bin/python3.3

import re

userInput = input("Enter your password: ")
if re.search("p@ssword", userInput):
    print("Correct Password Entered")
else:
    print("Error, incorrect password")
