#! /usr/local/bin/python3

x = int(input("Value of x = "))
y = int(input("Value of y = "))

menu = "What would you like to do with x and y?:\n\
    1. subtraction: x - y?\n\
    2. addition: x + y?\n\
    3. multiplication: x * y?\n\
    4. division: x / y?\n\
    9. Quit\n\
    Enter choice: "

z = int(input(menu))

if z == 1:
    print("x - y =",x-y)
elif z == 2:
    print("x + y =",x+y)
elif z == 3:
    print("x * y =",x*y)
elif z == 4:
    print("x / y =",x/y)
elif z == 9:
    print("Goodbye!")
    
