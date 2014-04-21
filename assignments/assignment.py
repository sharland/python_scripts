#! /usr/bin/env python3
"""
Program: assignment.py
Author: Mark Clarkson
Date: March, 2013
Description: A program to help explore variables and assignment
Notes:

"""
totalScore = 0

print("===========\nQUESTION 1\n===========\n\
    Read the following code:\n\
    a = 10\n\
    b = 5\n\
    a = b\n")

a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))

if a == b == 5:
    print("\nCorrect!\n\n")
    totalScore += 1
else:
    print("\nIncorrect :-(\n\n\
Line 3 means a <- b\n\n\
The value of b is copied to a: a = 5\n\
The value of b stays the same: b = 5\n\n")






print("===========\nQUESTION 2\n===========\n\
    Read the following code:\n\
    a = 20\n\
    b = 30\n\
    b = a\n")

a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))

if a == b == 20:
    print("\nCorrect!\n\n")
    totalScore += 1
else:
    print("\nIncorrect :-(\n\n\
Line 3 means b <- a\n\n\
The value of a is copied to b: b = 30\n\
The value of b stays the same: a = 30\n\n")






print("===========\nQUESTION 3\n===========\n\
    Read the following code:\n\
    a = 10\n\
    b = 15\n\
    a = b\n\
    b = a\n")

a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))

if a == b == 15:
    print("\nCorrect!\n\n")
    totalScore += 1
else:
    print("\nIncorrect :-(\n\n\
The value of b is copied to a: a = 15\n\
The NEW value of a is copied to b: b = 15\n\n")






print("===========\nQUESTION 4\n===========\n\
    Read the following code:\n\
    a = 100\n\
    b = 50\n\
    c = a\n\
    a = b\n\
    b = c\n")

a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))

if a == 50 and b == 100:
    print("\nCorrect!\n\n")
    totalScore += 1
else:
    print("\nIncorrect :-(\n\n\
The value of a is copied to c: c = 100\n\n\
The value of b is copied to a: a = 50\n\
The NEW value of c is copied to b: b = 100\n\n")






print("===========\nQUESTION 5\n===========\n\
    Read the following code:\n\
    a = 10\n\
    b = 20\n\
    c = b\n\
    a = c\n\
    b = a\n")

a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))

if a == b == 20:
    print("\nCorrect!\n\n")
    totalScore += 1
else:
    print("\nIncorrect :-(\n\n\
The value of b is copied to c: c = 20\n\
The NEW value of c is copied to a: a = 20\n\
The NEW value of a is copied to b: b = 20\n\n")






print("===========\nQUESTION 6\n===========\n\
    Read the following code:\n\
    a = 3\n\
    b = 5\n\
    a = 2 * b\n\
    b = 2 * a\n")

a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))

if a == 10 and b == 20:
    print("\nCorrect!\n\n")
    totalScore += 1
else:
    print("\nIncorrect :-(\n\n\
The value of b is doubled and stored in a: a = 10\n\n\
The value of a is doubled and stored in b: b = 20\n\n")






print("===========\nQUESTION 7\n===========\n\
    Read the following code:\n\
    a = 5\n\
    b = 2\n\
    a = a * 2\n\
    b = b + 7\n")

a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))

if a == 10 and b == 9:
    print("\nCorrect!\n\n")
    totalScore += 1
else:
    print("\nIncorrect :-(\n\n\
The value of a is doubled and stored in a: a = 10\n\n\
The value of b is increased by 7 and stored in b: b = 9\n\n")






print("===========\nQUESTION 8\n===========\n\
    Read the following code:\n\
    a = 10\n\
    b = 5\n\
    c = a * b\n\
    a = c - a\n\
    b = c - a\n")

a = int(input("What is the value of a? "))
b = int(input("What is the value of b? "))

if a == 40 and b == 10:
    print("\nCorrect!\n\n")
    totalScore += 1
else:
    print("\nIncorrect :-(\n\n\
The value of a is multiplied by the value of b and stored in c: c = 10 * 5 = 50\n\n\
The NEW value of c minus the value of a is stored in a: a = 50 - 10 = 40\n\n\
The value of c minus the NEW value of a is stored in b: b = 50 - 40 = 10\n\n")


print("===========\nFEEDBACK\n===========\n\n")


if totalScore == 8:
    print("Congratulations - full marks! Well done!")
elif totalScore > 6:
    print("Not bad. A couple of mistakes in there but you understand the principles.")
elif totalScore > 4:
    print("More than half right. Have another go - and make notes on scrap paper if it helps.")
else:
    print("A bit more work needed. Ask for help and keep trying until you get the hang of it.")


