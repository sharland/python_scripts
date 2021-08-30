#!f:
#filename: functions.py
def addition():
   # x = int(input('enter x :'))
   # y = int(input('enter y :'))        
    a = x + y
    print ('x + y = ', a)
    print()
    return

    
def subtraction():
   # x = int(input('enter x :'))
   # y = int(input('enter y :'))        
    b = x - y
    print ('x - y = ', b)
    print()
    return

def multiplication():
   # x = int(input('enter x :'))
   # y = int(input('enter y :'))        
    c = x * y
    print ('x * y = ', c)
    print()
    return

def division():
   # x = int(input('enter x :'))
   # y = int(input('enter y :'))        
    d = x / y
    print ('x / y = ', d)
    print()
    return

def enterxy():

    global x,y
    x = int(input('enter x :'))
    y = int(input('enter y :'))
    return

def menu():

    global choice
    print('Do you wish to draw:-')
    print('1. add?')
    print('2. subtract?')
    print('3. multiply?')
    print('4. divide?')
    print('5. quit?')
    print('choose 1 to 5')
    choice = int(input())
    return

def userchoice():

    while choice != 5:
        menu()
        if choice in [1,2,3,4]:
            enterxy()
            if choice == 1:
                addition()
            elif choice == 2:
                subtraction()
            elif choice == 3:
                multiplication()
            else:
                division()
        elif choice == 5: 
                print('goodbye')
        else:
            print('invalid choice')
    return
    
choice = 0
userchoice()

            
        
